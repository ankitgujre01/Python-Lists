# List methods are functions that are built into the list data type in Python. 
# They allow you to perform various operations on lists, such as adding, removing, and modifying elements. 
# Here are some commonly used list methods:
# # 1. append() - Adds an element to the end of the list
# # 2. extend() - Adds elements from another list to the end of the list
# # 3. insert() - Inserts an element at a specified index in the list
# # 4. remove() - Removes the first occurrence of a specified element from the list
# # 5. pop() - Removes and returns the element at a specified index (default is the last element)
# # 6. clear() - Removes all elements from the list
# # 7. index() - Returns the index of the first occurrence of a specified element
# # 8. count() - Returns the number of occurrences of a specified element in the list
# # 9. sort() - Sorts the elements of the list in ascending order
# # 10. reverse() - Reverses the order of the elements in the list
# # 11. copy() - Returns a shallow copy of the list
# # 12. join() - Joins the elements of a list into a string
# # 13. split() - Splits a string into a list of substrings
# # 14. find() - Returns the index of the first occurrence of a specified element
# # 15. findall() - Returns a list of all occurrences of a specified element
# # 16. replace() - Replaces all occurrences of a specified element with another element
# # 17. splitlines() - Splits a string into a list of lines

marks = [100, 90, 80, 70, 60, 50]
print(marks)

print(marks.append(40))  # None
print(marks)  # [100, 90, 80, 70, 60, 50, 40]
print(marks.extend([30, 20, 10]))  # None
print(marks)  # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
print(marks.insert(2, 25))  # None
print(marks)  # [100, 90, 25, 80, 70, 60, 50, 40, 30, 20, 10]
print(marks.remove(25))  # None
print(marks)  # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
print(marks.pop())  # 10
print(marks)  # [100, 90, 80, 70, 60, 50, 40, 30, 20]
# print(marks.clear())  # None
# print(marks)  # []
print(marks.reverse())
print(marks)
print(marks.sort())
print(marks)
print(marks)
print(marks.sort(reverse=True))
print(marks)

print(marks.insert(2, 225))  # None
print(marks)  # [100, 90, 225, 80, 70, 60, 50, 40, 30, 20]
print(marks.index(225))  # 2
print(marks.count(225))  # 1
print(marks.append(225))  # None
print(marks)  # [100, 90, 225, 80, 70, 60, 50, 40, 30, 20, 225]

