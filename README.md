# URLShortener

Tools and Technologies :  Django 2.2.2, Python 3.7, MongoDB, VSCode.

Front End Technologies :  Django Templates, HTML, CSS, Bootstrap4

Virtual Environment Test Database :  SqLite3 (Default db)

Production Database :  MongoDB  Refer  @http://mlab.com


Description:

This Application takes in a URL and generates a code in alphanumeric characters of size six. 

After generating the code it maps the generated code with the provided URL in the MongoDB database.

It then requests the application as (domain_name/code).

Using the URL pattern in Django it fetches the code and get the mapped URL updated in the database.

Simply creates a link with an additional prefix as domain name and redirects to the original URL.


check it out @http://myvitly.herokuapp.com/


See applications of the project:

Original domain name  :   @http://myvitly.herokuapp.com/


Generated URL for the original domain  :    @http://myvitly.herokuapp.com/XZ4JO4/

Both redirect to the same destination


