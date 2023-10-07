from os import popen, listdir
from .copeer import CopyFiles
from .abcdetect import ABCDetect, ABCDetectError

class MacDetectError(ABCDetectError):
	pass

class MacDetector(ABCDetect):

	def __init__(self, copeer:CopyFiles=None):
		if not copeer:
			raise MacDetectError("Copeer not found!")

		self.copeer = copeer
		self._paths = []

	def _start_copy(self) -> None:
		self.copeer.copy(self._paths)

	def _validate(self, paths:list[str]=None) -> None:
		if paths is None:
			paths = self._paths
		return self.copeer.validate(paths)

	def get_usb_devices(self) -> list[str]:
		pass

	def start_copy(self, todevices:list[str]=None):
		if (todevices == self._paths) or (todevices is None):
			self._start_copy()
			return self._validate()
		else:
			self.copeer.copy(todevices)
			return self._validate(todevices)