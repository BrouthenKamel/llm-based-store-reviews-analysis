from langchain import PromptTemplate

# The module is concerned of building and enginnering LLM prompts

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
    given a user review on an e-commerce website, extract the most important points only related to this category: {cluster} ignore all information that is not related to {cluster} and avoid being specific about the case or product but highlight the general information (at most 2 to 3 key insightful information), 

    from previous reviews, these key points were extracted, keep attention on them so avoid duplicating information : 
    {previous_points}

    the points should be given in a very concise way, insightful, non-specific, striaight to the point and most importantly strongly related to {cluster}, in the following format:
    - key point i

    review : {review}
    Key points :
    """
)

summarize_key_points_template = PromptTemplate(
    input_variables=["key_points", "cluster"],
    template="""
    given important key points extracted from user reviews on e-commerce website related to {cluster}, that are the following : {key_points}
    summarize the given key points in an insightful way through a paragraph which will be either held to the customer service team, displayed on a dashboard for the business in order to get an overview of the key information concerning {cluster} around the business and help promote the busness goals.
    Report: 
    """
)
