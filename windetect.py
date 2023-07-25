from os import listdir
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
	
	def _validate(self, paths:list[str]=None) -> bool:
		if paths is None:
			paths = self._paths
		return self.copeer.validate(paths)
	
	def get_usb_devices(self) -> list[str]:
			for disk in self.wmi.Win32_LogicalDisk():
				if (disk.DriveType == 5) and (disk.DeviceID not in self._paths):
					self._paths.append(disk.DeviceID)
			return self._paths

	def start_copy(self, todevices:list[str]=None):
		if todevices == self._paths:
			self._start_copy()
			self._validate()
		else:
			self.copper.copy(todevices)
			self._validate(todevices)