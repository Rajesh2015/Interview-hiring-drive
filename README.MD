# Interview Hiring Drive - Technical Assessment

Welcome to the technical assessment for the Data Engineering position. This test evaluates your skills in Python programming and Apache Spark.

## 📋 Test Overview

This assessment consists of two main components:

### 1. **Programming Question** 
📁 Location: `app/programming_question.py`

### 2. **Apache Spark Data Engineering Questions**
📁 Location: `Spark-Questions.md`

- **Topic**: Real-world Data Processing with PySpark
- **Business Context**: Healthcare training data analysis for Laerdal Medical
- **Number of Questions**: 7 questions covering:
  - Data loading and schema inspection
  - Nested data flattening
  - Aggregations and calculations
  - Join operations
  - Window functions
  - Performance metrics

**Data Files Provided:**
- `data/course_attempts.json` - Course attempt records with nested question responses
- `data/earner_details.json` - Learner master data

## 🚀 Getting Started

Notes:You can try solving it in your local before trying out to deploy through docker.
### Prerequisites
Please refer to **`SetUp.md`** for detailed setup instructions including:
- Docker Desktop installation
- Git installation
- Building and starting the Spark cluster
- Running your Spark jobs
- Accessing Jupyter Notebook (optional)

### Quick Start
1. Read the setup instructions in `SetUp.md`
2. Build and start the Docker environment
3. Start with the programming question in `app/programming_question.py`
4. Proceed to Spark questions in `Spark-Questions.md`
5. Write your Spark solutions and test them in the cluster

## 📝 Submission Guidelines

1. Complete the programming question in `app/programming_question.py`
2. Create your Spark solution files (e.g., `spark_solution.py` or notebooks)

Notes:You can use scala as well to solve these question.