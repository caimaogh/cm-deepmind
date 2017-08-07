#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 提供Connection集合操作


class Connections(object):
    def __init__(self):
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)

    def dump(self):
        for conn in self.connections:
            print conn