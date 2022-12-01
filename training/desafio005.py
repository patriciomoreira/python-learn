#5. Digite um número e exiba o antecessor e sucessor.

num = int(input('Digite um número inteiro: '))

print("O número digitado foi: {:>5}".format(num))
print('O seu antecessor é:    {:>5}'.format(num-1))
print('O seu sucessor é:      {:>5}'.format(num+1))