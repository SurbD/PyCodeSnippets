import os
import sqlite3

# You need to make this a context generator class so you can call the methods

basedir = os.path.abspath(os.path.dirname(__file__))
os.chdir(basedir)

conn = sqlite3.connect('videos.db')
c = conn.cursor()

def start_db():
    try:
        c.execute("SELECT * FROM videos")
    except:
        create_table()
        print("New Table Created")
    else:
        table = c.fetchall()
        print(table)
    

def create_table():
    c.execute("""CREATE TABLE videos (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              NAME            TEXT      NOT NULL,
              VIEWS           INTEGER   NOT NULL,
              LIKES           INTEGER   NOT NULL
    )""")

def get_video_data(video_id):
    c.execute("SELECT * FROM videos WHERE id=:video_id", {'video_id': video_id})
    return c.fetchall()

def insert_video(video):
    with conn:
        c.execute("INSERT INTO videos(name, views, likes) VALUES (:name, :views, :likes)", {'name':video['name'], 'views':video['views'], 'likes':video['likes']})

# start_db()

# data = {
#     'name': 'Peter',
#     'views': 110555,
#     'likes': '34400'
# }

# insert_video(data)
print(get_video_data(2))

conn.close()
