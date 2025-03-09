#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().system('pip install mysql-connector-python')


# In[10]:


import mysql.connector

def connect_db():
    # Step 1: Connect to MySQL without specifying a database
    c = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bj2003@27"
    )
    
    cursor = c.cursor()
    
    # Step 2: Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS search_recommend_db")
    cursor.close()
    c.close()
    
    # Step 3: Connect to the newly created/existing database
    c = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bj2003@27",
        database="search_recommend_db"  #  Corrected spelling
    )
    
    return c

def create_tables():
    c = connect_db()
    cursor = c.cursor()
    
    # Step 4: Create the table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_data(
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_query TEXT,
        search_type VARCHAR(10),
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    c.commit()  # Commit the changes
    cursor.close()  # Close the cursor
    c.close()  #  Close the connection

# Run the function to create the database and tables
create_tables()


# In[ ]:




