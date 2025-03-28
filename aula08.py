import random
import string

# Crie um programa que gere uma senha aleatória usando o módulo randon

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

comprimento_senha = 8
senha_gerada = gerar_senha(comprimento_senha)
print(f"Senha gerada: {senha_gerada}")