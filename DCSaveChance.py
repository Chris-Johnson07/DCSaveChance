import random
import matplotlib.pyplot as plt
import numpy as np

DCSave = 16
attempts = 10000

save_list = {'ST0': {'fail': 0, 'epic_fail': 0},
             'ST1': {'fail': 0, 'epic_fail': 0},
             'ST2': {'fail': 0, 'epic_fail': 0},
             'ST3': {'fail': 0, 'epic_fail': 0},
             'ST4': {'fail': 0, 'epic_fail': 0},
             'ST5': {'fail': 0, 'epic_fail': 0},
             'ST6': {'fail': 0, 'epic_fail': 0},
             'ST7': {'fail': 0, 'epic_fail': 0},
             'ST8': {'fail': 0, 'epic_fail': 0},
             'ST9': {'fail': 0, 'epic_fail': 0},
             'ST10': {'fail': 0, 'epic_fail': 0}}

unsettling_words = input('Using Unsettling Words? (y/n) ')

silvery_barbs = input('\nUsing Silvery Barbs? (y/n) ')

mind_sliver = input('\nUsing Mind Sliver? (y/n) ')

bane_spell = input('\nIs Bane in affect? (y/n) ')

has_advantage = input('\nDoes the enemy have advantage? (y/n) ')

active_effects = []

if unsettling_words == 'y':
    active_effects.append('unsettling words')
if silvery_barbs == 'y':
    active_effects.append('silvery barbs')
if bane_spell == 'y':
    active_effects.append('bane spell')
if has_advantage == 'y':
    active_effects.append('target has advantage')
if len(active_effects) == 0:
    active_effects.append('nothing')

print('\n')
print('==============================')
print('\n')


def roll_die(die_type, vantage='nor'):
    if vantage == 'adv':
        roll1 = random.randint(1, die_type)
        roll2 = random.randint(1, die_type)
        return max([roll1, roll2])
    elif vantage == 'dis':
        roll1 = random.randint(1, die_type)
        roll2 = random.randint(1, die_type)
        return min([roll1, roll2])
    elif vantage == 'nor':
        return random.randint(1, die_type)


for i in range(attempts):
    if has_advantage.lower() == silvery_barbs.lower():
        roll = roll_die(20)
    elif has_advantage == 'y':
        roll = roll_die(20, 'adv')
    elif silvery_barbs == 'y':
        roll = roll_die(20, 'dis')

    if unsettling_words == 'y':
        roll -= roll_die(8)
    if mind_sliver == 'y':
        roll -= roll_die(4)
    if bane_spell == 'y':
        roll -= roll_die(4)

    if roll < 0:
        roll = 0

    for a in range(0, 11):
        if roll + a < DCSave:
            list(save_list.values())[a]['fail'] += 1
        if roll + a <= DCSave - 5:
            list(save_list.values())[a]['epic_fail'] += 1

DCSave_Perc_List = []
DCSave_EF_Perc_List = []
save_counter = 0
print('With a DC of {} and {} active, the target\'s chances to fail are as follows:\n'.format(DCSave, active_effects))
for key in save_list:
    f = round(save_list[key]['fail'] / attempts * 100, 1)
    ef = round(save_list[key]['epic_fail'] / attempts * 100, 1)

    print('Saving Throw of +{}: \n{}% chance to fail \n{}% chance to fail by 5 or more'.format(save_counter, f, ef))
    print('\n')

    DCSave_Perc_List.append(f)
    DCSave_EF_Perc_List.append(ef)

    save_counter += 1

x_labels = ['+0', '+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+9', '+10']
X_axis = np.arange(len(save_list))

plt.bar(X_axis + 0.2, DCSave_Perc_List, 0.4, color='#4298ff', zorder=3, label='Fail')
plt.bar(X_axis - 0.2, DCSave_EF_Perc_List, 0.4, color='orange', zorder=3, label='Epic Fail')

plt.ylim([0, 100])
plt.ylabel('Percent Chance To Fail')

plt.xticks(X_axis, x_labels, rotation=45, ha='right')
plt.xlabel('Saving Throw')

plt.grid(zorder=0)
plt.legend()

plt.show()