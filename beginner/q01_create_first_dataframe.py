
from pyspark.sql import SparkSession


# Initialize SparkSession
spark = SparkSession.builder \
    .appName("CustomersDataFrame") \
    .master("local[*]") \
    .getOrCreate()

# Create sample data
data = [
    (1, "Ali", 25, "Karachi"),
    (2, "Sara", 28, "Lahore"),
    (3, "Ahmed", 22, "Islamabad"),
    (4, "John", 30, "Karachi"),
    (5, "Maria", 27, "Lahore"),
]

columns = ["id", "name", "age", "city"]

# Create DataFrame
df = spark.createDataFrame(data, schema=columns)

# Display all rows
print("All Rows:")
df.show()

# Display DataFrame schema
print("DataFrame Schema:")
df.printSchema()

# Display first 3 rows
print("First 3 Rows:")
df.show(n=3)

# Stop SparkSession
spark.stop()
