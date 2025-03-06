import random

list = [
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
]
print(list)

for n in list:
    print(n)

# Masyvai (Array) Dirbtinių intelektų uždavinių sprendimui nenaudoti. Googlinkite, arba klauskite.

# 1. Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29), kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.
print(
    "\n 1. Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29), kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.")
empty_list = []
for e in range(0, 30):
    empty_list.append(random.randint(5, 25))
print(empty_list)

# list = [random.randint(5,25) for _ in range(0,29)]
# print(list)

# 2. Naudodamiesi 1 uždavinio masyvu:
print("\n2. Naudodamiesi 1 uždavinio masyvu")
# a) Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;
print(" 2 a) Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;")
counter = 0
for a in empty_list:
    if a > 10:
        counter += 1
print(f'Count of values above 10: {counter}')

# b) Raskite didžiausią masyvo reikšmę;
print("\n 2 b) Raskite didžiausią masyvo reikšmę;")

maxvalue = empty_list[0]
for b in empty_list:
    if b > maxvalue:
        maxvalue = b
print(f'Max array value {maxvalue}')

# maxvalue = max(empty_list)
# print(f'Max array value: {maxvalue}')

# c) Suskaičiuokite visų reikšmių sumą;
print("\n 2 c) Suskaičiuokite visų reikšmių sumą")
sumvalue = 0
for c in empty_list:
    sumvalue += c
print(f"Sum of all array values: {sumvalue}")

# sumvalue = sum(empty_list)
# print(f"Sum of all array values: {sumvalue}")

# d) Sukurkite naują masyvą, kurio reikšmės yra 1 uždavinio masyvo reikšmes minus tos reikšmės indeksas;
print("\n 2 d) Sukurkite naują masyvą, kurio reikšmės yra 1 uždavinio masyvo reikšmes minus tos reikšmės indeksas;")
minus_index_list = []
for ind in range(0, len(empty_list)):
    minus_index_list.append(empty_list[ind] - ind)
print(minus_index_list)

# e) Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25, kad bendras masyvas padidėtų iki indekso 39;
print(
    "\n 2 e) Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25, kad bendras masyvas padidėtų iki indekso 39;")
new_list = empty_list + []
for e in range(0, 10):
    new_list.append(random.randint(5, 25))
print(new_list)

# f) Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių, o kitas iš porinių;
print(
    "\n 2 f) Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių, o kitas iš porinių;")
pairedind = []
unpairedind = []
for ind in range(0, len(empty_list)):
    if ind % 2 == 0:
        unpairedind.append(empty_list[ind])
    if ind % 2 != 0:
        pairedind.append(empty_list[ind])
print(f"Paired index list {pairedind}")
print(f"Unpaired index list {unpairedind}")

# print("\n atspausdinti atskirai lyginiai ir nelyginiai skaičiai")
# paired = []
# unpaired = []
# for f in empty_list:
#     if f % 2 == 0:
#         paired += [f]
#     elif f % 2 != 0:
#         unpaired += [f]
# print(f"Even numbers {paired}")
# print(f"Odd numbers {unpaired}")

# g) Masyvo elementus su poriniais indeksais padarykite lygius 0 jeigu jie didesni už 15;
print("\n 2 g) Masyvo elementus su poriniais indeksais padarykite lygius 0 jeigu jie didesni už 15;")
updated_list = []
for g in range(len(empty_list)):
    if g % 2 != 0:
        if empty_list[g] > 15:
            updated_list.append(0)
        else:
            updated_list.append(empty_list[g])
    else:
        updated_list.append(empty_list[g])
print(updated_list)

# h) Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10;
print("\n 2 h) Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10;")
for h in range(len(empty_list)):
    if empty_list[h] > 10:
        print(f"Smallest index where value > 10: {h}")
        break

# 3. Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D, o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės.
print(
    "\n3. Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D, o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės.")
letters = []
abcd = ['A', 'B', 'C', 'D']
counterA = 0
counterB = 0
counterC = 0
counterD = 0
for _ in range(0, 200):
    letters.append(random.choice(abcd))
for l in letters:
    if l == "A":
        counterA += 1
    if l == "B":
        counterB += 1
    if l == "C":
        counterC += 1
    if l == "D":
        counterD += 1
print(f" ".join(letters))
print(f"Count of letter A: {counterA}")
print(f"Count of letter B: {counterB}")
print(f"Count of letter C: {counterC}")
print(f"Count of letter D: {counterD}")

# 4. Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.
print("\n4. Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.")

arrayA = []
arrayB = []
arrayC = []
arrayD = []

for m in range(0, len(letters)):
    if letters[m] == "A":
        arrayA.append("A")
    if letters[m] == "B":
        arrayB.append("B")
    if letters[m] == "C":
        arrayC.append("C")
    if letters[m] == "D":
        arrayD.append("D")
print(f" ".join(arrayA) + " " + f" ".join(arrayB) + " " + f" ".join(arrayC) + " " + f" ".join(arrayD))

print("")
for i in range(0, len(letters)):
    for j in range(0, len(letters)):
        if letters[i] < letters[j]:
            letters[i], letters[j] = letters[j], letters[i]
j = ""
for i in range(0, len(letters)):
    j = j + letters[i]
print(f" ".join(j))

print("")
letters.sort()
print(f" ".join(letters))

a = sorted(letters)
print(f" ".join(a))

# 5. Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes. (turi gautis masyvas, kurio elementai, kaip pvz atrodo taip: “AAB”, “CBC”, “DDA”, 200 reikšmių). Paskaičiuokite kiek skirtingų reikšmių kombinacijų gavote.
print(
    "\n5. Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes. Paskaičiuokite kiek skirtingų reikšmių kombinacijų gavote.")
letters_list = []
letters_list1 = []
letters_list2 = []
letters_list3 = []
for i in range(0, 200):
    letters_list1.append(random.choice(abcd))
    letters_list2.append(random.choice(abcd))
    letters_list3.append(random.choice(abcd))
    letters_list.append(letters_list1[i] + letters_list2[i] + letters_list3[i])
print(f" ".join(letters_list))

print("\nUsing NOT IN function:")
unique_combinations = []
combinations_counter = 0
for x in letters_list:
    if x not in unique_combinations:
        unique_combinations.append(x)
        combinations_counter += 1
# print(f"List of unique combinations {unique_combinations}")
print(f"Number of unique values: {combinations_counter}")
print(unique_combinations)

print("\nUsing SET function:")
combinations_counter_set = 0
mylist = set(letters_list)
for x in mylist:
    combinations_counter_set += 1
print(f"Number of unique combinations: {combinations_counter_set}")

# 6. Sugeneruokite du masyvus, kurių reikšmės yra atsitiktiniai skaičiai nuo 100 iki 999. Masyvų ilgiai 100. Masyvų reikšmės turi būti unikalios savo masyve (t.y. neturi kartotis).
print(
    "\n6. Sugeneruokite du masyvus, kurių reikšmės yra atsitiktiniai skaičiai nuo 100 iki 999. Masyvų ilgiai 100. Masyvų reikšmės turi būti unikalios savo masyve (t.y. neturi kartotis)")

unique_array1 = []
unique_array2 = []
while len(unique_array1) < 100:
    array_value1 = random.randint(100, 999)
    if array_value1 not in unique_array1:
        unique_array1.append(array_value1)
print(unique_array1)

while len(unique_array2) < 100:
    array_value2 = random.randint(100, 999)
    if array_value2 not in unique_array2:
        unique_array2.append(array_value2)
print(unique_array2)

# 7. Sugeneruokite masyvą, kuris būtų sudarytas iš reikšmių, kurios yra pirmame 6 uždavinio masyve, bet nėra antrame 6 uždavinio masyve.
print(
    "\n7. Sugeneruokite masyvą, kuris būtų sudarytas iš reikšmių, kurios yra pirmame 6 uždavinio masyve, bet nėra antrame 6 uždavinio masyve.")
only_in_first_array = []
for number in unique_array1:
    if number not in unique_array2:
        only_in_first_array.append(number)
print(f"Values only in unique_array1: \n{only_in_first_array}")

# 8. Sugeneruokite masyvą iš elementų, kurie kartojasi abiejuose 6 uždavinio masyvuose.
print("\n8. Sugeneruokite masyvą iš elementų, kurie kartojasi abiejuose 6 uždavinio masyvuose.")
in_both_arrays = []
for number in unique_array1:
    if number in unique_array2:
        in_both_arrays.append(number)
print(f"Matching values in both arrays: \n{in_both_arrays}")

# 9. Sugeneruokite 10 skaičių masyvą pagal taisyklę: Du pirmi skaičiai- atsitiktiniai nuo 5 iki 25. Trečias, pirmo ir antro suma. Ketvirtas- antro ir trečio suma. Penktas trečio ir ketvirto suma ir t.t.
print(
    "\n9. Sugeneruokite 10 skaičių masyvą pagal taisyklę: Du pirmi skaičiai- atsitiktiniai nuo 5 iki 25. Trečias, pirmo ir antro suma. Ketvirtas- antro ir trečio suma. Penktas trečio ir ketvirto suma ir t.t.")
array = []
for n in range(0, 10):
    if n == 0 or n == 1:
        n = random.randint(5, 25)
    if n == 2:
        n = n + n
    array.append(n)
print(array)

# 10. Sugeneruokite 101 elemento masyvą su atsitiktiniais skaičiais nuo 0 iki 300. Reikšmes kurios tame masyve yra ne unikalios pergeneruokite iš naujo taip, kad visos reikšmės masyve būtų unikalios. Išrūšiuokite masyvą taip, kad jo didžiausia reikšmė būtų masyvo viduryje, o einant nuo jos link masyvo pradžios ir pabaigos reikšmės mažėtų. Paskaičiuokite pirmos ir antros masyvo dalies sumas (neskaičiuojant vidurinės). Jeigu sumų skirtumas (modulis, absoliutus dydis) yra didesnis nei | 30 | rūšiavimą kartokite. (Kad sumos nesiskirtų viena nuo kitos daugiau nei per 30)
