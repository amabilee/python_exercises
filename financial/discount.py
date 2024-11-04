def calcularDesconto(valor, desconto):
  vlr_desconto = (valor*desconto)/100
  return vlr_desconto

def totalItem(vlr_unit, qtde):
  valorTotal = vlr_unit*qtde
  return valorTotal

vlr_unit = 100
desconto = 10
qtde = 3

valor_desconto = calcularDesconto(vlr_unit, desconto)
valorVenda = vlr_unit - valor_desconto
valorTotal = totalItem(valorVenda,qtde)

print(valorTotal)