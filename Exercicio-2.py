
def h_index_linear(citacoes):
    h = 0
    for i, num_citacoes in enumerate(citacoes):
        if num_citacoes < i + 1:
            return i
        
        
        h = i + 1
    return h

def h_index_binaria(citacoes):
    n = len(citacoes)
    i, j = 0, n - 1
    h_index = 0

    while i <= j:
        m = (i + j) // 2
        
        
        if citacoes[m] >= m + 1:
           
            h_index = m + 1
            i = m + 1
        else:
            
            j = m - 1
            
    return h_index


   
citacoes = [10, 8, 5, 4, 3]
print(citacoes)
print(h_index_linear(citacoes)) 
print(h_index_binaria(citacoes))
