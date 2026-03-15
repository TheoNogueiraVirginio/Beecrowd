codigo, qtd, valor_uni = map(float,input().split())

codigo2, qtd2, valor_uni2 = map(float,input().split())

print(f'VALOR A PAGAR: R$ {qtd *valor_uni + qtd2*valor_uni2:.2f}')