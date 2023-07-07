import os
from scripts.credentials import OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

import pandas as pd

from langchain.llms import OpenAI
from langchain.chains import LLMChain

from scripts.prompts import general_clustering_template
from scripts.clustering import general_clustering
from scripts.summarize import extract_key_points, summarize_key_points
from scripts.chains import extract_key_points_chain, general_clustering_chain, summarize_key_points_chain

llm = OpenAI(temperature=0)
chain = LLMChain(llm=llm, prompt=general_clustering_template)

user_clusters = ["Complaints", "Complements", "Requests"]
response_format = (':0 ').join(user_clusters)
sample_review = "I am deeply disappointed with the performance and reliability of this GPU. Despite its promising specifications, it consistently underperforms and fails to meet my expectations. I have encountered frequent crashes, driver issues, and screen artifacts that hinder my gaming and graphic-intensive tasks. The GPU's cooling system seems inadequate, leading to overheating problems even during moderate usage. Overall, this GPU has been a frustrating and unreliable investment, and I cannot recommend it to others."

df_reviews_gpt = pd.read_csv("./data/extended_commerce_reviews_minimal.csv")
df_reviews_amazon = pd.read_csv("./data/reviews_minimal.csv")

df_reviews_amazon_complaints = pd.read_csv("./data/amazon_dataset_classified.csv").loc[:10]

response = extract_key_points(df_reviews=df_reviews_amazon_complaints, chain=extract_key_points_chain, cluster="Complaints")

# response = general_clustering(df_reviews=df_reviews_amazon, user_clusters=user_clusters, response_format=response_format, chain=general_clustering_chain)

# response.to_csv("./data/amazon_dataset_classified.csv", index=False)

with open("./data/key_points_compalints.txt", "w+") as f:
    f.write("Key points : ")
    f.write(response)

print(f"The key points : {response}")

print("\n")

summary = summarize_key_points(key_points=response, chain=summarize_key_points_chain, cluster="Complaints")

with open("./data/key_points_compalints.txt", "w+") as f:
    f.write("Summary : ")
    f.write(summary)

print(f"The summarization: {summary}")
