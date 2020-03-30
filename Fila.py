class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self. cidades = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numeroElementos = 0
        
    def enfileirar(self, cidade):
        if not Fila.filaCheia(self):            
            if self.fim == self.tamanho - 1:
                self.fim = -1
            self.fim += 1
            self.cidades[self.fim] = cidade
            self.numeroElementos += 1
                
        else:
            print("Fila esta cheia")
            
    def desenfileirar(self):
        if not Fila.filaVazia(self):
            temp = self.cidades[self.inicio]
            self.inicio += 1
            if self.inicio == self.tamanho:
                self.inicio = 0
            self.numeroElementos -= 1
            return temp
        else:
            print("Fila esta vazia")
            return None
            
    def getPrimeiro(self):
        return self.cidades[self.inicio]

    def filaVazia(self):
        return self.numeroElementos == 0
    
    def filaCheia(self):
        return self.numeroElementos == self.tamanho
        
            
        