import numpy as np

with open('./stats/tencentStock.txt', 'r') as file:
    lines2 = file.readlines()

with open('./stats/tencentFixedGPT.txt', 'r') as file:
    lines1 = file.readlines()

# Initialize lists to store the news labels and sentiment values
news_labels = []
sentiment_values = []
close_values = []
close_values2 = []
# Parse the data from the text file
i = 1
for line in lines1:
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

i = 1
for line in lines2:
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
            close_values2.append(float(parts[0]))
    

print(news_labels)
print(sentiment_values)
print(close_values2)
sentiment_values.reverse()
close_values2.reverse()

# Calculate the correlation coefficient for the overlapping data points
correlation_coefficient = np.corrcoef(sentiment_values, close_values2)[0, 1]

# Display the correlation coefficient
print(f"Correlation Coefficient: {correlation_coefficient:.2f}")