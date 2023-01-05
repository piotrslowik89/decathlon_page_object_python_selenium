# deacthlon_page_object_python_selenium


![Project Image](project-image-url)


### Table of Contents


- [Description](#description)
- [How To Use](#how-to-use)
- [Author Info](#author-info)


# Description
An example of an automated test project. Written in Java Selenium in Page Object Pattern.
It presents a simple journey through the decathlon.pl website.
Libraries for creating reports are implemented, e.g. 

The selectors are not perfectly added, so they may become outdated if the page is modified.

I plan to continue developing it.

## Technologies :
- python                3.11
- selenium              4.6.0
- webdriver-manager     3.8.5
- allure-pytest         2.12.0
- allure-python-commons 2.12.0
- xlrd                  1.2.0

# How To Use

#### Installation
Expand the green code button.
Copy the code with the command:
git clone

You can download the necessary dependencies with 
To install the required dependencies issue the below command in project root directory:
```commandline
    pip install -r requirements.txt
```
#### How to run?
```commandline
pytest
```
# How to generate report example
We run pytest tests and save the path to reports . (path depends on user and system)
```commandline
pytest --alluredir=C:\Users\userName\projects\pythonProjects\decathlon_page_object_python_selenium\report
```

Generating a report and displaying it:
```commandline
allure serve C:\Users\userName\projects\pythonProjects\\decathlon_page_object_python_selenium\report
```



# Author Info

- linkedin - [Piotr Slowik](www.linkedin.com/in/piotrslowik409)