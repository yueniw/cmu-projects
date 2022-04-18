def task2_4_1():
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
    cur.execute('SELECT count(sofifa_id),nation_position FROM "FIFA".players_20 GROUP BY nation_position order by count(sofifa_id) DESC;')
    result=[]
    for row in cur:
        result.append(row)
        break
        
    #dataframe=pd.DataFrame(result, columns=['count','nation position'])
    
    conn.commit()
    cur.close()
    conn.close()
    return result

def task2_4_2():
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
    cur.execute('SELECT count(sofifa_id),team_position FROM "FIFA".players_20 GROUP BY team_position order by count(sofifa_id) DESC;')
    result=[]
    for row in cur:
        result.append(row)
        break
        
    #dataframe=pd.DataFrame(result, columns=['count','nation position'])
    
    conn.commit()
    cur.close()
    conn.close()
    return result