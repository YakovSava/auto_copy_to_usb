from sys import platform
from copeer import CopyFiles, CopyError
from abcdetector import ABCDetect, ABCDetectError

class NotSupported(BaseException): pass

if platform == "win32":
	from windetect import Detector
elif platform.startswith('linux'):
	from linuxdetect import Detector
else:
	raise NotSupported(f"Platform \"{platform}\" not supported!")
	
if __name__ == '__main__':
	copy = CopyFiles('from')
	detector = Detector(copy)

	assert len(detector.test_get_all_ld()) == 2
	assert detector.start_copy(['D:/']) # for Windows
else:
	assert issubclass(Detector, ABCDetect)

__all__ = (
	Detector,
	CopyFiles,
	ABCDetect,
	CopyError,
	ABCDetectError
)