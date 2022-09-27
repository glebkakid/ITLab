'''marks = {
    "6m": {"5": 9.9, "4": 10.4, "3": 11.1},
    "6f": {"5": 10.3, "4": 10.6, "3": 11.2},
    "7m": {"5": 9.4, "4": 10.2, "3": 11.0},
    "7f": {"5": 9.8, "4": 10.6, "3": 11.4}
}'''

f = open('run_of_60_m.txt', 'r')
#new = open('run_of_60_mark.txt', 'x') если каждый раз создавать новый файл, то появляется ошибка, поэтому я открою его на запись
new = open('run_of_60_mark.txt', 'w')


for line in f:
    newString = ""
    list = line.split()
    if list[1] == "m":
        if list[2] == "6":
            if float(list[3]) <= 9.9:
                list.append("Mark - 5")
            elif (float(list[3]) >= 9.9) and (float(list[3]) <= 10.4):
                list.append("Mark - 4")
            elif (float(list[3]) >= 10.4) and (float(list[3]) <= 11.1):
                list.append("Mark - 3")
            else:
                list.append("Mark - 2")
        elif list[2] == "7":
            if float(list[3]) <= 9.4:
                list.append("Mark - 5")
            elif (float(list[3]) >= 9.4) and (float(list[3]) <= 10.2):
                list.append("Mark - 4")
            elif (float(list[3]) >= 10.2) and (float(list[3]) <= 11.0):
                list.append("Mark - 3")
            else:
                list.append("Mark - 2")
    elif list[1] == "f":
         if list[2] == "6":
            if float(list[3]) <= 10.3:
                list.append("Mark - 5")
            elif (float(list[3]) >= 10.3) and (float(list[3]) <= 10.6):
                list.append("Mark - 4")
            elif (float(list[3]) >= 10.6) and (float(list[3]) <= 11.2):
                list.append("Mark - 3")
            else:
                list.append("Mark - 2")
         elif list[2] == "7":
            if float(list[3]) <= 9.8:
                list.append("Mark - 5")
            elif (float(list[3]) >= 9.8) and (float(list[3]) <= 10.6):
                list.append("Mark - 4")
            elif (float(list[3]) >= 10.6) and (float(list[3]) <= 11.4):
                list.append("Mark - 3")
            else:
                list.append("Mark - 2")
    for i in list:
        newString += i + " "
    new.write(newString + "\n")

f.close()
new.close()
