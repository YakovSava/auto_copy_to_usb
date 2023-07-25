from os import listdir, stat
from copeer import CopyFiles
from abcdetector import ABCDetect, ABCDetectError

class LinuxDetectError(ABCDetectError):
	pass

class Detector(ABCDetect):

	def __init__(self, copeer:CopyFiles=None):
		if not copeer:
			raise LinuxDetectError('Copeer not found!')
		self.copeer = copeer
		self._paths = []

	def _start_copy(self) -> None:
		self.copeer.copy(self._paths)
	
	def _check_empty(self) -> bool:
		raise NotImplemented
	
	def _validate(self, paths:list[str]=None) -> bool:
		if paths is None:
			paths = self._paths
		return self.copeer.validate(paths)
	
	def get_usb_devices(self) -> list[str]:
		devices = [device  for device in listdir('/dev/') if device.startswith('sd') or device.startwith('mmcblk')]
		for device in devices:
			device_path = f'/dev/{device}'
			try:
				st = stat(device_path)

				if ((st.st_mode & 0o170000) == 0o100000) or (device_path not in self._paths):
					self._paths.append(device_path)
			except:
				pass
		return self._paths

	def start_copy(self, todevices:list[str]=None):
		if (todevices == self._path) or (todevices is None):
			self._start_copy()
			return self._validate()
		else:
			self.copeer.copy(todevices)
			return self._validate(todevices)