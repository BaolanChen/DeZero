"""
Function作为基类，实现所有函数通用的功能
"""

class Function:
    def __call__(self, *args, **kwds):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output
    
    def forward(self,x):
        raise NotImplementedError
                

class Square(Function):
    def forward(self, x):
        return x ** 2
    