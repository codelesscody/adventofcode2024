# each line of input is a "report" - space-separated string of numbers called "levels"

# reports are SAFE or UNSAFE. SAFE reports are always increasing or decreasing by 1 to 3




# 0: initiialize variables
safereports = 0
reports = []

# 1: open file, read each report into separate arrays, close file
with open("Day2/input") as file:
    for line in file:
        reports.append(tuple(line.split(None)))

# 3: pop a report from the list, 
for report in reports:
    ascending = False
    descending = False
    if int(report[0]) > int(report[1]):
        descending = True
    elif int(report[0]) < int(report[1]):
        ascending = True
    else:
        continue
    lastLevel = int(report[0])
    badreport = False
    for level in report[1:]:
        levint = int(level)
        if ascending and (levint - lastLevel >= 1) and (levint - lastLevel <= 3):
            pass
        elif descending and (lastLevel - levint >= 1) and (lastLevel - levint <= 3):
            pass
        else:
            badreport = True
            continue
        lastLevel = levint
    if not badreport:
        safereports = safereports + 1
        

# 4. output result
print(safereports)