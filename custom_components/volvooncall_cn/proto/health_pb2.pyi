from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceWarning(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_WARNING_UNSPECIFIED: _ClassVar[ServiceWarning]
    SERVICE_WARNING_NO_WARNING: _ClassVar[ServiceWarning]
    SERVICE_WARNING_UNKNOWN_WARNING: _ClassVar[ServiceWarning]
    SERVICE_WARNING_REGULAR_MAINTENANCE_ALMOST_TIME_FOR_SERVICE: _ClassVar[ServiceWarning]
    SERVICE_WARNING_ENGINE_HOURS_ALMOST_TIME_FOR_SERVICE: _ClassVar[ServiceWarning]
    SERVICE_WARNING_DISTANCE_DRIVEN_ALMOST_TIME_FOR_SERVICE: _ClassVar[ServiceWarning]
    SERVICE_WARNING_REGULAR_MAINTENANCE_TIME_FOR_SERVICE: _ClassVar[ServiceWarning]
    SERVICE_WARNING_ENGINE_HOURS_TIME_FOR_SERVICE: _ClassVar[ServiceWarning]
    SERVICE_WARNING_DISTANCE_DRIVEN_TIME_FOR_SERVICE: _ClassVar[ServiceWarning]
    SERVICE_WARNING_REGULAR_MAINTENANCE_OVERDUE_FOR_SERVICE: _ClassVar[ServiceWarning]
    SERVICE_WARNING_ENGINE_HOURS_OVERDUE_FOR_SERVICE: _ClassVar[ServiceWarning]
    SERVICE_WARNING_DISTANCE_DRIVEN_OVERDUE_FOR_SERVICE: _ClassVar[ServiceWarning]

class BrakeFluidLevelWarning(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BRAKE_FLUID_LEVEL_WARNING_UNSPECIFIED: _ClassVar[BrakeFluidLevelWarning]
    BRAKE_FLUID_LEVEL_WARNING_NO_WARNING: _ClassVar[BrakeFluidLevelWarning]
    BRAKE_FLUID_LEVEL_WARNING_TOO_LOW: _ClassVar[BrakeFluidLevelWarning]

class EngineCoolantLevelWarning(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENGINE_COOLANT_LEVEL_WARNING_UNSPECIFIED: _ClassVar[EngineCoolantLevelWarning]
    ENGINE_COOLANT_LEVEL_WARNING_NO_WARNING: _ClassVar[EngineCoolantLevelWarning]
    ENGINE_COOLANT_LEVEL_WARNING_TOO_LOW: _ClassVar[EngineCoolantLevelWarning]

class OilLevelWarning(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OIL_LEVEL_WARNING_UNSPECIFIED: _ClassVar[OilLevelWarning]
    OIL_LEVEL_WARNING_NO_WARNING: _ClassVar[OilLevelWarning]
    OIL_LEVEL_WARNING_SERVICE_REQUIRED: _ClassVar[OilLevelWarning]
    OIL_LEVEL_WARNING_TOO_LOW: _ClassVar[OilLevelWarning]
    OIL_LEVEL_WARNING_TOO_HIGH: _ClassVar[OilLevelWarning]

class TyrePressureWarning(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYRE_PRESSURE_WARNING_UNSPECIFIED: _ClassVar[TyrePressureWarning]
    TYRE_PRESSURE_WARNING_NO_WARNING: _ClassVar[TyrePressureWarning]
    TYRE_PRESSURE_WARNING_VERY_LOW_PRESSURE: _ClassVar[TyrePressureWarning]
    TYRE_PRESSURE_WARNING_LOW_PRESSURE: _ClassVar[TyrePressureWarning]
    TYRE_PRESSURE_WARNING_HIGH_PRESSURE: _ClassVar[TyrePressureWarning]

class WasherFluidLevelWarning(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WASHER_FLUID_LEVEL_WARNING_UNSPECIFIED: _ClassVar[WasherFluidLevelWarning]
    WASHER_FLUID_LEVEL_WARNING_NO_WARNING: _ClassVar[WasherFluidLevelWarning]
    WASHER_FLUID_LEVEL_WARNING_TOO_LOW: _ClassVar[WasherFluidLevelWarning]

class ExteriorLightWarning(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXTERIOR_LIGHT_WARNING_UNSPECIFIED: _ClassVar[ExteriorLightWarning]
    EXTERIOR_LIGHT_WARNING_NO_WARNING: _ClassVar[ExteriorLightWarning]
    EXTERIOR_LIGHT_WARNING_FAILURE: _ClassVar[ExteriorLightWarning]

class LowVoltageBatteryWarning(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOW_VOLTAGE_BATTERY_WARNING_UNSPECIFIED: _ClassVar[LowVoltageBatteryWarning]
    LOW_VOLTAGE_BATTERY_WARNING_NO_WARNING: _ClassVar[LowVoltageBatteryWarning]
    LOW_VOLTAGE_BATTERY_WARNING_TOO_LOW: _ClassVar[LowVoltageBatteryWarning]
SERVICE_WARNING_UNSPECIFIED: ServiceWarning
SERVICE_WARNING_NO_WARNING: ServiceWarning
SERVICE_WARNING_UNKNOWN_WARNING: ServiceWarning
SERVICE_WARNING_REGULAR_MAINTENANCE_ALMOST_TIME_FOR_SERVICE: ServiceWarning
SERVICE_WARNING_ENGINE_HOURS_ALMOST_TIME_FOR_SERVICE: ServiceWarning
SERVICE_WARNING_DISTANCE_DRIVEN_ALMOST_TIME_FOR_SERVICE: ServiceWarning
SERVICE_WARNING_REGULAR_MAINTENANCE_TIME_FOR_SERVICE: ServiceWarning
SERVICE_WARNING_ENGINE_HOURS_TIME_FOR_SERVICE: ServiceWarning
SERVICE_WARNING_DISTANCE_DRIVEN_TIME_FOR_SERVICE: ServiceWarning
SERVICE_WARNING_REGULAR_MAINTENANCE_OVERDUE_FOR_SERVICE: ServiceWarning
SERVICE_WARNING_ENGINE_HOURS_OVERDUE_FOR_SERVICE: ServiceWarning
SERVICE_WARNING_DISTANCE_DRIVEN_OVERDUE_FOR_SERVICE: ServiceWarning
BRAKE_FLUID_LEVEL_WARNING_UNSPECIFIED: BrakeFluidLevelWarning
BRAKE_FLUID_LEVEL_WARNING_NO_WARNING: BrakeFluidLevelWarning
BRAKE_FLUID_LEVEL_WARNING_TOO_LOW: BrakeFluidLevelWarning
ENGINE_COOLANT_LEVEL_WARNING_UNSPECIFIED: EngineCoolantLevelWarning
ENGINE_COOLANT_LEVEL_WARNING_NO_WARNING: EngineCoolantLevelWarning
ENGINE_COOLANT_LEVEL_WARNING_TOO_LOW: EngineCoolantLevelWarning
OIL_LEVEL_WARNING_UNSPECIFIED: OilLevelWarning
OIL_LEVEL_WARNING_NO_WARNING: OilLevelWarning
OIL_LEVEL_WARNING_SERVICE_REQUIRED: OilLevelWarning
OIL_LEVEL_WARNING_TOO_LOW: OilLevelWarning
OIL_LEVEL_WARNING_TOO_HIGH: OilLevelWarning
TYRE_PRESSURE_WARNING_UNSPECIFIED: TyrePressureWarning
TYRE_PRESSURE_WARNING_NO_WARNING: TyrePressureWarning
TYRE_PRESSURE_WARNING_VERY_LOW_PRESSURE: TyrePressureWarning
TYRE_PRESSURE_WARNING_LOW_PRESSURE: TyrePressureWarning
TYRE_PRESSURE_WARNING_HIGH_PRESSURE: TyrePressureWarning
WASHER_FLUID_LEVEL_WARNING_UNSPECIFIED: WasherFluidLevelWarning
WASHER_FLUID_LEVEL_WARNING_NO_WARNING: WasherFluidLevelWarning
WASHER_FLUID_LEVEL_WARNING_TOO_LOW: WasherFluidLevelWarning
EXTERIOR_LIGHT_WARNING_UNSPECIFIED: ExteriorLightWarning
EXTERIOR_LIGHT_WARNING_NO_WARNING: ExteriorLightWarning
EXTERIOR_LIGHT_WARNING_FAILURE: ExteriorLightWarning
LOW_VOLTAGE_BATTERY_WARNING_UNSPECIFIED: LowVoltageBatteryWarning
LOW_VOLTAGE_BATTERY_WARNING_NO_WARNING: LowVoltageBatteryWarning
LOW_VOLTAGE_BATTERY_WARNING_TOO_LOW: LowVoltageBatteryWarning

class GetHealthReq(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...

class TimeStamp(_message.Message):
    __slots__ = ("seconds", "nanos")
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    seconds: int
    nanos: int
    def __init__(self, seconds: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...

class HealthStatus(_message.Message):
    __slots__ = ("timestamp", "engine_hours_to_service", "days_to_service", "distance_to_service_km", "service_warning", "brake_fluid_level_warning", "engine_coolant_level_warning", "oil_level_warning", "front_left_tyre_pressure_warning", "front_right_tyre_pressure_warning", "rear_left_tyre_pressure_warning", "rear_right_tyre_pressure_warning", "washer_fluid_level_warning", "brake_light_left_warning", "brake_light_center_warning", "brake_light_right_warning", "fog_light_front_warning", "fog_light_rear_warning", "position_light_front_left_warning", "position_light_front_right_warning", "position_light_rear_left_warning", "position_light_rear_right_warning", "high_beam_left_warning", "high_beam_right_warning", "low_beam_left_warning", "low_beam_right_warning", "daytime_running_light_left_warning", "daytime_running_light_right_warning", "turn_indication_front_left_warning", "turn_indication_front_right_warning", "turn_indication_rear_left_warning", "turn_indication_rear_right_warning", "registration_plate_light_warning", "side_mark_lights_warning", "hazard_lights_warning", "reverse_lights_warning", "low_voltage_battery_warning", "front_left_tyre_pressure_kpa", "front_right_tyre_pressure_kpa", "rear_left_tyre_pressure_kpa", "rear_right_tyre_pressure_kpa")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ENGINE_HOURS_TO_SERVICE_FIELD_NUMBER: _ClassVar[int]
    DAYS_TO_SERVICE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_TO_SERVICE_KM_FIELD_NUMBER: _ClassVar[int]
    SERVICE_WARNING_FIELD_NUMBER: _ClassVar[int]
    BRAKE_FLUID_LEVEL_WARNING_FIELD_NUMBER: _ClassVar[int]
    ENGINE_COOLANT_LEVEL_WARNING_FIELD_NUMBER: _ClassVar[int]
    OIL_LEVEL_WARNING_FIELD_NUMBER: _ClassVar[int]
    FRONT_LEFT_TYRE_PRESSURE_WARNING_FIELD_NUMBER: _ClassVar[int]
    FRONT_RIGHT_TYRE_PRESSURE_WARNING_FIELD_NUMBER: _ClassVar[int]
    REAR_LEFT_TYRE_PRESSURE_WARNING_FIELD_NUMBER: _ClassVar[int]
    REAR_RIGHT_TYRE_PRESSURE_WARNING_FIELD_NUMBER: _ClassVar[int]
    WASHER_FLUID_LEVEL_WARNING_FIELD_NUMBER: _ClassVar[int]
    BRAKE_LIGHT_LEFT_WARNING_FIELD_NUMBER: _ClassVar[int]
    BRAKE_LIGHT_CENTER_WARNING_FIELD_NUMBER: _ClassVar[int]
    BRAKE_LIGHT_RIGHT_WARNING_FIELD_NUMBER: _ClassVar[int]
    FOG_LIGHT_FRONT_WARNING_FIELD_NUMBER: _ClassVar[int]
    FOG_LIGHT_REAR_WARNING_FIELD_NUMBER: _ClassVar[int]
    POSITION_LIGHT_FRONT_LEFT_WARNING_FIELD_NUMBER: _ClassVar[int]
    POSITION_LIGHT_FRONT_RIGHT_WARNING_FIELD_NUMBER: _ClassVar[int]
    POSITION_LIGHT_REAR_LEFT_WARNING_FIELD_NUMBER: _ClassVar[int]
    POSITION_LIGHT_REAR_RIGHT_WARNING_FIELD_NUMBER: _ClassVar[int]
    HIGH_BEAM_LEFT_WARNING_FIELD_NUMBER: _ClassVar[int]
    HIGH_BEAM_RIGHT_WARNING_FIELD_NUMBER: _ClassVar[int]
    LOW_BEAM_LEFT_WARNING_FIELD_NUMBER: _ClassVar[int]
    LOW_BEAM_RIGHT_WARNING_FIELD_NUMBER: _ClassVar[int]
    DAYTIME_RUNNING_LIGHT_LEFT_WARNING_FIELD_NUMBER: _ClassVar[int]
    DAYTIME_RUNNING_LIGHT_RIGHT_WARNING_FIELD_NUMBER: _ClassVar[int]
    TURN_INDICATION_FRONT_LEFT_WARNING_FIELD_NUMBER: _ClassVar[int]
    TURN_INDICATION_FRONT_RIGHT_WARNING_FIELD_NUMBER: _ClassVar[int]
    TURN_INDICATION_REAR_LEFT_WARNING_FIELD_NUMBER: _ClassVar[int]
    TURN_INDICATION_REAR_RIGHT_WARNING_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_PLATE_LIGHT_WARNING_FIELD_NUMBER: _ClassVar[int]
    SIDE_MARK_LIGHTS_WARNING_FIELD_NUMBER: _ClassVar[int]
    HAZARD_LIGHTS_WARNING_FIELD_NUMBER: _ClassVar[int]
    REVERSE_LIGHTS_WARNING_FIELD_NUMBER: _ClassVar[int]
    LOW_VOLTAGE_BATTERY_WARNING_FIELD_NUMBER: _ClassVar[int]
    FRONT_LEFT_TYRE_PRESSURE_KPA_FIELD_NUMBER: _ClassVar[int]
    FRONT_RIGHT_TYRE_PRESSURE_KPA_FIELD_NUMBER: _ClassVar[int]
    REAR_LEFT_TYRE_PRESSURE_KPA_FIELD_NUMBER: _ClassVar[int]
    REAR_RIGHT_TYRE_PRESSURE_KPA_FIELD_NUMBER: _ClassVar[int]
    timestamp: TimeStamp
    engine_hours_to_service: int
    days_to_service: int
    distance_to_service_km: int
    service_warning: ServiceWarning
    brake_fluid_level_warning: BrakeFluidLevelWarning
    engine_coolant_level_warning: EngineCoolantLevelWarning
    oil_level_warning: OilLevelWarning
    front_left_tyre_pressure_warning: TyrePressureWarning
    front_right_tyre_pressure_warning: TyrePressureWarning
    rear_left_tyre_pressure_warning: TyrePressureWarning
    rear_right_tyre_pressure_warning: TyrePressureWarning
    washer_fluid_level_warning: WasherFluidLevelWarning
    brake_light_left_warning: ExteriorLightWarning
    brake_light_center_warning: ExteriorLightWarning
    brake_light_right_warning: ExteriorLightWarning
    fog_light_front_warning: ExteriorLightWarning
    fog_light_rear_warning: ExteriorLightWarning
    position_light_front_left_warning: ExteriorLightWarning
    position_light_front_right_warning: ExteriorLightWarning
    position_light_rear_left_warning: ExteriorLightWarning
    position_light_rear_right_warning: ExteriorLightWarning
    high_beam_left_warning: ExteriorLightWarning
    high_beam_right_warning: ExteriorLightWarning
    low_beam_left_warning: ExteriorLightWarning
    low_beam_right_warning: ExteriorLightWarning
    daytime_running_light_left_warning: ExteriorLightWarning
    daytime_running_light_right_warning: ExteriorLightWarning
    turn_indication_front_left_warning: ExteriorLightWarning
    turn_indication_front_right_warning: ExteriorLightWarning
    turn_indication_rear_left_warning: ExteriorLightWarning
    turn_indication_rear_right_warning: ExteriorLightWarning
    registration_plate_light_warning: ExteriorLightWarning
    side_mark_lights_warning: ExteriorLightWarning
    hazard_lights_warning: ExteriorLightWarning
    reverse_lights_warning: ExteriorLightWarning
    low_voltage_battery_warning: LowVoltageBatteryWarning
    front_left_tyre_pressure_kpa: float
    front_right_tyre_pressure_kpa: float
    rear_left_tyre_pressure_kpa: float
    rear_right_tyre_pressure_kpa: float
    def __init__(self, timestamp: _Optional[_Union[TimeStamp, _Mapping]] = ..., engine_hours_to_service: _Optional[int] = ..., days_to_service: _Optional[int] = ..., distance_to_service_km: _Optional[int] = ..., service_warning: _Optional[_Union[ServiceWarning, str]] = ..., brake_fluid_level_warning: _Optional[_Union[BrakeFluidLevelWarning, str]] = ..., engine_coolant_level_warning: _Optional[_Union[EngineCoolantLevelWarning, str]] = ..., oil_level_warning: _Optional[_Union[OilLevelWarning, str]] = ..., front_left_tyre_pressure_warning: _Optional[_Union[TyrePressureWarning, str]] = ..., front_right_tyre_pressure_warning: _Optional[_Union[TyrePressureWarning, str]] = ..., rear_left_tyre_pressure_warning: _Optional[_Union[TyrePressureWarning, str]] = ..., rear_right_tyre_pressure_warning: _Optional[_Union[TyrePressureWarning, str]] = ..., washer_fluid_level_warning: _Optional[_Union[WasherFluidLevelWarning, str]] = ..., brake_light_left_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., brake_light_center_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., brake_light_right_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., fog_light_front_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., fog_light_rear_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., position_light_front_left_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., position_light_front_right_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., position_light_rear_left_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., position_light_rear_right_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., high_beam_left_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., high_beam_right_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., low_beam_left_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., low_beam_right_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., daytime_running_light_left_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., daytime_running_light_right_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., turn_indication_front_left_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., turn_indication_front_right_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., turn_indication_rear_left_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., turn_indication_rear_right_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., registration_plate_light_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., side_mark_lights_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., hazard_lights_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., reverse_lights_warning: _Optional[_Union[ExteriorLightWarning, str]] = ..., low_voltage_battery_warning: _Optional[_Union[LowVoltageBatteryWarning, str]] = ..., front_left_tyre_pressure_kpa: _Optional[float] = ..., front_right_tyre_pressure_kpa: _Optional[float] = ..., rear_left_tyre_pressure_kpa: _Optional[float] = ..., rear_right_tyre_pressure_kpa: _Optional[float] = ...) -> None: ...

class GetHealthResp(_message.Message):
    __slots__ = ("vin", "data")
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    vin: str
    data: HealthStatus
    def __init__(self, vin: _Optional[str] = ..., data: _Optional[_Union[HealthStatus, _Mapping]] = ...) -> None: ...
