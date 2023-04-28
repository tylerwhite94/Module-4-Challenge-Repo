# Dependencies and Setup
import pandas as pd
from pathlib import Path

# File to Load (Remember to Change These)
school_data_to_load = Path("Resources/schools_complete.csv")
student_data_to_load = Path("Resources/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
df_school_data = pd.read_csv(school_data_to_load)
df_student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
df_school_data_complete = pd.merge(df_student_data, df_school_data, how="left", on=["school_name"])
df_school_data_complete.head()

# Calculate the total number of unique schools
school_count = len(df_school_data["School ID"].unique())
school_count

# Calculate the total number of students
student_count = len(df_student_data["Student ID"].unique())
student_count

# Calculate the total budget
total_budget = sum(df_school_data["budget"])
total_budget

# Calculate the average (mean) math score
average_math_score = df_student_data["math_score"].mean()
average_math_score

# Calculate the average (mean) reading score
average_reading_score = df_student_data["reading_score"].mean()
average_reading_score

# Use the following to calculate the percentage of students who passed math (math scores greather than or equal to 70)
passing_math_count = df_school_data_complete[(df_school_data_complete["math_score"] >= 70)].count()["student_name"]
passing_math_percentage = passing_math_count / float(student_count) * 100
passing_math_percentage

# Calculate the percentage of students who passed reading (hint: look at how the math percentage was calculated)  
passing_reading_count = df_school_data_complete[(df_school_data_complete["reading_score"] >= 70)].count()["student_name"]
passing_reading_percentage = passing_reading_count / float(student_count) * 100
passing_reading_percentage 

# Use the following to calculate the percentage of students that passed math and reading
passing_math_reading_count = df_school_data_complete[
    (df_school_data_complete["math_score"] >= 70) & (df_school_data_complete["reading_score"] >= 70)
].count()["student_name"]
overall_passing_rate = passing_math_reading_count /  float(student_count) * 100
overall_passing_rate

# Create a high-level snapshot of the district's key metrics in a DataFrame
district_summary = pd.DataFrame({"Total Schools": [school_count],
                                    "Total Students": student_count,
                                    "Total Budget": total_budget,
                                    "Average Math Score": average_math_score,
                                    "Average Reading Score": average_reading_score,
                                    "Total Passing Math": passing_math_count,
                                    "Percent Passing Math": passing_math_percentage,
                                    "Total Passing Reading": passing_reading_count,
                                    "Percent Passing Reading": passing_reading_percentage,
                                    "Total Passing Math & Reading": passing_math_reading_count,
                                    "Percent Passing Math & Reading": overall_passing_rate})

# Formatting
district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,.2f}".format)

# Display the DataFrame
district_summary

# Use the code provided to select all of the school types
school_types = df_school_data.sort_values("school_name").type
school_types

# Calculate the total student count per school
students_per_school_count = df_school_data_complete["school_name"].value_counts()
students_per_school_count

# Calculate the total school budget and per capita spending per school
per_school_budget = df_school_data_complete.groupby(["school_name"]).mean()["budget"]
per_school_capita = per_school_budget / students_per_school_count
per_school_budget
per_school_capita

# Calculate the average test scores per school
per_school_math = df_school_data_complete.groupby(["school_name"]).mean()["math_score"]
per_school_reading = df_school_data_complete.groupby(["school_name"]).mean()["reading_score"]
per_school_math
per_school_reading

# Calculate the number of students per school with math scores of 70 or higher
students_passing_math = df_school_data_complete[(df_school_data_complete["math_score"] >= 70)]
school_students_passing_math = students_passing_math.groupby(["school_name"]).size()
students_passing_math
school_students_passing_math

# Calculate the number of students per school with reading scores of 70 or higher
students_passing_reading = df_school_data_complete[(df_school_data_complete["reading_score"] >= 70)]
school_students_passing_reading = students_passing_reading.groupby(["school_name"]).size()
students_passing_reading
school_students_passing_reading

# Use the provided code to calculate the number of students per school that passed both math and reading with scores of 70 or higher
students_passing_math_and_reading = df_school_data_complete[
    (df_school_data_complete["reading_score"] >= 70) & (df_school_data_complete["math_score"] >= 70)
]
school_students_passing_math_and_reading = students_passing_math_and_reading.groupby(["school_name"]).size()
school_students_passing_math_and_reading

# Use the provided code to calculate the passing rates
per_school_passing_math = school_students_passing_math / students_per_school_count * 100
per_school_passing_reading = school_students_passing_reading / students_per_school_count * 100
overall_passing_rate = school_students_passing_math_and_reading / students_per_school_count * 100

# Create a DataFrame called `per_school_summary` with columns for the calculations above.
per_school_summary = pd.DataFrame({"School Type": school_types,
                                      "Total Students": students_per_school_count,
                                      "Total School Budget": per_school_budget,
                                      "Per Student Budget": per_school_capita,
                                      "Average Math Score": per_school_math,
                                      "Average Reading Score": per_school_reading,
                                      "% Passing Math": per_school_passing_math,
                                      "% Passing Reading": per_school_passing_reading,
                                      "% Passing Overall": overall_passing_rate})

# Formatting
per_school_summary["Total School Budget"] = per_school_summary["Total School Budget"].map("${:,.2f}".format)
per_school_summary["Per Student Budget"] = per_school_summary["Per Student Budget"].map("${:,.2f}".format)

# Display the DataFrame
per_school_summary

# Sort the schools by `% Overall Passing` in descending order and display the top 5 rows.
top_schools = per_school_summary.sort_values("% Passing Overall", ascending=False)
top_schools.head(5)

# Sort the schools by `% Overall Passing` in ascending order and display the top 5 rows.
bottom_schools = per_school_summary.sort_values("% Passing Overall", ascending=True)
bottom_schools.head(5)

# Use the code provided to separate the data by grade
ninth_graders = df_school_data_complete[(df_school_data_complete["grade"] == "9th")]
tenth_graders = df_school_data_complete[(df_school_data_complete["grade"] == "10th")]
eleventh_graders = df_school_data_complete[(df_school_data_complete["grade"] == "11th")]
twelfth_graders = df_school_data_complete[(df_school_data_complete["grade"] == "12th")]

# Group by `school_name` and take the mean of the `math_score` column for each.
ninth_grade_math_scores = ninth_graders.groupby("school_name").mean()["math_score"]
tenth_grader_math_scores = tenth_graders.groupby("school_name").mean()["math_score"]
eleventh_grader_math_scores = eleventh_graders.groupby("school_name").mean()["math_score"]
twelfth_grader_math_scores = twelfth_graders.groupby("school_name").mean()["math_score"]

# Combine each of the scores above into single DataFrame called `math_scores_by_grade`
math_scores_by_grade = pd.DataFrame({
    "9th": ninth_grade_math_scores,
    "10th": tenth_grader_math_scores,
    "11th": eleventh_grader_math_scores,
    "12th": twelfth_grader_math_scores}
)

# Minor data wrangling
math_scores_by_grade.index.name = None

# Display the DataFrame
math_scores_by_grade

# Use the code provided to separate the data by grade
ninth_graders = df_school_data_complete[(df_school_data_complete["grade"] == "9th")]
tenth_graders = df_school_data_complete[(df_school_data_complete["grade"] == "10th")]
eleventh_graders = df_school_data_complete[(df_school_data_complete["grade"] == "11th")]
twelfth_graders = df_school_data_complete[(df_school_data_complete["grade"] == "12th")]

# Group by `school_name` and take the mean of the the `reading_score` column for each.
ninth_grade_reading_scores = ninth_graders.groupby("school_name").mean()["reading_score"]
tenth_grader_reading_scores = tenth_graders.groupby("school_name").mean()["reading_score"]
eleventh_grader_reading_scores = eleventh_graders.groupby("school_name").mean()["reading_score"]
twelfth_grader_reading_scores = twelfth_graders.groupby("school_name").mean()["reading_score"]

# Combine each of the scores above into single DataFrame called `reading_scores_by_grade`
reading_scores_by_grade = pd.DataFrame({
    "9th": ninth_grade_reading_scores,
    "10th": tenth_grader_reading_scores,
    "11th": eleventh_grader_reading_scores,
    "12th": twelfth_grader_reading_scores}
)

# Minor data wrangling
reading_scores_by_grade = reading_scores_by_grade[["9th", "10th", "11th", "12th"]]
reading_scores_by_grade.index.name = None

# Display the DataFrame
reading_scores_by_grade

# Use `pd.cut` to categorize spending based on the bins.
school_spending_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita,
                                                                spending_bins, labels=labels,
                                                                include_lowest=True)
school_spending_df

#  Calculate averages for the desired columns. 
spending_math_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"])["Average Math Score"].mean()
spending_reading_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"])["Average Reading Score"].mean()
spending_passing_math = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Math"].mean()
spending_passing_reading = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Reading"].mean()
overall_passing_spending = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Overall"].mean()

# Assemble into DataFrame
spending_summary = pd.DataFrame({"Average Math Score": spending_math_scores, 
                                    "Average Reading Score": spending_reading_scores,
                                    "% Passing Math": spending_passing_math,
                                    "% Passing Reading": spending_passing_reading,
                                    "% Passing Overall": overall_passing_spending,})

# Display results
spending_summary

# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

# Categorize the spending based on the bins
# Use `pd.cut` on the "Total Students" column of the `per_school_summary` DataFrame.

per_school_summary["School Size"] = pd.cut(per_school_summary["Total Students"],
                                          size_bins, labels=labels,
                                          include_lowest=True)
per_school_summary

# Calculate averages for the desired columns. 
size_math_scores = per_school_summary.groupby(["School Size"])["Average Math Score"].mean()
size_reading_scores = per_school_summary.groupby(["School Size"])["Average Reading Score"].mean()
size_passing_math = per_school_summary.groupby(["School Size"])["% Passing Math"].mean()
size_passing_reading = per_school_summary.groupby(["School Size"])["% Passing Reading"].mean()
size_overall_passing = per_school_summary.groupby(["School Size"])["% Passing Overall"].mean()

# Create a DataFrame called `size_summary` that breaks down school performance based on school size (small, medium, or large).
# Use the scores above to create a new DataFrame called `size_summary`
size_summary = pd.DataFrame({"Average Math Score": size_math_scores,
                                "Average Reading Score": size_reading_scores,
                                "% Passing Math": size_passing_math,
                                "% Passing Reading": size_passing_reading,
                                "% Passing Overall": size_overall_passing})

# Display results
size_summary

# Group the per_school_summary DataFrame by "School Type" and average the results.
average_math_score_by_type = per_school_summary.groupby(["School Type"])["Average Math Score"].mean()
average_reading_score_by_type = per_school_summary.groupby(["School Type"])["Average Reading Score"].mean()
average_percent_passing_math_by_type = per_school_summary.groupby(["School Type"])["% Passing Math"].mean()
average_percent_passing_reading_by_type = per_school_summary.groupby(["School Type"])["% Passing Reading"].mean()
average_percent_overall_passing_by_type = per_school_summary.groupby(["School Type"])["% Passing Overall"].mean()

# Assemble the new data by type into a DataFrame called `type_summary`
type_summary = pd.DataFrame({"Average Math Score": average_math_score_by_type,
                                "Average Reading Score": average_reading_score_by_type,
                                "% Passing Math": average_percent_passing_math_by_type,
                                "% Passing Reading": average_percent_passing_reading_by_type,
                                "% Passing Overall": average_percent_overall_passing_by_type})

# Display results
type_summary


