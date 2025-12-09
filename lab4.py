# r - Винтовка (rifle)
# p - Пистолет (pistol)
# a - Боекомплект (ammo)
# m - Аптечка (medkit)
# i - Ингалятор (inhaler)
# k - Нож (knife)
# x - Топор (axe)
# t - Оберег (talisman)
# f - Фляжка (flask)
# d - Антидот (antidot) !
# s - Еда (supplies)
# c - Арбалет (crossbow)

print("Выполнил: Опекунов Николай R3142\nВариант 6\n")
print("Том имеет 3x3 инвентарь, а также болеет параноей")

survive_points = 15
count_survive = 0
Optional_subjects = [
    ['r', 3, 25],
    ['p', 2, 15],
    ['a', 2, 15],
    ['m', 2, 20],
    ['i', 1, 5],
    ['k', 1, 15],
    ['x', 3, 20],
    ['t', 1, 25],
    ['f', 1, 15],
    ['s', 2, 20],
    ['c', 2, 20]]
Compulsory_subjects = [
    ['d', 1, 10]]
count_cell = 9 - Compulsory_subjects[0][1]
equipment = []
Optional_subjects.sort(key=lambda x: (x[2] // x[1], x[1]), reverse=True) # Сортировка по очкам выживания на ячейку и по количеству ячеек
for survive in Optional_subjects: # Подсчет максимальных очков выживания
    count_survive += survive[2]
for weapon in Optional_subjects: # Заполнение рюкзака
    if count_cell >= weapon[1]:
        count_cell -= weapon[1]
        survive_points += weapon[2]
        equipment.extend([weapon[0]] * weapon[1])
equipment.append(Compulsory_subjects[0][0])
survive_points = survive_points - (count_survive - survive_points)


bag = [] 
for i in range(0, len(equipment), 3):
    row = equipment[i:i + 3]
    bag.append(row)

for row in bag:
    for element in row:
        print(f"[{element}]", end = " ")
    print()
print(f'Итоговые очки выживания: {survive_points}')