def task2_5():
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
    cur.execute('SELECT count(sofifa_id),nationality FROM "FIFA".players_20 GROUP BY nationality order by count(sofifa_id) DESC;')
    result=[]
    for row in cur:
        result.append(row)
        break
        
    #dataframe=pd.DataFrame(result, columns=['count','nationality'])
    
    conn.commit()
    cur.close()
    conn.close()
    return result