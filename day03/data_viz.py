# Steps involve in data visualization
# Step 1: import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: setup a theme
sns.set_theme(style="ticks", color_codes=True)

# Step 3: import dataset (we can import our own dataset)
kashti = sns.load_dataset("titanic")
# print(kashti)

# Step 4: plot basic count graph with 1 variables (count)
p= sns.countplot(x = "sex", data=kashti)
plt.show()

# Step 5: plot basic count graph with 2 variables (count plot)
p= sns.countplot(x = "sex", data=kashti, hue='class')
p.set_title("Count plot")
plt.show()

