# 累加 reduce
from functools import reduce,partial
# 乘法 mul
from operator import mul


# 阶乘
def fact(n):
    return reduce(mul, range(1, n + 1))


# a = fact(3)
# print(a)
# print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
# print(reduce(mul, [1, 2, 3, 4]))
#  将两参数函数改编成但参数函数
triple = partial(mul, 3)
print(triple(8))