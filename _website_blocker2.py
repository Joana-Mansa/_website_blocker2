#!/usr/bin/env python
# coding: utf-8

# In[3]:


# run script as root

import time
from datetime import datetime as dt


# In[10]:


# change hosts path 
# this part is perculiar to ones OS
# mine is Linux

hosts_path = '/etc/hosts'

# localhost's IP
redirect = "127.0.0.1"


# websites that we want to block
website_list = ['wwww.facebook.com', 'facebook.com']


# In[11]:


while True:
    
    # time of work
    if dt(dt.now().year, dt.now().month, dt.now().day,8)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    # mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                    
                # removing hostnames from host file
                file.truncate()
                
        print("Fun hours...")
        time.sleep(5)
    


# In[ ]:




