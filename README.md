# DeZero
Implement DeZero Framework from scratch
--- 
DeZero是一种极简的深度学习框架，设计细节来自于<a href="https://www.ituring.com.cn/book/2863">《深度学习入门2：自制框架》</a>


## 项目简介

项目种创建了一个深度学习框架——DeZero。DeZero是《深度学习入门2：自制框架》原创的框架，它用最少的代码实现了现代深度学习框架的功能。DeZero是一个小而强大的框架，将通过60个步骤来完成它。

<p>
<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/dezero_logo.png" width="400px" </p>


<p>
  <a href="https://pypi.python.org/pypi/dezero"><img
		alt="pypi"
		src="https://img.shields.io/pypi/v/dezero.svg"></a>
  <a href="https://github.com/oreilly-japan/deep-learning-from-scratch-3/blob/master/LICENSE.md"><img
		alt="MIT License"
		src="http://img.shields.io/badge/license-MIT-blue.svg"></a>
</p>

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