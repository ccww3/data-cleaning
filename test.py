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

fullname = df.fname1.fillna('') + [' '] + df.lname1.fillna('')
print (fullname)
df['fname1'][df.lname1.isnull()] = fullname.apply(lambda x: str(x).split()[0])
df['lname1'][df.lname1.isnull()] = fullname.apply(lambda x: x[len(str(x).split()[0]):])

# [df.fname1 + [''] + df.lname1][df.lname1.isnull()] = [df.fname1 + [''] + df.lname1]
print (df)

### to get mname from lname
import re
regex = re.compile('. ')
l = df.lname1.tolist()
print (l)
matches = [string for string in l if re.match(regex,string)]
# print (matches)
df.mname1[df.lname1.isin(matches)]=[string.split()[0] for string in l if re.match(regex,string)]
df['lname1'][df.lname1.isin(matches)] = df.lname1.apply(lambda x: x[len(str(x).split()[0]):])
print (df)
