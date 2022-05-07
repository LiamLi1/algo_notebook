### Collections

###  unclassified:
```java
// comparator 有简单写法
Collections.sort(candidates, (w1, w2) ->  map.get(w1) - map.get(w2));
new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());

Comparator
Collections.sort:
Arrays.sort(temp); //也可以针对char, int等基本类型。但是这些基本类型就不能定制comparator 了。
Arrays.sort(a, Collections.reverseOrder());

Arrays.sort(array, new Comparator<int[]>() { //自定义类型和数组都没问题
           @Override
           public int compare(int[] a, int[] b) {
               if (a[1] == b[1]) {
                   return a[0] - b[0];
               }
               return b[1] - a[1];
           }
        }); 
        

// 创建Collections的数组写法
List<Character> [] bucket = new List[s.length() + 1];


//取模运算：
（-7 % 3） = -1;
转换为整正数，需要再加3


//类型转换：
Integer.valueOf("13"); // 转为自己
Integer i = 19;
int j = i.intValue(); // 转为基本类型
i.toString(); //转为String， 就是打印的语法。
char c=(char)(a+'0'); // 数字转char

// Math.floorDiv
int负数除法会取大的数。比如 （-5） / 2 = -2.
在线段树中会出问题。要改成Math.floorDiv(-5, 2) = -3 

```
### 0. Array相关
```java

对基本类型的快速转换：
ArrayUtils.toObject(); 
ArrayUtils.toPrimitive();


// array copy to another array
System.arraycopy(sourceArray, 0, targetArray, 0, len);


// copy array
copy = nums.clone();
```

### 1. List

```java
//1. 存/取
list.add(E e);
list.addAll(list); // 合并进来一个list，去除null。
可以以用来合并Set，很好用。

list.get(i);
list.set(i, E e);
//2. 长度 and 长度为零
list.size();
list.isEmpty();
// 3. 删除
list.remove(int e);
list.remove(E e);
//4. 转换
   
Integer[ ] array = { 1,2,3};
//如果需要删改的话只能这样做。
List<Integer> arrayList = new ArrayList<>(Arrays.asList(array)); 

arrayList.add(44);

Integer[] array1 = arrayList.toArray(new Integer[arrayList.size()]);
//5. 其他：
subList(0, k); 返回子List

//6. sort
Arrays.sort(arr, Collections.reverseOrder());

```

### 2. Stack
```java
//1. 存/取
E stack.pop(); // 返回元素并删除
E stack.peek(); // 返回元素不删除
stack.push(E e);
```



### 3. Map
```java
Map<Integer> map = new HashMap<Integer>();
//1. 存/取/删
V put(K key, V value)//把Key-Value放入Map
V get(K key//通过Key获取Value
V remove(K key);//删除K
注意：不能在自身key的for循环内删除。
	  
//2. 长度 and 长度为零
map.size();
map.isEmpty();
//3. 遍历
//用keySet()
	Map<String, Integer> map = ...
	for (string key : map.keySet()) {
		Integer value = map.get(key);
	}
//或者用entrySet() 
// iterator<Map.Entry<>> itr = map.entrySet().iterator();


	Map<String, Integer> map = ...
	for (Map.Entry<String, Integer> entry : map.entrySet()) {
		String key = entry.getKey();
		Integer value = entry.getValue();
	}
	
// 4.map.values(), 得到values的list。
//可以转为set， list等。

//5. get first key
        Map.Entry<Integer, Integer> entry 
		= map.entrySet().iterator().next();
        entry.getKey();

//6. getOrDefault
map.put("A", map.getOrDefault("A", 0) + 1);

```



### 4. Queue
```java
//1. 存/取
E add(E e)  / boolean offer(E e) //添加至队尾压栈：
E remove() / boolean E poll() // 获取队列头部元素并删除 
E element() / boolean E peek() //获取队列头部元素但不删除
// 前者抛出Exception， 后者返回null 或 false
boolean remove(Object o) //删除指定元素
```

### 5. Set
```java
//1. iterator
Set<String> set = new HashSet<String>();
Iterator<String> it = set.iterator();
while (it.hasNext()) {
	String str = it.next();
	System.out.println(str);
}

for (String str : set) {
	System.out.println(str);
}
```


### 6. String
```java
1. String与其他基本变量的转换：
 
String.valueOf(); //里面可以是 Integer， Double， int，等等。同样也可以String转其他变量。
 
2. substring
String substring(int beginIndex) //取从beginIndex位置开始到结束的子字符串。
String substring(int beginIndex, int endIndex) //取从beginIndex位置开始到endIndex位置前一位的子字符串。所以(3,4)(4,5) 都只有一个且不重复
 
3. indexOf/ lastIndexOf
双引号/单引号都可以
找不到的时候返回-1
text.indexOf(String word, int index) // 从index以后找。
 
 
4.s.toCharArray(); //扫字符串的时候很有用
String s = new String(charArray); 
 
5. 其他：
String[] = s.split(“[\\s,.]”); //返回string 数组. java转义字符是双杠。
String s1 = s.toLowerCase();
String s1 = s.replace(‘s’,‘q‘);
s1 = s.replaceAll("s", "s1");
//两个都是替换全部。区别在于All用的是正则, replace 用字符串。
s1 = s.trim();
//去掉左右两边的空格。
只有StringBuilder才有reverse

 
6. StringBuilder
StringBuilder sb = new StringBuilder();
sb.append(); // 什么数据类型都可以
sb.toString();
sb.deleteCharAt(permutation.length() - 1); //删除
sb.reverse(); //反方向
sb.replace(int start, int end, String str); //替换
StringBuilder/ String 直接相加，可以得到新的String
sb.insert(0, Integer.toString(i)); // 添加在指定位置。可以添加在字符串前面
 
7. String[] stubs = path.split("/+"); // 用正则表达式拆分成字符串数组
如果第一个字符串是split，会得到第一个为"".
" is blue" -> ["", "is", "blue"]
如果末尾是，却没有影响。会全部删除。
"is blue " -> ["is", "blue"]
中间“多余”出来的分隔符，会产生空字符串
"is   blue" -> ["is", , , "blue"]
三个空格。一个用来分割，两个多余的产生了空串。
 
8. String 不能被Character[] 初始化，只能被char[]初始化
```



### 7. Iterator

```java
List<Integer> list = new ArrayList<Integer>();
Iterator<String> it = list.iterator();


Map<Integer, Integer> map = new HashMap<Integer, Integer>();
Iterator<Map.Entry<Integer, Integer>> entries = map.entrySet().iterator();
while (entries.hasNext()) {
    Map.Entry<Integer, Integer> entry = entries.next();
    System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());

```

### 8. PriorityQueue
```java
boolean offer(E e) //添加至队尾压栈：失败时false
boolean add(E e) //同offer，但是失败时throw exception
//对pq，因为是同步的，所以上述两条没差别
boolean E poll() // 获取队列头部元素并删除 
boolean E peek() //获取队列头部元素但不删除
boolean remove(E e) //删除某个元素。复杂度是O(n + logn) = O(n)
```

### 9. Deque

```java
boolean offerLast(e)
boolean offerFirst(e)
boolean pollFirst(e)
boolean peekFirst(e)
```

### 10. Array 相关
```java
//1. Array 初始化
String[] array = new String[]{"Buenos Aires", "Córdoba", "La Plata"}；
String[] array = new String[3];

多元array，需要每个不一样长时，可以：
int [][]ans = new int[k][];
只定义第一个的长度。

//2. 与list的转换

//必须加上new。或者直接新建array2, 然后传入toArray(array2).
String[] array2 = testList.toArray(new String[testList.size()]);

//new 后面的加不加<“类型”>都可以， 直接asList 的话是只读的。
//通过Array来建：
List<Integer> arrayList = new ArrayList<>(Array.asList(array));
//直接把Array写出来
List<String> places = new ArrayList<String>(Arrays.asList("Buenos Aires", "Córdoba", "La Plata"));
```

### 11.LinkedHashMap

```java
LinkedHashMap<Integer, Integer> lhm 
= new LinkedHashMap<Integer, Integer>(capacity, 
                                                                    fillratio f, 
                                                                    addOrVisit); 
//默认按照添加顺序排序。false表示按照访问顺序排序。
//如果要实现LRU， 则需要重写
lru = new LinkedHashMap<Integer, Integer>(capacity, 0.7f, true) {
            @Override
            public boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest){
            return size() > capacity;  
            }
        };


如何扩展有template的类：必须用K,V!
如果只是在new的时候override，则用new中的数据类型

class LRULinkedHashMap<K,V> extends LinkedHashMap<K,V>{
	//定义缓存的容量
	private int capacity;
	private static final long serialVersionUID = 1L;
	//带参数的构造器	
	LRULinkedHashMap(int capacity){
		//调用LinkedHashMap的构造器，传入以下参数
		super(16,0.75f,true);
		//传入指定的缓存最大容量
		this.capacity=capacity;
	}
	//实现LRU的关键方法，如果map里面的元素个数大于了缓存最大容量，则删除链表的顶端元素
	@Override
	public boolean removeEldestEntry(Map.Entry<K, V> eldest){ 
		System.out.println(eldest.getKey() + "=" + eldest.getValue());  
		return size()>capacity;
	}  

```
### 12.1 TreeSet
```java
//TreeSet没有equal，而是用compareTo来进行排序。
//也就是说当两个元素相等时，会不能插入
//并不需要定义equals。
```


### 12.2 TreeMap
所有操作时间复杂度都是logn

```java
基本和Map一样
K firstKey();
Entry<K, V> firstEntry();

lastKey();
lastEntry();

remove(Object key)
pollFirstEntry()
pollLastEntry();

lowerEntry(K key) lowerKey(K key)
floorEntry(snap_id).getValue() // 找到小于等于
floorKey(K key)
ceilingEntry(K key).getrValue() // 大于等于
higherEntry(K key)

不能sort by values. 只能根据key的order正或反的sort。但是TreeSet可以sort values。

SortedSet<Map.Entry<String, Double>> sortedset = new TreeSet<Map.Entry<String, Double>>(
            new Comparator<Map.Entry<String, Double>>() {
                @Override
                public int compare(Map.Entry<String, Double> e1,
                        Map.Entry<String, Double> e2) {
                    return e1.getValue().compareTo(e2.getValue());
                }
            });

  sortedset.addAll(myMap.entrySet());
  
  可以拿到subMap
  
   for(Map.Entry<Integer, String> entry : treeMap
                                        .subMap(column_start, true, column_end, true)
                                        .entrySet()) {
            list.add(new Column(entry.getKey(), entry.getValue()));                              
        }

```

### 13 BigInteger

```java
//把该数转换为该类型的数的值。
intValue，longValue，
floatValue，doubleValue

BigInteger中一些常见的函数：

A=BigInteger.ONE

B=BigInteger.TEN

C=BigInteger.ZERO

一些常见的数的赋初值。
将String赋给BigInteger，
BigInteger bigValue = new BigInteger("10");

将int型的数赋值给BigInteger，
BigInteger.valueOf(k);


基本的函数：

valueOf:赋初值


```

### 14 BitSet
自带hash功能的数据结构。
``` java
// 新建
BitSet bitSet = new BitSet(int size);

// set
bitSet.set(1);  //这样就会变成{1}

//and
bits2.and(bits1); // 取两个都有的, 赋给bits2

//xor 取异或
bitSet.clear(); //清空
int bitSet.cardinality(); //返回为1 的个数。

void set(int startIndex, int endIndex)
//将指定的 fromIndex（包括）到指定的 toIndex（不包括）范围内的位设置为 true。

public boolean get(int pos); // 返回位置是pos的字位值。
boolean isEmpty( )// 判断是否为空
```
---
### 15 enum

[Java 语言中 Enum 类型的使用介绍](https://www.ibm.com/developerworks/cn/java/j-lo-enum/index.html)
1. 引出
如果想要定义一个常量类：
```java
public static final3432 class RainbowColor { 
    //final类不能被继承，没有子类，final类中的方法默认是final的。
    //final方法不能被子类的方法覆盖，但可以被继承。
    //final成员变量表示常量，只能被赋值一次，赋值后值不再改变。
   //final不能用于修饰构造方法。
   // 红橙黄绿青蓝紫七种颜色的常量定义
   public static final int RED = 0; 
   public static final int ORANGE = 1; 
   public static final int YELLOW = 2; 
   public static final int GREEN = 3; 
   public static final int CYAN = 4; 
   public static final int BLUE = 5; 
   public static final int PURPLE = 6; 
}

```
缺点在于：1. 给RED赋值会报错。2.必须通过RainbowColor.RED来访问。3.一致性差 4.无意义

解决方案：Enum

2. 定义
```java
enum RainbowColor { RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE }

// 读取当天的信息
WeekDayEnum today = readToday(); 
// 根据日期来选择进行活动
switch(today) { 
	case Mon: do something; break; 
	case Tue: do something; break; 
	case Wed: do something; break; 
	case Thu: do something; break; 
	case Fri: do something; break; 
	case Sat: play sports game; break; 
	case Sun: have a rest; break; 
}
因为switch已经传入了today，所以case
```

3. 与常量final类的关系：
```java
//其实可以看成
public final class WeekDayEnum extends Enum {
	private final static WeekDayEnum Mon;
	private final static WeekDayEnum Tue;
	// 其他天
}

// constructor必须是friend或者private
public enum WeekDayEnum { 
   Mon(1), Tue(2), Wed(3), Thu(4), Fri(5), Sat(6), Sun(7); 
   private int index; 
   WeekDayEnum(int idx) { 
       this.index = idx; 
   } 
   public int getIndex() { 
       return index; 
   } 
} 
```
4. 其他常用用法
```java
// 1. 用来循环。提供values()
for (WeekDayEnum day : WeekDayEnum.values()) {
}
for(WeekDayEnum day : EnumSet.range(WeekDayEnum.Mon, WeekDayEnum.Fri)) { 
    System.out.println(day); 
}
EnumSet<WeekDayEnum> subset = EnumSet.of(WeekDayEnum.Mon, WeekDayEnum.Wed); 
     for (WeekDayEnum day : subset) { 
         System.out.println(day);  // 只有Mon和Wed
     }

// 2. 
绑定整数
i. 可以像3里面定义一个getIndex();
ii. 可以直接调用 WeekDayEnum.Mon.ordinal();
iii. 
```


---

### e1. Comparator / Comparable 
[Java 中 Comparable 和 Comparator 比较](http://www.cnblogs.com/skywang12345/p/3324788.html)
Comparable是排序接口；若一个类实现了Comparable接口，就意味着“该类支持排序”。只有一个compareTo函数。
而Comparator是比较器；我们若需要控制某个类的次序，可以建立一个“该类的比较器”来进行排序。有equals和compare两个函数。equals因为object已经实现了，所以不用实现。

Comparable相当于“内部比较器”，而Comparator相当于“外部比较器”。实现了Comparator也可以用于Arrays，Collections的sort。或者PriorityQueue。



```java
1. 在定义class的时候， override compareTo.
    这时只用传入一个参数。 
public class Person implements Comparable<Person>{
	@Override
	public int compareTo(Person o) {
		return this.name.compareTo(o.name);
	}
}
//必须implement comparable。multiple implements的写法。
class Task implements Runnable, Comparable<Task>{}


2. 在PriorityQueue中传入
a. 直接new在传入的参数中:
Queue<Person> queue = new PriorityQueue<>(new Comparator<Person>() {
	@Override
	public int compare(Person arg0, Person arg1) {
		// TODO Auto-generated method stub
		return 0;
	}});

b. 传入一个Comparator的实例。
Comparator<String> mc = new Comparator<String>(){
            @Override
            public int compare(String s1, String s2) {
                int spaceS1 = s1.indexOf(' ');
                int spaceS2 = s2.indexOf(' ');
                String title1 = s1.substring(0, spaceS1);
                String title2 = s2.substring(0, spaceS2);
                String body1 = s1.substring(spaceS1);
                String body2 = s2.substring(spaceS2);
                
                if (!body1.equals(body2)) {
                    return body1.compareTo(body2);
                } else {
                    return title1.compareTo(title2);
                }
            }
        };

c. 传入一个实现了Comparator的class的实例。
class MyCompartor implements Comparator {
        @Override
        public int compare(Object a1, Object a2) {
            String o1 = (String)a1;
            String o2 = (String)a2;
            int idx1 = o1.indexOf(' ');
            int idx2 = o2.indexOf(' ');
            String head1 = o1.substring(0, idx1);
            String head2 = o2.substring(0, idx2);
            String body1 = o1.substring(idx1);
            String body2 = o2.substring(idx2);
            if(body1.equals(body2)) {
                return head1.compareTo(head2);
            } else {
                return body1.compareTo(body2);
            }
        }
    } 
MyCompartor mc = new MyCompartor();

d. 在class定义时实现Comparable， Override compareTo. 
TreeMap 的相等判定由compare 来决定，不是hashCode
```


### e2. equals/ hashCode

！！！treeset是靠compareTo函数来确定元素是否重复的，return 0 就说明两个元素相同，所以可以直接用。

**Objects.hashCode :beer:（注意不是Object而是java.util.Objects) :beer:**

```java
//Objects.hashCode 的定义
//只能传入一个Object
public static int hashCode(Object o) {
      return o != null ? o.hashCode() : 0;
	  }

//Objects.hash（Object... values)
// 可以传入多个object


//eg:
@Override
	public int hashCode() {
    return this.name.hasCode(); // 这个不对。因为可能为空。
		return Objects.hashCode(this.name);
    return Objects.hash(this.name, this.age)
	}
        
@Override 
	public boolean equals(Object obj) {
    if (obj == this) {
      return true;
    }
		if (obj instanceof CharCount) {
			CharCount counter = (CharCount) obj;
      return Objects.equals(this.name, counter.name) && this.age = counter.age
      } //挂上Objects可以避免为空的情况。
    return false
```

## e3 Goto
java 不支持goto。 但是支持break特定的地方。
```java

outer:
	for (int i = 0; i < 10; i++) {
		for(int j = 0; j < 10; j++) {
			if (i == 5 && j == 5) {
				break outer;
			}
		}
	}
```

## e4异常

1. 自定义异常：重写public类，String getMessage() 方法
```java
class MyException extends Exception { // 创建自定义异常类  
    String message; // 定义String类型变量  
    public MyException(String ErrorMessagr) { // 父类方法  
        message = ErrorMessagr;  
    }  
  
    public String getMessage() { // 覆盖getMessage()方法  
        return message;  
    }  
} 

throw new Exception("Exception message");

```
2. 异常链
```java

```

### final

```
对于一个final变量，如果是基本数据类型的变量，则其数值一旦在初始化之后便不能更改；如果是引用类型的变量，则在对其初始化之后便不能再让其指向另一个对象。
```