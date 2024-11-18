# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import readingFiles
import math_operations

studentsDic = readingFiles.reading_file('./students_data/student_data.txt')
students_avg,dict_output = math_operations.max_min_avg(studentsDic)
max_min_value = math_operations.max_min_marx(studentsDic)
dict_output.update(max_min_value)
sta = dict_output['max_avg']
sta.update(dict_output['min_avg'])
print(sta)
standard_d = math_operations.standard_deviation(sta)
first_key = next(iter(studentsDic))  # Get the first key
first_value = studentsDic['Mohammad']  # Get the value associated with the first key
marks = math_operations.sort(first_value)
print(marks)
Q1,Q2,Q3,IQR = math_operations.calculate_IQR(marks)
print(Q1,Q2,Q3,IQR)
print(marks)
print(standard_d)
print(dict_output)
print(students_avg)




# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
