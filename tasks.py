from crewai import Task
from textwrap import dedent

class ESGTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def write_esg_report(self, agent, date, interests):
        return Task(
            description=dedent(
                f"""
                **Task**: Develope a Comprehensive ESG Report
                **Description**: Write a comprehensive ESG report based on today's news, focusing on the finance industry,
                covering the latest trends, developments, targets published by other banks, and political news impacting ESG and financial institutions.
                The report should look like a morning digest for the chief sustainability officer of Societe Generale. It should be storytelling and pleasurable to read. If any additional intrests are provided, the report should include those as well, but make sure to only include information related to ESG.
                If Societe Generale has been mentioned negatively in a news article, this should be highlited.
                If any competitor, such as BNP, Credit Agricole, or La Banque postale or any other NZBA bank, is mentioned positively or negatively, this should also be highlighted.
                Include read more links to the original articles so that the CSO can read more if they want to.
              **Parameters**: 
             - Today's Date: {date}
             - Additional Interests: {interests}
                **Note**: {self.__tip_section()}
             """
            ),
            expected_output="The daily digest will be a short read about what the news say about ESG, focusing on financial institutions and Societe Generale.",
            agent=agent,
        )

    
    def gather_news(self, agent, date, interests):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Gather The Daily ESG News from the Internet
                    **Description**: Search the internet and collect the latest news on ESG, focusing on the finance industry. 
                    You should focus on news that is relevant to Societe Generale and other financial institutions in the ESG space.
                    If any additional interests are provided, the news should include those as well.
                    You will conduct mutiple searches using different keywords to gather the most relevant news. 
                    The most recent news should be prioritised.

                     **Parameters**: 
                      - Today's Date: {date}
                      - Additional Interests: {interests}

                     **Note**: {self.__tip_section()}
                """
                ),
            expected_output="A list of news articles that are relevant to ESG and the finance industry, focusing on Societe Generale and other financial institutions.",    
            agent=agent,
        )
    def summarise_news(self, agent, interests):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Read the articles and summarise them
                    **Description**: You will read the articles provided by the ESG News Researcher and summarise them in a concise and informative manner.
                    The sumary should be easy to read and understand, and should include the most important points of the article. It should be of interest to hte chief sustainability officer of Societe Generale.
                    If any additional interests are provided, the summary should include those as well.


                        **Parameters**: 
                        - Additional Interests: {interests}

                        **Note**: {self.__tip_section()}
                """
                ),
            expected_output="A summary of the articles focusing on the most important points to the eyes of the CSO of Societe Generale.",    
            agent=agent,
        )
