def task2_2(z):
    import pandas as pd
    import psycopg2
    #tweak the database parameters to match your specific postgres database
    conn=psycopg2.connect(host='localhost',
                          port='5432',
                          user='postgres',
                          password='mysecretpassword',
                          database='postgres',
                          #You may add the following line if you have schemas
                          options="-c search_path=nfl"
                         )
    cur=conn.cursor()
    cur.execute('SELECT count (sofifa_id),club FROM "FIFA".players_20 WHERE contract_valid_until = 2021 GROUP BY club order by count(sofifa_id) DESC;')
    result=[]
    for row in cur:
        result.append(row)
        
    #dataframe=pd.DataFrame(result[0:z], columns=['count','club'])
    
    conn.commit()
    cur.close()
    conn.close()
    return result[0:z]