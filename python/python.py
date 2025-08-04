from ctypes import CDLL, c_int

shared_lib = CDLL('../third_party/lib/shared_lib.so')

shared_lib.Hello()

shared_lib.plus.argtypes = [c_int, c_int]
shared_lib.plus.restype = c_int

a_plus_b_res = shared_lib.plus(114514, 1919810)
print(a_plus_b_res)