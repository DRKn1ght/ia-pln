import matplotlib.pyplot as plt
import numpy as np
# Read data from the text file
with open('./stats/tencentStock.txt', 'r') as file:
    lines = file.readlines()

# Initialize lists to store the news labels and sentiment values
news_labels = []
sentiment_values = []
sentiment_values2 = []
# Parse the data from the text file
i = 1
for line in lines:
    if line.strip():  # Skip empty lines
        parts = line.split(':')
        #print(parts)
        if len(parts) == 2:
            news_label = parts[0].strip()
            #print(parts[0].strip())
            #print(parts[0])
            #sentiment_value = float(parts[1])
            news_labels.append(news_label)
            #sentiment_values.append(sentiment_value)
        elif len(parts) == 1:
            # value1, value2 = map(float, parts[1].split('\n'))
            #sentiment_value, sentiment_value2 = map(float(parts[0].split('\n')))
            #sentiment_values.append(sentiment_value)
            sentiment_values.append(float(parts[0]))
            i += 1
print(news_labels)
print(sentiment_values)
print(sentiment_values2)
news_labels.reverse()
sentiment_values.reverse()

# Create a list of colors based on the comparison of values
colors = ['green' if val1 >= val2 else 'red' for val1, val2 in zip(sentiment_values, sentiment_values2)]

# Create a grouped bar plot
width = 0.35
x = np.arange(len(news_labels))
fig, ax = plt.subplots()

plt.plot(news_labels, sentiment_values, marker='o', linestyle='-', color='blue')
# Customize the plot appearance
plt.xlabel('Data')
plt.ylabel('Valor de Mercado')
plt.title('Valor de Mercado Fechado  - Tencent')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
# Show the plot
plt.show()