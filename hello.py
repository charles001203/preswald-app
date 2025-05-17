from preswald import connect, get_df

connect()  # Initialize connection to preswald.toml data sources
df = get_df("student_habits_performance.csv")  # Load data

from preswald import query

sql = "SELECT * FROM student_habits_performance.csv WHERE study_hours_per_day > 3"
filtered_df = query(sql, "student_habits_performance.csv")

from preswald import table, text

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

from preswald import plotly
import plotly.express as px

fig = px.scatter(df, x="study_hours_per_day", y="exam_score", color="category")
plotly(fig)
