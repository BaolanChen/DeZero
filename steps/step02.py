"""
步骤2 创建变量的函数
具体来说，就是假设变量x和y是之前实现的Variable实例，然后以Function类的形式实现可以处理它们的函数f。
1. 在Function类中实现的方法，其输入应为Variable实例，输出应为Variable实例
2. Variable实例的实际数据存在于实例变量data中

Function作为基类，实现所有函数通用的功能，其中__call__方法接收input参数
Square类继承自Function类，也继承了__call__的方法，因此只要在forward中编写具体的计算代码，就可以完成Square类的实现。
"""

from step01 import Variable


class Function:
    def __call__(self, *args, **kwds):
        """
        在Python中，__call__ 是一个特殊方法（也称为魔术方法），它允许一个对象像函数一样被调用。
        当一个类定义了 __call__ 方法后，其实例就可以像普通函数那样使用圆括号来调用，并可以传递参数。
        """
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output
    
    def forward(self,x):
        raise NotImplementedError
                

class Square(Function):
    """
    实现一个Square用于计算平方
    """
    def forward(self, x):
        return x ** 2
    
if __name__ == "__main__":
    import numpy as np
    x = Variable(np.array(10))
    f = Square()
    y = f(x)
    print(type(y))
    print(y.data)
