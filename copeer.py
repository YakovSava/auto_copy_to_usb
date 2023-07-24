from os import listdir, system
from warnings import showwarning

def _warn(text:str) -> None:
	def CopyWarning(): pass

	showwarning(
		text,
		CopyWarning,
		'copeer.py',
		6
	)

class CopyFiles:

	def __init__(self, copy_from:str=''):
		self._path = copy_from

	def copy(self, paths:list[str]=None) -> None:
		pass