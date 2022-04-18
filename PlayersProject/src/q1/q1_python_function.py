def task2_1(z):
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
    cur.execute('SELECT short_name FROM "FIFA".players_20 order by ((skill_dribbling + skill_curve + skill_fk_accuracy + skill_long_passing +skill_ball_control)/5 - overall) desc;')
    result=[]
    for row in cur:
        result.append(row)

    #dataframe=pd.DataFrame(result[0:z], columns=['shortname'])
    
    conn.commit()
    cur.close()
    conn.close()
    return result[0:z]