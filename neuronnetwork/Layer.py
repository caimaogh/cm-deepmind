#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 负责初始化一层；另外作为Node的集合对象，提供对Node集合的操作
import ConstNode
import Node


class Layer(object):
    def __init__(self, layer_index, node_count):
        """
        初始化一层
        :param layer_index:层编号
        :param node_count: 层所包含的节点个数
        """
        self.layer_index = layer_index
        self.nodes = []
        for i in range(node_count):
            self.nodes.append(Node(layer_index, i))
        self.nodes.append(ConstNode(layer_index, node_count))

    def set_output(self, data):
        """
        设置层的输出；当层时输入层时会用到
        :param data:
        :return:
        """
        for i in range(len(data)):
            self.nodes[i].set_output(data[i])

    def calc_output(self):
        """
        计算层的输出向量
        :return:
        """
        for node in self.nodes[:-1]:
            node.calc_output()

    def dump(self):
        """
        打印层信息
        :return:
        """
        for node in self.nodes:
           print node