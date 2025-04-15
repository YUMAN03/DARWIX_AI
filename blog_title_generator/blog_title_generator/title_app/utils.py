from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

def generate_title_suggestions(c):
    """
    Generate title suggestions based on the provided content.
    
    Args:
        content (str): The blog post content
        
    Returns:
        list: A list of suggested titles
    """
    # Title generation logic would go here
    # For now, we'll return placeholder titles
    
    # This is where you would implement your title generation algorithm
    # The function takes the content as input and returns a list of titles
    
    # Placeholder return
    l = []
    groq_api_key='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'

    llm = ChatGroq(temperature=0.5, groq_api_key=groq_api_key, model='llama3-70b-8192')

    template1 = "Generate 1 single catchy blog title based on the content: {content} \n to not give any opening or any ending remarks, just give the title"

    prompt1 = PromptTemplate.from_template(template1)

    llm_chain = prompt1 | llm
    for i in range(3):
        prepropq = (llm_chain.invoke({"content":c}).content)
        l.append(prepropq)
    return l