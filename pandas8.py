import pandas as pd

def age_18_to_30(a):
    return 18<=a<30

def level_a(s):
    return 85<=s<=100

Students = pd.read_excel('C:/Temp/Students.xlsx',index_col='ID')
# Students = Students.loc[Students['Age'].apply(age_18_to_30)].loc[Students['Score'].apply(level_a)]  #loc多重过滤
Students = Students.loc[Students.Age.apply(lambda a:18<=a<30)] \
    .loc[Students.Score.apply(lambda s:85<=s<=100)]  #loc多重过滤
print(Students)