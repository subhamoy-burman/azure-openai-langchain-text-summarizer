import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
from linkedin_scrapper import scrape_linkedin_profile
from linkedin_lookup_agent import lookup as linkedin_lookup_agent
# For loading environment variables
load_dotenv()


def ice_break_with_linkedin_profile(name:str) -> str:
    linkedin_profile_url = linkedin_lookup_agent(name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url, mock=True)

    summary_template = """
    given the linkedIn information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = AzureChatOpenAI(
        temperature=0,
        openai_api_key=os.environ['OPENAI_API_KEY'],
        openai_api_version="2024-08-01-preview",  # Specify API version
        azure_endpoint=os.environ['OPENAI_API_BASE'],
        azure_deployment="gpt-4o",
        model="gpt-4o"
    )

    chain = summary_prompt_template | llm
    result = chain.invoke(input={"information": linkedin_data})

    print(result)
    return result

if __name__ == "__main__":
    print("Hello LangChain!")
    load_dotenv()
    ice_break_with_linkedin_profile("Bill Gates")


    
    
    # llm = AzureChatOpenAI(
    #     temperature=0,
    #     openai_api_key=os.environ['OPENAI_API_KEY'],
    #     openai_api_version="2024-08-01-preview",  # Specify API version
    #     azure_endpoint=os.environ['OPENAI_API_BASE'],
    #     azure_deployment="gpt-4o",
    #     model="gpt-4o"
    # )

    # Use Ollama with local Deepseek model
    # llm = ChatOllama(
    #     model="llama3:8b",
    #     base_url="http://localhost:11434",  # Default Ollama URL
    #     temperature=0
    # )


    # chain = summary_prompt_template | llm
    # linkedin_data = scrape_linkedin_profile("https://www.linkedin.com/in/williamhgates/", mock=True)
    # result = chain.invoke(input={"information": linkedin_data})

    # print(result)
