import pandas as pd
data = pd.io.stata.read_stata('survey.dta')
data.to_csv('survey.csv')

#columns_drop =['studyno', 'doi', 'version', 'edition', 'mode']
#df = df.drop(columns = columns_drop)

print(data['country'])
