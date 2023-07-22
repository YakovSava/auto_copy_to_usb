from sys import platform
from copeer import CopyFiles

class NotSupported(BaseException): pass

if platform == "win32":
	from windetect import Detector
else:
	raise NotSupported(f"Platform \"{platform}\" not supported!")
	
__all__ = (
	Detector,
	CopyFiles
)