import numpy as np
import pandas as pd
import streamlit as st

#-----PAGE CONFIGURATION-------

st.set_page_config(
    page_title="STATISTICAL ANALYSIS PROJECT",
    page_icon=":random:")

df = pd.read_csv("stats.csv")
df = df.rename(columns={'STATISTICAL THEORY AND METHODS': 'STATISTICAL_THEORY_AND_METHODS'})

with st.sidebar.expander("DASHBOARD"):
         st.image("stats.png")
         st.markdown(" ## About")
         st.markdown(" > Analysis of data on performance  of Diploma students for academic years 2021/2022 and 2022/2023")
         st.markdown(" ## AIM")
         st.markdown(" > To write a report on the dataset which will summarise the characteristics of the data. including the suitable numerical summary measures to describe the distributions of  data and inferential analysis")
         
with st.sidebar.expander("CONTENTS"):
         st.markdown("- Description of the data")
         st.markdown("- Regression Analysis")
         st.markdown(" - Inferential Analysis")

      
      
cols1, cols2 = st.columns(2, gap="small")
with cols1:
      st.image("stats.png", width=200)

   
with cols2:
     st.subheader("STATISTICAL ANALYSIS PROJECT")
     st.write(" ***Dataset timeline 2021/2022 & 2022/2023***")
     st.write("***Date | 08/Feb/2024***")

tab1, tab2 = st.tabs(["2021/2022", "2022/2023"]) 

with tab1:
     st.title("Descriptive Analysis(IDA/EDA) ")
     st.caption(" (EDA: Exploratory Data Analysis & IDA: Initial Data Analysis)")     
     st.markdown("This is diploma results of Statistics students 2021/2022 who sat for variety of test subjects, these are the results. in the following slides i tried going through the neccesary analytical processes. the data set icludes females and males students who participated in different tests. the task is to study the data set and define different patterns existing in the data and derive data driven inference on the data ")   
     
     col1, col2, = st.columns(2)          

#------DATA IMPORTATION AND EXPLORATION------

with tab1:
     with st.expander("Click to view the data"):
         with col1:
             st.markdown(" ### DASHBOARDS: 2021/2022 RESULTS")
             st.dataframe(df.head(10))
        
     with col2:
         with st.expander(" click to results"):   
             st.write("Descriptive measures of central tendency and measures of dispersion")
             st.dataframe(df.describe())
           
         with st.expander("Click to view results"):
            st.write("In this dataset there are 16 male and 5 females")          
            st.write(pd.DataFrame(df['SEX']).value_counts())

         with st.expander("Click to view results"):
             st.write("Line chart of the data values")
             st.line_chart(df)    

         with st.expander("Clck to view the graphs distributions"):
             st.text(" Sex distribution : F = FEMALE. M = MALE")
             SEX = st.line_chart(df['SEX'])

             df1 = pd.DataFrame(df['APPLIED STATISTICS'].value_counts())
             st.text(" Applied Frequency V. Applied Statistics")
             st.bar_chart(df1)

             df2 = pd.DataFrame(df['STATISTICAL_THEORY_AND_METHODS'].value_counts()) 
             st.text("Frequency V.STATISTICAL THEORY AND METHODS ")
             st.bar_chart(df2)

             df3 = pd.DataFrame(df['ECONOMICS'].value_counts())
             st.text("Frequency V. ECONOMICS")
             st.bar_chart(df3)

             df4 = pd.DataFrame(df['STATISTICAL COMPUTING'].value_counts())
             st.text(" Frequency V. STATISTICAL COMPUTING ")
             st.bar_chart(df4)

             


     tab3, tab4 = st.tabs(["Regression analysis", "inferential statistics"])
with tab3:
     st.subheader("Regression Analysis: Trends and Relationships")
     st.markdown("Regression analysis is a powerful statistical technique used to model the relationship between one dependent variable and one or more independent variables. Its primary goal is to understand how changes in the independent variables influence the dependent variable. Think of it as drawing a line (in simple cases) or a more complex surface that best fits the data points, allowing you to predict the dependent variable based on the independent variables. Here are some key points about regression analysis")
     st.subheader("Types:") 
     st.write("There are various types of regression analysis, each suited for different situations. The most common ones include linear regression (straight line), logistic regression (for binary outcomes), and polynomial regression (curved lines).")
     st.subheader(" Applications:")
     st.write(" Regression analysis is widely used across various fields, including finance, economics, science, engineering, and social sciences. It helps with tasks like:")
     st.markdown(" - Predicting future values:  Estimating house prices based on size and location, or predicting customer churn based on their behavior.")
     st.markdown("  - Identifying relationships:  Understanding how factors like advertising spending impact sales, or how income affects health outcomes. ")
     st.markdown("  - Evaluating causal effects: Examining the impact of interventions or policies on specific outcomes.")
     st.markdown("  - Assumptions: It's essential to understand the assumptions underlying each regression model and ensure your data adheres to them for accurate results. ")
     st.markdown("  - Interpretation:  Interpreting the coefficients of the regression model helps you understand the magnitude and direction of the relationship between variables.")
     st.text("Results of OLS regression method from the dataset, determing the relatioship between economics and statistics and mathematics (samples)")
     st.image("reg1.PNG")
     st.markdown(" ### Results")
     st.image("Picutre1.png")
     st.markdown("the results potray a positive relationship for two of the subject and one potrays a negative relationship, but the results are not statistically significant except for one APPLIED STATS in which case potrays has a 0.006 significance level and shows a  positive relationship. a unit change in APPLIED STATISITICS results would affect ECONOMICS results by 1 unit positively. The model is shows positive relationship. the model is relevant to the real life situation")
     
     
    







 #-------------FOOTER-----------
cols3, cols4, cols5 = st.columns(3, gap='large')
cols3.page_link("https://tome.app/fx-3c4/johns-portfolio-cllaidgc700wkoe5qqmitxx1q", label='Portfolio')    
cols3.image("profile-pic.png", width=150)
cols4.page_link("https://williamjohnie61@gmail.com", label="Email")
cols4.write("Ndelembi, John")
cols4.write("Junior Data analyst / Developer")
cols4.write("For Calls | +255 625 232 734")
cols5.page_link("https://twitter.com/@Johnwills171", label='Social')

             
