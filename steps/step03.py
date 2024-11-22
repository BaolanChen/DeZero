"""
步骤3 函数的连续调用
之前的步骤1和2中已经实现了DeZero的变量与函数。
"""

import numpy as np
from step01 import Variable
from step02 import Function, Square


class Exp(Function):
    def forward(self,x):
        return np.exp(x)
    

if __name__ == "__main__":
    A = Square()
    B = Exp()
    C = Square()


    x = Variable(np.array(0.5))
    a = A(x)
    b = B(x)
    y = C(x)
    print(y.data)
