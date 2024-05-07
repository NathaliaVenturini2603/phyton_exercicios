def converter_para_centimetros(altura):
    return altura * 100

def main():
    altura_em_metros = float(input("Informe a sua altura em metros: "))
    altura_em_centimetros = converter_para_centimetros(altura_em_metros)
    print(f"Sua altura em centímetros é: {altura_em_centimetros} cm")

if __name__ == "__main__":
    main()
