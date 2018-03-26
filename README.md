# Credit Sense

 <img src="/images/cs.png" width="150" align= "center"/>

A decentralised credit scoring service based on blockchain which employs deep learning to calculate an intelligent credit score based on the credit history, delinquencies and 73 other parameters which are usually accounted while calculating a comprehensive credit score.

A flow chart describing the overall application is as follows:

<p align="center">
  <img src="/images/model.png" width="800"/>
</p>

1. Each bank has a loan application portal through which loan applicants generally input their sensitive data and upload important documents such as income-tax returns. This data is then converted into a JSON file to be stored on the blockchain ledger.

2. The only entity that has access to this ledger during the whole process is the deep learning model. This model removes the need of feature engineering and helps us find optimal features from more than 73 features which go into consideration such as annual income, number of delinquencies etc. Upon careful feature engineering, these features to a logistic regression model which then computes the probability with which the specific applicant will default on the loan.

3. Once the credit score is computed, it is then displayed on the dashboard with other useful data analysis such as the previous history of loan applicants who fell in the same credit score range, income bracket, home ownership status etc. This dashboard is powered by Microsoft Azure Data Lake Analytics and Microsoft Power BI which makes it easier for the user makes sense out of the data being processed.

4. The final step is more like an extension which works in the backdrop. Eventually, if the loan gets approved and the applicant either pays the amount or defaults, this information is fed to a reinforced machine learning model which learns that from the specific parameters and tries to understand what are specific factors which make applicants more likely to default. Thereby, the model learns from its own predictions and gets better with time as and when data is fed to it.

<b> Try having a look at our presentation for the project under presentation folder in the repository </b>

# System Technicalities

We have a deployable prototype of our solution already running. We also have a made short walkthrough video of the system which can be seen on: https://vimeo.com/253112175

The solution has 4 layers which includes:

<b>The Integrated front-end:</b> This is the layer with which the applicant interacts. The front-end is the place where the applicant submits his details and documents such as income tax report, employment history, mortgage status, etc. to the system which can be linked with the bank’s online banking facilities. This form data is actually converted into JSON format and lodged into the blockchain ledger with the hkid number as an identifier of the person. This hkid no is actually encrypted (hashed) so that the anonymity is maintained but identification isn’t lost. This no can be decrypted anytime by the software on the bank’s node. The front-end is created majorly using HTML, CSS and JavaScript.

<b>The Blockchain architecture:</b> Blockchain is the very base of our application architecture. The application stands due to the very reason that no one is in control of the system as a central manager which can be achieved through the blockchain. We are using ~~Private Ethereum Consortium Network~~ MultiChain to achieve this architecture which provides a secure private blockchain network in which each bank is a mining node which can access the whole blockchain ledger to access the data shared among all the banks which can also be accessed by the machine learning node where our reinforced machine learning model is deployed to return the most accurate credit score. The blockchain is connected to the frontend using Python Flask API. Flask also comes into play when the credit score is returned to the frontend of the bank for bank’s further processing.

#### Setup (Designed for Microsoft Azure)
###### Virtual Machine Setup (For Microsoft Azure)
1. Using Microsoft azure portal -> Login to your account -> Create a resource -> From Popular select Ubunutu Server 17.10 VM
2. Enter the VM username and password -> select disk size HDD Standard D2S_V3 -> Wait for auto validation and submit deployment
###### Creating the nodes (One node per Virtual Machine)
###### Create the Master-Machine Learning Node
1. In the Azure Portal allow go to the deployed virtual machine and ssh into the machine by clicking on connect and running the ssh command `ssh username@IP`. Enter the VM password during the setup and after successful login you should see `Welcome to Ubuntu 17.10 (GNU/Linux 4.13.0-37-generic x86_64)`

2. Create the Machine Learning Master Node and set up a fresh Blockchain network by running the command: `curl -s https://raw.githubusercontent.com/piy0999/CreditSense/master/bank_node/setup_master.sh | bash /dev/stdin`

3. Enter OK whenever prompted by Ubuntu and the installation using shell script should begin which takes around 4 minutes. 

4. After Successful installation the flask server initiates with message `Running on http://0.0.0.0:5000/`

5. In the Azure Portal allow the ports to accept incoming connection. Go to the Azure portal Virtual Machine Dashboard

6. Click on the networking tab -> Add inbound port rule. Inside the inbound port rule dialog type in port_ranges 5000 (This allows the API to listen to requests)

7. Create another port rule by clicking Add inbound port rule and inside the inbound port rule dialog type in port_ranges <b> Blockchain Port </b> (This allows the connection with blockchain). The Blockchain Port can be found inside the terminal in the message `Connect to chain1@10.0.0.4:2761 from other nodes` returned just before the message `9. Starting flask server...`. In this case the Blockchain Port is 2761. 

<p align="center">
  <img src="/images/ML-Final.png" width="800"/>
</p>

8. Now Setup another node inside the blockchain for further process. Remember to store the <b> chain address </b> with you for further processing which can be found before the `Connect to chain1@10.0.0.4:2761 from other nodes` message. In this case, it is `90c123532b29b4b07b3c072cab67502eabc64531804cb1aa3c741f03bd628dc3`. Please refer to the image for a better understanding. 

9. Use Ctrl-C and after <b> Granting the permission to node </b> press Ctrl-C again. 
###### Create the Bank Node
Please setup a new Virtual Machine on Azure before starting the further process using Virtual Machine Setup guide above.
In the Azure Portal allow go to the deployed virtual machine and ssh into the machine by clicking on connect and running the ssh command `ssh username@IP`. Enter the VM password during the setup and after successful login you should see `Welcome to Ubuntu 17.10 (GNU/Linux 4.13.0-37-generic x86_64)`

1. In the Azure Portal allow the ports to accept incoming connection. Go to the Azure portal Virtual Machine Dashboard

2. Click on the networking tab -> Add inbound port rule. Inside the inbound port rule dialog type in port_ranges 5000 (This allows the API to listen to requests)

3. Click on the networking tab -> Add inbound port rule. Inside the inbound port rule dialog type in port_ranges 80 (This allows the Frontend to run)

4. Create another port rule by clicking Add inbound port rule and inside the inbound port rule dialog type in port_ranges <b> Blockchain Port </b> found during the process of creating Master ML Node (This allows the connection with blockchain)

5. To join existing network, get IP address (IP address is the IP address of the Virtual Machine running the Master-ML Node) and port (Port is the <b> Blockchain Port </b> found during the process of creating Master ML Node) , run the following command by replacing the IP and PORT as specified above. `curl -s https://raw.githubusercontent.com/piy0999/CreditSense/master/bank_node/setup_node.sh | bash /dev/stdin IP:PORT`

6. Enter OK whenever prompted by Ubuntu and the installation using shell script should begin which takes around 4 minutes.

7. After finishing the setup you should see the message `frontend@0.0.0 start`. 

8. Scroll up inside the terminal until you see the message `9. Starting flask server...` and right above this message the node address is found in the message `Get 60% consensus from the network to grant admin permissions to your address 1BBpVCYkmwWEEGz3MfyAT5G18Fy3ByC7JD2uNd`. Save this address.  

<p align="center">
  <img src="/images/node.png" width="800"/>
</p>

9. Now permission is needed to join the network from the master Machine Learning node. Please follow the instructions for granting the permission to the node found below. 

###### Grant Permissions to bank node
1. Inside the Master-ML node type `multichain-cli chain1` and then type `getaddresses`. 
2. Copy the address returned without the double quotes and then type `grant from address(found using above getaddresses command) nodeaddress (sent by the node) admin`. 
3. If a transaction id is returned then there is no error and the node has been made an admin. 

###### Run the frontend from the bank node
Please do this process after successfully setting up the Master-ML node and the bank node. 
Let's Submit an application

1. Type `IP/user/apply_loan/` this is a sample application form which would be inside the bank's online banking portal. Just click on submit which generates a set of data and then sends it to the machine learning node. A dialog box saying `The Application has been received` appears on successful submission. 

<p align="center">
  <img src="/images/user-application.png" width="800"/>
</p>

2. After this type `IP/bank/dashboard/` which now shows the number of pending applications, approved applications and total number of applications being queried live from the blockchain. 

<p align="center">
  <img src="/images/bank-dashboard.png" width="800"/>
</p>

3. Now a bank can <b> Approve or Disapprove </b> the loan by clicking on Pending Applications tab and then selecting approve or disapprove from the list of applicants shown with their crypted IDs and credit scores. 

<p align="center">
  <img src="/images/bank-approve.png" width="800"/>
</p>

4. To generate the credit report of an applicant click on the Applicant data tab and enter the HKID (one of those which have been submitted using the apply_loan form above). This ID should be found from the chrome javascript console where the first parameter in the json object printed on the console is id (as random id's are being generated for testing purposes, it is possible to add your custom ID and data still). Use this ID (you can generate as many ID's and applications as possible) and enter on the Applicant data form which would result in returning of the credit score along with applicant's past applications history. 
To find the ID please refer to the screenshot:

<p align="center">
  <img src="/images/User-findID.png" width="800"/>
</p>

Enter the ID here:

<p align="center">
  <img src="/images/bank-report.png" width="800"/>
</p>

The final credit score is shown as:

<p align="center">
  <img src="/images/bank-creditscore.png" width="800"/>
</p>

# System Details

<b>The Machine Learning Node:</b> This node is the brain of the whole application as such. The process starts off with the deep learning model which consists of 2 layer neural network with 35 hidden neurons. The model removes the need to analyse each of the 73 factors and instead gives us the set of optimal features required to carry out the analysis with an improving accuracy of 92.71% (Currently migrating to RNN machine learning model with LSTM implementation). Upon finding the optimal features, the logistic regression model then accesses the data of those optimal features for the specific applicant on the ledger and then predicts the probability of the specific applicant to default on his loan. This analytics is further powered by Microsoft Azure Data Lake Analytics and Microsoft Power BI to create the necessary graphs and carry out the required analysis.

<b>Reinforced Learning:</b> This serves as an extension to the model that already resides on the machine learning node and exists to learn from the implications the real world had from the analysis it did. The deep reinforced learning allows the model to learn from the predictions it made and further analyse the features that caused the specific loan applicant to default on his loan and would look for a trend in similar loan applications. This enables banks to find similar loan applicant profiles and take counter measures accordingly to make a much safer investment.

# Why are we Different?

<b> Secure Anonymous Data Sharing - </b> Applicant data is shared by all the banks on a private blockchain ledger which maintains the security of the data due to a private network formation but at the same time does not contain any personal identifiers with the HKID number being hashed and stored on the block securely. Enabling faster, secure and anonymized data sharing.

<b> Decentralization removes the need for third party agencies like TransUnion - </b> As credit scoring can be done directly through the machine learning model with the training data from the banks as well as the current data provided by user on the decentralized system, there is no need for a centralized agency to actually maintain that data which saves the time and money for the banks to actually process the whole loan application.

<b> No hard coded credit score formula - </b> As we are implementing reinforced learning on our machine learning model we actually take into consideration in addition to our existing machine learning model parameters such as the employment history of the individual, the age but also when and in what time was the loan repaid and whether the applicant was able to repay or not. Through reinforced learning the calculation formula keeps getting better and this eliminates the need of a static mathematical formula.

# Our Target Customers

We have three main target customers:

<b> Banks → </b>Banks can directly receive user data for calculating credit score on spot from the user without the need of going through the process of TransUnion HK which reduces the time and trust that banks need to have on a third party credit score service provider.

<b> Loan Applicants → </b> Applicants can directly submit the requisite data required for credit score processing using the frontend integrated with the bank’s cyberbanking services with complete anonymity to the decentralized blockchain architecture.

<b> Government (i.e.: Financial regulators) → </b>  With the ease in acquiring a standardized credit score, governments could benefit from the increasingly accurate data by leveraging its ability to distinguish the financial capabilities of its citizens. Consequently, via data analyses, the government could derive or be one of the indicators to determine the economic stability of the region as a whole. This could be achieved by implementing a government node on the blockchain and having a specific machine learning model for their analysis in the form of anonymized data.

<b> Credit Sense makes Sense! </b>
