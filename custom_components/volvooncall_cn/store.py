
import logging
from typing import TypedDict, Unpack
from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import Store
from .volvooncall_cn import DOMAIN

_LOGGER = logging.getLogger(__name__)
STORE_VERSION = 1


class StoreData(TypedDict, total=False):
    """Volvo Store Data"""
    engine_duration_number: int


class VolvoStore(Store[StoreData]):
    def __init__(self, hass: HomeAssistant, vin: str):
        super().__init__(hass=hass, key=f"{DOMAIN}.{vin}", version=STORE_VERSION)
        self.data: StoreData | None = None
        self.default_data = StoreData(engine_duration_number=5)

    def get(self, key):
        assert self.data is not None
        return self.data.get(key)

    async def load_create_data(self) -> StoreData:
        self.data = await self.async_load() or self.default_data
        return self.data

    async def update(self, **kwargs: Unpack[StoreData]):
        self.data = self.data or await self.load_create_data()
        for key, value in kwargs.items():
            if value is not None and key in StoreData.__annotations__:
                self.data[key] = value
        await self.async_save(self.data)

    def get_engine_duration_number(self):
        self.data = self.data or self.default_data
        return self.data.get("engine_duration_number")

    async def set_engine_duration_number(self, value):
        await self.update(engine_duration_number=int(value))
