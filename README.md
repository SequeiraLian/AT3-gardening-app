# Year 12 Major Work: Compost Management App

## Project Description
This software is for gardeners to schedule and manage their compost bins. It includes a simple user interface, created on pygame, where the users can see what bins they need to flip on the main page. The bins are filtered using colours (a key is included), and new bins can be created by clicking on the plus button. Users can click on the calendar to select the initial creation date of the bin. 

### Justification of Technologies Used
I decided to create the user interface on pygame as I have had some previous experience with it. It allowed me to build upon my skills and utilise different features of the technology.

### Challenges I Faced
Time Management (for Part A/Coding): This was due to several factors, including procrastinating, and the large size of the project with a small time frame (around 6 weeks). To ensure that my time was used efficiently and effectively, I used available AI tools like Chat-GPT to build the majority of my user interface, which I had the least experience building. I also didn't include some features within my project, such as a log-in page and an insights page, as this wasn't the main focus or highest prioity of my project. 

Pygame: Despite using generative AI, I still struggled coding the pygame user interface. In this project, I have implemented an initial start to the user interface which includes a main screen and a key. I also created a button that creates a new bin, which leads to a pop-up window with a calendar. The bin number and the month is labelled at the top of the calendar, and the current date is highlighted. The user can select the initial creation date, and exit the page. The created bins appear on the main page as a circle with a number inside, which is the bin ID. If the bin is to be flipped that day, the circle will change colours from grey (not to be flipped), to yellow (to flip). 


### Features To Implement in the Future
- Log-in page to ensure data privacy and security
- Insights page to show productivity and bins flipped 
- Working user interface
    - To improve my project in the future, I would like to implement a function and event handling that allows the user to manually click and change the  colour of the bin, from 'to flip' to 'done.' Additionally, features such as ability to delete bins could be addded, as well as error handling, such as if a bin's status is incorrectly updated. 


## User Manual
In this repository, the main logic file is working_logic.py. The user, on Visual Studio Code, can easily interact with the program, as it will ask you for a number of inputs. 

To run this file, run 'python3 working_logic.py' in the terminal. 

## License
Public Domain 