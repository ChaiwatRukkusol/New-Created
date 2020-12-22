import pandas as pd
import numpy as np

df  = pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')[0]
df = df[df['Borough'] != 'Not assigned'].reset_index(drop=True)
df.head(15)
