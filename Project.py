summa = 0
print(" Микроэволюция приводит к образованию:")
print("1) видов")
print("2) родов")
print("3) семейств")
answer = str(input("Выберите номер ответа: "))
if answer == "1" or answer == "1)":
    print("Верно! +10 баллов")
    summa += 10
else:
    print("Неверно! +0 баллов")

print("\n Предупреждающая окраска характерна для:")
print("1) обыкновенной лисы")
print("2) уссурийского тигра")
print("3) жука-нарывника")
answer = str(input("Выберите номер ответа: "))
if answer == "3" or answer == "3)":
    print("Верно! +10 баллов")
    summa += 10
else:
    print("Неверно! +0 баллов")

print("\n К факторам эволюции не относится")
print("1) изоляция")
print("2) модификационная изменчивость")
print("3) борьба за существование")
answer = str(input("Выберите номер ответа: "))
if answer == "2" or answer == "2)":
    print("Верно! +10 баллов")
    summa += 10
else:
    print("Неверно! +0 баллов")

print("\n Элементарной единицей эволюции считают:")
print("1) вид")
print("2) популяция")
print("3) организм")
answer = str(input("Выберите номер ответа: "))
if answer == "2" or answer == "2)":
    print("Верно! +10 баллов")
    summa += 10
else:
    print("Неверно! +0 баллов")

print("\n Внутривидовая борьба за существование – это отношения между:")
print("1) отношения между волками из-за корма")
print("2) обыкновенной и сибирской сосной")
print("3) серой и чёрной крысой")
answer = str(input("Выберите номер ответа: "))
if answer == "1" or answer == "1)":
    print("Верно! +10 баллов")
    summa += 10
else:
    print("Неверно! +0 баллов")

if summa<=20:
    print("\n К сожалению, оценка 2. Вам следует больше времени уделять биологии")
elif summa == 30:
    print("\n Оценка 3. Не останавливайтесь на достигнутом результате")
elif summa == 40:
    print("\n Оценка 4. У вас почти получилось!")
else:
    print("\n Молодец! Оценка 5")
