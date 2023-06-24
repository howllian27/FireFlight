<p align="center">
    <img src = "./assets/logo.png"" style="vertical-align:middle" width="400">
</p>
<p align="center">
  <b>FireFlight</b>
</p>

<p align="center">
  <i>Your Travel Companion for Sparking Connections</i>
</p>
<p>&nbsp;</p>
<h1 align="center">📖 A Guide to FireFlight </h1>
<p> <b> FireFlight </b>  is an application that aspires to bring a fresh perspective to the travel and aviation industry. Our platform is designed to connect like-minded travelers, fostering a community that shares a passion for exploration and adventure. With Fireflight, users can find their perfect travel companion, making their journey more enjoyable and memorable. <a href="http://fireflightapp.com/"> </a>Click here to visit our website! </a> </p>
<p>&nbsp;</p>
<h1>⚙️ Technology Stack </h1>
<div align="center">
<p align="center">
  <kbd>
      <img height="60" src="./assets/mysql.png">
  </kbd>
  <kbd>
      <img height="60" src="./assets/pytorch.png">
  </kbd>
  <kbd>
      <img height="60" src="./assets/maps.png">
  </kbd>
  <kbd>
      <img height="60" src="./assets/networkX.png">
  </kbd>
  <kbd>
      <img height="60" src="./assets/bert.png">
  </kbd>
  <kbd>
      <img height="60" src="./assets/docker.png">
  </kbd>
  <kbd>
      <img height="60" src="./assets/aws.png">
  </kbd>
  <br></br>
  <b> MySQL | PyTorch | Google Maps | NetworkX | BERT | Docker | AWS </b>
</p>
</div>
<p>&nbsp;</p>
<h1>📽️ Demo Video </h1>
<img height="500" src="./assets/mockups/home.png">
<p>&nbsp;</p>
<h1>🔨 Core Functionalities </h1>
<p><b>1. User Profiles</b></p>
<img height="500" src="./assets/mockups/profile_creation.png">
<p>Users can create personalized profiles, including a self-made bio to introduce themselves. Our matchmaking algorithm will subsequently compare this bio to other users' bios to find the most compatible travel companions for our users. Users may also indicate their own personal interests, such that they may be matched with other users based on common interests.</p>
<p><b>2. Matchmaking Algorithm</b></p>
<img height="300" src="./assets/mockups/matches.png">
<p>Fireflight uses a sophisticated matchmaking algorithm that takes into account user preferences, shared interests, and other factors to suggest potential matches. The algorithm leverages machine learning and natural language processing to provide highly customised match suggestions.</p>
<p><b>3. Shared Travel Platform</b></p>
<img height="300" src="./assets/mockups/attractions.png">
<p>Our application acts as not only one that connects like-minded travelers together but also a one-stop platform where travelers can even make future plans for their trips. Once potential matches are formed, users can connect to each other within the app and a recommendation engine will recommend a series of attractions to the matched users. The attractions will be recommended based on their proximity from each of their hotels and shared interests.</p>
<p><b>3. Chat Platform with Real-Time Translation & Travel Chatbot </b></p>
<img height="300" src="./assets/mockups/chat.png">
<p>Our chat platform allows matched users to communicate with each other prior to the trip. It also has built-in real-time translation to connect users from different countries speaking different languages. For quick travel inqueries, users may also use our travel chatbot powered by ChatGPT. </p>
<h1> Our Enterprise Architecture </h1>
<img height = "400" src="./assets/arch.png">
<p><b>1. Presentation Layer </b></p>
<p>The presentation layer refers to the user interface of the application, including the website that travelers interact with. It aims to provide a seamless and user-friendly experience for solo travelers to connect with potential companions. We have also infused a storyline with engaging and interactive animations to enhance the customer journey. </p>
<p><b>2. Storage Layer </b></p>
<p>The storage layer in FireFlight encompasses the MySQL database used to store user profiles, preferences, and other relevant data. It ensures secure and efficient storage and retrieval of information to support the application's functionalities.</p>
<p><b>3. Data Access Layer </b></p>
<p>The data access layer in FireFlight manages the interaction between the application and the underlying data sources. It includes components like APIs, database connectors, and data access patterns that allow the application to retrieve and update user data from storage. We mainly use NetworkX to add users to a graph and calculate correlations in interests from there. In processing map data, we used the Google Maps API to find the closest relevant attractions for the user to visit. </p>
<p><b>4. Machine Learning Layer</b></p>
<p>The ML layer in FireFlight incorporates a thorough machine learning algorithm and model created with the aid of PyTorch to enhance the matching and recommendation capabilities of the application. It leverages user preferences, interests, and other relevant data to provide personalized suggestions for travel companions. Furthermore, we also utilised the BERT model to analyse compatabitility through user sentiments and speech patterns in their bios and thereby match them with other users. The combined effect of both the ML algorithm & model as well as the BERT model allow us to calculate a compatibility score between a pair of users, a score deeply enhanced by analysing user data. </p>
<p><b>5. CI/CD Pipeline</b></p>
<p>The CI/CD pipeline implemented for your project utilizes the integration between GitHub, AWS EC2, and Docker to enable a streamlined software delivery process. It involves code development and version control on GitHub, automated builds and tests through CI, containerization with Docker, and deployment to AWS EC2 instances. The pipeline ensures continuous delivery of reliable and scalable applications, empowering efficient development and deployment workflows.</p>
<h1> Our User Flow Chart </h1>
<img height = "700" src="./assets/user_flow_chart.png">
<h1> The Team </h1>
<table>
  <tr>
    <th><img width="180px" src="./assets/pics/howell.png"></th>
    <th><img width="180px" src="./assets/pics/eunice.jpg"></th>
    <th><img width="180px" src="./assets/pics/cl.jpg"></th>
    <th><img width="180px" src="./assets/pics/wei_hong.png"></th>
  </tr>
  <tr>
    <td align="center"><h3><b><a href="https://github.com/howllian27">Howell Chan</a></b></h3><p><i>Nanyang Technological University</i></p></td>
    <td align="center"><h3><b><a href="https://github.com/XeuniceX">Eunice Lee</a></b></h3><p><i>Nanyang Technological University</i></p></td>
    <td align="center"><h3><b><a href="https://github.com/chenglin2003">Cheng Lin</a></b></h3><p><i>Nanyang Technological University</i></p></td>
    <td align="center"><h3><b><a href="https://github.com/tayweihong">Tay Wei Hong</a></b></h3><p><i>Nanyang Technological University</i></p></td>
  </tr>
  <tr>
    <td align="center"><h3><b><p>Backend Developer</p></b></h3></td>
    <td align="center"><h3><b><p>Frontend Developer</p></b></h3></td>
    <td align="center"><h3><b><p>UI/UX Designer</p></b></h3></td>
    <td align="center"><h3><b><p>Web API Developer</p></b></h3></td>
  </tr>
</table>
