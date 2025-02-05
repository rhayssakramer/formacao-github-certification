# Solicitando uma palavra do usuário
palavra = input("Digite uma palavra: ").strip().lower()

# Invertendo a palavra
palavra_invertida = palavra[::-1]

# Verificando se é um palíndromo
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um PALÍNDROMO! 🎉")
else:
    print(f"A palavra '{palavra}' NÃO é um palíndromo. 😢")