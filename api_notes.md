## APIs (Application Programme Interface)

### What are APIs
- services/pieces of software that enable two software components to communicate with each other using a set of definitions and protocols

### How are APIs used?
- (definitions and protocols) help businesses connect the different applications used in day-to-day operations
saves employees time
  - breaks down silos that hinder collaboration and innovation. 
- For developers, API documentation provides the interface for communication between applications
  - simplifies application integration.

### How APIs Work
1. common example—third-party payment processing. When user purchases product on ecommerce site, they may be prompted to “Pay with Paypal” or another type of third-party system. This function relies on APIs to make the connection.

2. When buyer clicks the payment button, an API calls to retrieve information—also known as a request. This request is processed from an application to the web server via the API’s Uniform Resource Identifier (URI) and includes a request verb, headers, and sometimes, a request body.

3. After receiving valid request from product webpage, the API makes a call to external program or web server, (in this case: third-party payment system).
 
4. The server sends response to the API with the requested information.
 
5. The API transfers the data to the initial requesting application, here the product website.

### API Benefits 

1. Improved Collaboration
2. Accelerated innovation - offers flexibility
3. Data monetization - build audience of developers 
4. System security - layers of security 
5. End-user security and privacy - personal users

#### REST APIs - Representational State Transfer.
1. REST defines a set of functions like GET, PUT, DELETE, etc. that clients can use to access server data. Clients and servers exchange data using HTTP.
2. main feature of REST API is statelessness
3. Client requests to the server are similar to URLs you type in your browser to visit a website. The response from the server is plain data, without the typical graphical rendering of a web page.

#### What are REST APIs
- REST guidelines
- uniform interface
- decoupling
- CRUD
- layered architecture 

![](C:\Users\wafam\Downloads\api_diagram_process.png)

Diagram above shows the API services used to communicate between a server database and a patient.
##### Stateless
**Stateless** - means that servers do not save client data between requests

##### What is catching 
**Catching** - store data that is used often so you don't need to do too much work with it 

#### What is HTTP - Hypertext Transfer Protocol
- primary protocol used to send data between a web browser and a website
- foundation of the World Wide Web, and is used to load webpages using hypertext links.
- designed to transfer information between networked devices 

##### HTTPS Request 
1. HTTP request is the way Internet communications platforms such as web browsers ask for the information they need to load a website.
2. Each HTTP request made across the Internet carries with it a series of encoded data that carries different types of information. A typical HTTP request contains:

   - HTTP version type
   - a URL
   - an HTTP method
   - HTTP request headers
   - Optional HTTP body.



###### 5 HTTP verbs
1. GET - retrieve and read a representation of resources
2. POST - create new resources/send data and updates 
3. PUT - Update capabilities 
4. PATCH - modify capabilities 
5. DELETE - delete resources

![](C:\Users\wafam\Downloads\HTTP_request_structure.png)

![](C:\Users\wafam\Downloads\HTTP_response_structure.png)

HTTP requests, and responses, share similar structure and are composed of:

1. A start-line describing the requests to be implemented, or its status of whether successful or a failure. This start-line is always a single line.
2. An optional set of HTTP headers specifying the request, or describing the body included in the message.
3. A blank line indicating all meta-information for the request has been sent.
4. An optional body containing data associated with the request (like content of an HTML form), or the document associated with a response. The presence of the body and its size is specified by the start-line and HTTP headers.