import openai
from Secret_Key import openai_key
import json
import pandas as pd

openai.api_key = openai_key


def extract_Keywords(text):
    prompt = get_prompt_Description() + text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response.choices[0]['message']['content']

    try:
        data = json.loads(content)
        return pd.DataFrame(data.items(), columns=["Classes", "Keywords"])

    except (json.JSONDecodeError, IndexError):
        pass

    return pd.DataFrame({
        "Classes": ["Education", "Languages", "Technical Skills", "Soft Skills", "Technology and Concepts"],
        "Keywords": ["", "", "", "", ""]
    })


def get_prompt_Description():
    return '''  Please retrieve the keywords  from the following job description and divide it in five Section which are
     Education, Programming languages, Technical Skills, Soft Skills  and remaining Important in Technology and Concepts 
     section(only important and valid keywords with high prioriy) according to their specification  to make resume ATS 
     Friendly for given job opening. Don’t repeat Keywords of one section in another.  If you can't find the information 
    from  this job Description then return "". Do not make things up.   For this you can use  your general knowledge. 
    Always return your  response as a valid JSON string. The format of that string should be this, 
    {
        "Education": " ",
        "Languages": " ",
        "Technical Skills": " ",
        "Soft Skills": "  ",
        "Technology and Concepts": " "

    }

    Job Description:
    ============

    '''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text = '''
    ob Role: Data Science Analyst

Job Description

In Cisco, we have an outstanding opportunity where we actually get to use the technology we build!

We are Innovators

We drive innovation to propel business transformation while maintaining operational quality.

We are Accelerators

We accelerate digital solutions to generate cost savings and efficiency gains for enterprise growth and

success.

We are Transformers

As customer zero, we transform the customer experience by being our own customer first with agility, quality, and security, we continuously deliver business outcomes for our clients.


Who You'll Work With

ONEx Strategy & Planning, Business Insights team provides flexible and innovative ways to help meet customer needs while improving profitability for Cisco.
The team has specialized domains in 2 broad areas that function seamlessly to enable business outcomes through analytics for Cisco.


Specialized Domains are:

·         Data Engineering

·         Data Science/Data Analytics


Who you are:

• Experience in Data Science & analytics; 0-2 years of experience

• Ability to work cross functionally, very strong in business analytics,

• Previous experience in services will be helpful. Exposure to operational and 

financial data

• Good in communication (ability to articulate analysis and present)



Desired Skills

·         Strong in both, operational and financial data analysis

·         Experience using statistical computer languages (R, Python, SLQ, etc.) to manipulate data and draw insights from large data sets.

·         Knowledge of a variety of machine learning techniques (clustering, decision tree learning, artificial neural networks, etc.) and their real-world advantages/drawbacks.

·         Knowledge of advanced statistical techniques and concepts (regression, properties of distributions, statistical tests and proper usage, etc.) and experience with applications.

·         Mine and analyze data from company databases to drive optimization and improvement of product development, marketing techniques and business strategies.

·         Assess the effectiveness and accuracy of new data sources and data gathering techniques.

·         Develop custom data models and algorithms to apply to data sets.

·         Ability to work on multiple assignments in parallel and keep up with deadlines and quality

·         Articulate complex data in business terms and make recommendations

·         Excellent written and verbal communication skills for coordinating across teams.

·         A drive to learn and master new technologies and techniques.

·         Skill to extract intelligence from data, derive business insights and present to business


Why Cisco

WeAreCisco, where each person is unique, but we bring our talents to work as a team and make a difference powering an

inclusive future for all.

We embrace digital, and help our customers implement change in their digital businesses. Some may think we’re “old” (39

years strong) and only about hardware, but we’re also a software company. And a security company. We even invented an

intuitive network that adapts, predicts, learns and protects. No other company can do what we do – you can’t put us in a box!

But “Digital Transformation” is an empty buzz phrase without a culture that allows for innovation, creativity, and yes, even

failure (if you learn from it.)

Day to day, we focus on the give and take. We give our best, give our egos a break, and give of ourselves (because giving back

is built into our DNA.) We take accountability, bold steps, and take difference to heart. Because without diversity of thought

and a dedication to equality for all, there is no moving forward.


    '''
    df = extract_Keywords(text)

    print(df.to_string())