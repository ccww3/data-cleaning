###load into dataframe
import pandas as pd
path = r"C:\Users\cw83\Desktop\水彩颜料.xlsx"
df = pd.read_excel(path, sheetname='data')
print (df)
###if lname already populated, leave it alone; otherwise combine fname and lname then select 1: as lname
# df1 = df.lname1.isnull()
# print (df1)
# print ((df.fname1.fillna('') + ' ' + df.lname1.fillna('')).apply(lambda x: str(x).split()[0]))
# print (df['lname1'][df.lname1.isnull()==True])
# print (df['fname1'].apply(lambda x: str(x).split()[0]))
# print (df['fname1'].apply(lambda x: ' '.join(str(x).split()[1:])))
df1 = df.copy()
df['fname1'][df.lname1.isnull()& df.fname1.notnull()] = df.fname1.apply(lambda x: str(x).split()[0])
df['lname1'][df.lname1.isnull()& df.fname1.notnull()] = (df1.fname1.apply(lambda x: ' '.join(str(x).split()[1:])))

df['fname2'][df.lname2.isnull() & df.fname2.notnull()] = df.fname2.apply(lambda x: str(x).split()[0])
df['lname2'][df.lname2.isnull() & df.fname2.notnull()] = (df1.fname2.apply(lambda x: ' '.join(str(x).split()[1:])))

print (df)

### to get mname from lname
import re
regex = re.compile('. ')
l1 = df.lname1[df.lname1.notnull()].tolist()
l2 = df.lname2[df.lname2.notnull()].tolist()
matches1 = [string for string in l1 if re.match(regex,string)]
matches2 = [string for string in l2 if re.match(regex,string)]

df.mname1[df.lname1.isin(matches1)]=[string.split()[0] for string in l1 if re.match(regex,string)]
df.mname2[df.lname2.isin(matches2)]=[string.split()[0] for string in l2 if re.match(regex,string)]
df['lname1'][df.lname1.isin(matches1)] = df.lname1[df.lname1.notnull()].apply(lambda x: x[1:])
df['lname2'][df.lname2.isin(matches2)] = df.lname2[df.lname2.notnull()].apply(lambda x: x[1:])
print (df)
