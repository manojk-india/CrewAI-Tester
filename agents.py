from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
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
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7,
                                      verbose=True,
                                      api_key=os.getenv('OPENAI_API_KEY'))

    def feature_generator(self):
        return Agent(
            role=dedent(f"""Gherkin feature file generator expert"""),

            backstory=dedent(f"""An expert in gherkin language with full knowledge about the syntax of the gherkin language
                            and has worked in many projects to convert given english criteria to a gherkin test case content of feature file written in gherkin 
                            language required for testing an api using cucumber bdd framework in java maven project  """),

            goal=dedent(f"""
                        provide the content of the feature file in gherkin language 
                        when given the documentation of the api and the acceptance criteria for the test case"""),
            # tools=[tool_1, tool_2],
            allow_delegation=True,
            verbose=True,
            max_iter=20,
            llm=self.OpenAIGPT35,
        )
    
    def step_def_generator(self):
        return Agent(
            role=dedent(f"""Expert Java maven step definition file generator"""),

            backstory=dedent(f"""An expert in producing the content of step definition file in java language for the given feature 
                            file(gherkin language)  """),
            goal=dedent(f"""
                        provide the content of the stepdefinition file in java language"""),
            # tools=[tool_1, tool_2],
            allow_delegation=True,
            verbose=True,
            max_iter=20,
            llm=self.OpenAIGPT35,
        )
   