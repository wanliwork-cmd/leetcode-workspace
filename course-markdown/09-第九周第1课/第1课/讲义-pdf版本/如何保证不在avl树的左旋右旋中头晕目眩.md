# 如何保证不在avl树的左旋右旋中头晕目眩

## 第 1 页

如何保证不在avl树的左旋右旋中头晕目眩

今日目标：

1：能说出AVL树的定义及特点

2：能说出AVL树插入过程中出现的四种失衡情况及如何调整

3：完成AVL树的插入实现

1、AVL树

在前面的课程中，我们学习了二叉搜索树（BST）,它的插入、删除、查找操作时间复杂度在最好情况下才是 O(log n)，不过在二叉查找树频繁的动态更新过程中，会逐渐退化直至最坏的情况变为链表，时间复杂度退化为O(n)，所以我们要解决这种复杂度退化的问题就要找到一种平衡二叉树，平衡二叉查找树中“平衡”的意思，其实就是让整棵树左右看起来比较“对称”、比较“平衡”，不要出现左子树很高、右子树很矮的情况。这样就能让整棵树的高度相对来说低一些，相应的插入、删除、查找等操作的效率高一些。

在根据输入的数据构建BST树时，特别依赖输入数据是否有序，如果输入数据相对有序那产生的树的结构会非常的不平衡，那查询等相关操作的效率会受到影响。

平衡二叉查找树：简称平衡二叉树，发明平衡二叉查找树这类数据结构的初衷是，解决普通二叉查找树在频繁的插入、删除等动态更新的情况下，出现时间复杂度退化的问题。

也就是说这类二叉搜索树在插入，删除操作后，如果树失去了平衡，它能通过一些操作自平衡。常见的有 AVL树，红黑树等。

## 第 2 页

1.1、定义及特点

AVL树是最早发明的自平衡二叉搜索树之一，由前苏联的数学家 Adelse-Velskil 和 Landis 在 1962
年提出的高度平衡的二叉树，根据科学家的英文名也称为 AVL 树。它的定义如下：

1：它是一棵BST树

2：它的每个节点左右子树高度之差（简称平衡因子/Balance Factor）绝对值不超过1

3：可以是空树，如果不是空树，任何一个结点的左子树与右子树都是平衡二叉树

二叉树的高度有两种定义：

1. 从根节点到最深节点的最长路径的节点数。
2. 从根到最深节点的最长路径的边数。

如果采用第一种定义：空树的高度为0，叶子节点的高度为1

如果采用第二种定义：空树的高度为-1，叶子节点的高度为0

两种均可，为了便于理解我们取第一种定义（因为只需要数节点数即可）

图二中：7的左子树是一棵avl树，但是整体并非avl树。

AVL树具备以下的一些特点：

1、对于给定结点数为n的AVL树，最大高度为O(log2 n)，也就说，从n个数中，查找一个特定值的时间复杂度是O(log n)。因此，AVL 是一种特别适合进行查找操作的树,，此外在AVL树中插入，删除操作的时间复杂度均为O（n）

2、在平衡二叉树中，当我们插入新元素或删除某元素时，为了保证二叉搜索树的特性，很容易导致某些结点失衡，即该结点的平衡因子大于1，而平衡二叉树的平衡二字体现了它可以自动恢复平衡，这个自动平衡的过程是通过旋转来完成的。

1.2、四种失衡及旋转

在平衡二叉树的插入和删除操作中，某些节点会失去平衡，我们先来看插入的情况，如果A是一颗平衡二叉树，如果新插入一个元素，会有两个结果

平衡没有被打破，不用调整平衡被打破，需要调整

对于任意一次插入所造成的不平衡，都可以简化为下列4中情况：

情况1-RR：插入节点在失衡节点右子树的右边，我们要对失衡节点进行左旋。

## 第 3 页

图解如下：失衡节点的平衡因子为 -2

情况2-LL：插入节点在失衡节点左子树的左边，我们需要对失衡节点进行右旋

图解如下：失衡节点的平衡因子为2

## 第 4 页

与此同时，我们发现，左旋和右旋操作其实是成镜像关系的。

情况3-LR：插入节点在失衡节点左子树的右边，先对失衡节点的左子树左旋(左子树为RR情况)，再对失衡节点右旋(失衡节点为LL情况)

图解如下：失衡节点的平衡因子为2

## 第 5 页

情况4-RL：插入节点在失衡节点右子树的左边，先对失衡节点右子树右旋（右子树为LL情况），再对失衡节点左旋（失衡节点为RR情况）

图解如下：失衡节点的平衡因子为 -2

以上就是平衡二叉树四种失衡及对应的旋转调整情况。

1.3、AVL的实现

1、创建AVL树， com.itheima.tree.AvlTree，定义树的节点AvlNode

```java
1  package com.itheima.tree;
```
2
3 /**
4 * Created by 传智教育*黑马程序员.
5 */

```java
6  public class AvlTree {
```
7

## 第 6 页

```java
8       AvlNode root;
```
9
10
11
12 @Override

```java
13       public String toString() {
    14           StringBuilder sb = new StringBuilder();
    15           sb.append("该树的前序遍历结果为:");
    16           preOrder(root,sb);
    17           sb.append("该树的中序遍历结果为:");
    18           inOrder(root,sb);
    19           sb.append("该树的后序遍历结构为:");
    20           postOrder(root,sb);
    21           return sb.toString();
    22       }
    23       private void inOrder(AvlNode node, StringBuilder sb){
        24           if (node == null) {
            25               return;
            26           }
            27           inOrder(node.left,sb);
            28           sb.append(node.key).append("->");
            29           inOrder(node.right,sb);
            30       }
```
31

```java
32       private void preOrder(AvlNode node, StringBuilder sb) {
    33           if (node == null) {
        34               return;
        35           }
        36           sb.append(node.key).append("->");
        37           preOrder(node.left,sb);
        38           preOrder(node.right,sb);
        39       }
```
40

```java
41       private void postOrder(AvlNode node, StringBuilder sb) {
    42           if (node == null) {
        43               return;
        44           }
        45           postOrder(node.left,sb);
        46           postOrder(node.right,sb);
        47           sb.append(node.key).append("->");
        48       }
```
49
50

```java
51       public static class AvlNode{
    52           int key;
    53           AvlNode left;
    54           AvlNode right;
```
55 /**
56 * 我们取第一种高度定义:从根节点到最深节点的最长路径的节点数
57 * 故：空树高度记为0，叶子节点高度记为1
58 */

```java
59           int height =1;
60           public AvlNode(int key) {
    61               this.key = key;
    62           }
    63       }
    64   }
```
65

## 第 7 页

2、定义一个方法用以获取节点的高度

1 /**
2 * 获取节点的高度
3 * 这里高度的定义是：从根节点到最深节点的最长路径的节点数。
4 * @param node
5 * @return
6 */

```java
7  public  int getHeight(AvlNode node){
```
8 return node == null ? 0 : node.height; // 空树的高度为0

```java
9  }

3、编写一个函数针对           RR情况进行旋转        public AvlNode RRrotate(AvlNode unbalance) {

```
1 /**
2 * RR旋转:对失衡节点进行左旋
3 * 20 30
4 * / \ / \
5 * 10 30 20 40
6 * / \ --RR旋转- / \ \
7 * 25 40 10 25 50
8 * \
9 * 50
10 * @param unbalance失衡节点
11 * @return调整后的根节点
12 */
13 public AvlNode RRrotate(AvlNode unbalance) { // 20为失衡点
14 AvlNode root = unbalance.right;//失衡点的右子树的根结点30作为新的根结点
15 unbalance.right = root.left;//将新的根结点的左子树25成为失衡点20的右子树
16 root.left = unbalance; // 将失衡点20作为新的根结点的左子树
17 /**
18 * 重新设置失衡点20和新节点30的高度其他节点的高度不变
19 * 节点高度如何确定？
20 * 节点的高度= Math.max(左子树的高度,右子树的高度) +1
21 */
22 unbalance.height =

```java
Math.max(getHeight(unbalance.left),getHeight(unbalance.right)) +1;
23      root.height = Math.max(getHeight(root.left),getHeight(root.right)) +1;
```
24 return root;// 新的根节点取代原失衡点的位置

```java
25  }

4、编写一个函数针对           LL情况进行旋转：        public AvlNode LLrotate(AvlNode unbalance) {

```
1 /**
2 * LL旋转：对失衡节点进行右旋
3 * 30 20
4 * / \ / \
5 * 20 40 10 30
6 * / \ --LL旋转- / / \
7 * 10 25 5 25 40

## 第 8 页

8 * /
9 * 5
10 * @param unbalance 失衡节点
11 * @return调整后的根节点
12 */
13 public AvlNode LLrotate(AvlNode unbalance) { // 30为失衡点
14 AvlNode root = unbalance.left;//失衡点的左子树的根结点20作为新的根结点
15 unbalance.left = root.right;//将新的根结点的右子树25成为失衡点30的左子树
16 root.right = unbalance;// 将失衡点30作为新的根结点的右子树
17 // 重新设置失衡点30和新节点20的高度
18 unbalance.height =

```java
Math.max(getHeight(unbalance.left),getHeight(unbalance.right)) +1;
19      root.height = Math.max(getHeight(root.left),getHeight(root.right)) +1;
20      return root;
21  }

```
5、编写两个函数分别针对LR,RL两种情况进行旋转

1 /**
2 * LR旋转：先对失衡节点的左子树按RR情况处理，再对失衡节点按LL处理
3 * @param unbalance
4 * @return
5 */

```java
6  public AvlNode LRrotate(AvlNode unbalance) {
```
7 unbalance.left = RRrotate(unbalance.left); // 先将失衡点的左子树进行RR旋转
8 return LLrotate(unbalance);// 再将失衡点进行LL平衡旋转并返回新节点代替原失衡点

```java
9  }
```
10
11 /**
12 * RL旋转：先对失衡节点的右子树按LL情况处理，再对失衡节点按RR情况处理
13 * @param unbalance
14 * @return
15 */

```java
16  public AvlNode RLrotate(AvlNode unbalance) {
```
17 unbalance.right = LLrotate(unbalance.right);// 先将失衡点的右子树进行LL平衡旋转
18 return RRrotate(unbalance);// 再将失衡点进行RR平衡旋转并返回新节点代替原失衡点

```java
19  }

```
6、编写插入操作，插入操作要注意几点

AVL树也是一棵BST树，插入要符合BST树的特征插入操作涉及到从根节点开始依次进行比较，直到插入。插入完成后要从原路回溯查找失衡节点，并且进行旋转调整，故相对较好的实现方式是基于递归来完成。

```java
1  public void insert(int key) {
    2      this.root = insert(this.root,key);
    3  }
```
4
5 /**
6 * 针对一棵二叉搜索树,通过递归的方式去插入
7 * 同时在回溯的过程中找到失衡节点,判断属于RR,LL,LR,RL中的哪种情况，进行旋转调整，
8 * 最后插入路线上的每个节点需要重新调整高度

## 第 9 页

9 * @param tree
10 * @param key
11 * @return
12 */

```java
13  private AvlNode insert(AvlNode tree,int key) {
```
14 //terminal

```java
15      if (tree == null) {
    16          tree = new AvlNode(key);
    17          return tree;
    18      }
```
19 //current logic
20 /**
21 * 判断 key是插入到tree的左子树还是右子树
22 * 回溯的过程中判断该节点是否失衡
23 * 如果失衡判断属于哪种情况,根据情况进行调整
24 */
25 if (key > tree.key) { //插入到右子树
26 //drill down 插入到右子树

```java
27          tree.right = insert(tree.right,key);
```
28 //判断当前节点tree是否失衡

```java
29          if (Math.abs(getHeight(tree.left) - getHeight(tree.right)) > 1) {
```
30 //判断属于RR 还是RL

```java
31              if (key > tree.right.key) {
```
32 //RR情况

```java
33                  tree = RRrotate(tree);
34              }else {
```
35 //RL情况

```java
36                  tree = RLrotate(tree);
37              }
38          }
```
39 }else if (key < tree.key) {//插入到左子树
40 //drill down 插入到左子树

```java
41          tree.left = insert(tree.left,key);
```
42 //判断当前节点tree是否失衡

```java
43          if (Math.abs(getHeight(tree.left) - getHeight(tree.right)) > 1) {
```
44 //判断属于LL,还是LR

```java
45              if (key < tree.left.key) {
```
46 //LL情况

```java
47                  tree = LLrotate(tree);
48              }else {
```
49 //LR情况

```java
50                  tree = LRrotate(tree);
51              }
52          }
53      }else {
```
54 //根据情况，不做操作或者更新该节点

```java
55      }
```
56 //重新调整该节点的高度

```java
57      tree.height = Math.max(getHeight(tree.left),getHeight(tree.right)) +1;
58      return tree;
59  }

```
7、编写测试代码进行测试： com.itheima.tree.AvlTreeTest

比对RR,RL,LR,RL的四张图片测试理解。

## 第 10 页

```java
1   package com.itheima.tree;
```
2
3 /**
4 * Created by 传智教育*黑马程序员.
5 */

```java
6   public class AvlTreeTest {
```
7

```java
8       public static void main(String[] args) {
    9           //testRR();
    10           //testLL();
    11           //testLR();
    12           testRL();
    13       }
```
14 //测试RR情况

```java
15       public static void   testRR(){
    16           AvlTree avlTree = new AvlTree();
    17           avlTree.insert(1);
    18           avlTree.insert(2);
    19           avlTree.insert(3);
    20           System.out.println(avlTree);
    21           avlTree.insert(4);
    22           avlTree.insert(5);
    23           System.out.println(avlTree);
    24           avlTree.insert(6);
    25           System.out.println(avlTree);
    26           avlTree.insert(7);
    27           avlTree.insert(8);
    28           avlTree.insert(9);
    29           System.out.println(avlTree);
    30           avlTree.insert(10);
    31       }
```
32

```java
33       public static void testLL(){
    34           AvlTree avlTree = new AvlTree();
    35           avlTree.insert(10);
    36           avlTree.insert(9);
    37           avlTree.insert(8);
    38           System.out.println(avlTree);
    39           avlTree.insert(7);
    40           avlTree.insert(6);
    41           System.out.println(avlTree);
    42           avlTree.insert(5);
    43           System.out.println(avlTree);
    44           avlTree.insert(4);
    45           avlTree.insert(3);
    46           avlTree.insert(2);
    47           avlTree.insert(1);
    48           System.out.println(avlTree);
    49       }
```
50
51

```java
52       public static void testLR(){
    53           AvlTree avlTree = new AvlTree();
    54           avlTree.insert(10);
    55           avlTree.insert(7);
    56           avlTree.insert(9);
    57           System.out.println(avlTree);
    58           avlTree.insert(2);
```

## 第 11 页

```java
59          avlTree.insert(5);
60          avlTree.insert(6);
61          System.out.println(avlTree);
62          avlTree.insert(3);
63          avlTree.insert(1);
64          avlTree.insert(4);
65          System.out.println(avlTree);
66      }
```
67

```java
68      public static void testRL(){
    69          AvlTree avlTree = new AvlTree();
    70          avlTree.insert(1);
    71          avlTree.insert(4);
    72          avlTree.insert(2);
    73          System.out.println(avlTree);
    74          avlTree.insert(9);
    75          avlTree.insert(6);
    76          System.out.println(avlTree);
    77          avlTree.insert(5);
    78          System.out.println(avlTree);
    79          avlTree.insert(8);
    80          avlTree.insert(10);
    81          avlTree.insert(7);
    82          System.out.println(avlTree);
    83      }
    84  }
```
85

8、复杂度分析，插入操作主要分两部分

比较然后找到插入的位置，比较的过程类似二分，复杂度是O(log n)
回溯的过程中找到失衡节点并进行平衡，平衡操作最多进行两次旋转，复杂度O(1)

故总的时间复杂度是O(log n)

9、面试实战题目

1382. 将二叉搜索树变平衡

进阶：对于AVL树的查询操作和删除操作应该如何来完成呢？

1、对于查询，AVL树也是一棵BST树，所以查询操作跟BST的查询操作一样，比较简单，复杂度O(log n)

2、对于删除，删除情况跟BST树一样，只不过删除之后也需要查找失衡节点并进行自平衡操作。
