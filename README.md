# 🚀 20 PySpark Practice Exercises

A structured collection of **20 hands-on PySpark practice exercises**, designed to develop practical skills in distributed data processing, DataFrame manipulation, data cleaning, aggregation, joins, and window functions.

The exercises are divided into two difficulty levels, progressing from fundamental PySpark operations to intermediate data analytics and data engineering challenges.

## 🎯 Project Objectives

- Develop a strong understanding of PySpark and its DataFrame API.
- Learn to manipulate, transform, and analyse distributed datasets.
- Practise data cleaning and preprocessing techniques.
- Perform aggregations and grouping operations.
- Understand and implement different types of DataFrame joins.
- Develop practical experience with PySpark window functions.
- Apply PySpark concepts to real-world data analytics scenarios.

## 📚 Exercise Structure

This repository contains **20 exercises**, divided into two levels.

### 🟢 Beginner Level (Q1–Q10)

Focus: PySpark fundamentals and basic DataFrame operations.

| #   | Exercise                    | Key Concepts                                           |
| --- | --------------------------- | ------------------------------------------------------ |
| 01  | Create Your First DataFrame | SparkSession, createDataFrame(), show(), printSchema() |
| 02  | Select Specific Columns     | select()                                               |
| 03  | Filter Rows                 | filter(), where(), comparison operators                |
| 04  | Create a New Column         | withColumn(), column expressions                       |
| 05  | Rename and Drop Columns     | withColumnRenamed(), drop()                            |
| 06  | Sort a DataFrame            | orderBy(), asc(), desc()                               |
| 07  | Handle Missing Values       | isNull(), isNotNull(), dropna(), fillna()              |
| 08  | Remove Duplicate Rows       | dropDuplicates(), count()                              |
| 09  | Calculate Basic Statistics  | agg(), sum(), avg(), min(), max(), count()             |
| 10  | Group By                    | groupBy(), agg()                                       |

### 🟠 Intermediate Level (Q11–Q20)

Focus: Advanced DataFrame transformations, aggregations, joins, and analytical operations.

| #   | Exercise                                | Key Concepts                                                                       |
| --- | --------------------------------------- | ---------------------------------------------------------------------------------- |
| 11  | Conditional Columns with when()         | when(), otherwise()                                                                |
| 12  | Multiple Aggregations                   | groupBy(), multiple aggregations, aliases                                          |
| 13  | Group By + HAVING Equivalent            | groupBy(), agg(), filter()                                                         |
| 14  | Join Two DataFrames                     | join(), inner join, left join                                                      |
| 15  | Find Top N Employees Per Department     | Window functions, partitionBy(), orderBy(), row_number()                           |
| 16  | Rank Employees Within Departments       | rank(), dense_rank(), window functions                                             |
| 17  | Running Total                           | Window functions, cumulative sum()                                                 |
| 18  | Compare Current Row With Previous Row   | lag(), window functions                                                            |
| 19  | Customer Purchase Analysis              | Aggregations, window functions                                                     |
| 20  | Mini PySpark Data Engineering Challenge | Data cleaning, feature engineering, aggregations, joins, ranking, window functions |

## 🛠️ Technologies & Tools

- **Programming Language:** Python
- **Big Data Framework:** Apache Spark
- **Python API:** PySpark
- **Development Environment:** Visual Studio Code (Python scripts)
- **Version Control:** Git & GitHub

## 📖 Learning Roadmap

The exercises follow a progressive learning path:

1. **DataFrame Fundamentals** – Creating, inspecting, and manipulating DataFrames.
2. **Data Transformation** – Selecting, filtering, sorting, and creating columns.
3. **Data Cleaning** – Handling missing values and removing duplicates.
4. **Aggregations** – Applying aggregate functions and grouping datasets.
5. **Joins** – Combining multiple DataFrames.
6. **Window Functions** – Implementing row_number(), rank(), dense_rank(), and lag().
7. **Real-World Analysis** – Performing customer, sales, and product analysis.
8. **Data Engineering Challenge** – Building an end-to-end PySpark analysis pipeline.

## ⚙️ Getting Started

### Prerequisites

- Python installed.
- Java installed and configured for Apache Spark.
- Basic understanding of Python programming.
- Familiarity with Pandas and DataFrame operations is helpful.

### Installation

Install PySpark using pip:

```bash
pip install pyspark
```

### Verify Installation

```python
import pyspark

print(pyspark.__version__)
```

### Initialize SparkSession

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark Practice Exercises") \
    .master("local[*]") \
    .getOrCreate()
```

## 📂 Repository Structure

```text
pyspark-20-practice-exercises/
│
├── README.md
│
├── beginner/
│   ├── q01_create_first_dataframe.py
│   ├── q02_select_specific_columns.py
│   ├── q03_filter_rows.py
│   ├── q04_create_new_column.py
│   ├── q05_rename_and_drop_columns.py
│   ├── q06_sort_dataframe.py
│   ├── q07_handle_missing_values.py
│   ├── q08_remove_duplicates.py
│   ├── q09_basic_statistics.py
│   └── q10_group_by.py
│
└── intermediate/
    ├── q11_conditional_columns.py
    ├── q12_multiple_aggregations.py
    ├── q13_group_by_having.py
    ├── q14_dataframe_joins.py
    ├── q15_top_n_employees.py
    ├── q16_employee_ranking.py
    ├── q17_running_total.py
    ├── q18_lag_previous_row.py
    ├── q19_customer_purchase_analysis.py
    └── q20_pyspark_data_engineering_challenge.py
```

## 📈 Progress Tracker

### Beginner Level

- [x] Q01 – Create Your First DataFrame
- [ ] Q02 – Select Specific Columns
- [ ] Q03 – Filter Rows
- [ ] Q04 – Create a New Column
- [ ] Q05 – Rename and Drop Columns
- [ ] Q06 – Sort a DataFrame
- [ ] Q07 – Handle Missing Values
- [ ] Q08 – Remove Duplicate Rows
- [ ] Q09 – Calculate Basic Statistics
- [ ] Q10 – Group By

### Intermediate Level

- [ ] Q11 – Conditional Columns with when()
- [ ] Q12 – Multiple Aggregations
- [ ] Q13 – Group By + HAVING Equivalent
- [ ] Q14 – Join Two DataFrames
- [ ] Q15 – Find Top N Employees Per Department
- [ ] Q16 – Rank Employees Within Departments
- [ ] Q17 – Running Total
- [ ] Q18 – Compare Current Row With Previous Row
- [ ] Q19 – Customer Purchase Analysis
- [ ] Q20 – Mini PySpark Data Engineering Challenge

### Completed Exercise Details

#### Q01 – Create Your First DataFrame

**Objective:** Create a PySpark DataFrame, inspect its structure, display all records, and retrieve the first three rows.

**Implementation:**

- Initialized a SparkSession named `CustomersDataFrame` using `local[*]` for local execution.
- Created a dataset containing five customer records with `id`, `name`, `age`, and `city` fields.
- Defined the column names using a list and created the DataFrame with `createDataFrame()`.
- Used `show()` to display all records.
- Used `printSchema()` to inspect the DataFrame schema and inferred column data types.
- Used `show(n=3)` to display the first three records.
- Stopped the SparkSession using `spark.stop()` after completing the operations.

**Key Functions:** `SparkSession.builder`, `createDataFrame()`, `show()`, `printSchema()`, `stop()`

## 🎯 Learning Approach

Each exercise is designed to reinforce practical PySpark concepts through hands-on implementation.

The approach is to:

- Attempt each exercise independently before referring to solutions.
- Understand the logic behind each transformation.
- Experiment with different PySpark functions.
- Validate results and investigate unexpected outputs.
- Progress from basic operations to more complex analytical problems.

**The ultimate goal is to develop practical PySpark skills and build a strong foundation for working with big data and data engineering workflows.**

---

⭐ _Learning by doing, one exercise at a time._
