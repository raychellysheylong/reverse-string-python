from pilha import Pilha

def inverter_string(string):
    pilha = Pilha()  

    for char in string:
        pilha.push(char)

    reversed_string = ""
    
    while not pilha.is_empty():
        reversed_string += pilha.pop()

    return reversed_string

def main():
    string = input("Digite uma string para ser invertida: ")

    string_invertida = inverter_string(string)

    print("String invertida:", string_invertida)

if __name__ == "__main__":
    main()
