from preswald import connect, get_df

connect()  # Initialize connection to preswald.toml data sources
df = get_df('data/student_habits_performance.csv')  # Load data

from preswald import query

# query students who study more than 3 hours per day (show good work ethics!)
try:
    sql = "SELECT * FROM student_habits_performance WHERE study_hours_per_day > 3"
except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"Query error: {e}")

filtered_df = query(sql, 'data/student_habits_performance.csv')

from preswald import table, text

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

from preswald import plotly
import plotly.express as px

# identify the relationships between parent education level and good students' exam scores
fig = px.bar(filtered_df, x="parental_education_level", y="exam_score")
plotly(fig)
