num_binario=""
num_decimale=int(input("Inserire il numero decimale "))
num_decimale_fin=num_decimale
while num_decimale >0:
    num_decimale, resto=divmod(num_decimale, 2)
    num_binario=str(resto)+num_binario
print("La conversione del numero decimale", num_decimale_fin, "in numero binario è", num_binario)