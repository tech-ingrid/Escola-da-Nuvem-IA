import request
from datetime import datetime

def obter_cotacao(moeda):
	url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
	try:
		response = resquest.get(url)
		response.raise_for_status()
		dados = response.json()
		cotacao = dados[f"{moeda}BRL"]
		return f"""
		Moeda: {moeda} para BRL
		Valor: R$ {float(cotacao['bid'])}
		Maxima: R$ {float(cotacao['high']):2f}
		Minima: R$ {float(cotacao['low']):2f}
		Data/Hora: {datetime.fromtimestamp(int(cotacao['timestamp']))}
		"""
	except requests.RequestException as e:
		return f"Erro ao obter cotacao:{e}"
	except KeyError
		return "Moeda não encontrada ou não suportada"

def main():
	moeda = input("Digite o valor da moeda para cotação (ex: USD,EUR,GBP):").upper
	print("\nObtendo cotação...")
	resultado = obter_cotacao(moeda)
	print(resultado)

if __name__ == "__main__"
	main()
