import pandas as pd

df = pd.DataFrame({'ID':[1,2,3],'Name':['Tim','Victor','Nick']})
df = df.set_index('ID')
print(df)
df.to_excel('c:/Temp/output.xlsx')
print('Done!')