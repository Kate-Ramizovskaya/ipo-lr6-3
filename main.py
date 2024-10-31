kolv=input("Введите кол-во строк: ")

if kolv.isdigit() and int(kolv)>0:
    kolv=int(kolv)
else:
    print("Введены неправильные значения.")

str=[]
for i in range(kolv):
    strs=input(f"Введите {i+1}: ")
    str.append(strs)

text=' '.join(str)

words=text.split()

words=set(words)
count=len(words)

print(f"Кол-во различных слов: {count}")