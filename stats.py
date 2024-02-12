import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_lottie import st_lottie
import time

#-----PAGE CONFIGURATION-------

st.set_page_config(
    page_title="STATISTICAL ANALYSIS PROJECT",
    page_icon=":bar_chart:")


df = pd.read_csv("stats.csv")
df = df.rename(columns={'STATISTICAL THEORY AND METHODS': 'STATISTICAL_THEORY_AND_METHODS'})

with st.sidebar.expander("DASHBOARD"):
    choice = st.selectbox("", ["ABOUT", "CONTENTS"])
         
    if choice=='ABOUT':
        st.image("stats.png")
        st.markdown(" ## ABOUT")
        st.markdown(" Analysis of data on performance  of Diploma students for academic years 2021/2022")
        st.write("---")
        st.markdown(" ## AIM")
        st.markdown(" To report on the dataset summarizing the characteristics of the data. including the suitable numerical summary measures to describe the distributions in terms of regression and inferential analysis")
    else:
        st.markdown("- Overview")
        st.markdown("- Regression Analysis")
        st.markdown(" - Inferential Analysis")
        st.write("---")
        st.markdown(" - Data analysis model")

st.sidebar.write("Copyright 2024")
st.sidebar.write("[![Follow](https://img.shields.io/twitter/follow/Johnwills171?style=social)](https://www.twitter.com/Johnwills171)")
        

      
      
cols1, cols2 = st.columns(2, gap="small")
with cols1:
      st.image("stats.png", width=200)

   
with cols2:
     st.subheader(":green[STATISTICAL ANALYSIS PROJECT]")
     st.write(" ***Dataset timeline 2021/2022***")
     st.write("***Date | 08/Feb/2024***")
     st.write("[![Follow](https://img.shields.io/twitter/follow/Johnwills171?style=social)](https://www.twitter.com/Johnwills171)")


tab1, tab2 = st.tabs(["DATASET ANALYSIS", "RUN YOUR OWN ANALYSIS"]) 

#------DATA IMPORTATION AND EXPLORATION------


with tab1:
     st.title(":green[Overview] :sunglasses:")
     st.caption(" (EDA: Exploratory Data Analysis & IDA: Initial Data Analysis)")     
     st.markdown("The data shows scores of 21 students (5 females, 16 males) in 5 subjects (Mathematics, Statistical Theory And Methods, Applied Statistics, Economics, Statistical Computing). Females scored higher on average (70.8 vs. 62.7 for males), with scores ranging from 37 (male, Mathematics) to 96 (female, Economics). Positive correlations between subjects suggest students performing well in one tended to do well in others."
    )


with tab1:
    st.markdown(" ### DASHBOARDS: 2021/2022 RESULTS")
    st.dataframe(df)
        

    def describe_page():  
        st.write("Descriptive measures of central tendency and measures of dispersion")
        st.dataframe(df.describe())

    def sex():
        st.markdown("In this dataset there are 16 male and 5 females")          
        st.write(pd.DataFrame(df['SEX']).value_counts())

    def bar_chart():
        st.markdown("Bar chart of the data values")
        st.bar_chart(df)    

    def sex_line_chart():
        st.text(" Sex distribution : F = FEMALE. M = MALE")
        st.line_chart(df['SEX'])

    pages = {
          "Measures OF Central tendency": describe_page,
          "sex distribution": sex,
          "Bar chart of dataset": bar_chart,
          "Sex Line chart distribution": sex_line_chart}   

    choice = st.selectbox("Nav Bar", pages.keys())
    pages[choice]()    




    with st.expander("Graphs"):
        df1 = pd.DataFrame(df['APPLIED STATISTICS'].value_counts())
        st.text("Frequency V. Applied Statistics")
        st.bar_chart(df1)

        st.write("---")

        df2 = pd.DataFrame(df['STATISTICAL_THEORY_AND_METHODS'].value_counts()) 
        st.text("Frequency V.STATISTICAL THEORY AND METHODS ")
        st.bar_chart(df2)

        st.write("---")

        df3 = pd.DataFrame(df['ECONOMICS'].value_counts())
        st.text("Frequency V. ECONOMICS")
        st.bar_chart(df3)

        st.write("---")

        df4 = pd.DataFrame(df['STATISTICAL COMPUTING'].value_counts())
        st.text(" Frequency V. STATISTICAL COMPUTING ")
        st.bar_chart(df4)

             
               


    tab3, tab4 = st.tabs(["Regression analysis", "inferential statistics"])
with tab3:

    st.subheader("Regression Analysis: Trends and Relationships") 
    with st.expander("What is Regression and everything you need to know"):
        st.markdown("Regression analysis is a powerful statistical technique used to model the relationship between one dependent variable and one or more independent variables. Its primary goal is to understand how changes in the independent variables influence the dependent variable. Think of it as drawing a line (in simple cases) or a more complex surface that best fits the data points, allowing you to predict the dependent variable based on the independent variables. Here are some key points about regression analysis")
     
    st.subheader("Types") 
    with st.expander("What are the types of regression"): 
        st.write("There are various types of regression analysis, each suited for different situations. The most common ones include linear regression (straight line), logistic regression (for binary outcomes), and polynomial regression (curved lines).")
    
    st.subheader("Application")
    with st.expander("What are the Applications of Regression analysis"):
        st.write(" Regression analysis is widely used across various fields, including finance, economics, science, engineering, and social sciences. It helps with tasks like:")
        st.markdown(" - Predicting future values:  Estimating house prices based on size and location, or predicting customer churn based on their behavior.")
        st.markdown("  - Identifying relationships:  Understanding how factors like advertising spending impact sales, or how income affects health outcomes. ")
        st.markdown("  - Evaluating causal effects: Examining the impact of interventions or policies on specific outcomes.")
        st.markdown("  - Assumptions: It's essential to understand the assumptions underlying each regression model and ensure your data adheres to them for accurate results. ")
        st.markdown("  - Interpretation:  Interpreting the coefficients of the regression model helps you understand the magnitude and direction of the relationship between variables.")
    
    st.subheader("Results")
    with st.expander("Regression Table Results"):
        st.caption("Summary output determing the relatioship between economics and Applied statistics")
        st.image("output.png")
        st.write("---")
        st.write(" ###")
        st.image("output1.png")  
        st.markdown(" ### Results")
        st.markdown('''
                    Multiple R: 0.738 indicates a moderately strong positive relationship between the independent variable(s) and the dependent variable. This means that around 54.4% (R-squared value) of the variance in the dependent variable can be explained by the independent variable(s).
Adjusted R-squared: 0.520 is slightly lower than R-squared, suggesting that the model fit improves slightly when considering the number of predictors in the model.
F-statistic: 22.66 and a p-value of 0.000136 indicate that the model is statistically significant, meaning there is a statistically significant relationship between the independent variable(s) and the dependent variable.
Individual Coefficients:

Intercept: The intercept of -19.36 suggests that even when the independent variable (Applied Statistics) is zero, the predicted value of the dependent variable is -19.36. However, the p-value of 0.269 indicates that this intercept is not statistically significant.
Applied Statistics: The coefficient of 1.204 for Applied Statistics means that for every one-unit increase in Applied Statistics score, the predicted value of the dependent variable increases by 1.204 units, on average. The p-value of 0.000136 indicates that this coefficient is statistically significant, meaning that Applied Statistics has a significant positive impact on the dependent variable.''')


with tab4:
    st.warning("Page still under development")
    
    st.write(" #### ")
    st.write("---")

    with tab2:
        st.title(":violet[Data analysis App] :exploding_head:")
        st.write("Upload a csv file and run analysis by clicking the button")
        uploaded_file = st.file_uploader("Upload a csv file", type=['csv'])

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)

            choice = st.selectbox("Choose", ["DESCRIPTIVE ANALYSIS", "GRAPHICAL ANALYSIS"], help='DESCRIPTIVE ANALYSIS option will only display output from quantitative variables')

            if st.button('Analyze'):
                with st.spinner('Analysing.....'):
                    time.sleep(3)
                st.balloons()
                if choice=="DESCRIPTIVE ANALYSIS":
                    st.write(df.fillna(df.mode()).describe())
                else:
                    st.info("Function still in development")

st.write("####")


 #-------------FOOTER-----------
cols3, cols4, cols5 = st.columns(3, gap='large')
cols3.page_link("https://tome.app/fx-3c4/johns-portfolio-cllaidgc700wkoe5qqmitxx1q", label='Portfolio')    
cols3.image("profile-pic.png", width=150)
cols4.page_link("https://williamjohnie61@gmail.com", label="Email")
cols5.page_link("https://twitter.com/Johnwills171", label='Twitter')
cols4.write("Prepared by: Ndelembi, John")
cols4.write("Data analyst / Web Developer")
cols4.write("For Calls | +255 625 232 734")


    






