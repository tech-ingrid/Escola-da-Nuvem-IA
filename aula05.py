def registrar_notas():
    notas = []
    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um valor de 0 a 10.")
        except ValueError:
            print('Entrada inválida. Por favor, digite um número válido')

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
        print(f"Total de notas válidas registradas: {len(notas)}")
    else:
        print("\nNenhuma nota válida foi registrada.")

registrar_notas()