import sqlite3

with sqlite3.connect("blog.db") as connection :
    c= connection.cursor()
    data= [("Good","I\'m good."),
    ("Well","I\'m well."),
    ("Excellent","I\'m excellent."),
    ("Okay","I\'m okay.")
    ]
    c.execute("CREATE TABLE posts(title TEXT, post TEXT)")
    c.executemany("INSERT INTO posts VALUES(?,?)",data)
