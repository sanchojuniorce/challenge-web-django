import csv
from dotenv import dotenv_values
from mysql import connector
from datetime import datetime

FILE = 'openfoodfacts/csv/openfoodfacts_export.csv'
INSERT = "INSERT INTO challenge_open_food.products (code, status, imported_t, url, creator, created_t, last_modified_t, url, product_name, quantity, brands, categories, labels, cities, purchase_places, stores, ingredients_text, traces, serving_size, serving_quantity, nutriscore_score, nutriscore_grade, main_category, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

def envs_database_mysql():
    return dotenv_values(".env")
    
def query_database_mysql(sql, val):
    config = envs_database_mysql()

    connection = connector.connect(
        host=config['HOST'], port=config['PORT'],
        user=config['USER'], password=config['PASSWORD'],
        database=config['DATABASE']
    )

    cur = connection.cursor()
    query_database = cur.execute("SELECT * FROM challenge_open_food.products;")
    result = cur.fetchone()
    connection.close()
    return result

def read_import_csv():
    arr = []
    values = []
    with open(FILE, 'rb') as csvfile:
        for line in csvfile.readlines():
            try:
                arr = line.decode('UTF-8').split(' ')[0]

                code = verify_code(arr[0:13].split(' '))
                status = "published"
                imported_t = datetime.now()
                url = "https://world.openfoodfacts.org/product/{}".format(code)
                creator = "securita"
                created_t = datetime.now()
                last_modified_t = datetime.now()
                product_name = ' '.join(line.decode('UTF-8').split(' ')[29:35])
                quantity = line.decode('UTF-8').split(' ')[16::17] #"380 g (6 x 2 u.)"
                brands =  line.decode('UTF-8').split(' ')[21:22]
                print(line.decode('UTF-8').split(' ')[0::])
                categories = line.decode('UTF-8').split(',')[26:27]
                labels =  line.decode('UTF-8').split(',')[28:29]
                cities =  ""
                purchase_places = ','.join(line.decode('UTF-8').split(',')[33:40])
                stores = ','.join(line.decode('UTF-8').split(',')[41:42])
                ingredients_text = "farinha de trigo, açúcar, óleo vegetal de girassol, clara de ovo, ovo, humidificante (sorbitol), levedantes químicos (difosfato dissódico, hidrogenocarbonato de sódio), xarope de glucose-frutose, sal, aroma"
                traces = "Frutos de casca rija,Leite,Soja,Sementes de sésamo,Produtos à base de sementes de sésamo"
                serving_size = "madalena 31.7 g"
                serving_quantity = ''
                nutriscore_score = ''
                nutriscore_grade = "d"
                main_category = "en:madeleines"
                image_url = "https://static.openfoodfacts.org/images/products/{}/front_pt.5.400.jpg".format(code)
                values.append(
                    {
                        code, status, imported_t, url, creator, last_modified_t,
                        product_name, quantity, brands, categories, labels, cities,
                        purchase_places, stores, ingredients_text, traces, serving_size,
                        serving_quantity, nutriscore_score, nutriscore_grade, main_category, 
                        image_url
                    }
                )
            except:
                print('') 
    #return values              
    print(values)            
            #query_database_mysql(insert, val)
            #mycursor.execute(insert, val)
    #print(len(arr))

#       mydb.commit()

#       print(mycursor.rowcount, "record inserted.")

def verify_code(code_string):
    if "\t" in code_string[0]: 
        return code_string[0].split('\t')[0]
    else:
        return code_string[0]

if __name__ == "__main__":
    #print(query_database_mysql())
    print(read_import_csv())