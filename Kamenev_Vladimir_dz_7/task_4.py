import os
from collections import defaultdict
import django

root_dir = django.__path__[0]
files_size_statistic = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    if len(files) > 0:
        for file in files:
            files_size_statistic[10 ** len(str(os.stat(os.path.join(root, file)).st_size))] += 1

for key in (sorted(files_size_statistic)):
    print(f'{key}: {files_size_statistic[key]}')
