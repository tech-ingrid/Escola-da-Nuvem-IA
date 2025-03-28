import requests

def obter_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    response = requests.get(url)
    dados = response.json()
    cotacao = dados[f"{moeda}BRL"]
    return float(cotacao['bid'])

def main():
    moeda = input("Digite a moeda para cotação (USD ou EUR): ").upper()
    if moeda not in ["USD", "EUR"]:
        print("Moeda inválida! Digite USD ou EUR.")
    else:
        cotacao = obter_cotacao(moeda)
        print(f"Cotação de {moeda} para BRL: R$ {cotacao:.2f}")

if __name__ == "__main__":
    main()
