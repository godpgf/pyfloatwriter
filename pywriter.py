import ctypes
import platform
import os
import numpy as np
from ctypes import c_void_p, c_float, c_bool, c_char, c_char_p, c_int

sysstr = platform.system()
curr_path = os.path.dirname(os.path.abspath(os.path.expanduser(__file__)))
lib_path = curr_path + "/lib/"

try:
    py_writer = ctypes.windll.LoadLibrary(lib_path + 'writer_dymc.dll') if sysstr == "Windows" else ctypes.cdll.LoadLibrary(
        lib_path + 'libwriter_dymc.so')
except OSError as e:
    lib_path = curr_path + "/../../libLSH/build/"
    py_writer = ctypes.windll.LoadLibrary(
        lib_path + 'Release/writer_dymc.dll') if sysstr == "Windows" else ctypes.cdll.LoadLibrary(
        lib_path + 'libwriter_dymc.so')


class PYWriter(object):
    @classmethod
    def writer_int_array(cls, data, path):
        feature = np.reshape(np.array(data, np.int32), [-1])
        py_writer.writeInt(feature.ctypes.data_as(ctypes.POINTER(ctypes.c_int32)), len(feature), path.encode('utf-8'))

    @classmethod
    def writer_float_array(cls, data, path):
        feature = np.reshape(np.array(data, np.float32), [-1])
        py_writer.writeFloat(feature.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), len(feature), path.encode('utf-8'))


if __name__ == '__main__':
    PYWriter.writer_int_array([1, 2, 3, 4, 5, 6], "int.bat")
    PYWriter.writer_float_array([6.5, 5.4, 4.3, 3.2, 2.1], "float.bat")
