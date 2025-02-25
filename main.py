from crewai import Crew
from textwrap import dedent
from agents import ESGAgents
from tasks import ESGTasks

from dotenv import load_dotenv
load_dotenv()



import datetime

today = datetime.datetime.now()
localdate= today.strftime("%x")





class ESGCrew:
    def __init__(self, date, interests):
        self.date = date
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = ESGAgents()
        tasks = ESGTasks()

        # Define your custom agents and tasks here
        esg_news_reporter = agents.esg_news_reporter()
        esg_news_researcher = agents.esg_news_researcher()

        # Custom tasks include agent name and variables as input
        write_esg_report = tasks.write_esg_report(
            esg_news_reporter,
            self.date,
            self.interests
        )

        gather_news = tasks.gather_news(
            esg_news_researcher,
            self.date,
            self.interests
        )


        # Define your custom crew here
        crew = Crew(
            agents=[esg_news_reporter, esg_news_researcher],
            tasks=[gather_news, write_esg_report],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to ESG News Synthetiser")
    print('-------------------------------')
    interests = input(
        dedent("""
      Are there any specific interests you would like to include in the news? if not, leave blank.
    """))
    date = today

    esg_crew = ESGCrew(date,interests)
    result = esg_crew.run()
    print("\n\n########################")
    print("## Here is you ESG Digest")
    print("########################\n")
    print(result)