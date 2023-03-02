from csv import DictReader

with open('./actors.csv') as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)
    
    maiorTotalGross = 0
    nomeAtor = ''
    for elementos in data:
        TotalGross =  float(elementos['Total Gross'])
    if(maiorTotalGross < TotalGross):
        nomeAtor = elementos['Actor']
        maiorTotalGross = TotalGross
        
        
    #sorted(data, key=lambda x: x['Total Gross'], reverse=True)
    print(data)

#nao ta funcionando lamba e print... arrumar amanhã.