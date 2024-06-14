import os
from crewai import Crew,Process
from textwrap import dedent
from agents import TestAgents
from tasks import TestTasks
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()


print("## Welcome to Crew AI Template")
print("-------------------------------")
api = input(dedent("""Enter the base url of the api that needed to be tested   """))
api_doc = input(dedent("""Enter the documentation of the above api's representing all end points clearly   """))
acceptance_criteria= input(dedent("""Enter the test case to test clearly in plain english   """))


OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7,
                                      verbose=True,
                                      api_key=os.getenv('OPENAI_API_KEY'))

#declaring the agents
agents = TestAgents()
tasks = TestTasks()

#setting up the agents
feature_agent= agents.feature_generator()
stepdefinition_agent = agents.step_def_generator()

#setting up the tasks 
generate_feature= tasks.generate_feature(
            feature_agent,
            api_doc,
            acceptance_criteria,
        )

generate_stepdefinitions = tasks.generate_stepdefinitions(
            stepdefinition_agent,
            api,
            api_doc,
            [generate_feature],
        )

#setting up the crew
crew = Crew(
            agents=[feature_agent, stepdefinition_agent],
            tasks=[generate_feature, generate_stepdefinitions],
            verbose=True,
            process=Process.hierarchical,
            manager_llm=OpenAIGPT35,
        )

results=crew.kickoff()

print("crew worked results are .....")
print(results)