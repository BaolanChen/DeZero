"""
步骤1 创建DeZero的组成元素-变量

实现Variable类，作为变量类
"""

class Variable:
    def __init__(self, data):
        self.data = data


if __name__ == '__main__':
    import numpy as np
    data = np.array(1.0)
    x = Variable(data)
    print(x.data)
