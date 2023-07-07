from langchain import PromptTemplate

general_clustering_template = PromptTemplate(
    input_variables=["clusters", "review", "response_format"],
    template="""
    You are given a review by a user on an e-commerce website, your goal is to classify it (mutli-label) according to the following categories: {clusters}.
    Output would be exactly in this very specific format: {response_format}
    Review: {review}
    Output:
    """
)

extract_key_points_template = PromptTemplate(
    input_variables=["previous_points", "review", "cluster"],
    template="""
    given a user reviews on an e-commerce website, extract the most important points (in least necessary terms of the general {cluster}) only related to this term : {cluster} as it represents the category of all reviews that will be summarized and ignore all information that is not related to {cluster} and avoid being specific about the case or product yet highlight the general information, 

    from previous reviews, these points were extracted, so avoid duplicating information : 
    {previous_points}

    the points should be given in a very concise way(the fewest necessary) in least amount of terms(nominal simple phrase) in following format:
    - key point i

    review : {review}
    Key points :
    """
)
