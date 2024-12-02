# each line of input is a "report" - space-separated string of numbers called "levels"

# reports are SAFE or UNSAFE. SAFE reports are always increasing or decreasing by 1 to 3

def is_safe(report):
    ascending = False
    descending = False
    badreport = False
    if report[0] > report[1]:
        descending = True
    elif report[0] < report[1]:
        ascending = True
    else:
        badreport = True
    lastLevel = report[0]
    for level in report[1:]:
        if ascending and (level - lastLevel >= 1) and (level - lastLevel <= 3):
            pass
        elif descending and (lastLevel - level >= 1) and (lastLevel - level <= 3):
            pass
        else:
            badreport = True
            continue
        lastLevel = level
    return not badreport


# 0: initiialize variables
safereports = 0
reports = []

# 1: open file, read each report into separate arrays, close file
with open("Day2/input") as file:
    for line in file:
        reports.append([int(s) for s in line.split(None)])

# part1
for report in reports:
    if is_safe(report):
        safereports = safereports + 1
print("part1 result: " + str(safereports));

## part2
## same as above, but also accept any report that passes if any single value is removed
safereports = 0
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
print("part2 result: " + str(safereports))