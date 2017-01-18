s=input('Informe a distancia em Km: ')
v=round(s/input('Informe o consumo medio: '))
print'Total em litros de combustivel: %d Litros\nTotal gasto com combustivel: R$ %.2f\nParadas previstas: %d'%(v,v*3.8,s/250)
