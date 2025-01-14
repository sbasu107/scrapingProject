# Web Scraping Project

In this project, I created a simple HTML/CSS website and [hosted it online](https://samplearticlescraping.web.app) using Google Firebase. The website contains paragraphs that I copied and pasted from various online sources. 

To extract and process the content of the website, I used the `requests` and `Beautiful Soup` libraries in Python. These tools allowed me to parse through the website's content and print out the resulting text.

Then, I used Google's API for Gemini to pass the parsed content of the website into the LLM, and asked to "Explain the benefits of tofu that the following article points out."

The response, which is below, is written to the file response.txt.

"The article mentions the following benefits of tofu:

* **High in protein and low in calories:**  Tofu is a good source of protein, which is essential for building and repairing tissues.  The protein content varies depending on the firmness of the tofu.
* **Excellent source of vegan calcium:**  This is especially important for plant-based eaters who need to ensure they get enough calcium for bone health.
* **Fortified with vitamins:** Some brands of tofu are fortified with vitamin B12 and vitamin D, boosting its nutritional profile. These vitamins are often lacking in vegan diets. "