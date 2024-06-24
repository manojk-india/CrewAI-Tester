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
        file.write(content)



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
pom_file_agent=agents.pom_file_generator()
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

generate_pox_xml = tasks.generate_pox_xml(
            pom_file_agent,
            [generate_stepdefinitions],
        )

#setting up the crew
crew1 = Crew(
            agents=[feature_agent],
            tasks=[generate_feature],
            verbose=True,
            process=Process.sequential,
            manager_llm=genai,
        )

crew2 = Crew(
            agents=[stepdefinition_agent],
            tasks=[generate_stepdefinitions],
            verbose=True,
            process=Process.sequential,
            manager_llm=genai,
        )

crew3 = Crew(
            agents=[pom_file_agent],
            tasks=[generate_pox_xml],
            verbose=True,
            process=Process.sequential,
            manager_llm=genai,
        )

feature_file_content=crew1.kickoff()
save_to_file("java-app/src/test/resources/features/create_item.feature",feature_file_content)

stepdefinition_file_content=crew2.kickoff()
save_to_file("java-app/src/test/java/stepdefinitions/Products.java",stepdefinition_file_content)

pom_xml_file_content=crew3.kickoff()
save_to_file("java-app/pom.xml",pom_xml_file_content)

print("crew process complete and results are generated  .....")
