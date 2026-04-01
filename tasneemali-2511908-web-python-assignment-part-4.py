#!/usr/bin/env python
# coding: utf-8

# In[2]:


data = """name,math,science,english,history,pe,attendance_pct,study_hours_per_day,passed
Alice,88,92,76,80,95,92,4.5,1
Bob,42,55,48,50,60,65,1.2,0
Charlie,75,70,80,68,88,85,3.0,1
Diana,95,98,91,89,97,98,6.0,1
Eve,38,42,50,45,55,58,0.8,0
Frank,60,65,72,58,70,78,2.5,1
Grace,55,48,44,52,62,60,1.5,0
Henry,82,79,85,77,90,88,4.0,1
Iris,70,74,68,65,78,80,3.5,1
Jack,30,35,40,28,45,50,0.5,0
Karen,65,60,70,62,75,72,2.8,1
Liam,48,52,44,55,58,62,1.8,0
Mia,91,94,88,92,96,95,5.5,1
Noah,58,62,55,60,68,70,2.0,0
Olivia,78,75,82,70,85,84,3.8,1
"""

with open("students.csv", "w") as f:
    f.write(data)


# In[3]:


import pandas as pd

df = pd.read_csv("students.csv")
print(df.head())


# In[4]:


import pandas as pd

# Load the dataset
df = pd.read_csv("students.csv")

# Print shape
print("Shape of the DataFrame (rows, columns):", df.shape)

# Print data types of each column
print("\nData types of each column:")
print(df.dtypes)


# In[5]:


import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# Summary statistics for numeric columns
summary = df.describe()
print(summary)


# In[6]:


import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# Count of students who passed and failed
pass_fail_counts = df['passed'].value_counts()
print(pass_fail_counts)


# In[7]:


import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# List of subject columns
subject_cols = ['math', 'science', 'english', 'history', 'pe']

# Average scores for passing students
avg_pass = df[df['passed'] == 1][subject_cols].mean()
print("Average scores for passing students:")
print(avg_pass)

print("\nAverage scores for failing students:")
# Average scores for failing students
avg_fail = df[df['passed'] == 0][subject_cols].mean()
print(avg_fail)


# In[8]:


import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# Subject columns
subject_cols = ['math', 'science', 'english', 'history', 'pe']

# Compute average per student across subjects
df['avg_score'] = df[subject_cols].mean(axis=1)

# Find student with highest average
top_student = df.loc[df['avg_score'].idxmax()]

print("Student with the highest overall average:")
print(f"Name: {top_student['name']}")
print(f"Average Score: {top_student['avg_score']:.2f}")


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Subject columns
subject_cols = ['math', 'science', 'english', 'history', 'pe']

# Compute average per subject across all students
avg_subject_scores = df[subject_cols].mean()

# Create bar chart
plt.figure(figsize=(8,6))
plt.bar(avg_subject_scores.index, avg_subject_scores.values, color='skyblue')
plt.title("Average Score per Subject Across All Students")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save figure
plt.savefig("plot1_bar.png")

# Display
plt.show()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Compute mean math score
mean_math = df['math'].mean()

# Create histogram
plt.figure(figsize=(8,6))
plt.hist(df['math'], bins=5, color='lightgreen', edgecolor='black', alpha=0.7)
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")

# Add vertical line at mean
plt.axvline(mean_math, color='red', linestyle='--', linewidth=2, label=f"Mean = {mean_math:.2f}")
plt.legend()

# Save figure
plt.savefig("plot2_hist.png")

# Display
plt.show()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Compute average score across subjects
subject_cols = ['math', 'science', 'english', 'history', 'pe']
df['avg_score'] = df[subject_cols].mean(axis=1)

# Scatter plot
plt.figure(figsize=(8,6))

# Passed students
plt.scatter(df[df['passed']==1]['study_hours_per_day'], 
            df[df['passed']==1]['avg_score'], 
            color='green', label='Pass', s=80, alpha=0.7)

# Failed students
plt.scatter(df[df['passed']==0]['study_hours_per_day'], 
            df[df['passed']==0]['avg_score'], 
            color='red', label='Fail', s=80, alpha=0.7)

plt.title("Study Hours per Day vs Average Score")
plt.xlabel("Study Hours per Day")
plt.ylabel("Average Score")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Save figure
plt.savefig("plot3_scatter.png")

# Display
plt.show()


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Separate attendance percentages
pass_attendance = df[df['passed']==1]['attendance_pct'].tolist()
fail_attendance = df[df['passed']==0]['attendance_pct'].tolist()

# Box plot
plt.figure(figsize=(8,6))
plt.boxplot([pass_attendance, fail_attendance], labels=['Pass', 'Fail'], patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red', linewidth=2),
            whiskerprops=dict(color='blue'),
            capprops=dict(color='blue'))

plt.title("Attendance Percentage: Pass vs Fail")
plt.ylabel("Attendance Percentage")
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Save figure
plt.savefig("plot4_box.png")

# Display
plt.show()


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Line plot
plt.figure(figsize=(12,6))

# Plot math scores
plt.plot(df['name'], df['math'], marker='o', linestyle='-', color='blue', label='Math')

# Plot science scores
plt.plot(df['name'], df['science'], marker='s', linestyle='--', color='green', label='Science')

plt.title("Math and Science Scores for Each Student")
plt.xlabel("Student Name")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.ylim(0, 100)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

# Save figure
plt.savefig("plot5_line.png")

# Display
plt.show()


# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("students.csv")

# Set figure and subplots
plt.figure(figsize=(12,5))

# Subplot 1 — Math
ax1 = plt.subplot(1,2,1)
sns.barplot(data=df, x='passed', y='math', palette='Blues', ax=ax1)
ax1.set_title("Average Math Score by Pass/Fail")
ax1.set_xlabel("Passed (1=Pass, 0=Fail)")
ax1.set_ylabel("Average Math Score")

# Subplot 2 — Science
ax2 = plt.subplot(1,2,2)
sns.barplot(data=df, x='passed', y='science', palette='Greens', ax=ax2)
ax2.set_title("Average Science Score by Pass/Fail")
ax2.set_xlabel("Passed (1=Pass, 0=Fail)")
ax2.set_ylabel("Average Science Score")

plt.tight_layout()

# Save figure
plt.savefig("seaborn_barplot.png")

# Display
plt.show()


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("students.csv")

# Compute average score across subjects
subject_cols = ['math', 'science', 'english', 'history', 'pe']
df['avg_score'] = df[subject_cols].mean(axis=1)

# Create figure
plt.figure(figsize=(8,6))

# Scatter + regression for Pass
sns.regplot(
    data=df[df['passed']==1], 
    x='attendance_pct', 
    y='avg_score', 
    scatter=True,
    label='Pass', 
    color='green',
    ci=None
)

# Scatter + regression for Fail
sns.regplot(
    data=df[df['passed']==0], 
    x='attendance_pct', 
    y='avg_score', 
    scatter=True,
    label='Fail', 
    color='red',
    ci=None
)

plt.title("Attendance vs Average Score by Pass/Fail")
plt.xlabel("Attendance Percentage")
plt.ylabel("Average Score")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Save figure
plt.savefig("seaborn_scatter_reg.png")

# Display
plt.show()


# In[16]:


# Seaborn bar plot (average math & science by pass/fail)
plt.figure(figsize=(12,5))
ax1 = plt.subplot(1,2,1)
sns.barplot(data=df, x='passed', y='math', palette='Blues', ax=ax1)
ax1.set_title("Average Math Score by Pass/Fail")
ax1.set_xlabel("Passed (1=Pass, 0=Fail)")
ax1.set_ylabel("Average Math Score")

ax2 = plt.subplot(1,2,2)
sns.barplot(data=df, x='passed', y='science', palette='Greens', ax=ax2)
ax2.set_title("Average Science Score by Pass/Fail")
ax2.set_xlabel("Passed (1=Pass, 0=Fail)")
ax2.set_ylabel("Average Science Score")

plt.tight_layout()
plt.savefig("seaborn_barplot.png")  # Saved as PNG
plt.show()


# Seaborn scatter plot with regression lines
plt.figure(figsize=(8,6))
sns.regplot(data=df[df['passed']==1], x='attendance_pct', y='avg_score', scatter=True, label='Pass', color='green', ci=None)
sns.regplot(data=df[df['passed']==0], x='attendance_pct', y='avg_score', scatter=True, label='Fail', color='red', ci=None)

plt.title("Attendance vs Average Score by Pass/Fail")
plt.xlabel("Attendance Percentage")
plt.ylabel("Average Score")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.savefig("seaborn_scatter_reg.png")  # Saved as PNG
plt.show()


# In[17]:


# Using Seaborn felt easier and more concise for creating aesthetically pleasing plots with minimal customization.
# For example, adding regression lines or grouping by categories (Pass vs Fail) was simpler in Seaborn than in Matplotlib.
# Matplotlib gave more low-level control but often required extra code for styling, legends, and multiple groups.


# In[18]:


import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# Features (exclude 'name' and 'passed')
feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]

# Target
y = df['passed']

# Inspect
print("Features (X):")
print(X.head())
print("\nTarget (y):")
print(y.head())


# In[19]:


import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("students.csv")

# Features and target
feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]
y = df['passed']

# Split into train (80%) and test (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Inspect shapes
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)


# In[20]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("students.csv")

# Features and target
feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]
y = df['passed']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit only on training data
X_test_scaled  = scaler.transform(X_test)       # transform test data using same scaler

# Inspect
print("First 5 rows of scaled X_train:")
print(X_train_scaled[:5])


# In[21]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("students.csv")

# Features and target
feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]
y = df['passed']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Train Logistic Regression
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Confirm training
print("Model trained successfully.")


# In[22]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("students.csv")

# Features and target
feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]
y = df['passed']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Train Logistic Regression
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Print training accuracy
train_accuracy = model.score(X_train_scaled, y_train)
print(f"Training Accuracy: {train_accuracy:.2f}")


# In[23]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("students.csv")

# Features and target
feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]
y = df['passed']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Train Logistic Regression
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Predict on test set
y_pred = model.predict(X_test_scaled)

# Display predictions
print("Predictions on test set:", y_pred)


# In[24]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("students.csv")

# Features and target
feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]
y = df['passed']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Train Logistic Regression
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Predict on test set
y_pred = model.predict(X_test_scaled)

# Compute test accuracy
test_accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {test_accuracy:.2f}")


# In[25]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("students.csv")

# Features and target
feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]
y = df['passed']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Train Logistic Regression
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Predict on test set
y_pred = model.predict(X_test_scaled)

# Retrieve student names for test set
test_names = df.loc[X_test.index, 'name']

# Print results
for name, actual, pred in zip(test_names, y_test, y_pred):
    status = "✅" if actual == pred else "❌"
    print(f"{name}: Actual={actual}, Predicted={pred} {status}")


# In[26]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("students.csv")

# Features and target
feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]
y = df['passed']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Train Logistic Regression
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Extract feature coefficients
coefficients = model.coef_[0]

# Pair each coefficient with its feature name
feature_importance = list(zip(feature_cols, coefficients))

# Sort by absolute value descending
feature_importance_sorted = sorted(feature_importance, key=lambda x: abs(x[1]), reverse=True)

# Print feature importance
print("Feature Importance (sorted by absolute value):")
for feature, coef in feature_importance_sorted:
    print(f"{feature}: {coef:.4f}")


# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("students.csv")

# Features and target
feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]
y = df['passed']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Train Logistic Regression
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Extract coefficients
coefficients = model.coef_[0]

# Colors: green for positive, red for negative
colors = ['green' if c > 0 else 'red' for c in coefficients]

# Horizontal bar chart
plt.figure(figsize=(8,6))
plt.barh(feature_cols, coefficients, color=colors)
plt.title("Feature Coefficients for Predicting Pass/Fail")
plt.xlabel("Coefficient Value")
plt.ylabel("Feature")

# Annotate bars with coefficient values
for i, coef in enumerate(coefficients):
    plt.text(coef + 0.02 if coef > 0 else coef - 0.08, i, f"{coef:.2f}", va='center', color='black')

plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()

# Save figure
plt.savefig("feature_coefficients.png")

# Display
plt.show()


# In[28]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("students.csv")

# Features and target
feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]
y = df['passed']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Train Logistic Regression
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Define a new student (order must match feature columns)
new_student = [[75, 70, 68, 65, 80, 82, 3.2]]

# Scale new student
new_student_scaled = scaler.transform(new_student)

# Predict pass/fail
prediction = model.predict(new_student_scaled)[0]
prediction_label = "Pass" if prediction == 1 else "Fail"

# Predict probability
probability = model.predict_proba(new_student_scaled)[0]  # [prob_fail, prob_pass]

print(f"Prediction for the new student: {prediction_label}")
print(f"Probability: Fail={probability[0]:.2f}, Pass={probability[1]:.2f}")

