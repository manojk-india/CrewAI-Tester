```java
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
```