## Cada zig zag começa na posicao 0,0
## Se você olhar apenas a posicao de row, ela sempre começa em 0, vai somando de 1 em 1 até chegar no numRows e depois vai diminuindo de 1 a 1 até chegar em 0 e continuar o processo
## Isso consegue nos calcular a row de cada letra
## Para calcular a column, basta circular entre 0 e numRows e voltar

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        chars = list(s)
        zigzag = [ [] for j in range(numRows) ]
        counter = 0
        add = 1
        for char in chars:
            #print(zigzag, char, counter, add)
            zigzag[counter].append(char)
            counter += add
            if counter == 0:
                add = 1
            if counter >= numRows-1:
                add = -1
        frase_final = ""
        for arr in zigzag:
            frase_final = frase_final + "".join(arr)
        #print(frase_final)
        return frase_final

