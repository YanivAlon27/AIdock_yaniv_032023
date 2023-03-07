##AIdock classification assignment:

Given a string containing a description of a recipe return a JSON containing the ingredients and the recipe. 

using Python packages in this assignment: PyTorch, TensorFlow, pandas, numpy, and BeautifulSoup to build a scraper file and a model.

the scraper file - scraper.py is using BeautifulSoup to generate a JSON file with recipes and instructions from the website https://www.loveandlemons.com/.

then, the new JSON file is used to test the NLP classification model, which was built using TensorFlow and a small dataset from the website: https://www.loveandlemons.com/.
 the output of the test_profile.py is the model runtime, memory usage, and the classification of the paragraphs that were divided by the scraper to either recipe or instructions. the model then gives the input the probability it is a recipe or instructions.

all can run by the simple run.sh file, which executes the scraper and then asks for a URL from the user the teset_profile2 output. 
