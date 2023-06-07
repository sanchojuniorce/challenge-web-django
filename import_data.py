import csv
from dotenv import dotenv_values
from mysql import connector
from datetime import datetime

#FILE = 'openfoodfacts/csv/openfoodfacts_export.csv'
FILE = 'challenge_web/openfoodfacts/csv/openfoodfacts_export.csv'
INSERT = "INSERT INTO challenge_open_food.products (code, status, imported_t, url, creator, created_t, last_modified_t, product_name, quantity, brands, categories, labels, cities, purchase_places, stores, ingredients_text, traces, serving_size, serving_quantity, nutriscore_score, nutriscore_grade, main_category, image_url) "

def envs_database_mysql():
    return dotenv_values(".env")
    
def query_database_mysql(sql, val):
    config = envs_database_mysql()

    connection = connector.connect(
        host=config['HOST'], port=config['PORT'],
        user=config['USER'], password=config['PASSWORD'],
        database=config['DATABASE']
    )

    val = str(val).replace('}','),').replace('{','(').replace('[','').replace(']','')
    print("{} VALUES {}".format(sql, val))
    # cur = connection.cursor()
    # query_database = cur.execute("{} VALUES ({})".format(sql, val))
    # result = cur.fetchone()
    # connection.close()
    return 'result'

def read_import_csv():
    arr = []
    values = []
    with open(FILE, 'rb') as csvfile:
        for line in csvfile.readlines():
            try:
                arr = line.decode('UTF-8').split(' ')[0]

                values = values + [verify_code(arr[0:13].split(' '))]
                values = values + ["published"]
                values = values + [datetime.now().strftime("%d/%m/%Y, %H:%M:%S")]
                values = values + ["https://world.openfoodfacts.org/product/{}".format(code)]
                values = values + ["securita"]
                values = values + [datetime.now().strftime("%d/%m/%Y, %H:%M:%S")]
                values = values + [datetime.now().strftime("%d/%m/%Y, %H:%M:%S")]
                values = values + [' '.join(line.decode('UTF-8').split(' ')[29:35])]
                values = values + [' '.join(line.decode('UTF-8').split(' ')[16::17])]
                values = values + [' '.join(line.decode('UTF-8').split(' ')[21:22])]
                values = values + [' '.join(line.decode('UTF-8').split(',')[26:27])]
                values = values + [' '.join(line.decode('UTF-8').split(',')[28:29])]
                values = values + [' '.join(line.decode('UTF-8').split('\t')[50:51][0])]
                values = values + [','.join(line.decode('UTF-8').split(',')[33:40])]
                values = values + [','.join(line.decode('UTF-8').split(',')[41:42])]
                values = values + [','.join(line.decode('UTF-8').split(',')[80:89])]
                values = values + [' '.join(line.decode('UTF-8').split('\t')[50:51][0])]
                values = values + [' '.join(line.decode('UTF-8').split('\t')[59:60][0])]
                values = values + ['']
                values = values + [' '.join(line.decode('UTF-8').split('\t')[103:104])]
                values = values + [' '.join(line.decode('UTF-8').split('\t')[104:105])]
                values = values + [' '.join(line.decode('UTF-8').split('\t')[306:307][0])]
                values = values + ["https://static.openfoodfacts.org/images/products/{}/front_pt.5.400.jpg".format(code)]
            except:
                print('')  
            #print(values)            
            query_database_mysql(INSERT, values)
            #mycursor.execute(insert, val)
            #print(len(arr))

            #mydb.commit()

            #print(mycursor.rowcount, "record inserted.")
                  
        return values

def verify_code(code_string):
    if "\t" in code_string[0]: 
        return code_string[0].split('\t')[0]
    else:
        return code_string[0]

if __name__ == "__main__":
    #print(query_database_mysql())
    print(read_import_csv())