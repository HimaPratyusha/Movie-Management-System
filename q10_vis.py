import psycopg2
import pandas as pd
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')


# connecting to db
con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="DBproject",
    port="5432"
)

# cursor
cur = con.cursor()

# query execution
cur.execute("SELECT mov_id, mov_title FROM movie WHERE mov_year<1998 AND mov_lang = 'Japanese';")
movie_info= pd.DataFrame(columns = ['mov_id', 'mov_title'])

table = cur.fetchall()

for r in table:
    output_table_df ={'mov_id':r[0],'mov_title': r[1]}
    movie_info = movie_info.append(output_table_df, ignore_index = True)
print(movie_info)
x=(movie_info['mov_title'])
y=(movie_info['mov_id'])
plt.plot(x,y)
plt.xlabel('mov_title')
plt.ylabel('mov_id')
plt.show()
   

# close the curesor
cur.close()

# close the connection
con.close()
