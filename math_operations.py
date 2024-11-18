import math
# Calculate the maximum and the minimum average
def max_min_avg(students_data):
    """
    this function gets the students data (names and marks) then separate the marks and calculate the average of each
    student then find the maximum and the minimum average then return the maximum and minimum in dictionary also return
    the average of each student in another dictionary
    :param students_data:
    :return: dict_output , students_avg
    """
    students_avg = {}
    maxAvg = 0
    minAvg = 100000000000
    max_name = min_name = ""
    for key, value in students_data.items():
        mark_sum = 0
        for idx in value:
            mark_sum += idx
        avg = mark_sum / len(value)
        students_avg[key] = avg
        if avg > maxAvg:
            maxAvg = avg
            max_name = key
        if avg < minAvg:
            minAvg = avg
            min_name = key
    dict_output = {
        "max_avg": {max_name: maxAvg},
        "min_avg": {min_name: minAvg},
    }
    return students_avg, dict_output


# Calculate the maximum and the minimum mark
def max_min_marx(students_data):
    """
    This function determines the highest and lowest marks among all the students' scores.
    :param students_data:
    :return: dict_output
    """
    max_value = float('-inf')
    min_value = float('inf')
    student_min = student_max = ""
    for key, value in students_data.items():
        for idx in value:
            if max_value < idx:
                max_value = idx
                student_max = key
            if min_value > idx:
                min_value = idx
                student_min = key

    dict_output = {
        "max_value": {student_max: max_value},
        "min_value": {student_min: min_value},
    }
    return dict_output


# Standard Deviation

def standard_deviation(students_avg):
    if not students_avg:
        return 0
    mean = float(0)
    count = float(0)
    for key, value in students_avg.items():
        mean += value
        count += 1
    mean /= count
    variance = float(0)
    variance_sum = 0
    for key, value in students_avg.items():
        variance_sum += (mean - value) ** 2
    variance = variance_sum/count
    return math.sqrt(variance)
# sort marks find most frequent mark
def sort(student_data):
    marks = []
    holder = 0
    n = len(marks)
    for value in student_data:
        marks.append(value)
    n = len(marks)

    for x in range(0,n-1,1):
        for y in range(x+1,n,1):
            if marks[x] > marks[y]:
                holder = marks[y]
                marks[y] = marks[x]
                marks[x] = holder

    return marks

#find most frequent mark
def most_freq(marks):
    mostFreq = 0

    count1 = 0
    for idx in marks:
        count = 0
        for x in marks:
            if idx == x:
              count += 1
        if count > count1:
            count1 = count
            mostFreq = idx

    return mostFreq



#calculation of Q1,Q2,Q3 and IQR

def calculate_IQR(student_mark):
    marks = []
    for idx in student_mark:
        marks.append(idx)
    Q2 = Q1 = Q3 = IQR = holder = float(0)
    Q1List = []
    Q3List = []
    if len(marks)%2 == 0:
        Q2 = (marks[len(marks)//2] + marks[(len(marks)//2)+1])/2
        holder = len(marks)//2
        for idx in range(0,holder-1,1):
            Q1List.append(marks[idx])
        Q1 = Q1List[(len(Q1List)//2)]
        for idx in range(holder+1,len(marks)-1,1):
            Q3List.append(marks[idx])
        Q3 = Q3List[(len(Q3List)//2)]
        IQR = Q3 - Q1
    else:
        Q2 = marks[math.floor(len(marks)/2)]
        holder = math.floor(len(marks)/2)
        for idx in range(0,holder,1):
            Q1List.append(marks[idx])
        Q1 = Q1List[math.floor(len(Q1List)/2)]
        for idx in range(holder+1,len(marks)-1,1):
            Q3List.append(marks[idx])
        Q3 = Q3List[math.floor(len(Q3List)/2)]
        IQR = Q3 - Q1

    return Q1,Q2,Q3,IQR


"""def Standard_deviation (students_avg):
    mean = float('-inf')
    for idx in students_avg:
        mean += idx
    mean /= students_avg
    data_point = []
    for x in students_avg:
        data_point.append(mean-x)"""
