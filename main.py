kolv=input("Введите кол-во строк: ") #запрос кол-ва строк

if kolv.isdigit() and int(kolv)>0:#проверка на правильный ввод
    kolv=int(kolv)
else:
    print("Введены неправильные значения.")

str=[]#инициализация 
for i in range(kolv):#ввод строк через цикл for
    strs=input(f"Введите {i+1}: ")
    str.append(strs)

text=' '.join(str)#перекидывание списка в строку

words=text.split()#разделение на подстроки

words=set(words)#контейнер не повторяющихся значений
count=len(words)#подсчет words

print(f"Кол-во различных слов: {count}")#итоговый вывод значений 
