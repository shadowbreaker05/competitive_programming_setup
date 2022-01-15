#!/usr/bin/env python

''' -- by A_*_A -- '''

'''             
                -------------
                # जय श्री गणेश
                -------------
    Name : A_*_A | Country : India
    Language : Python 3.10.1
    Problem Link: https://www.codechef.com/problems/INTEST
'''

# INTRODUCTION
# '''           Meet my Codechef Doggie
#      |\_/|
#      | @ @   Woof!
#      |   <>              _
#      |  _/\------____ ((| |))
#      |               `--' |
#  ____|_       ___|   |___.'
# /_/_____/____/_______|
# I am here to guard this code, woof!
# '''

#--MODULES BEGINS--
''' --python 2 and pypy begins--    # Comment this line for Python 2
from __future__ import division, print_function
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
# --python 2 and pypy ends-- '''
import io
import os
import re
import string
import sys
import time
from io import BytesIO, IOBase
import math
import functools
import collections
# import bisect, heapq, numpy, statistics
# from contextlib import contextmanager
# from jinja2 import Template
#--MODULES ENDS--

#--SHORTHANDS BEGINS--
# input = raw_input
# input = sys.stdin.readline
# sys.stdout.flush()
# alphabets = "abcdefghijklmnopqrstuvwxyz"
# from statistics import mode
# from functools import reduce
# from bisect import bisect
# from collections import defaultdict, Counter
# hp = defaultdict(lambda: 0)
# hp = collections.defaultdict(int, collections.Counter(lis))
# lis = sorted(hp.items(), key = lambda kv:(kv[1], kv[0]))
# lis = sorted(lis, key = lambda ele: (ele[1], ele[0]))
# lis = list(filter(lambda a: a[1] != min(hp.values()), lis))
input = sys.stdin.readline
def istr(): return input().strip()
def inum(): return int(input().strip())


def imap(): return map(int, input().strip().split())
def ilist(): return list(map(int, input().strip().split()))
# sys.stdout.write(str(bits[-1]) + "\n")
# for line in sys.stdin
# except: print(f'Unknown Error: {sys.exc_info()[1]}')
# w = int(input()); print("YNEOS"[(w > 2 and not w % 2)::2])
# return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else list()
#--SHORTHANDS ENDS--


#----    CODE BEGINS    ----->

def squareMatrix(n):
    grid = [[0] * n for _ in range(n)]
    return grid


def Matrix2D(rows, cols):
    grid = [[0 for j in range(cols)] for i in range(rows)]
    return grid


class LinkedListNode:
    # __slots__ = ['data', 'next',]
    def __init__(self, data):
        self.data = data
        self.next = None


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

#--GLOBAL VALUES BEGINS--


class ConstantMod:
    ''' Constant Values for Competitive Programming '''
    # __slots__ = ['_modd', '_maxx', ]  # for fixed number of attributes in __dict__ of the class's instance object

    def __init__(self, n=None, *args, **kwargs):
        self._modd = n
        # self.minn = -(n)
        self._maxx = kwargs['maxvalue'] if 'maxvalue' in kwargs else int(
            1e9 + 7)
        self._maxx *= - \
            1 if 'negative' in kwargs and kwargs['negative'] == True else 1
    # def __str__(self):    # DEBUG
    #     return f'The value of the modulo is {self._maxx}'

    def value(self, vv=None):
        if vv:
            self._modd = vv
        try:
            return self._modd
        except AttributeError:
            return None

# @contextmanager
# def simple_context_manager(obj):
#     try:
#         obj.maxx = INF
#         obj.minn = -(INF)
#         yield
#     finally:
#         obj.maxx = 10 ** 9 + 7
#         obj.minn = -(10 ** 9 + 7)
# StartTime = time.time()
# print("\nExecution Time: ",time.time()-StartTime)
# input = lambda : sys.stdin.readline()
# alp = "abcdefghijklmnopqrstuvwxyz"
# modobj = ConstantMod()
# modobj = ConstantMod(negative = True)
# modobj = ConstantMod(maxvalue = 10 ** 5 + 9)
# INF = 10 ** 15     # Change as per need
#--GLOBAL VALUES ENDS--

#--FUNCTIONS BEGINS--


def solve():
    # YOUR CODE HERE
    # global modobj
    # print(modobj.value(int(1e15)))  #setting modobj._modd from None to given param
    try:
        queries = 1
        # queries = int(input())
        # s1 = "Yes"
        # s2 = "No"
        # def myFunc(e):
        #     return e % 2
        for query in range(queries):
            try:
                print("helloworld")
                arr = ilist()
                print(arr)
                while False:
                    # print("helloworld")
                    # n = inum()
                    # arr = ilist()
                    if True:
                        break
            except EOFError as e1:  # end of input file
                print("Error_inner: ", e1)
                break
            finally:
                pass
    except Exception as e2:
        print("ERROR_outer: ", e2)
        pass
    # os.write(1,"%d"%bits[-1])
    # sys.stdout.write(str(bits[-1]))
    # print("YES" if bits[-1] else "NO")
    # sys.stdout.write("{}".format(bits[-1]))
    # pass


def main():
    tcs = 1
    # tcs = int(input())
    for tc in range(tcs):
        # with simple_context_manager(modobj):    # temporary environment
        solve()

    # OUTPUT - GOOGLE KICKSTART
    # if solve():
    #     print('Case #{}: {}'.format(tc, "YES"))
    # else:
    #     print('Case #{}: {}'.format(tc, "NO"))
#--FUNCTIONS ENDS--


# # REGION FASTIO
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

def input(): return sys.stdin.readline().rstrip("\r\n")
# # END REGION


if __name__ == "__main__":
    main()
#<-----    CODE ENDS    ----


'''

#----INPUT----

# INPUT DATA HERE

#----OUTPUT----

# OUTPUT DATA HERE

'''

''' SHORTER CODE - comment this line to run the below code

# YOUR NOTES HERE

# '''

''' -- by A_*_A -- '''
