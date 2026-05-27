# 超级好用之Bloom Filter与LRU Cache

## 第 1 页

超级好用之Bloom Filter与LRU Cache

今日目标：

1：完成实战面试题目

2：能说出布隆过滤器的工作原理面试实战

146. LRU 缓存机制

```java
1   class LRUCache {
```
2

```java
3       int capacity;
4       int size;
5       Map<Integer,Node> hashtable;
```
6
7 Node head; //链表头
8 Node tail;//链表尾
9

```java
10       public LRUCache(int capacity) {
    11           hashtable = new HashMap();
    12           this.capacity = capacity;
    13           this.size = 0;
```
14 head = new Node();//哨兵头
15 tail = new Node();//哨兵尾
16 //头尾先接上

```java
17           head.next = tail;
18           tail.prev = head;
19       }
```
20 //获取元素

```java
21       public int get(int key) {
```
22 //判断hashtable中是否存在key

```java
23           Node node = hashtable.get(key);
24           if (node==null) {
    25               return -1;
    26           }
```
27 //将该节点移动到链表头（哨兵后面）

```java
28           moveToHead(node);
29           return node.value;
30       }
31       private void moveToHead(Node node) {
```
32 //分两步走：第一步：将该节点删除,第二步：将该节点添加到头哨兵后面

```java
33           removeNode(node);
34           addToHead(node);
35       }
```
36 //从双向链表中删除该节点

```java
37       private void removeNode(Node node) {
```
38 //拿到前驱和后继

```java
39           Node prevNode = node.prev;
40           Node nextNode = node.next;
```
41 //前驱指向后继

```java
42           prevNode.next = nextNode;
```

## 第 2 页

43 //后继指向前驱

```java
44           nextNode.prev = prevNode;
```
45
46 //清理node的prev和next指针

```java
47           node.prev = null;
48           node.next = null;
49       }
```
50 //将该节点添加到链表头部（头哨兵后面）

```java
51       private void addToHead(Node node) {
```
52 //先拿到原本头部元素(头哨兵后面的第一个元素)

```java
53           Node firstNode = head.next;
```
54 //在哨兵和firstNode中插入node

```java
55           head.next = node;
56           node.next = firstNode;
57           firstNode.prev = node;
58           node.prev = head;
59       }
```
60 //插入元素

```java
61       public void put(int key, int value) {
```
62 //判断key是否在hashtable中

```java
63           Node node = hashtable.get(key);
64           if (node!=null) {
```
65 //更新value

```java
66               node.value = value;
```
67 //将该节点移动到头部

```java
68               moveToHead(node);
69               return;
70           }
```
71
72 //创建新节点

```java
73           node = new Node(key,value);
```
74 //添加哈希表中

```java
75           hashtable.put(key,node);
```
76 //将该新节点添加到头部

```java
77           addToHead(node);
```
78 //元素个数加1

```java
79           this.size ++;
```
80 //判断是否超过容量大小

```java
81           if (this.size > this.capacity) {
```
82 //移除最少使用的元素(尾元素，尾哨兵的前一个)

```java
83               Node n = removeTail();
```
84 //从哈希表中移除对应的key/value

```java
85               hashtable.remove(n.key);
```
86 //元素个数减少

```java
87               this.size--;
88           }
```
89

```java
90       }
```
91 //干掉尾哨兵的前一个元素

```java
92       private Node removeTail() {
    93           Node node = tail.prev;
    94           Node prevNode = node.prev;
```
95 //从双向链表中拿掉node

```java
96           prevNode.next = tail;
97           tail.prev = prevNode;
98           node.prev = null;
99           node.next = null;
100           return node;
```

## 第 3 页

```java
101       }
```
102

```java
103       class Node {
    104           int key;
    105           int value;
```
106

```java
107           Node prev;
108           Node next;
```
109

```java
110           public Node() {}
```
111

```java
112           public Node(int key,int value) {
    113               this.key = key;
    114               this.value = value;
    115           }
    116       }
```
117

```java
118   }
```
119
120 /**
121 * Your LRUCache object will be instantiated and called as such:

```java
122    * LRUCache obj = new LRUCache(capacity);
123    * int param_1 = obj.get(key);
124    * obj.put(key,value);
```
125 */

同类题目：

面试题 16.25. LRU 缓存

460. LFU 缓存
