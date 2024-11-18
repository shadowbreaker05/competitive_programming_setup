# '''
#
#      |\_/|
#      | @ @   Woof!
#      |   <>              _
#      |  _/\------____ ((| |))
#      |               `--' |
#  ____|_       ___|   |___.'
# /_/_____/____/_______|
#
# Hey, I am here to guard this code, woof woof...
#
# '''

import array
import bisect
import collections
import fractions
import functools
import heapq
import itertools
import math
import random
import string
import sys

# input = lambda: sys.stdin.readline().rstrip("\r\n")
inum = lambda: int(input())
imap = lambda: map(int, input().split())
itup = lambda: tuple(map(int, input().split()))
isor = lambda: sorted(map(int, input().split()))
isor2 = lambda nums: sorted(nums, key=lambda num1: (num1[0], num1[1]))
ilis = lambda: [int(nums) for nums in input().split()]
dd = lambda nums: collections.defaultdict(lambda: nums)
freq = lambda nums: dict(collections.Counter(nums))
adjlist = lambda: collections.defaultdict(lambda: [])
matrix = lambda num1, num2: [[0 for y in range(num2)] for x in range(num1)]
flattenlist = lambda nums: [x for num1 in nums for num2 in num1]
lcm = lambda num1, num2: num1 * num2 // math.gcd(num1, num2)
npr = lambda num1, num2: math.factorial(num1) // math.factorial(num1 - num2)
lowerpower = lambda num1, num2: pow(num2, math.floor(math.log(num1, num2)))
upperpower = lambda num1, num2: pow(num2, math.ceil(math.log(num1, num2)))
isperfectsquare = lambda num1: math.ceil(math.log(num1, 2)) == math.floor(math.log(num1, 2))
ncr = lambda num1, num2: math.factorial(num1) // (math.factorial(num2) * math.factorial(num1 - num2))
filtereven = lambda nums: list(filter(lambda num1: num1 % 2 == 0, nums))
filteroddd = lambda nums: list(filter(lambda num1: num1 % 2 != 0, nums))
fact = lambda num1: functools.reduce(lambda num2, num3: num2 * num3, range(1, num1 + 1))
freqarray = lambda nums: collections.Counter(nums)
binarylength = lambda num1: len(bin(num1)[2:])
binarylength = lambda num1: math.floor(math.log2(num1)) + 1
bitsetarray = lambda nums: [int(num1) for num1 in bin(nums)[2:]]
lengthbitset = lambda num1: math.ceil(math.log(num1 + 0.1, 2))
bit_chk = lambda num1, num2: num1 & (1 << num2)   # num2 = position of bit (...3210) and (1 << num2) is bitmask
bit_set = lambda num1, num2: num1 | (1 << num2)     # num2 = position of bit (...3210) and (1 << num2) is bitmask
bit_unset = lambda num1, num2: num1 & (~(1 << num2))# num2 = position of bit (...3210) and (1 << num2) is bitmask
bit_toggle = lambda num1, num2: num1 ^ (1 << num2)  # num2 = position of bit (...3210) and (1 << num2) is bitmask
bit_update = lambda num1, num2: (num1 & ~(1 << num2)) | (1 << num2)
ispow2 = lambda num1: (num1 and not(num1 & (num1 - 1)))
minheap = lambda nums: 1 if heapq.heapify(nums) == None else 0
maxheap = lambda nums: 1 if heapq._heapify_max(nums) == None else 0   # maybe deprecated!!!
lowerbound = lambda nums, key, start, stop: bisect.bisect_left(nums, key, lo=start, hi=stop)
upperbound = lambda nums, key, start, stop: bisect.bisect_right(nums, key, lo=start, hi=stop)
inorder = lambda root: inorder(root.left) + [root.val] + inorder(root.right) if root else []
pows2 = lambda num1: [1 << idx for idx in range(num1)]
adjpairarray = lambda nums: list(itertools.pairwise(nums))
prefixsumarray = lambda nums: list(itertools.accumulate(nums, lambda num1, num2: num1 + num2))
suffixsumarray = lambda nums: prefixsum(reversed(nums))
grid = lambda rows, cols: [[0 for y in range(cols)] for idx in range(rows)]
palindromeindices = lambda num1: [(num1 // 2 - idx - (0 if num1 & 1 else 1), num1 // 2 + idx) for idx in range(num1 // 2 + (1 if num1 & 1 else 0))]
onum = lambda num1: '%d' % num1
omap = lambda num1, num2: '%d %d' % (num1, num2)
olis = lambda nums: ' '.join((str(nums[idx]) for idx in range(len(nums))))
odict = lambda nums: "\n".join((str("%idx: %s" % (num1[0], " ".join((str(num2) for num2 in num1[1])))) for num1 in zip(nums.keys(), nums.values())))
ogrid = lambda grid: '\n'.join((' '.join((str(num1) for num1 in nums)) for nums in grid))
toint = lambda wrd: int(wrd, 2)
tobytearray = lambda wrd: bytearray(wrd, 'utf-8')
tobinstr = lambda num: format(num, '032b')

# Create the wrapper class to avoid hash collisions
RANDOM = random.getrandbits(32)
class Wrapper(int):
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

zer, one, temp = 0, 1, 2
tcs = 1
MOD = 10**9 + 7


zer, one = 0, 1
tcs = 1
tcs = int(input())
for tc in range(tcs):
    if one:
        cs = 0
        ps = {"0": -1}
        n = inum()
        arr = ilis()
        dp = [0 for i in range(n + 1)]
        for i in range(n):
            if one:
                cs += arr[i]
                dp[i + 1] = max(dp[i], dp[ps[cs] + 1] + 1) if cs in ps else dp[i]
                ps[str(cs)] = i
        print(dp[-1])
