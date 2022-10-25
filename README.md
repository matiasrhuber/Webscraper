# Webscraper
Initial program to scrape web for laptop pricings
:computer:
There was a large difficulty understanding the HTML language. This is a succesful single-page scraper for the following website:
https://www.flipkart.com/laptops/a~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp%3Bamp%3Bamp%3Bamp%3Bamp%3Bamp%3Bamp%3Bamp%3Bamp%3Buniq=&

It analyzes the prices and names of each laptop. There was an attempt to create a multi-page scraper, however, due to Selenium's limitations with the webdriver timeout, it was unsuccessful. For future projects where only information gathering is needed, it is best to use the Requests module; Selenium is more adequate for more complex interactions with a Webpage.
