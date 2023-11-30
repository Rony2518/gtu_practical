import matplotlib.pyplot as plt
import numpy as np

# Sample data
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_scores = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# Create a scatter plot
plt.scatter(hours_studied, exam_scores, label = "Exam Scores")

coefficient = np.polyfit(hours_studied, exam_scores, 1)
tradline = np.poly1d(coefficient)

plt.plot(hours_studied,tradline(hours_studied), color = "red", label = "Trandline")
plt.legend()
plt.show()