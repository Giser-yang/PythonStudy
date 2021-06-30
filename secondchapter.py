# import array
# symbols = '$^&*#%'
# # ord() 函数是 chr() 函数的配对函数，它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。
# a = array.array('I', (ord(symbol)for symbol in symbols))
# print(a)

# lax_coordinates = (33.9425, -118.408056)
# city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# for passport in sorted(traveler_ids):
#     print('%s/%s' % passport)
#
# for country, _ in traveler_ids:
#     print(country)
#
# latitude, longitude = lax_coordinates
# print(latitude, longitude)

# # 20除以8的商和余数
# # divmod(20, 8)
# c = (20, 8)
# print(c)
# print(*c)
# print(divmod(*c))

# import os
# path = 'E:/PythonStudy/secondchapter.py'
# _, filename = os.path.split(path)
# print(filename)

# a, b, c, *rest = range(6)
# print(a, b, c, rest)

# metro_areas=[
#     ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
#     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#     ('Mexico City', 'MX', 20.142, (19.43333, -99.133333)),
#     ('Nem York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#     ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
# ]
# # :15为占位15个字符宽度 ^为居中对齐，9为字符宽度
# print('{:15}|{:^9}|{:^9}'.format('', 'lat.', 'long.'))
# fmt = '{:15}|{:9.4f}|{:9.4f}'
# for name, cc, pop, (latitude, longitude) in metro_areas:
#     # if longitude<=0:
#         print(fmt.format(name, latitude, longitude))


# from collections import namedtuple
#
# City = namedtuple('City', 'name country population coordinates')
# tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# # print(tokyo)
# # print(tokyo.country)
# # print(City._fields)
# LatLong = namedtuple('LatLong','lat long')
# delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# delhi = City._make(delhi_data)
# print(delhi._asdict())

# from array import array
# from random import random
# floats = array('d', (random() for i in range(10**7)))
# print(floats[-1])
# fp = open('floats.bin', 'wb')
# floats.tofile(fp)
# fp.close()
# floats2 = array('d')
# fp = open('floats.bin', 'rb')
# floats2.fromfile(fp, 10**1)
# fp.close()
# print(floats2[-1])
# print(floats == floats2)
# floats2 = array('d', sorted(floats2))
# print(floats2)
#
# import numpy
# a = numpy.arange(12)
# print(a)
# print(a.shape)
# a.shape = 3, 4
# print(a)
# print(a[:, 1])  # 打印第一列
# print(a.transpose())    # 将行和列交换
#
# from collections import deque
#
# dq = deque(range(10),maxlen=10)
# print(dq)
# dq.rotate(3)
# print(dq)
# dq.rotate(-4)
# print(dq)
# dq.appendleft(-1)
# print(dq)
# dq.extend([10,20,30])
# print(dq)
# dq.extendleft([11,22,33])
# print(dq)

