
def reading_file (file):
    with open (file,'r', encoding="utf-8-sig") as student_data:
        studentsDic ={}
        for line in student_data:
            newLine = line.split(",")
            marks = []
            for idx in range(1,len(newLine)):
                 marks.append(int(newLine[idx]))
            studentsDic[newLine[0]] = marks
            #print(newLine[0])

        #print(studentsDic)
    return studentsDic