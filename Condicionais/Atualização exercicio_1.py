import json
import urllib.request
import urllib.parse

def consultar_endereco_por_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    return data

def main():
    cep = input("Insira o CEP para consultar o endereço: ")
    endereco = consultar_endereco_por_cep(cep)
    
    if "erro" not in endereco:
        print("Informações do endereço:")
        print(f"CEP: {endereco['cep']}")
        print(f"Logradouro: {endereco['logradouro']}")
        print(f"Complemento: {endereco.get('complemento', 'N/A')}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Cidade: {endereco['localidade']}")
        print(f"Estado: {endereco['uf']}")
    else:
        print("CEP não encontrado.")

if __name__ == "__main__":
    main()