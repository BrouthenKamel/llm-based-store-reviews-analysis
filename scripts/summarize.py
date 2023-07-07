
def extract_key_points(df_reviews, chain, cluster):
    previous_points = ""
    for review in df_reviews.values:
        previous_points += chain.run(review=review, previous_points=previous_points, cluster=cluster)
        
    return previous_points

def summarize_key_points(key_points, chain, cluster):
    return chain.run(key_points=key_points, cluster=cluster)
    