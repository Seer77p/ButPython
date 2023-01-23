from random import randint

x=randint(0,100)

count_perebor=0
#метод последовательного перебора
for i in range(0,100):
    count_perebor+=1
    if i==x:
        print("Число найдено")
        break
print("Загаданное числоо было", x, "и для его поиска перебором потребовалось", count_perebor, "итераций")

count_random=1
#метод случайного отгадывания
y=randint(0,100)
while x!=y:
    y=randint(0,100)
    count_random+=1
print("Загаданное числоо было", x, "и для его поиска угадывания потребовалось", count_random, "итераций")

count_bin=1
print("Начнем игру - угадай число от 0 до 100")
y=int(input('Введи чило'))
while x!=y:
    if x<y: print("Меньше")
    else: print("Больше")
    y=int(input('Введи чило'))
    count_bin+=1
print("Загаданное числоо было", x, "и для его поиска угадывания потребовалось", count_bin, "итераций")

right=1000000
left=0

x=randint(left, right)
count_bin1=1
print('Начнем игру - угадай число от 0 до ', right)
mid=(right+left)//2
while x!=mid:
    print(mid)
    if x<mid:
        print("Меньше")
        right=mid-1
    else:
        print("Больше")
        left=mid+1
    mid=(right+left)//2
    count_bin1+=1
print("Загаданное числоо было", x, "и для его поиска угадывания потребовалось", count_bin1, "итераций")