from sklearn.feature_extraction.text import *
data = ['My name is ronak',
        'All is this ronak',
        'your name is me',
        ]
Vector = CountVectorizer()
counts = Vector.fit_transform(data)
print(Vector.vocabulary_)
print(counts.toarray())