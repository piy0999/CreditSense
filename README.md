# Credit Sense 
 <img src="/images/cs.png" width="150" align= "center"/>


A decentralised credit scoring service based on blockchain which employes deep learning to calculate an intelligent credit score based on the credit history, deliquencies and 73 other parameters which are usually accounted while calculating a comprehensive credit score.

A flow chart describing the overall application is as follows:

<p align="center">
  <img src="/images/model.png" width="800"/>
</p>

1. Each bank has a loan application portal through which loan applicants generally input their sensitive data and upload important documents such as income-tax returns. This data is then converted into a JSON file to be stored on the blockchain ledger. 

2. The only entity that has access to this ledger during the whole process is the deep learning model. This model removes the need of feature engineering and helps us find optimal features from more than 73 features which go into consideration such as annual income, number of delinquencies etc. Upon careful feature engineering, these features to a logistic regression model which then computes the probability with which the specific applicant will default on the loan.

3. Once the credit score is computed, it is then displayed on the dashboard with other useful data analysis such as the previous history of loan applicants who fell in the same credit score range, income bracket, home ownership status etc. This dashboard is powered by Microsoft Azure Data Lake Analytics and Microsoft Power BI which makes it easier for the user makes sense out of the data being processed. 

4. The final step is more like an extension which works in the backdrop. Eventually, if the loan gets approved and the applicant either pays the amount or defaults, this information is fed to a reinforced machine learning model which learns that from the specific parameters and tries to understand what are specific factors which make applicants more likely to default. Thereby, the model learns from its own predictions and gets better with time as and when data is fed to it. 


# System Technicalities

We have a deployable prototype of our solution already running. We also have a made short walkthrough video of the system which can be seen on: https://vimeo.com/253112175

The solution has 4 layers which includes:

The Integrated front-end: This is the layer with which the applicant interacts. The front-end is the place where the applicant submits his details and documents such as income tax report, employment history, mortgage status, etc. to the system which can be linked with the bank’s online banking facilities. This form data is actually converted into JSON format and lodged into the blockchain ledger with the hkid number as an identifier of the person. This hkid no is actually encrypted (hashed) so that the anonymity is maintained but identification isn’t lost. This no can be decrypted anytime by the software on the bank’s node. The front-end is created majorly using HTML, CSS and JavaScript. 

The Blockchain architecture: Blockchain is the very base of our application architecture. The application stands due to the very reason that no one is in control of the system as a central manager which can be achieved through the blockchain. We are using Ethereum Consortium Network (upgrading to MultiChain now) to achieve this architecture which provides a secure private blockchain network in which each bank is a mining node which can access the whole blockchain ledger to access the data shared among all the banks which can also be accessed by the machine learning node where our reinforced machine learning model is deployed to return the most accurate credit score. The blockchain is connected to the frontend using Python Flask API. Flask also comes into play when the credit score is returned to the frontend of the bank for bank’s further processing. 

The Machine Learning Node:  This node is the brain of the whole application as such. The process starts off with the deep learning model which consists of 2 layer neural network with 35 hidden neurons. The model removes the need to analyse each of the 73 factors and instead gives us the set of optimal features required to carry out the analysis with an improving accuracy of 92.71% (Currently migrating to RNN machine learning model with LSTM implementation). Upon finding the optimal features, the logistic regression model then accesses the data of those optimal features for the specific applicant on the ledger and then predicts the probability of the specific applicant to default on his loan. This analytics is further powered by Microsoft Azure Data Lake Analytics and Microsoft Power BI to create the necessary graphs and carry out the required analysis. 

Reinforced Learning:  This serves as an extension to the model that already resides on the machine learning node and exists to learn from the implications the real world had from the analysis it did. The deep reinforced learning allows the model to learn from the predictions it made and further analyse the features that caused the specific loan applicant to default on his loan and would look for a trend in similar loan applications. This enables banks to find similar loan applicant profiles and take counter measures accordingly to make a much safer investment.  

# Why are we Different?

Secure Anonymous Data Sharing - Applicant data is shared by all the banks on a private blockchain ledger which maintains the security of the data due to a private network formation but at the same time does not contain any personal identifiers with the HKID number being hashed and stored on the block securely. Enabling faster, secure and anonymized data sharing.


Decentralization removes the need for third party agencies like TransUnion - As credit scoring can be done directly through the machine learning model with the training data from the banks as well as the current data provided by user on the decentralized system, there is no need for a centralized agency to actually maintain that data which saves the time and money for the banks to actually process the whole loan application.


No hard coded credit score formula - As we are implementing reinforced learning on our machine learning model we actually take into consideration in addition to our existing machine learning model parameters such as the employment history of the individual, the age but also when and in what time was the loan repaid and whether the applicant was able to repay or not. Through reinforced learning the calculation formula keeps getting better and this eliminates the need of a static mathematical formula. 


# Our Target Customers

We have three main target customers: 

Banks → Banks can directly receive user data for calculating credit score on spot from the user without the need of going through the process of TransUnion HK which reduces the time and trust that banks need to have on a third party credit score service provider.  

Loan Applicants → Applicants can directly submit the requisite data required for credit score processing using the frontend integrated with the bank’s cyberbanking services with complete anonymity to the decentralized blockchain architecture.

Government (i.e.: Financial regulators) → With the ease in acquiring a standardized credit score, governments could benefit from the increasingly accurate data by leveraging its ability to distinguish the financial capabilities of its citizens. Consequently, via data analyses, the government could derive or be one of the indicators to determine the economic stability of the region as a whole. This could be achieved by implementing a government node on the blockchain and having a specific machine learning model for their analysis in the form of anonymized data. 


Credit Sense makes Sense!


