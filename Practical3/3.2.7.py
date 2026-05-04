import numpy as np

a = np.loadtxt("Sample.csv", delimiter=',', skiprows=1)
import numpy as np

a = np.loadtxt("Sample.csv", delimiter=',', skiprows=1)

# 1
print("All student Details:\n", a)

# 2
print("Total Students:", a.shape[0])

# 3
print("All Student Roll Nos", a[:, 0])

# 4
print("Subject 1 Marks", a[:, 1])

# 5
print("Min marks in Subject 2", np.min(a[:, 2]))

# 6
print("Max marks in Subject 3", np.max(a[:, 3]))

# 7
print("All subject marks:", a[:, 1:])

# 8
print("Total Marks", np.sum(a[:, 1:], axis=1))

# 9 (FIXED: NumPy-style rounded output, not list)
print(np.round(np.mean(a[:, 1:], axis=1), 1))

# 10
print("Average Marks of each subject", np.round(np.mean(a[:, 1:], axis=0), 1))

# 11
print("Average Marks of S1 and S2", np.round(np.mean(a[:, 1:3], axis=0), 1))

# 12
print("Average Marks of S1 and S3", np.round(np.mean(a[:, [1, 3]], axis=0), 1))

# 13
print("Roll no who got maximum marks in Subject 3", a[np.argmax(a[:, 3]), 0])

# 14
print("Roll no who got minimum marks in Subject 2", a[np.argmin(a[:, 2]), 0])

# 15 (keep 2D structure)
print("Roll no who got 24 marks in Subject 2", a[a[:, 2] == 24][:,0:1])

# 16
print("Count of students who got marks in Subject 1 < 40", np.sum(a[:, 1] < 40))

# 17
print("Count of students who got marks in Subject 2 > 90:", np.sum(a[:, 2] > 90))

# 18
print("Count of students in each subject who got marks >= 90:", np.sum(a[:, 1:] >= 90, axis=0))

# 19
print("Roll no:", a[:, 0])
print("Count of subjects in which student got marks >= 90:", np.sum(a[:, 1:] >= 90, axis=1))

# 20 (NO LABEL)
print(np.sort(a[:, 1]))

# 21 (FULL ROWS, NOT JUST MARKS)
print(a[(a[:, 1] >= 50) & (a[:, 1] <= 90)])

# 22 (FULL ARRAY + tuple output)
print(a)
print(np.where(a[:, 1] == 79))