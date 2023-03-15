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
cur.execute("SELECT mov_id, mov_title, mov_year FROM movie WHERE mov_title LIKE 'Slumdog%' ORDER BY mov_year;")
movie_details = pd.DataFrame(columns = ['mov_id','mov_title','mov_year'])

table = cur.fetchall()

for r in table:
    output_table_df ={'mov_id':r[0],'mov_title':r[1],'mov_year':r[2]}
    movie_details = movie_details.append(output_table_df, ignore_index = True)
print(movie_details)
x=(movie_details['mov_title'])
y=(movie_details['mov_year'])
plt.plot(x,y,'o')
plt.xlabel('mov_title')
plt.ylabel('mov_year')
plt.show()
   

# close the curesor
cur.close()

# close the connection
con.close()
