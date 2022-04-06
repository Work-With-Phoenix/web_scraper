### WEB SCRAPER

The following repo contains a web scraper project for the jumia ecommerce website product pages.
The project also fetches the data obtained into an indexed .json file specified that will in turn be used by a search API created using JS which a user can access from the html file created for the client server.

### Tech Stack
* python3
* HTML
* JSON
* JavaScript

### Dependencies
* BS4
* LXML
* BEAUTIFULSOUP4
* JSON
* PANDAS
* REQUESTS

## Dependencies Installation
Install the dependencies above with the following command

```shell 
# installing the dependecies used in the project your project
pip3 install bs4 requests lxml json beautifulsoup4 pandas 
```

## Running the script
```shell 
# You can run the scraper.py script using the command below
python3 scraper.py
```

## TODO
* SMTP Configurations - will facilitate email alerts when the price of a product drops
* Search API Modification
* Script Automation
* Version Control
* UI Design for a user dashboard
