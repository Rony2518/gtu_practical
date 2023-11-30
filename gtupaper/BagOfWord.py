import nltk
from nltk.tokenize import word_tokenize
import pandas as pd
# nltk.download('punkt')  # Download the punkt tokenizer data (only required once)

text = "This is an example sentence for tokenization."
tokens = word_tokenize(text)
print(tokens)


