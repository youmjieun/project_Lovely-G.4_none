# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

data={'name':['Jerry', 'Rich', 'Paul'],
      'algol':["A", "A+", "B"],
      'basic':["C", "B", "B+"],
      'C++':["B+", "C", "C+"],
      }

df=pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

df.to_excel("./df_sample.xlsx")