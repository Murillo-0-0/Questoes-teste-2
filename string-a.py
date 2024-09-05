def verificar_letra_a(string):
    count = 0
    for char in string:
        if char.lower() == 'a':
            count += 1
    return count

def main():
    texto = input("Informe uma string: ")
    
    ocorrencias = verificar_letra_a(texto)
    
    if ocorrencias > 0:
        print(f"A letra 'a' (maiúscula ou minúscula) aparece {ocorrencias} vezes na string.")
    else:
        print("A letra 'a' (maiúscula ou minúscula) não aparece na string.")

if __name__ == "__main__":
    main()
