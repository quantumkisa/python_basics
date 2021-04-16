import re
subj = {}
with open('5_6_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.replace(":", "")
        summary_of_hours = 0
        hours = re.findall(r'\d+', line)
        for el in hours:
            if el.isdigit():
                summary_of_hours += int(el)
        subj[line.split()[0]] = summary_of_hours
print(subj)
