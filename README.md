# HomeWork

当然不只会写代码！这是一个 Python 练习项目，包含算法练习与数据分析工具。

> Of course not! This is a Python practice project featuring algorithm exercises and data analysis utilities.

---

## 文件说明 / Files

### `fibfunc`
最初的斐波那契数列练习，返回前 n 项的列表。

The original Fibonacci practice: returns a list of the first n terms.

### `deepresearch.py`
数据分析模块，提供常用描述性统计函数，并以斐波那契数列为示例演示用法。

A data analysis module providing common descriptive statistics, demonstrated with the Fibonacci sequence.

| 函数 / Function | 说明 / Description |
|---|---|
| `fibonacci(n)` | 生成前 n 个斐波那契数 / Generate the first n Fibonacci numbers |
| `mean(data)` | 算术平均值 / Arithmetic mean |
| `median(data)` | 中位数 / Median |
| `variance(data)` | 方差 / Population variance |
| `std_dev(data)` | 标准差 / Standard deviation |
| `analyze(data)` | 完整统计摘要 / Full descriptive statistics summary |

## 快速开始 / Quick Start

```bash
python deepresearch.py
```

示例输出 / Example output:

```
Fibonacci sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
  count: 10
  mean: 8.8
  median: 4.0
  variance: 109.56
  std_dev: 10.467
  min: 0
  max: 34
```

也可以在自己的代码中导入 / You can also import it in your own code:

```python
from deepresearch import fibonacci, analyze

stats = analyze(fibonacci(15))
print(stats)
```

---

持续更新中 🚀 / More exercises coming soon 🚀
