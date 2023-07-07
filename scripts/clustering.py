def general_clustering(user_clusters, response_format, df_reviews, chain):
    """ clustering your reviews according to user-defined clusters

    Args:
        user_clusters (list[str]): list of clusters names
        response_format (string): constraints on the LLM output 
        df_reviews (pd.DataFrame): the reviews dataframe
        chain (langchain.LLMChain): the prompt chain

    Returns:
        pd.Dataframe: a modified version of the the input dataframe adding the clusters columns
    """
    general_cluster_name = []
    general_cluster_oh = []
    for review in df_reviews["review"]:
        predicted_cluster = chain.run(clusters=user_clusters, review=review, response_format=response_format).strip().split(" ")
        print(f"predictd : {predicted_cluster}")
        
        clusters_name = [cluster[:-2] for cluster in predicted_cluster if cluster[-1]=="1"]
        print(f"clusters_name : {clusters_name}")
        
        clusters_oh = [int(cluster[-1]) for cluster in predicted_cluster]
        print(f"clusters_oh : {clusters_oh}")
        
        general_cluster_name.append(clusters_name)
        general_cluster_oh.append(clusters_oh)
        
        
    df_reviews["general_clusters_name"] = general_cluster_name
    for i, cluster in enumerate(user_clusters):
        df_reviews[cluster] = [1 if cluster_oh[i]==1 else 0 for cluster_oh in general_cluster_oh ]

    return df_reviews
        