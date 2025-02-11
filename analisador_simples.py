import string

def pre_processamento(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    tokens = texto.split()

    return tokens
    
def classificar_sentimento(tokens, positivas, negativas):
    qtd_palavras_boas = 0
    qtd_palavras_ruins = 0
    i = 0  

    while i < len(tokens):
        if tokens[i] == "não":  
            i += 1  
            while i < len(tokens) and tokens[i] not in positivas + negativas:
                i += 1  
            
            if i < len(tokens):  
                if tokens[i] in positivas:
                    qtd_palavras_ruins += 1  
                elif tokens[i] in negativas:
                    qtd_palavras_boas += 1  
        else:
            if tokens[i] in positivas:
                qtd_palavras_boas += 1
            elif tokens[i] in negativas:
                qtd_palavras_ruins += 1
        
        i += 1

    if qtd_palavras_boas > qtd_palavras_ruins:
        return "Positivo."
    elif qtd_palavras_ruins > qtd_palavras_boas:
        return "Negativo."
    else:
        return "Neutro."

def main():
    positivas = ["bom", "gostei", "gostar", "gosto", "ótimo", "legal", "agrádavel", "alegre", "feliz", "excelente", "boa"]
    negativas = ["ruim", "péssimo", "horroroso", "chato", "odiei", "odiar", "triste", "desagradável", "horrível", "horror", "decepção", "decepcionado"]
    texto = input("Insira o texto que deseja analisar: ")
    tokens = pre_processamento(texto)
    status = classificar_sentimento(tokens, positivas, negativas)
    print(status)

if __name__ == "__main__":
    main()
