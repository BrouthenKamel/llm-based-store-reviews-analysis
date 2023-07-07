
def extract_key_points(df_reviews, chain, cluster):
    """extract key information from users reviews

    Args:
        df_reviews (pd.DataFrame): the reviews dataframe
        chain (langchain.LLMChain): the prompt chain
        cluster (string): user defined cluster

    Returns:
        string: LLM output
    """
    previous_points = ""
    for review in df_reviews.values:
        previous_points += chain.run(review=review, previous_points=previous_points, cluster=cluster)
        
    return previous_points

def summarize_key_points(key_points, chain, cluster):
    """summarize the key points of the reviews into a comprehensible paragraph

    Args:
        key_points (string): reviews important infos
        chain (langchain.LLMChain): the prompt chain
        cluster (string): user defined cluster

    Returns:
        string: insights paragraph
    """
    return chain.run(key_points=key_points, cluster=cluster)
    