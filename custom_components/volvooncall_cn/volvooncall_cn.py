import logging

import base64
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
import math

from aiohttp import ClientSession, ClientTimeout, BasicAuth
from aiohttp.hdrs import METH_GET, METH_POST

from sign import sign_request

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

DIGITALVOLVO_HEADERS = {
    "Content-Type": "application/json",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "X-Ca-Version": "1.0",
    "x-sdk-content-sha256": "UNSIGNED-PAYLOAD",
    "version": "5.27.0",
    "Accept": "application/json; charset=utf-8",
}

DIGITALVOLVO_URL = "https://apigateway.digitalvolvo.com"
VOCAPI_URL = "https://vocapi.cn.prod.vocw.cn"

TIMEOUT = timedelta(seconds=10)
MAX_RETRIES = 3


class VolvoAPIError(Exception):
    def __init__(self, message):
        self.message = message

class VehicleAPI:
    def __init__(self, session, username, password):
        self._session = session
        self._username = username
        self._password = password

        self._refresh_token = ""
        self._digitalvolvo_access_token = ""
        self._vocapi_access_token = ""
        self._access_token_expire_at = 0

    async def _request_vocapi(self, method, url, headers, **kwargs):
        for i in range(MAX_RETRIES):
            try:
                final_headers = {}
                for k in VOCAPI_HEADERS:
                    final_headers[k] = VOCAPI_HEADERS[k]
                for k in headers:
                    final_headers[k] = headers[k]

                final_headers["authorization"] = "Bearer " + self._vocapi_access_token

                async with self._session.request(
                        method,
                        url,
                        headers=final_headers,
                        timeout=ClientTimeout(total=TIMEOUT.seconds),
                        **kwargs
                ) as response:
                    response.raise_for_status()
                    res = await response.json(loads=json_loads)
                    return res
            except Exception as error:
                _LOGGER.warning(
                    "Failure when communicating with the server: %s",
                    error,
                    exc_info=True,
                )
                if i < MAX_RETRIES - 1:  # Don't delay on last attempt
                    await asyncio.sleep(2**i)  # Exponential backoff
                else:
                    raise

    async def _request_digitalvolvo(self, method, url, headers, **kwargs):
        for i in range(MAX_RETRIES):
            try:
                final_headers = {}
                for k in DIGITALVOLVO_HEADERS:
                    final_headers[k] = DIGITALVOLVO_HEADERS[k]

                for k in headers:
                    final_headers[k] = headers[k]

                if self._digitalvolvo_access_token:
                    final_headers["authorization"] = "Bearer " + self._digitalvolvo_access_token

                sign = sign_request(url, method, kwargs.get('body', None))
                final_headers["x-sdk-date"] = sign['x-sdk-date']
                final_headers["v587sign"] = sign['v587sign']

                async with self._session.request(
                        method,
                        url,
                        headers=final_headers,
                        timeout=ClientTimeout(total=TIMEOUT.seconds),
                        **kwargs
                ) as response:
                    response.raise_for_status()
                    res = await response.json(loads=json_loads)

                    if not res["success"]:
                        raise VolvoAPIError(res["errMsg"])

                    return res
            except Exception as error:
                _LOGGER.warning(
                    "Failure when communicating with the server: %s",
                    error,
                    exc_info=True,
                )
                if i < MAX_RETRIES - 1:  # Don't delay on last attempt
                    await asyncio.sleep(2**i)  # Exponential backoff
                else:
                    raise

    async def vocapi_get(self, url, headers):
        """Perform a query to the online service."""
        return await self._request_vocapi(METH_GET, url, headers)

    async def vocapi_post(self, url, headers, data):
        """Perform a query to the online service."""
        return await self._request_vocapi(METH_POST, url, headers, json=data)

    async def digitalvolvo_get(self, url, headers):
        """Perform a query to the online service."""
        return await self._request_digitalvolvo(METH_GET, url, headers)

    async def digitalvolvo_post(self, url, headers, data):
        """Perform a query to the online service."""
        return await self._request_digitalvolvo(METH_POST, url, headers, json=data)

    async def login(self):
        now = int(time.time())

        if (self._access_token_expire_at - now) >= 60*10:
            return

        url = urljoin(DIGITALVOLVO_URL, "/app/iam/api/v1/auth")
        result = await self.digitalvolvo_post(url, {}, {
            "authType": "password",
            "password": self._password,
            "phoneNumber": "0086" + self._username
        })

        if not result["success"]:
            return

        if not result["data"]["globalAccessToken"]:
            return

        if not result["data"]["accessToken"]:
            return

        self._refresh_token = result["data"]["refreshToken"]
        self._vocapi_access_token = result["data"]["globalAccessToken"]
        self._digitalvolvo_access_token = result["data"]["accessToken"]
        now = int(time.time())
        self._access_token_expire_at = now + int(result["data"]["expiresIn"])

    async def update_token(self):
        now = int(time.time())

        if (self._access_token_expire_at - now) >= 60*10:
            return

        url = urljoin(DIGITALVOLVO_URL, "/app/iam/api/v1/refreshToken?refreshToken=" + self._refresh_token)

        result = await self.digitalvolvo_get(url, {})
        self._refresh_token = result["data"]["refreshToken"]
        self._vocapi_access_token = result["data"]["globalAccessToken"]
        self._digitalvolvo_access_token = result["data"]["accessToken"]
        self._access_token_expire_at = now + int(result["data"]["expiresIn"])

    async def get_vehicles(self):
        url = urljoin(DIGITALVOLVO_URL, "/app/account/vehicles/api/v1/owner/listBindCar")
        result = await self.digitalvolvo_get(url, {})
        if result['success']:
            return result['data']

        return []

    async def get_vehicles_vins(self):
        data = await self.get_vehicles()
        vins = []
        for k in data:
            vins.append(k["vinCode"])

        return vins

    async def get_vehicle_status(self, vin):
        url = urljoin(VOCAPI_URL, "/customerapi/rest/vehicles/" + vin + "/status")
        return await self.vocapi_get(url, {
            "content-type": "application/vnd.wirelesscar.com.voc.VehicleStatus.v8+json; charset=utf-8",
            "accept": "application/vnd.wirelesscar.com.voc.VehicleStatus.v8+json; charset=utf-8",
        })

    async def get_vehicle_position(self, vin):
        url = urljoin(VOCAPI_URL, "/customerapi/rest/vehicles/" + vin + "/position")
        return await self.vocapi_get(url, {
            "content-type": "application/json; charset=utf-8",
            "accept": "application/vnd.wirelesscar.com.voc.Position.v4+json; charset=utf-8",
        })

    async def lock_vehicle(self, vin):
        url = urljoin(VOCAPI_URL, "/customerapi/rest/vehicles/" + vin + "/lock")
        return await self.vocapi_post(url, {
            "content-type": "application/json; charset=utf-8",
            "accept": "application/vnd.wirelesscar.com.voc.Service.v4+json; charset=utf-8",
        }, None)

    async def unlock_vehicle(self, vin):
        url = urljoin(VOCAPI_URL, "/customerapi/rest/vehicles/" + vin + "/unlock")
        return await self.vocapi_post(url, {
            "content-type": "application/json; charset=utf-8",
            "accept": "application/vnd.wirelesscar.com.voc.Service.v4+json; charset=utf-8",
        }, None)

    async def get_vehicle_active_services(self, vin):
        url = urljoin(VOCAPI_URL, "/customerapi/rest/vehicles/" + vin + "/services?active=true")
        return await self.vocapi_get(url, {
            "content-type": "application/json; charset=utf-8",
            "accept": "application/vnd.wirelesscar.com.voc.Services.v4+json; charset=utf-8",
        })


class Vehicle:

    def __init__(self, vin, api):
        self.vin = vin
        self._api = api

        self.series_name = ""
        self.model_name = ""
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
        self.sunroof_open = False
        self.engine_running = False
        self.odo_meter = 0
        self.front_left_window_open = False
        self.front_right_window_open = False
        self.rear_left_window_open = False
        self.rear_right_window_open = False
        self.fuel_amount = 0
        self.fuel_amount_level = 0
        self.position = {
            "longitude": 0.0,
            "latitude": 0.0
        }
        self.position_wgs84 = {
            "longitude": 0.0,
            "latitude": 0.0
        }

        self.remote_door_unlock = False

    def toMap(self):
        return {
            "series_name": self.series_name,
            "model_name": self.model_name,
            "car_locked": self.car_locked,
            "car_lock_open": not self.car_locked,
            "car_locked_updated_at": self.car_locked_updated_at,
            "distance_to_empty": self.distance_to_empty,
            "distance_to_empty_updated_at": self.distance_to_empty_updated_at,
            "tail_gate_open": self.tail_gate_open,
            "rear_right_door_open": self.rear_right_door_open,
            "rear_left_door_open": self.rear_left_door_open,
            "front_right_door_open": self.front_right_door_open,
            "front_left_door_open": self.front_left_door_open,
            "hood_open": self.hood_open,
            "sunroof_open": self.sunroof_open,
            "engine_running": self.engine_running,
            "odo_meter": self.odo_meter,
            "front_left_window_open": self.front_left_window_open,
            "front_right_window_open": self.front_right_window_open,
            "rear_left_window_open": self.rear_left_window_open,
            "rear_right_window_open": self.rear_right_window_open,
            "fuel_amount": self.fuel_amount,
            "fuel_amount_level": self.fuel_amount_level,
            "position": {
                "longitude": self.position["longitude"],
                "latitude": self.position["latitude"],
            },
            "position_wgs84": {
                "longitude": self.position_wgs84["longitude"],
                "latitude": self.position_wgs84["latitude"],
            },
            "remote_door_unlock": self.remote_door_unlock,

        }

    async def update(self):
        if not self.series_name:
            vehicles = await self._api.get_vehicles()
            for vehicle in vehicles:
                if vehicle["vinCode"] == self.vin:
                    self.series_name = vehicle["seriesName"]
                    self.model_name = vehicle["modelName"]

        data = await self._api.get_vehicle_status(self.vin)
        self.car_locked = data["carLocked"]
        self.distance_to_empty = data["distanceToEmpty"]
        self.tail_gate_open = data["doors"]["tailgateOpen"]
        self.rear_right_door_open = data["doors"]["rearRightDoorOpen"]
        self.rear_left_door_open = data["doors"]["rearLeftDoorOpen"]
        self.front_right_door_open = data["doors"]["frontRightDoorOpen"]
        self.front_left_door_open = data["doors"]["frontLeftDoorOpen"]
        self.hood_open = data["doors"]["hoodOpen"]
        self.sunroof_open = data["sunroofOpen"]
        self.engine_running = data["engineRunning"]
        self.odo_meter = int(data["odometer"] / 1000)
        self.front_left_window_open = data["windows"]["frontLeftWindowOpen"]
        self.front_right_window_open = data["windows"]["frontRightWindowOpen"]
        self.rear_left_window_open = data["windows"]["rearLeftWindowOpen"]
        self.rear_right_window_open = data["windows"]["rearRightWindowOpen"]
        self.fuel_amount = data["fuelAmount"]
        self.fuel_amount_level = data["fuelAmountLevel"]

        position_data = await self._api.get_vehicle_position(self.vin)
        self.position = {
            "longitude": position_data["position"]["longitude"],
            "latitude": position_data["position"]["latitude"]
        }
        wgs84_data = gcj02towgs84(self.position["longitude"], self.position["latitude"])
        self.position_wgs84 = {
            "longitude": wgs84_data[0],
            "latitude": wgs84_data[1]
        }

        services_resp = await self._api.get_vehicle_active_services(self.vin)
        is_rdu_existed = False
        if "services" in services_resp:
            for service in services_resp["services"]:
                if service["serviceType"] == "RDU" and service["status"] == "MessageDelivered":
                    is_rdu_existed = True
                    self.remote_door_unlock = True

        if not is_rdu_existed:
            self.remote_door_unlock = False

    async def unlock(self):
        await self._api.unlock_vehicle(self.vin)

    async def lock(self):
        await self._api.lock_vehicle(self.vin)

def json_loads(s):
    return json.loads(s)

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626 # π
a = 6378245.0 # 长半轴
ee = 0.00669342162296594323 # 扁率
def gcj02towgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]

def transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + 0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
    math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
    math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret

def transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + 0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret

async def main():
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(
                    prog='Volvo On Call CN',
                    description='',
                    epilog='')

    parser.add_argument('--username')
    parser.add_argument('--password')
    args = parser.parse_args()

    async with ClientSession() as session:
        vehicle_api = VehicleAPI(session, args.username, args.password)
        await vehicle_api.login()
        await vehicle_api.update_token()
        vins = await vehicle_api.get_vehicles_vins()
        for vin in vins:
            vehicle = Vehicle(vin, vehicle_api)
            await vehicle.update()
            _LOGGER.debug(vehicle.__dict__)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
