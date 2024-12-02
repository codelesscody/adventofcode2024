# each line of input is a "report" - space-separated string of numbers called "levels"

# reports are SAFE or UNSAFE. SAFE reports are always increasing or decreasing by 1 to 3

from part1 import is_safe


# 0: initiialize variables
safereports = 0
reports = []

# 1: open file, read each report into separate arrays, close file
with open("Day2/input") as file:
    for line in file:
        reports.append(line.split(None))

# 3: pop a report from the list, 
for report in reports:
    if is_safe(report):
        safereports = safereports + 1
    else:
        for index in range(len(report)):
            shortreport = report.copy()
            del shortreport[index]
            if is_safe(shortreport):
                safereports = safereports +1
                break
        

# 4. output result
print("part2 result: " + str(safereports))