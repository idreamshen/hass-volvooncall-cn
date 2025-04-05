import logging
import datetime
import grpc
import asyncio
from .volvooncall_base import VehicleBaseAPI, gcj02towgs84
from .proto.exterior_pb2_grpc import ExteriorServiceStub
from .proto.exterior_pb2 import GetExteriorReq, GetExteriorResp, ExteriorStatus
from .proto.exterior_pb2 import LockStatus, OpenStatus
from .proto.health_pb2_grpc import HealthServiceStub
from .proto.health_pb2 import GetHealthReq, GetHealthResp, HealthStatus
from .proto.fuel_pb2_grpc import FuelServiceStub
from .proto.fuel_pb2 import GetFuelReq, GetFuelResp
from .proto.invocation_pb2_grpc import InvocationServiceStub
from .proto.invocation_pb2 import invocationHead, invocationStatus, invocationControlType, invocationCommResp
from .proto.invocation_pb2 import windowControlReq
from .proto.invocation_pb2 import EngineStartReq
from .proto.invocation_pb2 import HonkFlashReq, HonkFlashType
from .proto.invocation_pb2 import LockReq, LockType
from .proto.invocation_pb2 import UnlockReq, UnlockType
from .proto.invocation_pb2 import TailgateControlReq
from .proto.invocation_pb2 import SunroofControlReq
from .proto.invocation_pb2 import UpdateStatusReq
from .proto.odometer_pb2_grpc import OdometerServiceStub
from .proto.odometer_pb2 import GetOdometerReq, GetOdometerResp
from .proto.availability_pb2_grpc import AvailabilityServiceStub
from .proto.availability_pb2 import GetAvailabilityReq, GetAvailabilityResp, AvailabilityStatus, AvailabilityReason
from .proto.dtlinternet_pb2_grpc import DtlInternetServiceStub
from .proto.dtlinternet_pb2 import StreamLastKnownLocationsReq, StreamLastKnownLocationsResp
from .proto.engineremotestart_pb2_grpc import EngineRemoteStartServiceStub
from .proto.engineremotestart_pb2 import GetEngineRemoteStartReq, GetEngineRemoteStartResp, EngineRunningStatus
from .proto.car_preferences_pb2_grpc import CarPreferencesStub
from .proto.car_preferences_pb2 import GetPreferencesReq, GetPreferencesResp
from .proto.car_preferences_pb2 import UpdatePreferencesReq, UpdatePreferencesResp, Preference


_LOGGER = logging.getLogger(__name__)

GRPC_DIGITALVOLVO_HOST = "cepmobtoken.prod.c3.volvocars.com.cn:443"
GRPC_LBS_VOLVO_HOST = "cepmobtoken.lbs.prod.c3.volvocars.com.cn:443"
USER_AGENT = "vca-android/5.51.1 grpc-java-okhttp/1.68.0"
MAX_RETRIES = 1
TIMEOUT = datetime.timedelta(seconds=10)
DOMAIN = "volvooncall_cn"


def isWindowOpen(status) -> bool:
    return status == OpenStatus.OPEN_STATUS_OPEN or status == OpenStatus.OPEN_STATUS_AJAR


class VehicleAPI(VehicleBaseAPI):
    def __init__(self, session, username, password):
        super(VehicleAPI, self).__init__(session, username, password)
        self.channel = None
        self.channel_token: str = ""
        self.lbs_channel = None
        self.lbs_channel_token: str = ""
        self.engine_duration = 5

    async def gen_channel(self, token, target):
        callCreds = grpc.access_token_call_credentials(token)
        sslCreds = grpc.ssl_channel_credentials()
        creds = grpc.composite_channel_credentials(sslCreds, callCreds)
        channel_options: tuple = (("grpc.primary_user_agent", USER_AGENT), ('grpc.accept_encoding', 'gzip'),)
        channel = grpc.secure_channel(target, creds, options=channel_options)
        return channel

    async def get_channel(self):
        if self.channel and self.channel_token == self._vocapi_access_token.strip():
            return
        self.channel_token = self._vocapi_access_token.strip()
        self.channel = await self.gen_channel(self.channel_token, GRPC_DIGITALVOLVO_HOST)

    async def get_lbs_channel(self):
        if self.lbs_channel and self.lbs_channel_token == self._vocapi_access_token.strip():
            return
        self.lbs_channel_token = self._vocapi_access_token.strip()
        self.lbs_channel = await self.gen_channel(self.lbs_channel_token, GRPC_LBS_VOLVO_HOST)

    def raise_invocation_fail(self, status):
        if status in [invocationStatus.SUCCESS, invocationStatus.SENT, invocationStatus.DELIVERED]:
            return
        if status == invocationStatus.CAR_OFFLINE:
            raise Exception("车辆离线或无网络")
        elif status in [invocationStatus.DELIVERY_TIMEOUT, invocationStatus.RESPONSE_TIMEOUT]:
            raise Exception("请求超时")
        elif status == invocationStatus.UNKNOWN_CAR_ERROR:
            raise Exception("车辆未知错误")
        elif status == invocationStatus.NOT_ALLOWED_PRIVACY_ENABLED:
            raise Exception("车辆隐私协议未同意")
        elif status == invocationStatus.NOT_ALLOWED_WRONG_USAGE_MODE:
            raise Exception("请求模式错误")
        elif status == invocationStatus.NOT_ALLOWED_CONFLICTING_INVOCATION:
            raise Exception("请求操作存在冲突")
        else:
            raise Exception("未知错误")

    async def get_fuel_status(self, vin) -> GetFuelResp:
        stub = FuelServiceStub(self.channel)
        req = GetFuelReq(vin=vin)
        metadata: list = [("vin", vin)]
        res = GetFuelResp()
        for res in stub.GetFuel(req, metadata=metadata, timeout=TIMEOUT.seconds):
            break
        return res

    async def get_exterior(self, vin) -> GetExteriorResp:
        stub = ExteriorServiceStub(self.channel)
        req = GetExteriorReq(vin=vin)
        metadata: list = [("vin", vin)]
        res = GetExteriorResp()
        for res in stub.GetExterior(req, metadata=metadata, timeout=TIMEOUT.seconds):
            break
        return res

    async def get_health(self, vin) -> GetHealthResp:
        stub = HealthServiceStub(self.channel)
        req = GetHealthReq(vin=vin)
        metadata: list = [("vin", vin)]
        res = GetHealthResp()
        for res in stub.GetHealth(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug("get_health resp")
            _LOGGER.debug(res)
            break
        return res

    async def get_odometer(self, vin) -> GetOdometerResp:
        stub = OdometerServiceStub(self.channel)
        req = GetOdometerReq(vin=vin)
        metadata: list = [("vin", vin)]
        res = GetOdometerResp()
        for res in stub.GetOdometer(req, metadata=metadata, timeout=TIMEOUT.seconds):
            break
        return res

    async def get_availability(self, vin) -> GetAvailabilityResp:
        stub = AvailabilityServiceStub(self.channel)
        req = GetAvailabilityReq(vin=vin)
        metadata: list = [("vin", vin)]
        res = GetAvailabilityResp()
        for res in stub.GetAvailability(req, metadata=metadata, timeout=TIMEOUT.seconds):
            break
        return res

    async def window_control(self, vin, opentype):
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = windowControlReq(head=req_header, openType=opentype)
        metadata: list = [("vin", vin)]
        res: invocationCommResp = invocationCommResp()
        for res in stub.WindowControl(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            self.raise_invocation_fail(res.data.status)
            break
        return

    async def get_location(self, vin) -> StreamLastKnownLocationsResp:
        await self.get_lbs_channel()
        stub = DtlInternetServiceStub(self.lbs_channel)
        req = StreamLastKnownLocationsReq(vin=vin)
        metadata: list = [("vin", vin)]
        res: StreamLastKnownLocationsResp = StreamLastKnownLocationsResp()
        for res in stub.StreamLastKnownLocations(req, metadata=metadata, timeout=TIMEOUT.seconds):
            break
        return res

    async def engine_control(self, vin, isStart: bool):
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = EngineStartReq()
        if isStart:
            duration = int(self.engine_duration)
            req = EngineStartReq(head=req_header, isStart=isStart, startDurationMin=duration)
        else:
            req = EngineStartReq(head=req_header, isStart=isStart)
        metadata: list = [("vin", vin)]
        res: invocationCommResp = invocationCommResp()
        for res in stub.EngineStart(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            self.raise_invocation_fail(res.data.status)
            break
        return

    async def honk_flash_control(self, vin, honk_flash_type: HonkFlashType):
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = HonkFlashReq(head=req_header, honkFlashType=honk_flash_type)
        metadata: list = [("vin", vin)]
        res: invocationCommResp = invocationCommResp()
        for res in stub.HonkFlash(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            self.raise_invocation_fail(res.data.status)
            break
        return

    async def door_lock(self, vin):
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = LockReq(head=req_header, lockType=LockType.LOCK_REDUCED_GUARD)
        metadata: list = [("vin", vin)]
        res: invocationCommResp = invocationCommResp()
        for res in stub.Lock(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            self.raise_invocation_fail(res.data.status)
            break
        return

    async def door_unlock(self, vin, unlockType):
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = UnlockReq(head=req_header)
        if unlockType != UnlockType.UNLOCK_UNSPECIFIED:
            req = UnlockReq(head=req_header, unlockType=unlockType)
        metadata: list = [("vin", vin)]
        res: invocationCommResp = invocationCommResp()
        for res in stub.Unlock(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            self.raise_invocation_fail(res.data.status)
            break
        return

    async def get_engine_status(self, vin):
        stub = EngineRemoteStartServiceStub(self.channel)
        req = GetEngineRemoteStartReq(vin=vin)
        metadata: list = [("vin", vin)]
        res: GetEngineRemoteStartResp = GetEngineRemoteStartResp()
        for res in stub.GetEngineRemoteStart(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            break
        return res

    async def sunroof_contorl(self, vin: str, controlType: invocationControlType):
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = SunroofControlReq(head=req_header, type=controlType)
        metadata: list = [("vin", vin)]
        res: invocationCommResp = invocationCommResp()
        for res in stub.SunroofControl(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            self.raise_invocation_fail(res.data.status)
            break
        return

    async def tailgate_contorl(self, vin: str, controlType: invocationControlType):
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = TailgateControlReq(head=req_header, type=controlType)
        metadata: list = [("vin", vin)]
        res: invocationCommResp = invocationCommResp()
        for res in stub.TailgateControl(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            self.raise_invocation_fail(res.data.status)
            break
        return

    async def update_status(self, vin: str):
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = UpdateStatusReq(head=req_header)
        metadata: list = [("vin", vin)]
        res: invocationCommResp = invocationCommResp()
        for res in stub.UpdateStatus(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug("update_status resp")
            _LOGGER.debug(res)
            self.raise_invocation_fail(res.data.status)
            break
        return

    async def get_car_preferences(self, vin: str):
        stub = CarPreferencesStub(self.channel)
        req = GetPreferencesReq(vin=vin)
        metadata: list = [("vin", vin)]
        res: GetPreferencesResp = GetPreferencesResp()
        for res in stub.GetPreferences(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            break
        return res

    async def update_car_preference(self, vin: str, nickname: str):
        stub = CarPreferencesStub(self.channel)
        preference = Preference(nickName=nickname)
        req = UpdatePreferencesReq(vin=vin, preference=preference)
        metadata: list = [("vin", vin)]
        res: UpdatePreferencesResp = UpdatePreferencesResp()
        for res in stub.UpdatePreferences(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            break
        return res


class Vehicle(object):
    def __init__(self, vin, api, isAaos):
        self.vin = vin
        self._api = api
        self.isAaos = isAaos

        self.series_name = ""
        self.model_name = ""
        self.car_locked = False
        self.distance_to_empty = 0  # 续航公里
        self.tail_gate_open = False
        self.rear_right_door_open = False
        self.rear_left_door_open = False
        self.front_right_door_open = False
        self.front_left_door_open = False
        self.hood_open = False
        self.sunroof_open = False
        self.engine_running = False
        self.engine_remote_running = False
        self.odo_meter = 0
        self.front_left_window_open = False
        self.front_right_window_open = False
        self.rear_left_window_open = False
        self.rear_right_window_open = False
        self.front_left_window_open_ajar = False
        self.front_right_window_open_ajar = False
        self.rear_left_window_open_ajar = False
        self.rear_right_window_open_ajar = False
        self.fuel_amount = 0
        self.fuel_average_consumption_liters_per_100_km = 0
        self.tank_lid_open = False
        self.availability_status = AvailabilityStatus.Available
        self.unavailable_reason = AvailabilityReason.Unspecified1
        self.engine_remote_start_time = 0
        self.engine_remote_end_time = 0
        # self.fuel_amount_level = 0
        self.position = {
            "longitude": 0.0,
            "latitude": 0.0
        }
        self.position_wgs84 = {
            "longitude": 0.0,
            "latitude": 0.0
        }
        self.service_warning_msg = "1"
        self.service_warning = False
        self.brake_fluid_level_warning = False
        self.engine_coolant_level_warning = False
        self.oil_level_warning = False
        self.washer_fluid_level_warning = False
        self.front_left_tyre_pressure_warning = False
        self.front_right_tyre_pressure_warning = False
        self.rear_left_tyre_pressure_warning = False
        self.rear_right_tyre_pressure_warning = False
        self.nickname = ""

    async def _parse_exterior(self):
        try:
            exterior_resp: GetExteriorResp = await self._api.get_exterior(self.vin)
            exterior_status: ExteriorStatus = exterior_resp.data
            _LOGGER.debug(exterior_status)
        except Exception as err:
            _LOGGER.error(err)
            return
        self.car_locked = exterior_status.central_lock == LockStatus.LOCK_STATUS_LOCKED
        self.front_left_door_open = isWindowOpen(exterior_status.front_left_door)
        self.front_right_door_open = isWindowOpen(exterior_status.front_right_door)
        self.rear_left_door_open = isWindowOpen(exterior_status.rear_left_door)
        self.rear_right_door_open = isWindowOpen(exterior_status.rear_right_door)
        self.sunroof_open = isWindowOpen(exterior_status.sunroof)
        self.tail_gate_open = isWindowOpen(exterior_status.tailgate)
        self.hood_open = isWindowOpen(exterior_status.hood)
        self.tank_lid_open = isWindowOpen(exterior_status.tank_lid)
        window_sensors = ["front_left_window", "front_right_window", "rear_left_window", "rear_right_window"]
        for window_sensor in window_sensors:
            status = getattr(exterior_status, window_sensor)
            openkey = window_sensor + "_open"
            ajarkey = window_sensor + "_open_ajar"
            if status == OpenStatus.OPEN_STATUS_OPEN:
                setattr(self, openkey, True)
                setattr(self, ajarkey, False)
            elif status == OpenStatus.OPEN_STATUS_AJAR:
                setattr(self, openkey, True)
                setattr(self, ajarkey, True)
            else:
                setattr(self, openkey, False)
                setattr(self, ajarkey, False)

    async def _parse_health(self):
        try:
            health_resp: GetHealthResp = await self._api.get_health(self.vin)
            health_status: HealthStatus = health_resp.data

            # Set the service_warning field based on the enum value
            self.service_warning_msg = health_status.service_warning
            self.service_warning = health_status.service_warning > 1
            self.brake_fluid_level_warning = health_status.brake_fluid_level_warning > 1
            self.engine_coolant_level_warning = health_status.engine_coolant_level_warning > 1
            self.oil_level_warning = health_status.oil_level_warning > 1
            self.washer_fluid_level_warning = health_status.washer_fluid_level_warning > 1
            self.front_left_tyre_pressure_warning = health_status.front_left_tyre_pressure_warning > 1
            self.front_right_tyre_pressure_warning = health_status.front_right_tyre_pressure_warning > 1
            self.rear_left_tyre_pressure_warning = health_status.rear_left_tyre_pressure_warning > 1
            self.rear_right_tyre_pressure_warning = health_status.rear_right_tyre_pressure_warning > 1

        except Exception as err:
            _LOGGER.error(err)
            return

    async def _parse_fuel(self):
        try:
            fuel_resp: GetFuelResp = await self._api.get_fuel_status(self.vin)
            fuel_data = fuel_resp.data
            _LOGGER.debug(fuel_data)
        except Exception as err:
            _LOGGER.error(err)
            return
        self.fuel_amount = round(fuel_data.fuelAmount, 2)
        self.distance_to_empty = fuel_data.distanceToEmptyKm
        self.fuel_average_consumption_liters_per_100_km = fuel_data.TMFuelAvgConsum
        # self.fuel_amount_level = fuel_data.fluelHalfLevel / 5

    async def _parse_odometer(self):
        try:
            odometer_resp: GetOdometerResp = await self._api.get_odometer(self.vin)
            odometer_data = odometer_resp.data
            _LOGGER.debug(odometer_data)
        except Exception as err:
            _LOGGER.error(err)
            return
        self.odo_meter = odometer_data.odometerMeters / 1000

    async def _parse_availability(self):
        try:
            availability_resp: GetAvailabilityResp = await self._api.get_availability(self.vin)
            availability_data = availability_resp.data
            _LOGGER.debug(availability_data)
        except Exception as err:
            _LOGGER.error(err)
            return
        self.availability_status = availability_data.availableStatus
        self.unavailable_reason = availability_data.unavailableReason
        self.engine_running = self.availability_status == AvailabilityStatus.Unavailable and self.unavailable_reason == AvailabilityReason.CarInUse

    async def _parse_location(self):
        try:
            location_resp: StreamLastKnownLocationsResp = await self._api.get_location(self.vin)
        except Exception as err:
            _LOGGER.error(err)
            return
        self.position = {
            "latitude": location_resp.latitude,
            "longitude": location_resp.longitude,
        }
        wgs84_data = gcj02towgs84(self.position["longitude"], self.position["latitude"])
        if len(wgs84_data) >= 2:
            self.position_wgs84 = {
                "longitude": wgs84_data[0],
                "latitude": wgs84_data[1],
            }

    async def _parse_engine_status(self):
        try:
            engine_resp: GetEngineRemoteStartResp = await self._api.get_engine_status(self.vin)
            engine_data = engine_resp.data
        except Exception as err:
            _LOGGER.error(err)
            return
        if engine_data.engineRunningStatus in [EngineRunningStatus.Starting, EngineRunningStatus.Running]:
            self.engine_remote_running = True
            self.engine_running = True
        else:
            self.engine_remote_running = False
        self.engine_remote_start_time = engine_data.engineStartTime
        self.engine_remote_end_time = engine_data.engineEndTime

    async def _parse_car_preference(self):
        try:
            preference_resp: GetPreferencesResp = await self._api.get_car_preferences(self.vin)
            _LOGGER.debug("preference:%s", preference_resp)
        except Exception as err:
            _LOGGER.error(err)
            return
        if preference_resp and preference_resp.preference:
            self.nickname = preference_resp.preference.nickName

    async def update(self):
        if not self.series_name:
            vehicles = await self._api.get_vehicles()
            for vehicle in vehicles:
                if vehicle["vinCode"] == self.vin:
                    self.series_name = vehicle["seriesName"]
                    self.model_name = vehicle["modelName"]

        tasks = []
        await self._api.get_channel()
        if not self.isAaos:
            # 旧款车机（非安卓）增加强制刷新状态接口调用
            await self._api.update_status(self.vin)
        async with asyncio.TaskGroup() as tg:
            funcs = [self._parse_exterior, self._parse_odometer,
                     self._parse_fuel, self._parse_availability,
                     self._parse_location, self._parse_engine_status,
                     self._parse_health, self._parse_car_preference]
            for runf in funcs:
                task = tg.create_task(runf())
                tasks.append(task)
        for task in tasks:
            _LOGGER.debug(task.result())

    async def lock_window(self):
        await self._api.window_control(self.vin, invocationControlType.CLOSE)

    async def unlock_window(self):
        await self._api.window_control(self.vin, invocationControlType.OPEN)

    async def lock_vehicle(self):
        await self._api.door_lock(self.vin)

    async def unlock_vehicle(self):
        await self._api.door_unlock(self.vin, UnlockType.UNLOCK_UNSPECIFIED)

    async def unlock_vehicle_trunk_only(self):
        await self._api.door_unlock(self.vin, UnlockType.TRUNK_ONLY)

    async def flash(self):
        await self._api.honk_flash_control(self.vin, HonkFlashType.FLASH)

    async def honk_and_flash(self):
        await self._api.honk_flash_control(self.vin, HonkFlashType.HONK_AND_FLASH)

    async def honk(self):
        await self._api.honk_flash_control(self.vin, HonkFlashType.HONK)

    async def engine_start(self):
        await self._api.engine_control(self.vin, True)

    async def engine_stop(self):
        await self._api.engine_control(self.vin, False)

    async def set_engine_duration(self, durationMin):
        self._api.engine_duration = durationMin

    def get_engine_duration(self) -> float:
        return self._api.engine_duration

    def get(self, key):
        if not hasattr(self, key):
            raise Exception(f"{key} not found")
        return getattr(self, key)

    async def tail_gate_control_open(self):
        await self._api.tailgate_contorl(self.vin, invocationControlType.OPEN)

    async def tail_gate_control_close(self):
        await self._api.tailgate_contorl(self.vin, invocationControlType.CLOSE)

    async def sunroof_control_open(self):
        await self._api.sunroof_contorl(self.vin, invocationControlType.OPEN)

    async def sunroof_control_close(self):
        await self._api.sunroof_contorl(self.vin, invocationControlType.CLOSE)
