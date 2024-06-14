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
            **Task**: [Generate the content of feature file]
            **Description**: [Generate the content of feature file of java maven project to run a cucumber test case for the given 
            acceptance criteria ]

            **Parameters**: 
            - api documentation: {api_doc}
            - acceptance criteria : {acceptance_criteria}
            ... [Add more parameters as needed.]

            **Note**: {self.__tip_section()}
            """
            ),
            expected_output=""" 
            Feature: Get all products from the API
            As a user
            I want to retrieve a list of products from the API
            So that I can view the available products

            Scenario: Verify the GET API for the products
                Given I have the base URL of the product API
                When I send a GET request to the "products" endpoint
                Then I should receive a response with status code 200
                And the response should contain a list of products

            """,
            agent=agent,
            output_file='feature.md',
        )

    def generate_stepdefinitions(self, agent,api,api_doc,feature_file_content):
        return Task(
            description=dedent(f"""
            **Task**: [Generate the content of step definition file according to given feature file of java maven project]
            **Description**: [Generate the content of feature file of java maven project to run a cucumber test case for the given 
            acceptance criteria ]

            **Parameters**: 
            - api : {api}
            - api documentation: {api_doc}
            - feature_file_content:{feature_file_content}


            **Note**: {self.__tip_section()}
            """
            ),
            expected_output=""" 
            package stepdefinitions;

            import io.cucumber.java.en.*;
            import io.restassured.RestAssured;
            import io.restassured.response.Response;
            import io.restassured.specification.RequestSpecification;
            import static org.junit.Assert.*;

            public class Products {
                private Response response;
                private RequestSpecification httpRequest;

                @Given("I have the base URL of the product API")
                public void i_have_the_base_url_of_the_product_api() {
                    RestAssured.baseURI = "https://fakestoreapi.com/";
                }

                @When("I send a GET request to the {string} endpoint")
                public void i_send_a_get_request_to_the_endpoint(String endpoint) {
                    httpRequest = RestAssured.given();
                    response = httpRequest.get(endpoint);
                }

                @Then("I should receive a response with status code {int}")
                public void i_should_receive_a_response_with_status_code(Integer statusCode) {
                    assertEquals(statusCode.intValue(), response.getStatusCode());
                }

                @Then("the response should contain a list of products")
                public void the_response_should_contain_a_list_of_products() {
                    String responseBody = response.getBody().asString();
                    assertTrue(responseBody.contains("id"));  // Assuming the response contains an "id" field for products
                    assertTrue(responseBody.contains("title"));  // Assuming the response contains a "title" field for products
                }
            }
            """,
            agent=agent,
            context=feature_file_content,
            output_file='stepdefinition.md',
        )
