import os
from crewai import Crew,Process
from textwrap import dedent
from agents import TestAgents
from tasks import TestTasks
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

def save_to_file(filename, content):
        with open(filename, 'w') as file:
            file.write(content + '\n')



print("## Welcome to Crew AI Template")
print("-------------------------------")
api = input(dedent("""Enter the base url of the api that needed to be tested   """))
api_doc = input(dedent("""Enter the documentation of the above api's representing all end points clearly   """))

acceptance_criteria= input(dedent("""Enter the test case to test clearly in plain english   """))


genai = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))
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
            process=Process.sequential,
            manager_llm=genai,
            output_log_file=True,
        )

results=crew.kickoff()

feature_content = str(generate_feature.output.description)
step_def_content = str(generate_stepdefinitions.description)

save_to_file("feature.feature", feature_content)
save_to_file("step_definitions.py", step_def_content)
print("crew worked results are .....")
print(results)