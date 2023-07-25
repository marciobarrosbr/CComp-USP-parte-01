def maximo_primo(n):
    for c in range(n, 1, -1):
        if primo(c):
            return c
        
def primo(m):
    i = 1
    cont = 0
    while i <= m:
        if m % i == 0:
            cont += 1
        i += 1
        if cont > 2:
            return False
    else:
        return True
num = int(input('entre com o valor:: '))
print(f'o valor {num} tem como maior primo {maximo_primo(num)}')