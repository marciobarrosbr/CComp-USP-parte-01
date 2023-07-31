# Crie um programa que leia  uma sequencia de numeros inteiro que sera encerrado ao receber zero,
#  e em seguida seus valores devem ser apresentados em onder inversa a sua entrada

my_list = []
n = 1
while n!= 0:
    n = int(input('n: '))
    if n == 0:
        break
    else:
        my_list.append(n)
    

print(len(my_list))
a = len(my_list)
a *= -1
for i in range(-1, (a-1), -1):
    print(my_list[i],end=', ')