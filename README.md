Traceback (most recent call last):
  File "/home/eagles/Desktop/southestcon/eaglesvm/lib-dt-apriltags-daffy/test/test.py", line 25, in <module>
    at_detector = Detector(families='tag36h11',
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/eagles/Desktop/southestcon/eaglesvm/lib/python3.11/site-packages/dt_apriltags/apriltags.py", line 258, in __init__
    self.libc = ctypes.CDLL(os.path.join(os.path.dirname(__file__), filename))
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/ctypes/__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: /home/eagles/Desktop/southestcon/eaglesvm/lib/python3.11/site-packages/dt_apriltags/libapriltag.so: cannot open shared object file: No such file or directory
