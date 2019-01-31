lista = ['p','y','t','h','o','n']

for item in lista:

    print(item)



for i in range(100):
     print(i)
else:
    print('pós iteração')


count = 0
a = 'A'
while count < 236:
    print (a)
    a += 'A'
    count += 1
else:
    print('pós iteração 2')


def juntar(x,y):
    return x + " " + y

print(juntar('Olá', 'mundo'))

def biggest_thing(*args):
    return (max(args))

print(biggest_thing('ze', 'ZMaria','João','Pedro'))

choices = ['pizza','pasta','salad','nachos']
print('Your choise are:')
for index, item in enumerate(choices):
    print(index,item)


lista = ['c','b','a','d']
print(sorted(lista))

meu_dicionario = {
        'a':'1',
        'b':'2',
        'c':'3',
        'd':'4' 
}


print(meu_dicionario.items())

print(meu_dicionario.keys())

print(meu_dicionario.values())



def divisao(x,y):
    try:
        res = x/y
        print('O resultado é {}'.format(res))        
    except TypeError:
        print('Erro: Entradas devem ser números e não letras')
    except ZeroDivisionError:
        print('Erro: o divisor não pode ser zero')


divisao(4,2)
divisao(4,0)
divisao(a,4)
divisao(4,'a')
print()
print()
print()

	
import hashlib
hash_object = hashlib.md5(b'Henrique')
print(hash_object.hexdigest())

print()
print()
print()

lista = list(range(10))
print(lista[5])


print('pense em um número entre 0 e 100 e tentarei adivinhar qual é,')
print('em no máximo 7 tentativas: ')
count = 0
menor = 0
maior = 100
chute = int((maior - menor)/2)
resp = ''
lista = list(range(101))
while resp != 'igual': 
    resp = input('O número é maior, menor ou igual a {}? '.format(chute)).strip().lower()
    if resp == 'maior':
          menor = chute + 1
          indice = int(((maior - menor)/2) + menor)
          chute = lista[indice]
          count += 1 
    elif resp == 'menor':
          maior = chute - 1
          indice = int(((maior - menor)/2) + menor)
          chute = lista[indice]
          count += 1 
print('Acertei na {}ª tentativa! O número era {}'.format(count+1,chute))

print()
print()
print()
       


