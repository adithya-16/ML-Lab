import csv

data = []

# Print data
with open('Lab-01/enjoysport.csv', 'r') as csvfile:
    for line in csv.reader(csvfile):
        data.append(line)
        print(line)
        
num_attribute = len(data[0])-1
print("\n The initial hypothesis is : ")
hypothesis = ['0'] * num_attribute
print(hypothesis)

for i in range(0, len(data)):
    if data[i][num_attribute] == 'yes':
        for j in range(0, num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == data[i][j]:
                hypothesis[j] = data[i][j]
            else:
                hypothesis[j] = '?'
    print("\n The hypothesis for the training instance {} is :\n" .format(i+1), hypothesis)
    
print("\n The Maximally specific hypothesis for the training instance is ")
print(hypothesis)