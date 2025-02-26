from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools
from tools.website_scraper_tools import CrawlWebsiteTools
#from tools.calculator_tools import CalculatorTools


class ESGAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        

    def esg_news_reporter(self):
        return Agent(
            role="Expert report writer",
            backstory=dedent(
                f"""You are the manager of the crew. Expert in writing concise and informative reports and memos for the chief sustainability officer, You will rely on other agents to get content for your report"""),
            goal=dedent(f"""
                        IMPORTANT, First thing to do: You will ask other agents (ESG News researcher) to give you a list of news, then you will ask a detailer agent (Expert ESG News Summariser) to read the content of the most relevant links and summarise them for you.
                        Create a comprehensive ESG news report from the daily news provided, focusing on banks. The report could include the Net zero banking alliance developments,
                        the latest ESG trends, and the impact of ESG on the banking sector. It could also cover te latest ESG developments of Societe Generale's peers and competitors. If the elements provided are not enough you can ask other agents to search the internet for more news with better keywords.
                        Only you can write the final report.
                        """),
            allow_delegation=True,
            tools=[],
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
                f"""You are looking for news that might interest the chief sustainability officer of the bank. Find the most relevant and important ESG daily news for the finance industry, focusing on banks, other financial institutions, Net zero banking alliance, highly emissive sectors, and the competitors of Societe Generale."""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    def esg_news_detailer(self):
        return Agent(
        role="Expert ESG News Summariser",
        backstory=dedent(
            f"""Expert in reading news articles and summarising them in a concise and informative manner."""),
        goal=dedent(f"""
                   You goal is to read the articles sent to you and summarise them in a manner that is concise and informative. You will then send them to the Expert Report writer for him to continue the process."""),
        tools=[CrawlWebsiteTools.scrape_website],
        verbose=True,
        llm=self.OpenAIGPT35,
        )