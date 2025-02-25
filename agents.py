from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools
#from tools.calculator_tools import CalculatorTools


class ESGAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        

    def esg_news_reporter(self):
        return Agent(
            role="Expert ESG News Reporter",
            backstory=dedent(
                f"""Expert in writing concise and informative ESG daily news reports for financial institutions, knows the latest trends and developments in the ESG sector"""),
            goal=dedent(f"""
                        Create a comprehensive ESG news report from the daily news for the finance industry, focusing on banks. The report could include the NZBA developments,
                        the latest ESG trends, and the impact of ESG on the banking sector. It could also cover te latest ESG developments of Societe Generale's peers and competitors.
                        """),
            tools=[
                SearchTools.search_internet,
            ],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def esg_news_researcher(self):
        return Agent(
            role="ESG News Researcher",
            backstory=dedent(
                f"""Expert at reading the daily ESG news and identifying the most relevant and important news for the finance industry,
                 focusing on banks. An employee at Societe Generale, with a keen interest in ESG news and developments.
                 """),
            goal=dedent(
                f"""Find the most relevant and important ESG daily news for the finance industry, focusing on banks, other financial institutions, NZBA, and the competitors of Societe Generale.
                If there are any news about Societe Generale, a summary of those news should be included in the report."""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT35,
        )
