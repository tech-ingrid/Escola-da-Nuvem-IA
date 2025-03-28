def is_palindromo(texto):
    texto_limpo = "".join(char.lower()
                          for char in texto
                          if char.isalnum())
    return texto_limpo == texto_limpo[:: -1]
frase = "A cara rajada da jararaca"
resultado = is_palindromo(frase)
if resultado == True:
    Resposta = "Sim"
else:
    Resposta = "Não"
print(Resposta)