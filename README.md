# What is it?
This is a program to automatically copy data from one directory to a *flash drive* (*USB sticks*), however, it is mostly configured for **Windows** or **Linux**, but I will try to ensure **cross-platform compatibility**

# Why is this necessary?
For mass copying of data to a *USB flash drive*. I'm not sure that anyone will need it besides me.

# How to use the code?
You can use the following piece of code to copy data to flash drives:
```Python
from auto_copy_to_usb import CopyFiles, Detector, ABCDetectError
from auto_copy_to_usb.copeer import CopyError

def start_copy(copy_from:str) -> bool:
	try:
		detector = Detector(CopyFiles(copy_from))
		detector.start_copy()
	except ABCDetectError:
		return False
	except CopyError:
		return False
	else:
		return True

if __name__ == '__main__':
	start_copy('from')
```
However, you should understand that warnings (for example, that the flash drive is not empty) will be output to the console:
```
copeer.py:10: CopyWarning: Directory D:/ not empty. Possible warnings during validation
  showwarning(text, CopyWarning, 'copeer.py', 10)
copeer.py:10: CopyWarning: There are extraneous files in the directory. Perhaps this is a mistake
  showwarning(text, CopyWarning, 'copeer.py', 10)
```
And also when starting `__init__.py` you may see an `AssertionError` due to the fact that during validation, the flash drive was not empty, *however, in real code you can ignore this moment*

#### A few other chips
You can also get all the paths to flash drives 

##### Windows example
```Python
all_usb_devices = detector.get_usb_devices()
print(all_usb_devices) # ["D:", "E:"]
```
##### Linux example
```Python
all_usb_devices = detector.get_usb_devices()
print(all_usb_devices) # ["/media/ubuntu/430E-A770", "/media/ubuntu/CCBIN-528TYS"]
# It only looks for mount points, not the /dev/sd* themselves.
```
##### Mac OS (OS X) example
```Python
all_usb_devices = detector.get_usb_devices()
print(all_usb_devices) # ["/Volumes/YourUSB", "/Volumes/usb_device"]
```

And also when copying, you can specify a custom path to the flash drive or even specify any other folder you wish:
```Python
assert detector.start_copy(['D:', 'C:\\path\\to\\my\\directory'])
```

## Important note
On __linux__, I specifically added such a feature that you can copy files not only to _flash drives_ (_USB_), but also to memory cards (_mmcblk_), as well as disks, if someone still uses them (_/dev/cd_)
In turn, this is not yet provided for on __Windows__, but I think that I will add it here soon. If you need to copy _ONLY to USB_, open the corresponding _issue_ so that I make changes.