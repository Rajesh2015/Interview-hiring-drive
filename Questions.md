🏥 Business Context

Laerdal Medical provides digital medical training programs to healthcare professionals.
Learners from different organizations attempt courses such as BLS, ACLS, and Simulation.

Each course attempt consists of multiple questions.
For every question, the learner submits an answer and receives a score.

The data is provided in nested JSON format.

📂 Input Data

You are given two JSON files:

1️⃣ course_attempts.json

Contains course attempts with nested question-level responses.

Key fields:

attempt_id

learner_id

course_type

attempt_date

responses (array of structs with question details)

2️⃣ learner_details.json

Contains learner master data.

Key fields:

learner_id

learner_name

organization

role

country

🔹 Question 1: Read & Inspect the Data

Load both JSON files into Spark DataFrames.

Print the schema for each DataFrame.

Briefly explain the structure of the responses column.

🔹 Question 2: Flatten Nested Responses

The responses column is an array of structs.

Flatten the data so that each row represents a single question attempt.

Expected columns:

attempt_id

learner_id

learner_name

organization

course_type

attempt_date

question_id

user_answer

correct_answer

score

🔹 Question 3: Course Attempt Score Calculation

For each learner and course attempt, calculate:

Total score obtained

Maximum possible score

Assume each question carries 5 marks

Percentage score

🔹 Question 4: Pass / Fail Evaluation

Apply the following rule:

PASS if percentage ≥ 70

FAIL otherwise

Return:

learner_id

learner_name

course_type

percentage

result

🔹 Question 5: Organization-Level Performance Metrics

For each organization, calculate:

Total number of course attempts

Average percentage score

Pass rate

Percentage of attempts that resulted in PASS

🔹 Question 6: Learners Who Never Took Any Course

Identify learners who never attempted any course.

Expected output:

learner_id

learner_name

organization

role

💡 Hint: Use an appropriate join strategy.

🔹 Question 7: Top Performer per Course (Window Function)

For each course:

- Identify the top-scoring learner
- If multiple learners have the same score, select the earliest attempt


## Notes:
Write clean, readable Spark code

Add brief comments explaining your logic

You may choose Scala or PySpark

Assume data fits in Spark (do not use collect for logic)