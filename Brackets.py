
### Brackets.py

import math


## Main
teams = int(input('How many teams? '))


## Generate the seeded list
power = 1
seeds = [1,2]
while power < math.sqrt(teams):
    power += 1
    twos = 2**power
    #print(f'{power=}  {twos=}  {seeds=}')
    #print(f'{seeds}')
    new_seeds = []
    for slot in seeds:
        new_seeds.append(slot)
        new_seeds.append((twos + 1) - slot)
    seeds = new_seeds


## Replace surplus teams with a bye = "0"
if teams < twos:
    #print(f'{twos=}  {twos-teams}')
    for seed_no in range(twos,teams,-1):
        #print(f'{seed_no=}')
        new_seeds = []
        for seed in seeds:
            #print(f'Seeds: {seed_no=}  {seed}')
            if seed == seed_no:
                new_seeds.append(0)
            else:
                new_seeds.append(seed)
        #print(f'{seeds=}')
        #print(f'{new_seeds=}')
        seeds = new_seeds
print()
#print(f'Final:  {power=}  {twos=}  {seeds=}')
print(f'Initial Draw Order: {seeds}')
#print()


## Build list of possible oppostion teams for each round - but build list backwards (easier)
opposition = []
for team in range(1, teams + 1):
    teams_faced = []
    start = 0
    end = len(seeds) -1
    while end - start >= 1:
        halfway = (start + end + 1) //2
        location = seeds.index(team)
        if location < halfway:
            old_end = end
            end = halfway - 1
            teams_faced.append(seeds[end+1:old_end+1])
            #print(f'{start=}  {halfway=}  {end=}  {old_end=}  {end+1}  {old_end}  {seeds[end+1:old_end+1]}')
        else:
            old_start = start
            start = halfway
            teams_faced.append(seeds[old_start:start])
            #print(f'{start=}  {halfway=}  {end=}  {old_start=}  {old_start}  {start-1}  {seeds[old_start:start]}')
        #print(f'{teams_faced}')
    opposition.append(teams_faced[::-1])  ## Reverse to go first round to final
print()
for team_num, op_teams in enumerate(opposition,start=1):
    print(f'{team_num} - {op_teams}')

## Further work:
## When there are byes in the opposition lists that are longer than two items, they should be removed.

