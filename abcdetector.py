from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from copeer import CopyFiles


class ABCDetectError(Exception):
    pass


class ABCDetect:
    "Abstract base class for detection USB and other removable media"
    copeer: "CopyFiles"

    def __init__(self, copeer: "CopyFiles"=None, **kwargs):
        pass

    def _start_copy(self) -> None:
        pass

    def _check_empty(self) -> bool:
        pass

    def _validate(self) -> bool:
        pass

    def get_usb_devices(self) -> list[str]:
        pass

    def start_copy(self, frompath: str=None, todevice: list[str]=None):
        pass
