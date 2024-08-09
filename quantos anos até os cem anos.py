import time 
nome = input("Olá, qual o seu nome?")
time.sleep(2)   
print (f"Belíssimo nome, {nome}!")
time.sleep(2)
while True: 
 idade = input("Qual sua idade?")
 try: 
   idade = int(idade)
   break 
 except ValueError:
  print(f"Ou você não me deu sua idade em número ou foi em algarismo romano! Fale sua idade em um número inteiro!")
time.sleep(1)
print (f"É uma ótima idade!{idade} aninhos só!")
resposta = input("Você gostaria de saber quantos anos faltam para você completar 100? Sim ou não?")
time.sleep(1)
if resposta.lower() == "sim":
    print (f"Vamos lá!")
else:
    print (f"Você não teria escolha mesmo!")
time.sleep(2)
anos_faltantes = 100 - idade
if idade <= 100:
 print (f"Faltam apenas {anos_faltantes} para você completar 100 anos!")
else:
 print (f"Você é bem velho, ein! Já passou da idade!")
 
 