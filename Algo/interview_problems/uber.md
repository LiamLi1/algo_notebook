- [x] [longest-valid-parentheses/](https://leetcode.com/problems/longest-valid-parentheses/submissions/) dp配合状态来update。
```
dp 或者栈，近栈的是index。如果消不掉的数中间都是valid的pairs。把栈回扫一遍就可以。
dp的话，需要和之前的状态互动

类似的dp思路：
[minimum-window-subsequence](https://leetcode.com/problems/minimum-window-subsequence/)
```

- [x] [minesweeper/](https://leetcode.com/problems/minesweeper/)

1.https://www.1point3acres.com/bbs/thread-885063-1-1.html
- [ ] [find-the-closest-palindrome/](https://leetcode.com/problems/find-the-closest-palindrome/)
```
字符串处理/ candidates select
```

2.https://www.1point3acres.com/bbs/thread-866335-1-1.html
- [x] [longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

3.https://www.1point3acres.com/bbs/thread-868626-1-1.html
```
两数做差。字符串处理。考虑比大小等多种情况。
```


5.https://www.1point3acres.com/bbs/thread-864817-1-1.html
```
第一题 
1. verison compatibility 要求Time O(1)
  1->2->3->4->5->6
    T   T    F      T    T
写两个函数
1. addVersion(int version, boolean compatible)// compatible 代表和前一个verion是不是compatible,
2. isCompatible(int sourceVersion, int targetVersion)，判断任意两个version是不是compatible
可以用union find，也可以直接binary search，因为版本号是递增的

第二题unique island 用dfs+map
```

6.https://www.1point3acres.com/bbs/thread-864299-1-1.html
```
类似calculator 1
recursion返回下一个要处理的位置
```

7.https://www.1point3acres.com/bbs/thread-857243-1-1.html
8.https://www.1point3acres.com/bbs/thread-871568-1-1.html
```
multithreading? 想一想怎么做
```

8.https://www.1point3acres.com/bbs/thread-884709-1-1.html
