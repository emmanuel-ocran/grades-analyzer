import streamlit as st

st.title("📊 Student Grades Analyzer")

students = []
scores = []

# Step 1: Get number of students to be analyzed
num_students = st.number_input("How many students do you want to analyze?", min_value=1, max_value=100, step=1)

# Step 2: Collect names and scores of students
with st.form("student_form"):
    for i in range(num_students):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input(f"Student #{i + 1} Name", key=f"name_{i}")
        with col2:
            score = st.number_input(f"Score for Student #{i + 1}", min_value=0.0, max_value=100.0, step=0.1, key=f"score_{i}")
        students.append(name)
        scores.append(score)

    submitted = st.form_submit_button("Analyze")

# Step 3: Show Results
if submitted:
    if all(students) and all(s is not None for s in scores):
        average_score = sum(scores) / len(scores)
        highest_score = max(scores)
        lowest_score = min(scores)

        highest_index = scores.index(highest_score)
        lowest_index = scores.index(lowest_score)

        st.success("✅ Analysis Complete!")
        st.subheader("📈 Class Performance Summary")
        st.write(f"**Average Score:** {average_score:.2f}")
        st.write(f"**Highest Score:** {students[highest_index]} ({highest_score:.2f})")
        st.write(f"**Lowest Score:** {students[lowest_index]} ({lowest_score:.2f})")
    else:
        st.error("Please fill in all names and scores.")