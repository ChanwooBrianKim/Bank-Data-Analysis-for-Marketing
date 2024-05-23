# Bank Data Anlaysis for Marketing
Data Link: 'https://archive.ics.uci.edu/ml/datasets/bank+marketing'

## Overview
The given dataset encapsulates information from a marketing campaign conducted by a European bank utilising outbound telemarketing strategies. The primary objective of the campaign was to persuade customers to subscribe to a term deposit. The dataset comprises 41,188 records and 21 attributes, detailing various customer characteristics and the specifics of the marketing effots.

## Steps Taken
1. **Data Processing**
  **Data Loading**: The dataset was imported from a CSV file with a semicolon (;) delimiter.

  **Initial Inspection**: Preliminary examination of the data was performed using head() to       display   initial rows, and shape to determine the dataset's dimensions.

  **Missing Values**: A check for missing values using isnull() revealed no missing data.

2. **Data Exploration**
  **Summary Statistics**: Descriptive statistics were generated using describe(), providing       insights into the central tendencies and variances of numerical features.

  **Unique Values and Frequencies**: The unique values and their frequencies for categorical     variables, such as education and marital, were analyzed.

3. **Data Visualisation**
  **Age Distribution**: The distribution of ages was visualized through histograms. A detailed   age analysis was also conducted by sorting the dataset by age and creating a line plot.

  **Duration Distribution**: The duration of calls was examined and visualized using histograms   to understand its spread and central tendencies.

  **Categorical Variables**: Bar plots were created for categorical variables like marital and    education to visualize the distribution of different categories.

4. **Hypothesis Testing and Analysis**
  **Loan and Subscription Status**: Explored the hypothesis that customers with loans are less    likely to subscribe to the term deposit.

  **Group Division**: Data was divided into two groups based on the subscription status (y):      those who subscribed ('yes') and those who did not ('no').

  **Loan Status Comparison**: The proportion of customers with loans was compared between the     two groups, revealing a slightly lower proportion of loan holders among those who subscribed.

  **Marketing Strategy Based on Age, Job, and Subscription Status**:

  **Pivot Tables**: Pivot tables were utilized to analyze the average age of subscribers and      non-subscribers across different job categories.

  **Multi-level Indexing**: Further analysis was conducted by including marital status and        contact type to identify any significant differences in age across these subgroups.

## Key Insights
  **Age Distribution**: The majority of customers are in their 30s to 40s, with a notable         number in their 50s and 60s, displaying a right-skewed distribution.

  **Call Duration**: Call durations vary widely, with many short calls and a few very long        ones. Most calls last between 100 and 500 seconds.

  **Loan Status**: Customers with loans are slightly less likely to subscribe to the term         deposit, possibly indicating financial conservatism or pre-existing commitments.

  **Occupation and Age**: Different occupations show varying average ages of subscribers and      non-subscribers. For example, students who subscribed tend to be younger than subscribers in    other job categories.

## Conclusion
This analysis provided valuable insights into the characteristics of customers who are likely to subscribe to a term deposit. Factors such as age, job, and loan status significantly influence subscription rates. These findings can guide the bank in tailoring marketing strategies to effectively target specific customer segments, potentially increasing the success rate of future campaigns. For instance, focusing on younger customers in certain professions or those without existing loans might enhance campaign effectiveness.

