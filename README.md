# LeetCode Workspace

这个仓库用于记录 Java 版 LeetCode 题解与日常算法练习。

## 项目环境

- Java 17
- Maven
- 包名：`com.wan`

## 目录结构

```text
.
├── pom.xml
├── README.md
└── src
    └── main
        └── java
            └── com
                └── wan
                    ├── Main.java
                    ├── topic_1.java
                    ├── topic_11.java
                    └── topic_283.java
```

## 已包含题目

| 文件 | 题目 | 说明 |
| --- | --- | --- |
| `topic_1.java` | 1. 两数之和 | 待完善 |
| `topic_11.java` | 11. 盛最多水的容器 | 暴力解法、双指针解法 |
| `topic_283.java` | 283. 移动零 | 原地移动、减少写操作优化 |

## 运行方式

编译项目：

```bash
mvn compile
```

运行指定题目示例：

```bash
mvn exec:java -Dexec.mainClass="com.wan.topic_11"
```

如果本地没有配置 `exec-maven-plugin`，也可以直接在 IntelliJ IDEA 中运行对应类的 `main` 方法。

## 新增题解约定

1. 在 `src/main/java/com/wan/` 下新增题目文件，例如 `topic_20.java`。
2. 类名与文件名保持一致。
3. 在类注释或方法注释中记录题目名称、核心思路和复杂度。
4. 如有多种解法，可以使用不同方法名区分，例如 `solution1`、`solution2`。

## Git 忽略规则

仓库会提交源码、`pom.xml`、`README.md` 等必要文件。

以下内容不会提交：

- IntelliJ IDEA 配置：`.idea/`、`*.iml`
- Maven 编译输出：`target/`
- 系统缓存、日志、临时文件

