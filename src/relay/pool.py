"""Shared device pool (see PRD: Shift hand-off with automatic session wipe)."""
from enum import Enum


class DeviceState(Enum):
    READY = "ready"
    CHECKED_OUT = "checked_out"
    WIPING = "wiping"


class DevicePool:
    def __init__(self):
        self.devices: dict[str, DeviceState] = {}

    def check_out(self, device_id: str, user_id: str) -> None:
        if self.devices.get(device_id, DeviceState.READY) is not DeviceState.READY:
            raise ValueError(f"{device_id} is not ready")
        self.devices[device_id] = DeviceState.CHECKED_OUT

    def check_in(self, device_id: str) -> None:
        self.devices[device_id] = DeviceState.WIPING
        self._wipe(device_id)
        self.devices[device_id] = DeviceState.READY

    def _wipe(self, device_id: str) -> None:
        # TODO: sign out managed apps, clear local session data (Android 16 path unverified)
        pass
