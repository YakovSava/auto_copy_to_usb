from wmi import WMI
from abcdetector import ABCDetect, ABCDetectError
from copeer import CopyFiles

class WinDetectorError(ABCDetectError): pass

class Detector(ABCDetect):
	"That's USB detector for Windows OS"
	
	def __init__(self, copeer:CopyFiles=None, custom_wmi:WMI=WMI()):
		if not copeer:
			raise WinDetectorError("Copeer not found!")
		
		self.wmi = custom_wmi
		self.copeer = copeer
		self._paths = []
	
	def _start_copy(self) -> None:
		self.copeer.copy(self._paths)
	
	def _check_empty(self) -> list[str]:
		return [path for path in self._paths if len(listdir(path)) == 0]
	
	def _validate(self) -> bool:
		return all([self.copeer.dir == listdir(path) for path in self._paths])
	
	def get_usb_devices(self) -> list[str]:
			for disk in self.wmi.Win32_DiskDrive():
				if (disk.InterfaceType == "USB") and (disk.DeviceID not in self._paths):
					self._paths.append(disk.DeviceID)
			return self._paths

	def start_copy(self, frompath:str=None, todevice:list[str]=None):
		