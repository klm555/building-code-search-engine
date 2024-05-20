import os
import pandas as pd
import numpy as np
import openai
from openai import OpenAPI
from langchain_openai import OpenAIEmbeddings

# OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# text
text = 'Hello World'

# Embedding Model
embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
