from crewai import Agent
from textwrap import dedent
from langchain_google_genai import ChatGoogleGenerativeAI
import os


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Given an api and required clear doc about the endpoints of the api and also the acceptance criteria of the test case
the agent should give the feature and the step definition file which is needed in maven project

Captain/Manager/Boss:
-  testAI

Employees/Experts to hire:
-none



Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""



class TestAgents:
    def __init__(self):
        self.genai = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))
        

    def feature_generator(self):
        return Agent(
            role=dedent(f"""Gherkin feature file generator expert"""),

            backstory=dedent(f"""You are an expert in gherkin language with full knowledge about the syntax of the gherkin language
                            and has worked in many projects to convert given english criteria to a gherkin test case content of feature file 
                            required for testing an api using cucumber bdd framework in java maven project  """),

            goal=dedent(f"""
                        provide the content of the feature file for the given documentation of the api 
                        and the acceptance criteria for the test case"""),
            verbose=True,
            max_iter=25,
            llm=self.genai,
        )
    
    def step_def_generator(self):
        return Agent(
            role=dedent(f"""Expert Java maven step definition file generator"""),

            backstory=dedent(f"""You are an expert in producing the content of step definition file in java language when the feature 
                            file(gherkin language) is given  """),
            goal=dedent(f"""
                        provide the content of the stepdefinition file in java language accurately with no syntax error"""),
            verbose=True,
            max_iter=20,
            llm=self.genai,
        )
    
    def pom_file_generator(self):
        return Agent(
            role=dedent(f"""Expert Java maven pom.xml file generator"""),

            backstory=dedent(f"""You are an expert in producing the content of pom.xml file in java language for the given stepdefinition file
                            to solve all the dependency issues and you have never missed out to add any dependency in pom.xml file which is 
                            needed to run the stepdefinition file"""),
            goal=dedent(f"""
                        provide the content of the pom.xml file to resolve all dependencies for the given stepdefinition file"""),
            verbose=True,
            max_iter=20,
            llm=self.genai,
        )
    
    '''def QA_engineer(self):
        return Agent(
            role=dedent(f"""Expert quality assurance software engineer"""),

            backstory=dedent(f"""You are an expert in finding error in code and wont make any mistake in spotting any errors"""),
            goal=dedent(f"""
                        Find the errors associated with given stepdefinition file"""),
            verbose=True,
            max_iter=24,
            llm=self.genai,
        )'''

    def software_engineer(self):
        return Agent(
            role=dedent(f"""Expert and experianced java software developer"""),

            backstory=dedent(f"""You are the world best and finest java developer who will write codes with absolutely no errors
                             and no one is better than you """),

             goal=dedent(f"""
                        producing accurate code in accordance to the task assigned to you"""),
            verbose=True,
            max_iter=20,
            llm=self.genai,
        )
   