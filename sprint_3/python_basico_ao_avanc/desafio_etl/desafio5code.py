#5 A lista dos Autores ordenada por pagamento. Do mais bem pago para o menos bem pago: + bem pago: total gross
  
from csv import DictReader

with open('./actors.csv') as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)

    sorted_data = sorted(data, key=lambda x: float(x['Total Gross']), reverse=True)
  
    print(f'A lista de atores em ordem de pagamento do mais bem pago para o menos bem pago é:\n')
    
    for elementos in sorted_data:
      TotalGross = float(elementos['Total Gross'])
      nomeAtor = elementos['Actor']
      print(nomeAtor)