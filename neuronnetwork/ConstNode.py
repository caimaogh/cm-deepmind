#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了实现一个输出恒为1的节点（计算偏置项Wb时需要）


class ConstNode(object):
    def __init__(self, layer_index, node_index):
        """
        构造节点对象
        :param layer_index:
        :param node_index:
        """
        self.layer_index = layer_index
        self.node_index = node_index
        self.downstream = []
        self.upstream = []
        self.output = 1

    def append_downstream_connction(self, conn):
        """
        添加一个到下游节点的连接
        :param conn:
        :return:
        """
        self.downstream.append(conn)

    def calc_hidden_layer_delta(self):
        """
        节点属于隐藏层时，根据式4计算delta
        :return:
        """
        downstream_delta = reduce(lambda ret, conn: ret + conn.downstream_node.delta * conn.weight, self.downstrem, 0.0)
        self.delta = self.output * (1 - self.output) * downstream_delta

    def __str__(self):
        """
        打印节点信息
        :return:
        """
        node_str = '%u-%u: output: 1' % (self.layer_index, self.node_index)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.downstream, '')
        return node_str + '\n\tdownstream:' + downstream_str

