#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 主要职责是记录连接的权重，以及这个连接所关联的上下游节点
from random import random

class Connection(object):
    def __init__(self, upstream_node, downstream_node):
        """
        初始化连接，权重初始化为一个很小的随机数
        :param upstream_node: 连接的上游节点
        :param downstream_node: 连接的下游节点
        """
        self.upstream_node = upstream_node
        self.downstream_node = downstream_node
        self.weight = random.uniform(-0.1, 0.1)
        self.gradient = 0.0

    def calc_gradient(self):
        """
        计算梯度
        :return:
        """
        return self.gradient

    def update_weight(self, rate):
        """
        根据梯度下降算法更新权重
        :param rate:
        :return:
        """
        self.calc_gradient()
        self.weight += rate * self.gradient

    def __str__(self):
        """
        打印连接信息
        :return:
        """
        return '(%u-%u) -> (%u-%u) = %f' % (
            self.upstream_node.layer_index,
            self.upstream_node.node_index,
            self.downstream_node.layer_index,
            self.downstream_node.node_index,
            self.weight
        )

