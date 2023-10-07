from os import popen, listdir
from .copeer import CopyFiles
from .abcdetect import ABCDetect, ABCDetectError

class MacDetectError(ABCDetectError):
	pass

class MacDetector(ABCDetect):

	def __init__(self, copeer:CopyFiles=None)