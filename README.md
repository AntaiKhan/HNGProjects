# NUMBER CLASSIFICATION API WITH PYTHON ON AWS (HNGProjects Stage 1 Task)

### Overview

This project is a Flask-based API that provides interesting mathematical properties of a given number. It determines whether a number is prime, perfect, or an Armstrong number, and also provides its digit sum and a fun fact.

### Features

- Determines if a number is prime, perfect, or an Armstrong number.

- Computes the sum of digits.

- Returns a fun fact about the number.

- Supports CORS for cross-origin access.

- Returns responses in JSON format.

## STEP 0 -  SETUP NECESSARY TOOLS AND DEPENDENCIES.

Ensure you have python installed.

Install Flask and Zappa
`pip install flask flask-cors zappa`

Note: Zappa is a very lightweight and powerful tool that allows you to deploy and update python applications to AWS. Using Zappa you can host your WSGI app on AWS Lambda, API Gateway quickly.

## Setup your API on app.py in your local environment 

<img width="997" alt="image" src="https://github.com/user-attachments/assets/8542a0cc-11da-430a-966c-d981f9a7a62d" />


Test your API Locally

`http://127.0.0.1:5000/math/123`

<img width="1099" alt="image" src="https://github.com/user-attachments/assets/0a394d11-92ae-4ccf-af6a-1d77f014f5bc" />

## Deploy API with Zappa on AWS Lambda using API Gateway

Initialize Zappa

`zappa init`

<img width="564" alt="image" src="https://github.com/user-attachments/assets/448c9e0f-febb-44ab-b0b9-0e35c54ebde8" />

Follow the prompts to configure deployment settings.

Deploy your Flask app to AWS Lambda using the code below:

`zappa deploy dev`

This would take a while. After deployment, a link will be shared to access your API.

`https://6p02e91ii9.execute-api.us-east-1.amazonaws.com/dev/math/153`

<img width="1436" alt="image" src="https://github.com/user-attachments/assets/2bc55687-6295-449a-8553-d5316c7d366e" />

## Optimize Speed for Fast Response Time

Zappa will automatically set up a regularly occurring execution of your application in order to keep the Lambda function warm.

For extra step, you can Enable API Caching on AWS.







