#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict
import random
import faker
import datetime
import re

fake = faker.Faker()


# ## Schools
# 
# https://www.harvard.edu/schools

# In[3]:


with open("Schools.txt") as f:
    schools = f.read().split("\n")[:-2]
    
schools


# In[ ]:





# In[42]:


def random_date():
    d = str(random.randint(1,28)).zfill(2)
    m = str(random.choice("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split()))
    y = str(random.randint(1995,2017)).zfill(2)
    
    return f"{d}-{m}-{y}"


# In[82]:


for i, school in enumerate(schools):
    print(f"INSERT INTO TABLE SCHOOL (ID , SCHOOL_NAME, FOUNDING_DATE) \n\t({i+1}, '{school}', '{random_date()}')")


# ## MODULE

# In[94]:


for i in range(1, 51):
    print(f"INSERT INTO TABLE MODULE VALUES ({i}, 'MODULE_{i}');")


# ## TUTOR

# In[58]:


tutor_titles = ['Associate Lecturer',
  'Lecturer',
  'Senior Lecturer',
  'Associate Professor',
  'Professor']

def random_birthdate():
    d = str(random.randint(1,28)).zfill(2)
    m = str(random.choice("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split()))
    y = str(random.randint(1965,1985)).zfill(2)
    
    return f"{d}-{m}-{y}"


# In[96]:


for i in range(1, 51):
    # 10% of values have no city  (should be defaulted)
    add = re.sub('\n', ', ', fake.address())
    if i % 10 == 3:
        
        print(f"INSERT INTO TABLE TUTOR VALUES ({i}, '{random.choice(tutor_titles)}', '{fake.first_name()[:30].upper()}', '{fake.last_name()[:30].upper()}', '{add[:100]}', '{fake.city()[:50]}', '{fake.postalcode()[:5]}', '{fake.phone_number()[:30]}', '{fake.email()[:100]}', '{random_birthdate()}');")
    # 10% of values have neither
    else:
        print(f"INSERT INTO TABLE TUTOR VALUES ({i}, '{random.choice(tutor_titles)}', '{fake.first_name()[:30].upper()}', '{fake.last_name()[:30].upper()}', '{add}', '{fake.city()[:50]}', '{fake.postalcode()[:5]}', '{fake.phone_number()[:30]}', '{fake.email()[:100]}', '{random_birthdate()}', 'OFFICE {i%10+1}');")


# ## BOOK

# In[97]:


s = ""
isbns = []
for book in range(1, 501):
    curr_isbn = fake.isbn13()
    isbns.append(curr_isbn)
    ss = f"INSERT INTO TABLE BOOK VALUES ('{curr_isbn}', '{fake.sentence(5)[:100]}', '{fake.name().upper()[:100]}', '{random_date()}');"
    s = s + "\n" + ss


# In[98]:


with open("fff.txt", 'w') as f:
    f.write(s)


# 
# ## Courses

# In[99]:


s = ""
for i in range(1, 101):
    ss = f"INSERT INTO TABLE COURSE VALUES ({i}, 'Course {i}', '{fake.name().upper()[:100]}', '{random_date()}', {random.randint(1,13)});"
    # up to 13 schools
    s = s + "\n" + ss
    
with open("fff.txt", 'w') as f:
    f.write(s)


# ## COPY

# In[100]:


s = ""
# for every book we have
copies = []
for i in range(len(isbns)):
    # for every copy (which ranges from 1 to 6 copies per book)
    for j in range(1, random.randint(2,6)):
        c = f"{isbns[i]}_{str(j).zfill(3)}"
        copies.append(c)
        ss = f"INSERT INTO TABLE COPY VALUES ('{c}', '{isbns[i]}');"
    # up to 13 schools
        s = s + "\n" + ss
#     print(ss)
    
with open("fff.txt", 'w') as f:
    f.write(s)


# In[51]:


len(isbns)


# In[49]:


len(f"{isbns[i]}_{str(j).zfill(3)}")


# ## Student

# In[60]:


student_title = ['MRS',
  'MISS',
  'MR',
  'DR']

def random_birthdate():
    d = str(random.randint(1,28)).zfill(2)
    m = str(random.choice("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split()))
    y = str(random.randint(1985,1998)).zfill(2)
    
    return f"{d}-{m}-{y}"


# In[86]:


import re


# In[93]:


s = ""
# for every book we have
for i in range(1, 1001): 
    add = re.sub('\n', ', ', fake.address())
    if i % 10 == 3:
    # 10% of students have no contact number
        ss = f"INSERT INTO TABLE STUDENT (ID , TITLE, FIRST_NAME, LAST_NAME, ADDRESS, CITY, POSTCODE, COUNTRY, EMAIL, BIRTHDAY) VALUES ({i}, '{random.choice(student_title)}', '{fake.first_name()[:30].upper()}', '{fake.last_name()[:30].upper()}', '{add[:100]}', '{fake.city()[:50]}', '{fake.postalcode()[:5]}', '{fake.country()[:30]}', '{fake.email()[:100]}', '{random_birthdate()}');"
    elif i % 10 == 5:
        
    # 10% of students have no country
        ss = f"INSERT INTO TABLE STUDENT (ID , TITLE, FIRST_NAME, LAST_NAME, ADDRESS, CITY, POSTCODE, CONTACT_NUMBER, EMAIL, BIRTHDAY) VALUES ({i}, '{random.choice(student_title)}', '{fake.first_name()[:30].upper()}', '{fake.last_name()[:30].upper()}', '{add[:100]}', '{fake.city()[:50]}', '{fake.postalcode()[:5]}', '{fake.phone_number()[:30]}', '{fake.email()[:100]}', '{random_birthdate()}');"
    else:
        ss = f"INSERT INTO TABLE STUDENT (ID , TITLE, FIRST_NAME, LAST_NAME, ADDRESS, CITY, POSTCODE, COUNTRY, CONTACT_NUMBER, EMAIL, BIRTHDAY) VALUES ({i}, '{random.choice(student_title)}', '{fake.first_name()[:30].upper()}', '{fake.last_name()[:30].upper()}', '{add[:100]}', '{fake.city()[:50]}', '{fake.postalcode()[:5]}', '{fake.country()[:30]}', '{fake.phone_number()[:30]}', '{fake.email()[:100]}', '{random_birthdate()}');"
    s = s + "\n" + ss
#     print(ss)
    
with open("fff.txt", 'w') as f:
    f.write(s)


# ## COURSE_MODULE
# 
# * 50 modules
# * 100 courses

# In[102]:


for module in range(1, 201):
    # id, course_id (1-100), module_id (1-50)
    print(f"INSERT INTO TABLE COURSE_MODULE VALUES ({module}, {random.randint(1,100)}, {random.randint(1,50)});")


# #### A module can be taught in many courses, so use random.choice (with replacement). Also loop over ALL courses and make many random choices

# ## ASSESSMENT

# In[103]:


s = ""
for i in range(1, 501):
    # pick randomly one course_module
    ss = f"INSERT INTO TABLE ASSESSMENT VALUES ({i}, {random.randint(1,200)});"
    s = s + "\n" + ss
#     print(ss)
    
with open("fff.txt", 'w') as f:
    f.write(s)


# ## STUDENT_ASSESSMENT

# In[104]:


s = ""
for i in range(1, 1001):
    # assessment_id (range 1-500), student_id (range 1-1000)
    ss = f"INSERT INTO TABLE STUDENT_ASSESSMENT VALUES ({random.randint(1,500)}, {random.randint(1,1000)}, {random.randint(0,100)});"
    s = s + "\n" + ss
#     print(ss)
    
with open("fff.txt", 'w') as f:
    f.write(s)


# ## LOAN

# In[72]:


def random_loandate():
    d = str(random.randint(1,28)).zfill(2)
    m = str(random.choice("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split()))
    y = str(random.randint(2007,2018)).zfill(2)
    
    return f"{d}-{m}-{y}"


# In[105]:


s = ""

for i in range(1, 2001):
    # 20% of books have no return dates
    if i % 5 == 0:
        
        ss = f"INSERT INTO TABLE LOAN VALUES ({i}, {random.randint(1,1000)}, {random.randint(1,50)}), '{random.choice(copies)}', '{random_loandate()}');"

    else:
        ss = f"INSERT INTO TABLE LOAN VALUES ({i}, {random.randint(1,1000)}, {random.randint(1,50)}, '{random.choice(copies)}', '{random_loandate()}', '{random_loandate()}');"
    
    s = s + "\n" + ss
#     print(ss)
    
with open("fff.txt", 'w') as f:
    f.write(s)


# ## TUTOR_C_MODULE

# In[106]:


s = ""
for i in range(1, 300):
    # assessment_id (range 1-500), student_id (range 1-1000)
    ss = f"INSERT INTO TABLE TUTOR_C_MODULE VALUES ({random.randint(1,50)}, {random.randint(1,200)});"
    s = s + "\n" + ss
    print(ss)
    
with open("fff.txt", 'w') as f:
    f.write(s)


# In[ ]:




