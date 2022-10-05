import pandas as pd

from functools import reduce
import xml.etree.ElementTree as ET
import os  
from collections import Counter
import datetime
import numpy 
#functions open files XML´s
def read_xml(file):
    read = ET.parse(file)
    root = read.getroot()
    return root

#Files in to chunks
def chunckify(file,chunks):
    for i in range(0,len(file), chunks):
        yield file[i:i + chunks]

 

#  Get Score by "PostTypeId == 1" Question

def score(file):
    post_id_stack = file.attrib['PostTypeId']
    if post_id_stack== '1':
        post_id = file.attrib['Id']
        post_score = int(file.attrib['Score'])
        change_datetime = datetime.datetime.strptime(file.attrib["CreationDate"], '%Y-%m-%dT%H:%M:%S.%f')
        return post_id, post_score, change_datetime
    
# Get score by "PostTypeId == 2" Answer

def score_2(file):
    post_id_stack = file.attrib['PostTypeId']
    if post_id_stack== '2':
        post_id_2 = file.attrib['ParentId']
        change_datetime_2 = datetime.datetime.strptime(file.attrib["CreationDate"], '%Y-%m-%dT%H:%M:%S.%f')
        return post_id_2, change_datetime_2
    
#Functions Map() ==1
def map_post(data):
    map_date_post = list(map(score, data))
    date_count= Counter(map_date_post)
    return date_count


#Functions Map() ==2
def map_post_2(data):
    map_date_post = list(map(score_2, data))
    date_count= Counter(map_date_post)
    return date_count

# Merge function
def merge_date(D1,D2) :
    D1.update(D2) 
    return D1 

#Reducer questions
def reduce_date(iter):
    reduce_post = reduce(merge_date,iter)
    top100 =reduce_post.most_common(10)
    df = pd.DataFrame(top100, columns=['date', 'count'])
    #delete index 0
    df.drop(df.index[0], inplace=True)
    #create columns for tuple date
    df['post_id'] = df['date'].apply(lambda x: x[0]) 
    df['post_score'] = df['date'].apply(lambda x: x[1])
    df['change_datetime'] = df['date'].apply(lambda x: x[2])
    #delete column date
    df.drop(['date'], axis=1, inplace=True)
    return df

#Reducer Answer
def reduce_date_2(iter):
    reduce_post = reduce(merge_date,iter)
    top100 =reduce_post.most_common(10)
    df2 = pd.DataFrame(top100, columns=['date', 'count'])
    #delete index 0
    df2.drop(df2.index[0], inplace=True)
    #create columns for tuple date
    df2['post_id'] = df2['date'].apply(lambda x: x[0])
    df2['change_datetime'] = df2['date'].apply(lambda x: x[1])
    #delete column date
    df2.drop(['date'], axis=1, inplace=True)
    #calculate unique valor post_id
    return df2
    
# join df and df2
def join_df(df,df2):
    df_join = pd.merge(df, df2, on='post_id', how='inner')
    df_join['time_diff'] = df_join['change_datetime_y'] - df_join['change_datetime_x']
    df_join['time_diff'] = df_join['time_diff'].dt.total_seconds()
    return df_join
    
#main
if __name__ == '__main__': 
    
    #Questions
    read_file = read_xml("posts.xml")
    chunky_data = chunckify(read_file,50)
    Map_data = list(map(map_post, chunky_data))
    df = reduce_date(Map_data)

if __name__ == '__main__': 
    
    #Answer
    read_file = read_xml("posts.xml")
    chunky_data = chunckify(read_file,50)
    Map_data_2 = list(map(map_post_2, chunky_data))
    df2 =reduce_date_2(Map_data_2)