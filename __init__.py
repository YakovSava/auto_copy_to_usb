from sys import platform
from .copeer import CopyFiles, CopyError
from .abcdetector import ABCDetect, ABCDetectError


class NotSupported(BaseException):
    pass


if platform == "win32":
    from .windetect import Detector
elif platform.startswith('linux'):
<<<<<<< HEAD
	from .linuxdetect import Detector
elif platform == "darwin":
	from .macdetect import Detector
=======
    from .linuxdetect import Detector
elif platform == "darwin":
    from .macdetect import Detector
>>>>>>> 594169bf85c9438a9ce175d9cc83974f11a64513
else:
    raise NotSupported(f"Platform \"{platform}\" not supported!")

if __name__ == '__main__':
    copy = CopyFiles('from')
    detector = Detector(copy)

    assert detector.start_copy(['D:/'])  # for Windows
else:
    assert issubclass(Detector, ABCDetect)

__all__ = (
    Detector,
    CopyFiles,
    ABCDetect,
    CopyError,
    ABCDetectError
)
