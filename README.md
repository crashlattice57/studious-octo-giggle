# Data Science State-Sponsored-Cyber Attacks: Project Overview

- Created a dashboard that analyzes the Kaggle Dataset
- Engineered Columns and conducted EDA to discover insights 
- Built clientfacing Streamlit Dashboard using heroku  


## Code and Resources Used

**Python Version:** 3.9

**Packages:** pandas, seaborn, matplotlib.pyplot, nltk, plotly, streamlit

**DataSet:** https://www.kaggle.com/datasets/justin2028/state-sponsored-cyber-operations-2005-present \

**Streamlit Youtube Video:** https://www.youtube.com/watch?v=Sb0A9i6d320 

**Streamlit github** https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbk9QaUJwRGxVVG9PRDZLa0gzNlE2OVV6U3Bsd3xBQ3Jtc0tsb2JZSFZ1STVEUkhjMWxCMW1yOWNvOUJnMlh6ekNoN0toTjd3ZjdfcXIza2NCdFlMcDhjd09tTjh5emE1c1ZnUGVkV3AtbFJ1cDRNRHZsWmcyLU9XakZrSXlscXBwMFJFQm9uZXNxSi1rLTd1ZEUxTQ&q=https%3A%2F%2Fgithub.com%2FSven-Bo%2Fstreamlit-sales-dashboard&v=Sb0A9i6d320

## Original Data Columns

- Tilte
- Date
- Affiliation
- Description
- Response
- Victims
- Sponsor
- Type
- Category
- Source_1
- Source_2
- Source_3

## Data Cleaning

- Removed Targeting of from Title Column
- Parsed the Date column and created seperate columns of Day, Month, Year
- Used Pandas Explode Method to split columns by delimiter and transpose data
- Remove stop words and additional words from the Affiliations column using stop_words file
- Merge the 3 Sources Columns into 1 single column named Sources
- Split Response Column to identify response action
- Remove bad values from the Category Column that don't make sense

## EDA

- ![alt text](https://github.com/crashlattice57/studious-octo-giggle/blob/main/attacks_by_month.png)
- ![alt text](https://github.com/crashlattice57/studious-octo-giggle/blob/main/Count_By_Categories.png)

## Dashboard Creation

- Created a Dashboard using streamlit and tested hosting the dashboard via heroku
- ![alt text](https://github.com/crashlattice57/studious-octo-giggle/blob/main/Dashboard_Screenshot.png)
