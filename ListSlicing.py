# list slicing is a technique used to access a portion of a list
# # list slicing is done using the colon operator
marks = [100, 90, 80, 70, 60, 50]
print(marks)
print(marks[1:3])

# # list slicing can also be done using negative indexing
print(marks[-3:-1])  # [70, 60]
# # list slicing can also be done using the step parameter
print(marks[::2])  # [100, 80, 60]
# # list slicing can also be done using the step parameter with negative indexing
print(marks[::-2])  # [50, 70, 90]
# # list slicing can also be done using the step parameter with negative indexing and a range
print(marks[-1:-4:-1])  # [50, 60, 70]
