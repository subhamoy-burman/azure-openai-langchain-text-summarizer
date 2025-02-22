import os
from dotenv import load_dotenv

load_dotenv()
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
from tools.tools import get_profile_url_tavily


def lookup (name: str) -> str:
    llm = AzureChatOpenAI(
        temperature=0,
        openai_api_key=os.environ['OPENAI_API_KEY'],
        openai_api_version="2024-08-01-preview",  # Specify API version
        azure_endpoint=os.environ['OPENAI_API_BASE'],
        azure_deployment="gpt-4o",
        model="gpt-4o"
    )

    template = """ given the full name {name} of a person I want you to find their LinkedIn profile URL.
    Your answer should only be a single valid LinkedIn URL.
    """

    prompt_template = PromptTemplate(input_variables=["name"], template=template)

    tools_for_agent = [ Tool( name = "Crawl Google for linkedin profile page",
                              func=get_profile_url_tavily,
                              description="useful for when you want to find a LinkedIn profile page for a person") ]
    
    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        tools = tools_for_agent,
        prompt= react_prompt,
        llm = llm
    )

    agent_executor = AgentExecutor(agent = agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input": prompt_template.format_prompt(name=name)})

if __name__ == "__main__":
    linkedin_url = lookup(name = "Bill Gates")
    print(linkedin_url)