import sqlite3
import streamlit as st


# Connect to database
conn = sqlite3.connect('example.db')

# Create table
conn.execute('CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)')

# Insert a row of data
conn.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# Query the database
cursor = conn.execute("SELECT * FROM stocks")

for row in cursor:
    #print(row)
    st.write(row)

# Close the connection
conn.close()
