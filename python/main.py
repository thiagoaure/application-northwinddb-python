from extract_csv_order import extract_order_details
from extract_db_data import extract_db_data
from insert_mongo import insert_data_mongodb
from read_mongo import read_mongo

print("DIGITE O NÚMERO DA PIPELINE QUE DESEJA EXECUTAR\n")
print("OU NÚMERO 5 PARA EXECUTAR TODAS EM ORDEM CORRETA\n")
print("DIGITE 0 (zero) PARA PARAR A EXECUCAO \n")
print("1- EXTRACT ORDER DATAILS FROM CSV FILE")
print("2- EXTRACT DATA FROM POSTGRE DATABASE")
print("3- INSERT DATA  FROM LOCAL MEMORY IN MONGO DATABASE")
print("4- SAVE DATA FROM MONGO DATABASE IN LOCAL MEMORY")
print("5- ALL PIPELINES - PROCESADO COM A DATA ATUAL")
    
opt = int(input())
while opt != 0:
    match opt:
        case 1:
            extract_order_details()
            print("EXTRACT ORDER DATAILS FROM CSV FILE: OK")
        case 2:
            extract_db_data()
            print("EXTRACT DATA FROM POSTGRE DATABASE: OK")
        case 3:
            print("-----ANTES DE TUDO, INFORME A DATA DO DIA QUE DESEJA PROCESSAR OS DADOS-----") 
            print("----CASO NÃO INFORME, SERÁ CONSIDERADO O DIA DE HOJE\n----")
            strdate = input("DIGITE A DATA NO FORMATO: AAAA-MM-DD, OU PRESSIONE ENTER PARA MANTER A DATA DE HOJE\n")
            if strdate.strip() == "":
                strdate = None
            insert_data_mongodb(strdate)
            print("INSERT DATA  FROM LOCAL MEMORY IN MONGO DATABASE: OK")
        case 4:
            read_mongo()
            print("SAVE DATA FROM MONGO DATABASE IN LOCAL MEMORY: OK")
        case 5:
            extract_order_details()
            extract_db_data()
            insert_data_mongodb()
            read_mongo()
            print("ALL PIPELINES: OK")
        case _:
            print("NENHUMA OPÇÃO VÁLIDA, EXECUTANDO TODAS PIPELINES...")
            extract_order_details(strdate)
            extract_db_data(strdate)
            insert_data_mongodb(strdate)
            read_mongo()
    opt = int(input())