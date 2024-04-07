# Vaccine Usage Prediction

### Abstract
Subjects receiving the same vaccine often show different levels of immune responses and some may even present adverse side effects to the vaccine. Systems vaccinology can combine omics data and machine learning techniques to obtain highly predictive signatures of vaccine immunogenicity and reactogenicity. This project aims to predict the likelihood of individuals taking an H1N1 flu vaccine using Logistic Regression, leveraging a dataset containing various demographic and behavioral attributes of the respondents.

### Problem Statement
The objective of this project is to develop a predictive model using Logistic Regression to determine the likelihood of individuals taking the H1N1 flu vaccine. By analyzing the provided dataset, we will explore the relationships between different variables and identify key factors that influence vaccination decisions.

### Dataset Information
The dataset contains information related to the technical specifications of cars. Here are the column descriptions:<br>

1. unique_id: Unique identifier for each respondent.<br>
2. h1n1_worry: Worry about the H1N1 flu (0, 1, 2, 3). (0=Not worried at all, 1=Not very worried, 2=Somewhat worried, 3=Very worried)<br>
3. h1n1_awareness: Signifies the amount of knowledge or understanding the respondent has about the H1N1 flu (0, 1, 2). (0=No knowledge, 1=Little knowledge, 2=Good knowledge)<br>
4. antiviral_medication: Indicates whether the respondent has taken antiviral vaccination (0, 1).<br>
5. contact_avoidance: Reflects whether the respondent has avoided any close contact with people who have flu-like symptoms (0, 1).<br>
6. bought_face_mask: Indicates whether the respondent has bought a mask (0, 1).<br>
7. wash_hands_frequently: Indicates whether the respondent washes hands frequently or uses hand sanitizer (0, 1).<br>
8. avoid_large_gatherings: Indicates whether the respondent has reduced time spent at large gatherings (0, 1).<br>
9. reduced_outside_home_cont: Indicates whether the respondent has reduced contact with people outside their own house (0, 1).<br>
10. avoid_touch_face: Indicates whether the respondent avoids touching the nose, eyes, and mouth (0, 1).<br>
11. dr_recc_h1n1_vacc: Reflects whether the doctor has recommended the H1N1 vaccine (0, 1).<br>
12. dr_recc_seasonal_vacc: Reflects whether the doctor has recommended the seasonal flu vaccine (0, 1).<br>
13. chronic_medic_condition: Indicates whether the respondent has any chronic medical condition (0, 1).<br>
14. cont_child_undr_6_mnth: Indicates whether the respondent has regular contact with a child under the age of 6 months (0, 1).<br>
15. is_health_worker: Indicates whether the respondent is a health worker (0, 1).<br>
16. has_health_insur: Indicates whether the respondent has health insurance (0, 1).<br>
17. is_h1n1_vacc_effective: Reflects the respondent's perception of the effectiveness of the H1N1 vaccine (1, 2, 3, 4, 5). (1=Thinks not effective at all, 2=Thinks it is not very effective, 3=Doesn't know if it is effective or not, 4=Thinks it is somewhat effective, 5=Thinks it is highly effective)<br>
18. is_h1n1_risky: Reflects the respondent's perception of the risk of getting ill with H1N1 in the absence of the vaccine (1, 2, 3, 4, 5). (1=Thinks it is not very low risk, 2=Thinks it is somewhat low risk, 3=Don't know if it is risky or not, 4=Thinks it is somewhat high risk, 5=Thinks it is very highly risky)<br>
19. sick_from_h1n1_vacc: Reflects whether the respondent worries about getting sick by taking the H1N1 vaccine (1, 2, 3, 4, 5). (1=Respondent not worried at all, 2=Respondent is not very worried, 3=Doesn't know, 4=Respondent is somewhat worried, 5=Respondent is very worried)<br>
20. is_seas_vacc_effective: Reflects the respondent's perception of the effectiveness of the seasonal flu vaccine (1, 2, 3, 4, 5). (1=Thinks not effective at all, 2=Thinks it is not very effective, 3=Doesn't know if it is effective or not, 4=Thinks it is somewhat effective, 5=Thinks it is highly effective)<br>
21. is_seas_flu_risky: Reflects the respondent's perception of the risk of getting ill with seasonal flu in the absence of the vaccine (1, 2, 3, 4, 5). (1=Thinks it is not very low risk, 2=Thinks it is somewhat low risk, 3=Don't know if it is risky or not, 4=Thinks it is somewhat high risk, 5=Thinks it is very highly risky)<br>
22. sick_from_seas_vacc: Reflects whether the respondent worries about getting sick by taking the seasonal flu vaccine (1, 2, 3, 4, 5). (1=Respondent not worried at all, 2=Respondent is not very worried, 3=Doesn't know, 4=Respondent is somewhat worried, 5=Respondent is very worried)<br>
23. age_bracket: Age bracket of the respondent (18-34 Years, 35-44 Years, 45-54 Years, 55-64 Years, 64+ Years)<br>
24. qualification: Qualification/education level of the respondent as per their response (<12 Years, 12 Years, College Graduate, Some College)<br>
25. race: Respondent's race (White, Black, Other or Multiple, Hispanic)<br>
26. sex: Respondent's sex (Female, Male)<br>
27. income_level: Annual income of the respondent as per the 2008 poverty Census (<=75000−AbovePoverty, >75000−AbovePoverty, >75000, Below Poverty)<br>
28. marital_status: Respondent's marital status (Not Married, Married)<br>
29. housing_status: Respondent's housing status (Own, Rent)<br>
30. employment: Respondent's employment status (Not in Labor Force, Employed, Unemployed)<br>
31. census_msa: Residence of the respondent with the MSA (metropolitan statistical area) (Non-MSA, MSA-Not Principle, City MSA-Principle city) (Yes, No)<br>
32. no_of_adults: Number of adults in the respondent's house (0, 1, 2, 3)<br>
33. no_of_children: Number of children in the respondent's house (0, 1, 2, 3)<br>
34. h1n1_vaccine (Dependent variable): Did the respondent receive the H1N1 vaccine or not (1, 0) (Yes, No)<br>

### Scope
This project will involve the following steps:<br>
**Data Pre-processing**: We will understand the basic structure and perform necessary data cleaning, handling missing values, handling duplicate values.<br>
**Exploratory Data Analysis (EDA)**: We will conduct an initial exploration of the dataset to perform Univariate, Bivariate, Multivariate Analysis and find patterns in the data. Also, we will treat outliers. <br>
**Training Models**: We have created user-defined functions which will ease our process of training dataset. We will train multiple Machine learning algorithms like Logistic Regression, Decision Tree, Random Forest, Bagging, AdaBoost, XGBoost, Naive Bayes, KNN, SVM with different tunning parameters to predict the likelihood of individuals taking the H1N1 flu vaccine based on the provided features.<br>
**Model Evaluation**: We will tabulate and evaluate the performance of all trained models using appropriate evaluation metrics and assess their predictive capabilities.<br>
**Learning Outcome**: Through this project, you will gain a better understanding of exploratory data analysis, data preprocessing, and knowledge of various machine learning algorithms. You will also develop skills in model evaluation, and drawing insights from the results.<br>

### Conclusion
By completing this project, you will gain practical experience in applying machine learning techniques, specifically Logistic Regression, to predict the likelihood of individuals taking the H1N1 flu vaccine. You will also improve your data analysis and modeling skills, allowing you to tackle similar classification problems in the future. Happy learning and exploring the fascinating world of data science and machine learning!
