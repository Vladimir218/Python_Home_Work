import os
import json
import django
from collections import defaultdict

root_dir = django.__path__[0]
files_size_statistic_work = defaultdict(list)
files_size_statistic = defaultdict(tuple)
for root, dirs, files in os.walk(root_dir):
    if len(files) > 0:
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            extention = file.split('.')[-1].lower()
            if size not in files_size_statistic_work.keys():
                files_size_statistic_work[size] = [1, [extention]]
            else:
                if extention not in files_size_statistic_work[size][1]:
                    files_size_statistic_work[size][1].append(extention)
                files_size_statistic_work[size][0] += 1

for key, item in sorted(files_size_statistic_work.items()):
    files_size_statistic[key] = tuple(item)

file_path = os.getcwd().split('\\')[-1] + '_summary.json'
with open(file_path, 'w', encoding="UTF-8") as f:
    json.dump(files_size_statistic, f, indent=4)
