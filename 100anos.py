import time #Biblioteca time importada, para dar espaçamento entre as respostas. 
import sys #atualização com o sys importado, para encerramento do programa.

nome = input("Olá, qual o seu nome?") #primeira vez que input foi criado, com a variável nome.
time.sleep(2) #tempo de dois segundos, pela  
print (f"Belíssimo nome, {nome}!") #print sendo usada para transmitir a mensagem para o código.
time.sleep(2)
while True:  #Como na própria tradução, enquanto verdade, e o usuário fizer corretamente, colocando uma idade como número inteiro, o código seguirá em frente.
 idade = input("Qual sua idade?") 
 try:   #É uma tentativa de um prosseguimento correto.
   idade = int(idade)   #int para garantir que seja um número inteiro
   break     #break para encerrar o ciclo
 except ValueError: #com exceção do erro de o valor por acaso não ter sido um número inteiro.
  print(f"Ou você não me deu sua idade em número ou foi em algarismo romano! Fale sua idade em um número inteiro!")
time.sleep(1)
print (f"É uma ótima idade!{idade} aninhos só!")
resposta = input("Você gostaria de saber quantos anos faltam para você completar 100? Sim ou não?")
time.sleep(1)
if resposta.lower() == "sim": #caso a resposta seja sim, 
    print (f"Vamos lá!")
else:
    print (f"Beleza então. Caso mude de ideia, inicie novamente o programa. Em 5 segundos, ele será encerrado!")
    time.sleep(5)
    sys.exit() #Programa descoberto enquanto estava fazendo outra atividade. Esse sys que foi importado serve para essa função.
time.sleep(2)
anos_faltantes = 100 - idade
if idade <= 100:
 print (f"Faltam apenas {anos_faltantes} para você completar 100 anos!")
else:
 print (f"Você é bem velho, ein! Ou já passou da idade ou já tem 100 anos!")
 
 print(f"O programa será encerrado em 5 segundos. Espero que você tenha ficado feliz com o tempo que tem restante. Ou não!")
 time.sleep(5)
 sys.exit()
