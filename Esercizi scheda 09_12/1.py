#Trovare se una parola è palindroma

parola_reverse=""
parola=input("Inserire la parola ")
parola=parola.lower()
parola_reverse=parola[::-1]
if parola==parola_reverse:
    print(parola, "è un palindromo")
else:
    print(parola, "non è un palindromo")