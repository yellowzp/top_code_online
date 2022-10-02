#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Vesper Huang
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> None:
        if self.a:
            self.a = self.a[:-1]

    def top(self) -> int:
        if len(self.a) > 0:
            return self.a[-1]
        return None

    def min(self) -> int:
        return min(self.a)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

if __name__ == '__main__':
    obj = MinStack()
    obj.push(10)
    obj.push(3)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.min()
    print(param_3)
    print(param_4)