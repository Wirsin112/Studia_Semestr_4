import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


df2 = pd.read_csv("supermarket.csv")
del df2["total"]
df2 = df2.mask(df2 == "?",0)
df2 = df2.mask(df2 == "t",1)



print(df2)
czeste = apriori(df2, min_support=0.35, use_colnames=True)
print(czeste)
reguly = association_rules(czeste, metric="confidence", min_threshold=0.8)
print(reguly)