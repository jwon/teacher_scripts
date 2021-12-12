#!/usr/bin/env python3
import math
import random
import os
import sys


scores = []
with open(sys.argv[1]) as f:
    for line in f:
        first, last, score = line.strip().split(',')
        scores.append((first, last, float(score)))
scores.sort(key=lambda x: x[2])
# for student in scores:
#     print(student)
# print(len(scores))

NUM_GROUPS = int(input('How many groups do you want? '))
students_per_group = math.ceil(len(scores) / NUM_GROUPS)

group_by_score = []
for i in range(students_per_group):
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
    
    for group_num, group in groups.items():
        print(f'Group #{group_num+1}')
        for (first_name, last_name, score) in group:
            print(f'{first_name} {last_name}')
        print()

    if input('Accept groups? [y/n]').strip() == 'y':
        break
