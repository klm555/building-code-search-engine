#%% OpenAI Embeddings
import os
import pandas as pd
import numpy as np
import openai
from openai import OpenAI

# OpenAI API key
os.environ["OPENAI_API_KEY"] = ""

# text
text = '밑면전단력 어떻게 구함?'

# OpenAI Client
llm = OpenAI()

# Create a new embedding
embeddings = llm.embeddings.create(model='text-embedding-3-small'
                                 , input=text)
result = embeddings.data[0].embedding

# Print
print(embeddings.data[0].embedding[:5]) # vector (only first 5 elements)
print(len(embeddings.data[0].embedding)) # vector size

#%% OpenAI Embeddings with Langchain
from langchain_openai import OpenAIEmbeddings

# Create a new embedding
embed_model = OpenAIEmbeddings(model='text-embedding-3-small') # dimensions(int) : vector size
embeddings = embed_model.embed_query(text)
# embeddings = embed_model.embed_documents([text]) # several docs

# Print
print(embeddings[:5])
print(len(embeddings))
