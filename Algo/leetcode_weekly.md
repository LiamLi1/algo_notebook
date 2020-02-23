 - [ ] [sort integers by the number of 1 bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits)

进制转换：
```java
例如以十进制的数除以你所要转换的进制数,把每次除得的余数记在旁边,所得的商数继续除以进制数,直到余数为0时止.例如你要把100转换成八进制: 
100/8=12...(余数为4); 
12/8=1.....(余数为4); 
1/8=0......(余数为1); 
然后把相应的余数从低向高顺着写出来,如上的为144,此即为100的八进制表示形式.

堆排序：
private void shiftDown(int[] arr, int n, int last) {
    // shift down the (n)th number down.  
    if (2 * n + 1 > last) {
        return;
    }
    int minSon = 2 * n + 1;
    int rightSon = 2 * n + 2;
    if (rightSon <= last && compare(arr[rightSon], arr[minSon]) < 0) {
        minSon = rightSon;
    }
    if (compare(arr[n], arr[minSon]) > 0) {
        int tmp = arr[n];
        arr[n] = arr[minSon];
        arr[minSon] = tmp;
        shiftDown(arr, minSon, last);
    }
}
```

