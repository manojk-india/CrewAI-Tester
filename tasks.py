from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - Generate a feature and a step definition file

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - feature file generation
    - step definition generation

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""
def save_to_file(self, filename, content):
        with open(filename, 'a') as file:
            file.write(content + '\n')

class TestTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def generate_feature(self, agent, api_doc,acceptance_criteria):
        return Task(
            description=dedent(f"""
            **Task**: [Generate the content of feature file ]
            **Description**: [Generate the content of feature file of java maven project to run a cucumber test case for the given 
            acceptance criteria]

            **Parameters**: 
            - api documentation: {api_doc}
            - acceptance criteria : {acceptance_criteria}
            ... [Add more parameters as needed.]

            **Note**: {self.__tip_section()}
            """
            ),
            agent=agent,
            outputs=['feature_file_content'],
        )

    def generate_stepdefinitions(self, agent,api,api_doc,feature_file_content):
        return Task(
            description=dedent(f"""
            **Task**: [Generate the content of step definition file named "Products.java" according to given feature_file_content of java maven project]
            **Description**: [Generate the content of stepdefinitionsfile "Products.java" of java maven project to run a cucumber test case for the given 
            acceptance criteria and first line use it as package stepdefinitions; ]

            **Parameters**: 
            - api : {api}
            - api documentation: {api_doc}
            - feature_file_content:{feature_file_content}


            **Note**: {self.__tip_section()}
            """
            ),
            agent=agent,
            context=feature_file_content,
            outputs=['stepdefinition_file_content'],
        )
    
    def generate_pox_xml(self,agent,stepdefinition_file_content):
         return Task(
            description=dedent(f"""
            **Task**: [Generate the content of pom.xml file named "pom.xml" according to given step definition file conten of java maven project]
            **Description**: [Generate the content of pom.xml file when the respective stepdefinition java file is given ]

            **Parameters**: 
            - stepdefinitions_file_content:{stepdefinition_file_content}


            **Note**: {self.__tip_section()}
            """
            ),
            agent=agent,
            context=stepdefinition_file_content,
            outputs=['pom_xml_file_content'],
            expected_output="""
            <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
                <modelVersion>4.0.0</modelVersion>

                <groupId>com.example</groupId>
                <artifactId>cucumber-bdd</artifactId>
                <version>1.0-SNAPSHOT</version>

                <properties>
                    <maven.compiler.source>1.8</maven.compiler.source>
                    <maven.compiler.target>1.8</maven.compiler.target>
                    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
                </properties>

                <dependencies>
                    <!-- Cucumber dependencies -->
                    <dependency>
                        <groupId>io.cucumber</groupId>
                        <artifactId>cucumber-java</artifactId>
                        <version>6.10.4</version>
                        <scope>test</scope>
                    </dependency>
                    <dependency>
                        <groupId>io.cucumber</groupId>
                        <artifactId>cucumber-junit</artifactId>
                        <version>6.10.4</version>
                        <scope>test</scope>
                    </dependency>
                    
                    <!-- JUnit dependency -->
                    <dependency>
                        <groupId>junit</groupId>
                        <artifactId>junit</artifactId>
                        <version>4.13.2</version>
                        <scope>test</scope>
                    </dependency>
                    
                    <!-- RestAssured dependency -->
                    <dependency>
                        <groupId>io.rest-assured</groupId>
                        <artifactId>rest-assured</artifactId>
                        <version>4.4.0</version>
                        <scope>test</scope>
                    </dependency>
                </dependencies>

                <build>
                    <plugins>
                        <plugin>
                            <groupId>org.apache.maven.plugins</groupId>
                            <artifactId>maven-compiler-plugin</artifactId>
                            <version>3.8.1</version>
                            <configuration>
                                <source>1.8</source>
                                <target>1.8</target>
                            </configuration>
                        </plugin>
                        <plugin>
                            <groupId>org.apache.maven.plugins</groupId>
                            <artifactId>maven-surefire-plugin</artifactId>
                            <version>2.22.2</version>
                            <configuration>
                                <includes>
                                    <include>**/RunCucumberTest.java</include>
                                </includes>
                            </configuration>
                        </plugin>
                    </plugins>
                </build>
            </project>
            """,
        )
    
    '''def error_check(self,agent,feature_file_content,stepdefinition_file_content):
        return Task(
            description=dedent(f"""
            **Task**: [Generate the content of new stepdefinition file according to given feature file in case there is any error]

            **Parameters**: 
            - feature_file_content:{feature_file_content}
            - stepdefinitions_file_content:{stepdefinition_file_content}


            **Note**: {self.__tip_section()}
            """
            ),
            agent=agent,
            outputs=['new_stepdefinition_file_content'],
         )'''
    
    
    

