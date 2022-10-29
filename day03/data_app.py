#------------ammar uses CSV file to extract data from--------------
#-------I didn't find the CSV file but i practice the code----------

# import library
import pandas as pd

# import data from file
df = pd.read_csv("[PATH]")
print(df)


# plot countplot using previous code of day02
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)

p = sns.countplot(x='Gender', data=df, hue='Age')
plt.show()