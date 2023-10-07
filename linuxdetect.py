from os import popen, listdir
from .copeer import CopyFiles
from .abcdetector import ABCDetect, ABCDetectError

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
	
	def _check_empty(self, lst:list[str]) -> bool:
		return listdir(lst[0]) <= 0
	
	def _validate(self, paths:list[str]=None) -> bool:
		if paths is None:
			paths = self._paths
		return self.copeer.validate(paths)
	
	def get_usb_devices(self) -> list[str]:
		mounts_point_list = popen('findmnt').read().splitlines()
		mounts_point_list_splited = map(lambda x: x.split(), mounts_point_list)
		for info in filter(lambda x: x[1].startswith('/dev/sd') or x[1].startswith('/dev/mmcblk') or x[1].startswith('/dev/sr'), mounts_point_list_splited):
			if info[1].startswith('/dev/sd'):
				for info_line in popen(f'udevadm info --query=all --name={info[1]}').read().splitlines():
					if (info_line.startswith('E: DEVPATH')) and ('usb' in info_line):
						if info[1] not in self._paths:
							self._paths.append(info[0])
			else:
				if info[1] not in self._paths:
					self._paths.append(info[0])
		return self._paths

	def start_copy(self, todevices:list[str]=None):
		if (todevices == self._paths) or (todevices is None):
			self._start_copy()
			return self._validate()
		else:
			self.copeer.copy(todevices)
			return self._validate(todevices)
