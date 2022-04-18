
import pandas as pd
df = pd.read_csv('/Users/yueniwang/Desktop/36650_course_project/players_20.csv')
df.columns = [c.lower() for c in df.columns] 

from sqlalchemy import create_engine, MetaData
engine = create_engine('postgresql://postgres:yueniwang@localhost:5432/postgres')


meta = MetaData(engine, schema='FIFA')
meta.reflect(engine, schema='FIFA')
pdsql = pd.io.sql.SQLDatabase(engine, meta=meta)
pdsql.to_sql(df, 'players_20')