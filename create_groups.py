#!/usr/bin/env python3
import math
import random
import os
import sys

from tabulate import tabulate


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


scores = []
with open(sys.argv[1]) as f:
    for line in f:
        first, last, score = line.strip().split(',')
        scores.append((first, last, float(score)))
scores.sort(key=lambda x: x[2])
# for student in scores:
#     print(student)
# print(len(scores))

ROLES = ['Facilitator', 'Team Captain', 'Recorder/Reporter', 'Resource Manager']
NUM_GROUPS = math.ceil(len(scores) / len(ROLES))

group_by_score = []
for i in range(len(ROLES)):
    group_by_score.append(scores[i*NUM_GROUPS:min((i+1)*NUM_GROUPS, len(scores))])

# for group in group_by_score:
#     for student in group:
#         print(student)
#     print(len(group))

while True:
    os.system('clear')
    # Shuffle the order
    for group in group_by_score:
        random.shuffle(group)
    
    groups = {i: [] for i in range(NUM_GROUPS)}
    
    for group in group_by_score:
        for idx, student in enumerate(group):
            groups[idx].append(student)
    for group in groups.values():
        random.shuffle(group)
    
    table = [[color.PURPLE + role + color.END] for role in ROLES]
    headers = [color.UNDERLINE + 'Group Roles' + color.END] + [color.UNDERLINE + f'Group {i+1}' + color.END for i in groups]
    for group_num, group in groups.items():
        for idx, (first_name, last_name, score) in enumerate(group):
            table[idx].append(f'{first_name} {last_name}')

    print(tabulate(table, headers=headers, tablefmt="pretty"))

    if input('Accept groups? [y/n]').strip() == 'y':
        break
