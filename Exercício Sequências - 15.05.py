#1
def bombons (dinheiro, preço):
    numero_bombons = dinheiro // preço
    troco = dinheiro % preço
    return numero_bombons, troco

#2
def mais_um_bombom (dinheiro, preço):
    qtd, troco = bombons(dinheiro, preço)
    return preço - troco 
