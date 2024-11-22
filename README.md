# DeZero
Implement DeZero Framework from scratch
--- 
DeZero是一种极简的深度学习框架，设计细节来自于《深度学习入门2：自制框架》
## DeZero框架特点

### 1. 极简主义
DeZero是以简单易懂为第一设计原则的极简深度学习框架。
在设计方面尽量减少了外部库的使用，内部代码也压缩到了最简化

### 2. 纯Python
许多深度学习框架中使用多种编程语言(纯Python和C++)来实现，而DeZero只采用Python来实现。
因此只要懂Python，就可以很容易地阅读DeZero框架中地源代码。
由于该框架只使用Python来实现，所以可以轻松地在智能手机上，或者使用Google Colaboratory等服务在云端运行它。

### 3. 具备现代深度学习框架的功能
PyTorch和TensorFlow等现代深度学习框架有许多相同的功能，
其中一个重要的功能是Define-by-Run。Define-by-Run是在进行深度学习计算时在计算之间建立"连接"的机制。
本项目创建的DeZero框架就是一个Define-by-Run风格的框架，其中采用了许多与现代深度学习框架相同的设计。
