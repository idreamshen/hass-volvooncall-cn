import logging
from datetime import timedelta
from json import dumps as to_json
from collections import OrderedDict
from sys import argv
from urllib.parse import urljoin
import asyncio
import argparse
import time
import json
from datetime import date, datetime

from aiohttp import ClientSession, ClientTimeout, BasicAuth
from aiohttp.hdrs import METH_GET, METH_POST

_LOGGER = logging.getLogger(__name__)

VOCAPI_HEADERS = {
    "x-client-version": "5.27.0.60",
    "x-app-name": "Volvo On Call",
    "accept-language": "zh-CN,zh-Hans;q=0.9",
    "user-agent": "Volvo%20Cars/5.27.0.60 CFNetwork/1399 Darwin/22.1.0",
    "x-os-type": "iPhone OS",
    "x-os-version": "16.1.1",
    "x-originator-type": "app",
}

TIMEOUT = timedelta(seconds=30)

class VehicleAPI:
    def __init__(self, session, refresh_token):
        self._session = session
        self._refresh_token = refresh_token
        self._digitalvolvo_access_token = ""
        self._vocapi_access_token = ""
        self._access_token_expire_at = 0

    async def _request_vocapi(self, method, url, headers, **kwargs):
        try:
            _LOGGER.debug("Request for %s", url)

            final_headers = {}
            for k in VOCAPI_HEADERS:
                final_headers[k] = VOCAPI_HEADERS[k]
            for k in headers:
                final_headers[k] = headers[k]

            final_headers["authorization"] = "Bearer " + self._vocapi_access_token

            _LOGGER.debug("final_headers=%s", final_headers)

            async with self._session.request(
                    method,
                    url,
                    headers=final_headers,
                    timeout=ClientTimeout(total=TIMEOUT.seconds)
            ) as response:
                response.raise_for_status()
                res = await response.json(loads=json_loads)
                _LOGGER.debug("Received %s", res)
                return res
        except Exception as error:
            _LOGGER.warning(
                "Failure when communicating with the server: %s",
                error,
                exc_info=True,
            )
            raise

    async def _request_digitalvolvo(self, method, url, headers, **kwargs):
        try:
            _LOGGER.debug("Request for %s", url)

            final_headers = {}
            for k in headers:
                final_headers[k] = headers[k]

            final_headers["authorization"] = "Bearer " + self._digitalvolvo_access_token

            _LOGGER.debug("final_headers=%s", final_headers)

            async with self._session.request(
                    method,
                    url,
                    headers=final_headers,
                    timeout=ClientTimeout(total=TIMEOUT.seconds)
            ) as response:
                response.raise_for_status()
                res = await response.json(loads=json_loads)
                _LOGGER.debug("Received %s", res)
                return res
        except Exception as error:
            _LOGGER.warning(
                "Failure when communicating with the server: %s",
                error,
                exc_info=True,
            )
            raise

    async def vocapi_get(self, url, headers):
        """Perform a query to the online service."""
        return await self._request_vocapi(METH_GET, url, headers)

    async def vocapi_post(self, url, headers, **data):
        """Perform a query to the online service."""
        return await self._request_vocapi(METH_POST, url, headers, json=data)

    async def digitalvolvo_get(self, url, headers):
        """Perform a query to the online service."""
        return await self._request_digitalvolvo(METH_GET, url, headers)

    async def digitalvolvo_post(self, url, headers, **data):
        """Perform a query to the online service."""
        return await self._request_digitalvolvo(METH_POST, url, headers, json=data)


    async def get_vehicles_vins(self):
        url = "https://apigateway.digitalvolvo.com/app/account/vehicles/api/v1/owner/listBindCar"
        result = await self.digitalvolvo_get(url, {})
        vins = []
        for k in result["data"]:
            vins.append(k["vinCode"])

        return vins

    async def update_access_token(self):
        url = "https://apigateway.digitalvolvo.com/app/iam/api/v1/refreshToken?refreshToken=" + self._refresh_token
        result = await self.digitalvolvo_get(url, {})
        self._vocapi_access_token = result["data"]["globalAccessToken"]
        self._digitalvolvo_access_token = result["data"]["accessToken"]
        now = int(time.time())
        self._access_token_expire_at = now + int(result["data"]["expiresIn"])

    async def get_vehicle_status(self, vin):
        url = "https://vocapi.cn.prod.vocw.cn/customerapi/rest/vehicles/" + vin + "/status"
        return await self.vocapi_get(url, {
            "content-type": "application/vnd.wirelesscar.com.voc.VehicleStatus.v8+json; charset=utf-8",
            "accept": "application/vnd.wirelesscar.com.voc.VehicleStatus.v8+json; charset=utf-8",
        })

class Vehicle:

    def __init__(self, vin, api):
        self.vin = vin
        self._api = api

        self.car_locked = False
        self.car_locked_updated_at = 0
        self.distance_to_empty = 0 # 续航公里
        self.distance_to_empty_updated_at = 0
        self.tail_gate_open = False
        self.rear_right_door_open = False
        self.rear_left_door_open = False
        self.front_right_door_open = False
        self.front_left_door_open = False
        self.hood_open = False
        self.engine_running = False
        self.odo_meter = 0

    async def update(self):
        data = await self._api.get_vehicle_status(self.vin)
        self.car_locked = data["carLocked"]
        self.distance_to_empty = data["distanceToEmpty"]
        self.tail_gate_open = data["doors"]["tailgateOpen"]
        self.rear_right_door_open = data["doors"]["rearRightDoorOpen"]
        self.rear_left_door_open = data["doors"]["rearLeftDoorOpen"]
        self.front_right_door_open = data["doors"]["frontRightDoorOpen"]
        self.front_left_door_open = data["doors"]["frontLeftDoorOpen"]
        self.hood_open = data["doors"]["hoodOpen"]
        self.engine_running = data["engineRunning"]
        self.odo_meter = data["odometer"]

def obj_parser(obj):
    """Parse datetime."""
    for key, val in obj.items():
        try:
            obj[key] = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S%z")
        except (TypeError, ValueError):
            pass
    return obj

def json_loads(s):
    return json.loads(s, object_hook=obj_parser)

async def main():
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(
                    prog='Volvo On Call CN',
                    description='',
                    epilog='')

    parser.add_argument('--refresh_token')
    args = parser.parse_args()

    async with ClientSession() as session:
        vehicle_api = VehicleAPI(session, args.refresh_token)
        await vehicle_api.update_access_token()
        vins = await vehicle_api.get_vehicles_vins()
        for vin in vins:
            vechicle = Vehicle(vin, vehicle_api)
            await vechicle.update()
            _LOGGER.debug(vechicle.__dict__)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
