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

def task2_3(z):
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
    cur.execute('SELECT count(sofifa_id),club FROM "FIFA".players_20 GROUP BY club order by count(sofifa_id) DESC;')
    result=[]
    for row in cur:
        result.append(row)
        
    #dataframe=pd.DataFrame(result[0:z], columns=['Number of Players','Club Name'])
    
    conn.commit()
    cur.close()
    conn.close()
    return result[0:z]

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


def test_happy_path():
    #Both happy and sad paths
    task2_1(2)
    task2_2(3)
    task2_3(4)
    task2_4_1()
    task2_4_2()
    task2_5()

    assert len(task2_1(2)) == 2, "Returned should be length 6"
    assert len(task2_2(3)) == 3, "Returned should be length 6"
    assert len(task2_3(4)) == 4, "Returned should be length 5"
    assert len(task2_4_1()) == 1, "Returned should be length 1"
    assert len(task2_4_2()) == 1, "Returned should be length 1"
    assert len(task2_5()) == 1, "Returned should be length 1"

    assert task2_1(2) == [('T. Haye',), ('Àlex Corredera',)], "Returned value"
    assert task2_2(3) == [(18, 'FC Ingolstadt 04'),(18, '1. FC Kaiserslautern'),(17, 'FC Girondins de Bordeaux')], "Returned value"
    assert task2_3(4) == [(33, 'VfL Wolfsburg'), (33, 'Norwich City'), (33, 'AS Monaco'), (33, 'Crystal Palace')], "Returned value"
    assert task2_4_1() == [(17152, None)], "Returned value"
    assert task2_4_2() == [(7820, 'SUB')], "Returned value"
    assert task2_5() == [(1667, 'England')], "Returned value"

def test_sad_path():
    task2_1(2)
    task2_2(3)
    task2_3(4)
    task2_4_1()
    task2_4_2()
    task2_5()
    assert task2_1(2) is not None, "Returned should not be None"
    assert task2_2(3) is not None, "Returned should not be None"
    assert task2_3(4) is not None, "Returned should not be None"
    assert task2_4_1() is not None, "Returned should not be None"
    assert task2_4_2() is not None, "Returned should not be None"
    assert task2_5() is not None, "Returned should not be None"

    assert task2_1(2) is not int, "Returned should be integer"
    assert task2_2(3) is not int, "Returned should be integer"
    assert task2_3(4) is not int, "Returned should be integer"