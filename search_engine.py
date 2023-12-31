#-------------------------------------------------------------------------
# AUTHOR: Sunjay Guttikonda
# FILENAME: search_engine.py
# SPECIFICATION: Analyze three documents and perform various
# information retrieval tasks and present the results in an organized format
# FOR: CS 4250- Assignment #1
# TIME SPENT: 3.5 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv
from collections import Counter
import math

documents = []
labels = []

#reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      #print(row)
      if i > 0:  # skipping the header
            documents.append (row[0])
            labels.append(row[1])

stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}
#Conduct stopword removal.
#--> add your Python code here
"""counter = [0,1,2,3,4]
with open('collection.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row_number, row in enumerate(reader):
          for col_number, cell in enumerate(row):
              words = cell.split(' ')
              for word_number, word in enumerate(words):
                  if word in stopWords:
                      print(word)"""
csv_file_path = 'collection.csv'  # Path to your CSV file
stopWords = ['I', 'and', 'She', 'They', 'her', 'their']

with open('collection.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

    for i in range(1, len(data)):  # Start from 1 to skip the header
        document = data[i][0]
        # Remove stopwords
        document = ' '.join(word for word in document.split() if word not in stopWords)
        data[i][0] = document

# Write the updated content back to the CSV file
with open('collection.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

"""with open(updated_csv_file_path, 'w', newline='') as csvfile:I
    writer = csv.writer(csvfile)
    writer.writerows(updated_rows)
    for i, row in enumerate(reader):
        print(row)
"""


#Conduct stemming.
#--> add your Python code here
steeming = {
  "cats": "cat",
  "dogs": "dog",
  "loves": "love",
}
for i in range(1, len(data)):  # Start from 1 to skip the header
    document = data[i][0]
    # Apply stemming
    document = ' '.join(steeming.get(word, word) for word in document.split())
    data[i][0] = document

# Write the updated content back to the CSV file
with open('collection.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

#Identify the index terms.
#--> add your Python code here
terms = []
index_terms = set()
for i in range(1, len(data)):  # Start from 1 to skip the header
    document = data[i][0]
    words = document.split()
    index_terms.update(words)

print('Index terms:', index_terms)
counter = 1
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i==0:
          continue
      print('Tokenized d'+ str(counter), ": ", row[0].split())
      counter += 1

#Build the tf-idf term weights matrix.
#--> add your Python code here
docMatrix = []
# Build TF-IDF term weights matrix
tfidf_matrix = []

# Load data from the CSV file
documents = []
labels = []

with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:
            document = row[0]
            documents.append(document)
            labels.append(row[1])

# Calculate TF-IDF
#tf = document.split().count(term) / len(document.split())
#idf = math.log(3 / sum(1 for doc in all_documents if term in doc.split()))
#tfidf = tf * idf

# Calculate TF-IDF term weights matrix
tfidf_matrix = []
#for document in documents:
#    tfidf_document = {term: calculate_tfidf(term, document, documents) for term in document.split()}
#    tfidf_matrix.append(tfidf_document)
#doc1 calcs
d1lovetf = 0
d1lovedf = 3
d1oveidf = math.log(3/3,10)
d1lovetfidf = d1lovetf*d1oveidf
d1cattf = 2/3
d1catidf = math.log(3/2,10)
d1cattfidf = d1cattf*d1catidf
d1dogtf = 0
d1dogidf = math.log(3/2,10)
d1dogtfidf = d1dogtf*d1dogidf
#doc2 calcs
d2lovetf = 0
d2loveidf = math.log(3/3,10)
d2lovetfidf = d2lovetf*d2loveidf
d2cattf = 0
d2catidf = math.log(3/2,10)
d2cattfidf = d2cattf*d2catidf
d2dogtf = 1/2
d2dogidf = math.log(3/2,10)
d2dogtfidf = d2dogtf*d2dogidf
#doc3 calcs
d3lovetf = 0
d3loveidf = math.log(3/3,10)
d3lovetfidf = d3lovetf*d3loveidf
d3cattf = 1/3
d3catidf = math.log(3/2,10)
d3cattfidf = d3cattf*d1catidf
d3dogtf = 1/3
d3dogidf = math.log(3/2,10)
d3dogtfidf = d3dogtf*d1dogidf


#Results
print("\nBelow is the tf-idf term weights matrix:")
print("       love             cat                  dog")
print("doc1   ",float(d1lovetfidf),"   ",float(d1cattfidf),"        ",float(d1dogtfidf))
print("doc2   ",float(d2lovetfidf),"            ",float(d2cattfidf),"          ",float(d2dogtfidf))
print("doc3   ",float(d3lovetfidf),"   ",float(d3cattfidf),"  ",float(d3dogtfidf), "\n")




#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []
userquery = 'cat and dogs'
print('The user query is \"' + userquery + '\"')
userquery = ' '.join(word for word in userquery.split() if word not in stopWords)
userquery = ' '.join(steeming.get(word, word) for word in userquery.split())
splituserquery = userquery.split()
for i in splituserquery:
    if i in stopWords:
        userquery.replace(i, '')
userqueryArray = userquery.split()
binaryQuery = []
tokenizedD3 = ['love', 'dog', 'cat']
for k in tokenizedD3:
    if k == userqueryArray[0] or k == userqueryArray[1]:
        binaryQuery.append(1)
    else:
        binaryQuery.append(0)

print("Tokenized query is ", userquery.split())
print("The binary query is", binaryQuery, "\n")
doc1score = d1lovetfidf+d1cattfidf+d1dogtfidf
doc2score = d2lovetfidf+d2cattfidf+d2dogtfidf
doc3score = d3lovetfidf+d3cattfidf+d3dogtfidf
print("Document 1 score is ", doc1score)
print("Document 2 score is ", doc2score)
print("Document 3 score is ", doc3score, "\n")
retrievedDocs = []
relevantDocs = []
hitDocs = []
missedDocs = []
noise = []
docscoreList = [doc1score, doc2score, doc3score]
maxdocscoreList = max(docscoreList)
if doc1score > 0.1:
    retrievedDocs.append(1)
if doc2score > 0.1:
    retrievedDocs.append(2)
if doc3score > 0.1:
    retrievedDocs.append(3)
relevantCounter = -1
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      relevantCounter += 1
      if str(row[1]) == ' R':
          relevantDocs.append(relevantCounter)
      #print(row[1])
retrievedTotal = 0
relevantTotal = 0
for i in range(0, len(retrievedDocs)):
    #retrievedTotal += retrievedDocs[i]
    #relevantTotal += relevantDocs[i]
    hitDocs.append(int((retrievedDocs[i]+relevantDocs[i])/2))

with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if str(row[0]) == 'Document' or 'love cat cat' or 'love dog' or 'love dog cat':
          continue

with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if str(row[1]) == ' R' or ' I' or ' Label':
          continue

print("Retrieved documents: " + str(retrievedDocs))
print("Relevant documents: " + str(relevantDocs))
print("Hit documents: " + str(hitDocs))
print("Missed documents: ", missedDocs)
print("Noise: ", noise, "\n")

#Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here
precision = (len(hitDocs)/(len(hitDocs)+len(missedDocs)))*100
recall = (len(hitDocs)/(len(hitDocs)+len(noise)))*100
print("The precision: " + str(precision) + "%")
print("The recall: " + str(recall) + "%")