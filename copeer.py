from os import listdir
from os.path import join
from shutil import copy2
from warnings import showwarning


class CopyError(BaseException):
    pass


def _warn(text: str) -> None:
    def CopyWarning(): pass
    showwarning(text, CopyWarning, 'copeer.py', 10)


class CopyFiles:

    def __init__(self, copy_from: str=''):
        self._path_from = copy_from

    def copy(self, paths: list[str]=None) -> None:
        if paths is None:
            raise CopyError("Paths not found!")
        for path_to in paths:
            if len(listdir(path_to)) != 0:
                _warn(
                    f"Directory {path_to} not empty. Possible warnings during validation")
            for filename in listdir(self._path_from):
                copy2(join(self._path_from, filename), path_to)

    def validate(self, paths: list[str]=None) -> bool:
        original_files = listdir(self._path_from)
        checker = []
        for path in paths:
            if listdir(path) != original_files:
                _warn(
                    f'There are extraneous files in the directory. Perhaps this is a mistake')
                checker.append(False)
            else:
                checker.append(True)
        return all(checker)
