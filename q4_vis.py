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
cur.execute("SELECT DISTINCT mov_title,mov_id FROM movie WHERE mov_id IN (SELECT mov_id FROM movie WHERE mov_id NOT IN (SELECT mov_id FROM Rating));")
movie_details = pd.DataFrame(columns = ['mov_title','mov_id'])

table = cur.fetchall()

for r in table:
    output_table_df ={'mov_title':r[0],'mov_id':r[1]}
    movie_details = movie_details.append(output_table_df, ignore_index = True)
print(movie_details)
x=(movie_details['mov_title'])
y=(movie_details['mov_id'])
plt.plot(x,y)
plt.xlabel('mov_title')
plt.ylabel('mov_id')
plt.show()   

# close the curesor
cur.close()

# close the connection
con.close()
