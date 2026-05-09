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

//7. stream for loop
empList.stream().forEach(e -> e.salaryIncrement(10.0));
empList.parallelStream().forEach(e -> e.salaryIncrement(10.0));

// combine with lambda function
pipelines.stream()
            .forEach(pipeline -> executorService.execute(() -> {
                logger.info("Starting Pipeline: {}", pipeline.getName());
                runner.run(pipeline);
            }));

// params
// Lambda expressions can be stored in variables if the 
// variable's type is an interface which has only one method. 
// The lambda expression should have the same number of 
// parameters and the same return type as that method. 
// Java has many of these kinds of interfaces built in, 
// such as the Consumer interface (found in the java.util
//  package) used by lists.

ArrayList<Integer> numbers = new ArrayList<Integer>();
numbers.add(5);
numbers.add(9);
numbers.add(8);
numbers.add(1);
Consumer<Integer> method = (n) -> { System.out.println(n); };
numbers.forEach( method );

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

### 16 Stream<T> (java 8)
```java
//1. Creation - Stream.of()
Employee[] arrayOfEmps = {
    new Employee(1, "Jeff Bezos", 100000.0), 
    new Employee(2, "Bill Gates", 200000.0), 
    new Employee(3, "Mark Zuckerberg", 300000.0)
};
Stream.of(arrayOfEmps);
Stream.of(arrayOfEmps[0], arrayOfEmps[1], arrayOfEmps[2]);

// List
private static List<Employee> empList = Arrays.asList(arrayOfEmps);
empList.stream();
// builder
Stream.Builder<Employee> empStreamBuilder = Stream.builder();
empStreamBuilder.accept(arrayOfEmps[0]);
empStreamBuilder.accept(arrayOfEmps[1]);
empStreamBuilder.accept(arrayOfEmps[2]);
Stream<Employee> empStream = empStreamBuilder.build();

// 2.Operation
// forEach - terminal operation. Used elements will not be used again.
empList.stream().forEach(e -> e.salaryIncrement(10.0));

// map | collect - apply to every elems
// get stuff out of the stream, using reduce funciont Collectors.toList()

public void whenMapIdToEmployees_thenGetEmployeeStream() {
    Integer[] empIds = { 1, 2, 3 };
    
    List<Employee> employees = Stream.of(empIds)
      .map(employeeRepository::findById)
      .collect(Collectors.toList());
    
    assertEquals(employees.size(), empIds.length);
}

//filter
Integer[] empIds = { 1, 2, 3, 4 };
    
List<Employee> employees = Stream.of(empIds)
    .map(employeeRepository::findById)
    .filter(e -> e != null)
    .filter(e -> e.getSalary() > 200000)
    .collect(Collectors.toList());

//findFirst
Employee employee = Stream.of(empIds)
    .map(employeeRepository::findById)
    .filter(e -> e != null)
    .filter(e -> e.getSalary() > 100000)
    .findFirst()
    .orElse(null);

//toArray
Employee[] employees = empList.stream().toArray(Employee[]::new);

//flatMap
//Notice how we were able to convert the Stream<List<String>> to a simpler Stream<String> – using the flatMap() API.
List<List<String>> namesNested = Arrays.asList( 
    Arrays.asList("Jeff", "Bezos"), 
    Arrays.asList("Bill", "Gates"), 
    Arrays.asList("Mark", "Zuckerberg"));

List<String> namesFlatStream = namesNested.stream()
    .flatMap(Collection::stream)
    .collect(Collectors.toList());

//peek
//performs the specified operation on each element of the stream and returns a new stream which can be used further. peek() is an intermediate operation
// forEach is terminal operation, this is intermediate operation. 
// peek can follow a peek, then filter, ...
empList.stream()
    .peek(e -> e.salaryIncrement(10.0))
    .peek(System.out::println)
    .collect(Collectors.toList());

stream.peek(record -> logRecord(record))
                 .peek(record -> inputRate.mark())
                 .filter(record -> {
                if (Objects.isNull(record.value())) {
                nullRecords.inc();
                logger.warn("Null value received from source – Key:{} Topic: {} Partition:{} ",
                    record.key(), record.topic(), record.partition());
                return false;
                }
                return true;
            });

```


### 17 Reflection (Dropwizard config -> factory create sub class)
反射是为了解决在运行期，对某个实例一无所知的情况下，如何调用其方法。

1. Class类 （Class 是一种 class）
```java
//每加载一种class，JVM就为其创建一个Class类型的实例，并关联起来。
Class cls = new Class(String); // Class<String>

//Class实例在JVM中是唯一的。
// 获取class的Class实例的方法有3种，得到的是同一个Class实例
Class cls1 = String.class;
String s = "Hello";
Class cls2 = s.getClass();
boolean sameClass = cls1 == cls2; // true
Class cls3 = Class.forName("java.lang.String");

//Class有这个class的全部信息 
// ┌───────────────────────────┐
// │      Class Instance       │──────> String
// ├───────────────────────────┤
// │name = "java.lang.String"  │
// ├───────────────────────────┤
// │package = "java.lang"      │
// ├───────────────────────────┤
// │super = "java.lang.Object" │
// ├───────────────────────────┤
// │interface = CharSequence...│
// ├───────────────────────────┤
// │field = value[],hash,...   │
// ├───────────────────────────┤
// │method = indexOf()...      │
// └───────────────────────────┘

//拿到了Class实例以后，可以用它创建class
// 获取String的Class实例:
Class cls = String.class;
// 创建一个String实例:
String s = (String) cls.newInstance();
```
2.获取字段

```java

Field getField(name)：根据字段名获取某个public的field（包括父类）
Field getDeclaredField(name)：根据字段名获取当前类的某个field（不包括父类）
Field[] getFields()：获取所有public的field（包括父类）
Field[] getDeclaredFields()：获取当前类的所有field（不包括父类）

一个Field对象包含了一个字段的所有信息

getName()：返回字段名称，例如，"name"；
getType()：返回字段类型，也是一个Class实例，例如，String.class；
getModifiers()：返回字段的修饰符，它是一个int，不同的bit表示不同的含义。

Field f = String.class.getDeclaredField("value");
f.getName(); // "value"
f.getType(); // class [B 表示byte[]类型


例如，对于一个Pair实例，我们可以先拿到name字段对应的Field，再获取这个实例的name字段的值
Field f = Pair.class.getDeclaredField("value");
Pair p = new Pair("Xiao Ming");
String s = (String) f.get(p);
// System.out.println(s); "Xiao Ming"

修改字段的值
Field f = c.getDeclaredField("name");
f.setAccessible(true);
f.set(p, "Xiao Hong");

```

3.调用方法
```java
Method getMethod(name, Class...)：获取某个public的Method（包括父类）
Method getDeclaredMethod(name, Class...)：获取当前类的某个Method（不包括父类）
Method[] getMethods()：获取所有public的Method（包括父类）
Method[] getDeclaredMethods()：获取当前类的所有Method（不包括父类）

一个Method对象包含一个方法的所有信息：
getName()：返回方法名称，例如："getScore"；
getReturnType()：返回方法返回值类型，也是一个Class实例，例如：String.class；
getParameterTypes()：返回方法的参数类型，是一个Class数组，例如：{String.class, int.class}；
getModifiers()：返回方法的修饰符，它是一个int，不同的bit表示不同的含义。
 
invoke
Method m = String.class.getMethod("substring", int.class);
// 在s对象上调用该方法并获取结果:
String r = (String) m.invoke(s, 6);
调用静态方法时，由于无需指定实例对象，所以invoke方法传入的第一个参数永远为null
Method m = Integer.class.getMethod("parseInt", String.class);
// 调用该静态方法并获取结果:
Integer n = (Integer) m.invoke(null, "12345");
为了调用非public方法，我们通过Method.setAccessible(true)

多态时 调用的是子类复写的

```

4.构造函数
调用Class.newInstance()的局限是，它只能调用该类的public无参数构造方法。
如果构造方法带有参数，或者不是public，就无法直接通过Class.newInstance()来调用。

所以提供了Constructor对象

```java
Constructor cons1 = Integer.class.getConstructor(int.class);
// 调用构造方法:
Integer n1 = (Integer) cons1.newInstance(123);
System.out.println(n1);
```

5.获取继承关系
```java
//父类
Class i = Integer.class;
Class n = i.getSuperclass();
//接口
Class[] is = s.getInterfaces();
//继承关系 Class 实例来判断
Integer.class.isAssignableFrom(Integer.class); // true，因为Integer可以赋值给Integer


```

6.动态代理
不编写实现类，直接在运行期创建某个interface的实例呢？
这是可能的，因为Java标准库提供了一种动态代理（Dynamic Proxy）的机制：可以在运行期动态创建某个interface的实例。


---

### 18 Generic type 范型
ref: [liaoxuefeng java](https://www.liaoxuefeng.com/wiki/1252599548343744/1265102638843296)

1.Use Generic Type(Array as example):
```java
public class ArrayList<T> {
    private T[] array;
    private int size;
    public void add(T e) {...}
    public void remove(int index) {...}
    public T get(int index) {...}
}

// 向上转型/implements
public class ArrayList<T> implements List<T> {
    ...
}
List<String> list = new ArrayList<String>();

// 但是T不能继承U，
// 比如Integer -> Number 
// 否则会出现添加Float/Double也能添加的状况

```
使用泛型时，把泛型参数<T>替换为需要的class类型，例如：ArrayList<String>，ArrayList<Number>等；
可以省略编译器能自动推断出的类型，例如：List<String> list = new ArrayList<>();；
不指定泛型参数类型时，编译器会给出警告，且只能将<T>视为Object类型；
可以在接口中定义泛型类型，实现此接口的类必须实现正确的泛型类型。

2.Write Generic Type
把特定的类型用T表示，static单独列出。因为static的范型和这个类已经没有关系了。
```java
public class Pair<T> {
    private T first;
    private T last;
    public Pair(T first, T last) {
        this.first = first;
        this.last = last;
    }
    public T getFirst() {
        return first;
    }
    public T getLast() {
        return last;
    }
    // 静态泛型方法应该使用其他类型区分:
    public static <K> Pair<K> create(K first, K last) {
        return new Pair<K>(first, last);
    }
}
```
多个范型
```java
public class Pair<T, K> {
    private T first;
    private K last;
    public Pair(T first, K last) {
        this.first = first;
        this.last = last;
    }
    public T getFirst() { ... }
    public K getLast() { ... }
}
Pair<String, Integer> p = new Pair<>("test", 123);
```
范型擦拭法：编译器把所有T视作Object，在用的时候强制转型。
所以
i. 不能用基本类型，比如int
ii. 不能获得范型的class。因为得来的都是<Object>的class 
iii. 不能用 instanceof
iv. 不能在范型里new
```java
// public class Pair<T> {
//     private T first;
//     private T last;
//     public Pair() {
//         // Compile error:
//         first = new T();
//         last = new T();
//     }
// }

public class Pair<T> {
    private T first;
    private T last;
    public Pair(Class<T> clazz) {
        first = clazz.newInstance();
        last = clazz.newInstance();
    }
}
Pair<String> pair = new Pair<>(String.class);
```
v. Override要注意不能和Object重名
```java
// public class Pair<T> {
//     public boolean equals(T t) {
//         return this == t;
//     }
// }
public class Pair<T> {
    public boolean same(T t) {
        return this == t;
    }
}
```

3.extend generic type class
```java
public class IntPair extends Pair<Integer> {
}
IntPair ip = new IntPair(1, 2);
// 前面讲了，我们无法获取Pair<T>的T类型，即给定一个变量Pair<Integer> p，无法从p中获取到Integer类型。
// 但是，在父类是泛型类型的情况下，编译器就必须把类型T（对IntPair来说，也就是Integer类型）保存到子类的class文件中，不然编译器就不知道IntPair只能存取Integer这种类型。
// 在继承了泛型类型的情况下，子类可以获取父类的泛型类型. 获取父类的泛型类型代码比较复杂.

```

4.通配符 ? / extends / super
实现T的子类通用
```java
public class Main {
    public static void main(String[] args) {
        Pair<Integer> p = new Pair<>(123, 456);
        int n = add(p);
        System.out.println(n);
    }

    static int add(Pair<? extends Number> p) {
        Number first = p.getFirst();
        Number last = p.getLast();
        return first.intValue() + last.intValue();
    }
}

class Pair<T> {
    private T first;
    private T last;
    public Pair(T first, T last) {
        this.first = first;
        this.last = last;
    }
    public T getFirst() {
        return first;
    }
    public T getLast() {
        return last;
    }
}
```
只读但是不能用来修改
```java
int sumOfList(List<? extends Integer> list) {
    int sum = 0;
    for (int i=0; i<list.size(); i++) {
        Integer n = list.get(i);
        sum = sum + n;
    }
    return sum;
}
// 允许调用get()方法获取Integer的引用；
// 不允许调用set(? extends Integer)方法并传入任何Integer的引用（null除外）
```
定义的时候,T extends 可以限制其类型
```java
public class Pair<T extends Number> { ... }
```
super: 用的时候再看

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

## e5 MultiThreading
```java
// multithreading syntax

available.awaitNanos(waitMillSec * 1000000);
Thread.currentThread().getName();
Thread.sleep(); // sleep, await, join时要处理InterruptedException
Thread.currentThread().isInterrupted()
/* 处理thread.interrupt()
当线程A运行时，线程B可以调用A.interrupt()方法，来设置线程A的中断标志为true ()，然后线程B立即返回。注意，这里仅仅是设置标志，线程A实际并没有被中断，它会继续往下执行。但是有一种情况，如果线程A调用了wait系列函数、join方法或者sleep方法而被阻塞挂起，这时候线程B调用A.interrupt()方法时，线程A会在调用wait/join/sleep方法处抛出InterruptedException异常而返回。
*/



// 1.synchronized lock
Object lock = new Object();
public void increment() {
    synchronized (lock) {
        items++;
    }
}

public void run() {
    synchronized (queue) {
        ....
    }
}

// 2.ReentrantLock lock + condition
Lock lockObject = new ReentrantLock();
Condition cond = lockObject.newCondition();
Resource resource = new Resource();
public void method(){
    try {
        lockObject.lock();
        while () {
            cond.await();
        }
    } catch (InterruptedException e){
        e.printStackTrace();
    }
    finally {
        lockObject.unlock();
    }
}
cond.signal();
cond.signalAll();



// 3.Semophora
```

## e6 lambda function

```java
ArrayList<Integer> numbers = new ArrayList<Integer>();
numbers.add(5);
numbers.add(9);
numbers.add(8);
numbers.add(1);
numbers.forEach( (n) -> { System.out.println(n); } );
// stream().forEach is undefined. forEach() is defined.

```



### final & static

```
1. final 
对于一个final变量，如果是基本数据类型的变量，则其数值一旦在初始化之后便不能更改；如果是引用类型的变量，则在对其初始化之后便不能再让其指向另一个对象。
//final类不能被继承，没有子类，final类中的方法默认是final的。
//final方法不能被子类的方法覆盖，但可以被继承。
//final成员变量表示常量，只能被赋值一次，赋值后值不再改变。
//final不能用于修饰构造方法。

2. static
static final用来修饰成员变量和成员方法，可简单理解为“全局常量”
static 可以修饰代码块
static 全class共享
```

