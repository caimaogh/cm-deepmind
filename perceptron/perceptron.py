#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# 感知器类，可以训练多个函数，例如and与函数，or或函数
# perceptron  [pɚ'sɛptrɑn] n. 感知器，[计] 感知机（模拟人类视神经控制系统的图形识别机）


class Perceptron (object):
    def __init__(self, input_num, activator):
        """
        初始化感知器，设置输入参数的个数，以及激活函数，激活函数的类型为double
        """
        self.activator = activator
        # 权重向量初始化为0  （用下划线表示不用但是有需要出现的变量名称）有几个输入参数就生成相应长的权重项list
        self.weights = [0.0 for _ in range(input_num)]
        # 偏置项初始化为0
        self.bias = 0.0

    def __str__(self):
        """
        打印学习到的权重weights、偏置项bias
        """
        return 'weights \t :%s \n bias \t :%f \n' % (self.weights, self.bias)

    # 预测函数
    def predict(self, input_vec):
        """
        输入向量，输出感知器的计算结果
        """
        # 把input_vec[x1, x2, x3 ...]和weights[w1, w2, w3, ...]打包在一起变成[(x1, w1), (x2, w2), (x3, w3), ...]
        # 然后利用map函数计算[x1*w1, x2*w2, x3*w3]
        # 最后利用reduce函数求和后加上偏置项作为输出

        print "predict start ------> ", 'inout_vec=', input_vec, 'self.weights=', self.weights, 'self.bias=', self.bias
        return self.activator(
            reduce(lambda a, b: a + b,
                   map(lambda (x, w): x * w, zip(input_vec, self.weights)),
                   0.0) + self.bias)

    # 训练函数
    def train(self, input_vecs, labels, iteration, rate):
        """
         输入训练数据：一组向量input_vecs、与每个向量对应的label、以及训练轮数iteration和学习率rate
        """
        for _ in range(iteration):
            self._one_iteration(input_vecs, labels, rate)

    def _one_iteration(self, input_vecs, labels, rate):
        """
        一次迭代，把所有的训练数据过一遍
        """
        # 把输入和输出打包在一起，成为样本的列表[(input_vec, label), ...]
        # 而每个训练样本是(input_vec, label)
        samples = zip(input_vecs, labels)
        print '_one_iteration start ------> ', 'samples=', samples
        # 对每个样本，按照感知器规则更新权重
        for (input_vec, label) in samples:
            # 计算感知器在当前权重下的输出
            output = self.predict(input_vec)
            print '_one_iteration in process --->', 'input_vec', input_vec, 'label', label, 'output=', output
            # 更新权重
            self._update_weights(input_vec, output, label, rate)
            print '_one_iteration end ------> ',  'self.weights=', self.weights, 'self.bias=', self.bias

    def _update_weights(self, input_vec, output, label, rate):
        """
        按照感知器规则更新权重
        Wi = Wi + △Wi   b = b + △b
        △Wi = η*(t-y)*xi  △b = η*(t-y)
        注：η 学习效率， t label值， y 输出值， xi 输入值
        """
        # 把input_vec[x1, x2, x3, ...]和weights[w1, w2, w3, ...]打包在一起
        # 变成[(x1, w1), (x2, w2), (x3, w3), ...]
        # 然后利用感知器规则更新权重
        delta = label - output
        print '_update_weights===', 'delta=', delta, 'label=', label, 'output=', output, 'rate=', rate
        self.weights = map(
            lambda (x, w): w + rate * delta * x,
            zip(input_vec, self.weights))
        # 更新bias
        self.bias += rate * delta


# 越阶函数 f(z) = {1,z>0; 0 z<=0}
def f(x):
    return 1 if x > 0 else 0


def get_training_dataset():
    """
    基于and真值表构建训练数据
    """
    # 输入向量列表
    input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
    # 期望的输出列表，注意与输入一一对应 [1, 1] --> 1, [0, 0] --> 0, [1, 0] --> 0, [0, 1] --> 0
    labels = [1, 0, 0, 0]
    return input_vecs, labels


def get_training_or():
    """
    基于or真值表构建训练数据
    """
    input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
    labels = [1, 0, 1, 1]
    return input_vecs, labels


def train_and_perceptron():
    """
    使用and真值表训练机器感知
    """
    # 创建感知器，输入学习个数为2，and是二元函数，激活函数为f
    p = Perceptron(2, f)
    # 训练，迭代10轮，学习速率为0.1
    # input_vecs, labels = get_training_dataset()
    input_vecs, labels = get_training_or()
    p.train(input_vecs, labels, 10, 0.1)
    # 返回训练好的感知器
    return p

if __name__ == '__main__':
    # 训练and感知器
    and_perception = train_and_perceptron()
    # 打印训练获得的权重
    print and_perception
    # 测试
    print '1 and 1 = %d' % and_perception.predict([1, 1])
    print '0 and 0 = %d' % and_perception.predict([0, 0])
    print '0 and 1 = %d' % and_perception.predict([0, 1])
    print '1 and 0 = %d' % and_perception.predict([1, 0])




















