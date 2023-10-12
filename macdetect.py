from os import popen, listdir
from os.path import isdir
from .copeer import CopyFiles
from .abcdetector import ABCDetect, ABCDetectError
<<<<<<< HEAD
=======

>>>>>>> 594169bf85c9438a9ce175d9cc83974f11a64513

class MacDetectError(ABCDetectError):
    pass

<<<<<<< HEAD
class Detector(ABCDetect):
=======
>>>>>>> 594169bf85c9438a9ce175d9cc83974f11a64513

class Detector(ABCDetect):

    def __init__(self, copeer: CopyFiles=None):
        if not copeer:
            raise MacDetectError("Copeer not found!")

        self.copeer = copeer
        self._paths = []

    def _start_copy(self) -> None:
        self.copeer.copy(self._paths)

<<<<<<< HEAD
	def get_usb_devices(self) -> list[str]:
		for line in popen('diskutil list | grep /dev/').read().splitlines():
			#print('Line: ', line)
			if popen(f'diskutil info {line.split()[0]} | grep Protocol').read().split()[1] == 'USB':
				mnt_point = ('/Volumes/' + popen(f'diskutil list {line.split()[0]}').read().splitlines()[-1].split()[2])
				#print(mnt_point)
				if (isdir(mnt_point) and (mnt_point not in self._paths)):
					#print("Mount point: ", mnt_point)
					self._paths.append(mnt_point)
		return self._paths
=======
    def _validate(self, paths: list[str]=None) -> None:
        if paths is None:
            paths = self._paths
        return self.copeer.validate(paths)
>>>>>>> 594169bf85c9438a9ce175d9cc83974f11a64513

    def get_usb_devices(self) -> list[str]:
        for line in popen('diskutil list | grep /dev/').read().splitlines():
            print('Line: ', line)
            if popen(f'diskutil info {line.split()[0]} | grep Protocol').read().split()[1] == 'USB':
                mnt_point = (
                    '/Volume/' + popen(f'diskutil list {line.split()[0]}').read().splitlines()[-1].split()[2])
                if (isdir(mnt_point) and (mnt_point not in self._paths)):
                    print("Mount point: ", mnt_point)
                    self._paths.append(mnt_point)
        return self._paths

    def start_copy(self, todevices: list[str]=None):
        if (todevices == self._paths) or (todevices is None):
            self._start_copy()
            return self._validate()
        else:
            self.copeer.copy(todevices)
            return self._validate(todevices)
