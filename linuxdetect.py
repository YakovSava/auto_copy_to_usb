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
		mounts_point_list_filtred = filter(lambda x: x[1].startswith('/dev/sd') or x[1].startswith('/dev/mmcblk') or x[1].startswith('/dev/sr'), mounts_point_list_splited)
		mounts_point_list_double_filtred = filter(lambda x: 'nodev' in x[3], mounts_point_list_filtred)
		self._paths = filter(self._check_empty, mounts_point_list_double_filtred)
		return self._paths

	def start_copy(self, todevices:list[str]=None):
		if (todevices == self._path) or (todevices is None):
			self._start_copy()
			return self._validate()
		else:
			self.copeer.copy(todevices)
			return self._validate(todevices)
