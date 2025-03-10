#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().system('pip install mysql-connector-python')


# In[10]:

import mysql.connector

def connect_db():
    c = mysql.connector.connect(
        host="bnzaupzpdfrwncuael3m-mysql.services.clever-cloud.com",
        port="3306",
        user="uwr0cftsf6pb8a5q",
        password="JlaFlg6E4keN5rlfCQph",
        database="bnzaupzpdfrwncuael3m"
    )
    
    return c

def create_tables():
    c = connect_db()
    cursor = c.cursor()
    
    # Create table if not exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_query TEXT,
        search_type VARCHAR(10),
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    c.commit()
    cursor.close()
    c.close()

# Run function to create table
create_tables()


# In[ ]:




