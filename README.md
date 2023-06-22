# Poetry

非常全的古诗词数据，收录了从先秦到现代的共计 85 万余首古诗词。

## 统计信息

| 朝代                   | 诗词数  | 作者数  |
|-----------------------|--------|--------|
| 宋                    | 287114 |   9446 |
| 明                    | 236957 |   4439 |
| 清                    |  90089 |   8872 |
| 唐                    |  49195 |   2736 |
| 元                    |  37375 |   1209 |
| 近现代                |  28419 |    790 |
| 当代                  |  28219 |    177 |
| 明末清初               |  17700 |    176 |
| 元末明初               |  15736 |     79 |
| 清末民国初             |  15367 |     99 |
| 清末近现代初           |  12464 |     48 |
| 宋末元初              |  12058 |     41 |
| 南北朝                |   4586 |    434 |
| 近现代末当代初         |   3426 |     23 |
| 魏晋                  |   3020 |    251 |
| 金末元初              |   3019 |     17 |
| 金                    |   2741 |    253 |
| 民国末当代初           |   1948 |      9 |
| 隋                    |   1170 |     84 |
| 唐末宋初              |   1118 |     44 |
| 先秦                  |    570 |      8 |
| 隋末唐初              |    472 |     40 |
| 汉                    |    363 |     83 |
| 宋末金初              |    234 |      9 |
| 辽                    |     22 |      7 |
| 秦                    |      2 |      2 |
| 魏晋末南北朝初          |      1 |      1 |
| 总和                  | 853385 |  29377 |

## 数据说明

古诗词数据按朝代存储在多个 CSV 文件中，以避免单个文件过大。有 `题目`、`朝代`、`作者` 和 `内容` 四个字段。

古诗词中有一些生僻字，属于 utf8mb4 字符，在许多设备中无法显示，使用 `?` 替代。

## 导入数据库

为方便导入，将多个 CSV 文件合并成一个。这通过执行如下命令实现：

```shell
python scripts/merge.py
```

该命令将在当前目录下生成 `poetry.csv` 文件。

### MySQL 8

创建数据库：

```sql
CREATE DATABASE poetry CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

创建数据表：

```sql
use poetry;
CREATE TABLE `poetry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` char(200) DEFAULT NULL,
  `dynasty` char(50) DEFAULT NULL,
  `author` char(100) DEFAULT NULL,
  `content` text,
  PRIMARY KEY (`id`)
);
```

查看 `secure_file_priv` 设置：

```sql
SHOW variables like '%secure_file_priv%';
```

结果类似于：

```sql
+------------------+------------------------------------------------+
| Variable_name    | Value                                          |
+------------------+------------------------------------------------+
| secure_file_priv | C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\ |
+------------------+------------------------------------------------+
1 row in set, 1 warning (0.0014 sec)
```

该目录可能因环境不同而不同。若 `secure_file_priv` 的 `Value` 为空，请自行搜索如何设置。

把 `poetry.csv` 文件复制到 `secure_file_priv` 目录中，Windows 用户可参考如下命令：

```shell
copy poetry.csv "C:\ProgramData\MySQL\MySQL Server 8.0\Uploads"
```

从 CSV 文件中导入数据：

```sql
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\poetry.csv'
INTO TABLE `poetry`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' (title, dynasty, author, content);
```

## License

[MIT](https://github.com/werner-wiki/Poetry/blob/master/LICENSE) 许可证。
