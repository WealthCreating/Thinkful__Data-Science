'''
Using selected questions from the 2012 and 2014 editions of the European Social Survey, address the following questions.

1.  Did people become less trusting from 2012 to 2014? Compute results for each country in the sample.
'''
import numpy as np
import pandas as pd
import os

df = pd.read_csv('C:/Users/18047/Documents/Main/5 Algorithms, scraping, and big data/Challenges/3 dataset.csv')
df2012 = df.loc[df['year'] == 6]
df2014 = df.loc[df['year'] == 7]
ppltrst2012 = df2012.groupby('cntry')['ppltrst'].mean()
ppltrst2014 = df2014.groupby('cntry')['ppltrst'].mean()
print(ppltrst2014 - ppltrst2012)

'''2. Did people become happier from 2012 to 2014? Compute results for each country in the sample.'''
happy2012 = df2012.groupby('cntry')['happy'].mean()
happy2014 = df2014.groupby('cntry')['happy'].mean()
print(happy2014 - happy2012)

'''3. Who reported watching more TV in 2012, men or women?'''
print(df2012.groupby('gndr')['tvtot'].mean())

'''4. Who was more likely to believe people were fair in 2012, people living with a partner or people living alone?'''
print(df2012.groupby('partner')['pplfair'].mean())

'''5. Pick three or four of the countries in the sample and compare how often people met socially in 2014.
	  Are there differences, and if so, which countries stand out?'''
countries = ['CZ', 'DE', 'NO']
social2014 = df2014.loc[df2014['cntry'].isin(countries)]
print(social2014.groupby('cntry')['sclmeet'].mean())

'''6. Pick three or four of the countries in the sample and compare how often people took part in social activities,
	  relative to others their age, in 2014. Are there differences, and if so, which countries stand out?'''
