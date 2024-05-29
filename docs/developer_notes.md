# Developer Notes

Description: This document is a record of regular (weekly) uodates to my prroject. It will describes the current task I am doing, any challenges I am facing, and upcoming goals/steps to do.

### Term 1 Week 11
Monday 08 April
- Received unofficial MW assessment notification
- Started putting together this documentation (Part B)

### Term 2 Week 3
Monday 13 May
- Worked on part B documentation:

    Documentation
    List and briefly explain 3 types of documentation that is essential for the software solution. Explain the purpose of each type of documentation and how you have implemented it.

    Documentation is an essential part of the software solution, especially in communicating ideas to clients and stakeholders. This can be presented in different ways, such as a log book document, user manual, and documentation strings or code commenting. 

    Log-Book Documentation
    A log book document, such as this one, is a helpful tool to explain and justify the choices made within the software development cycle. This could involve specific areas such as legal, social and ethical considerations that have been addressed while building the project, or creating a criteria to evaluate the effectiveness of the project in solving the required problem. 

    Furthermore, I have consistently tracked my progress in a markdown file (developer_notes.md). This is a record of regular (weekly) updates to my project. It describes the current task I am doing, any challenges I am facing, and upcoming goals/steps to do. This allows me to record ideas and reflect on the process and speed of development of the project. More so, it can act as proof of concept, progression and all my own work if required by a teacher or other stakeholders. 
    User Manual
    Clients may have trouble accessing, updating or using the project, as they may not have the required knowledge or experience to do so. Thus, it is useful and important to include a user manual; a document provided to a user that helps in using a particular system, product or service seamlessly. 

    I have implemented this documentation within my own project to help my client (Sona Dsouza) use the software efficiently and effectively in order to schedule and track her composting. 
    Documentation Strings (Code Comments)
    Software developers use code comments to describe the code to and for developers. The main intended audience are the maintainers and developers of the Python code. In conjunction with well-written code, comments help to guide the reader to better understand your code and its purpose and design. 

    Code comments are helpful in all stages of development:
    Planning and reviewing: When developing new portions of code, it may be appropriate to first write and use comments as a way of planning or outline that section of code. These comments can be later removed once the actual code has been implemented and reviewed/tested.
    Code Description: Comments can be used to explain the intent of specific sections of code
    Algorithm Description: When algorithms are used, especially complicated ones, it can be useful to explain how the algorithm works or how its implemented within your code. It may also be appropriate to describe why a specific algorithm was selected over another. 
    Tagging: Tagging can be used to label specific sections of code where known issues or areas of improvement are located. Some examples are: BUG, FIXME, and TODO. 

    I have utilised these commenting techniques within my own project, especially during the planning, development and execution of the written code. 
- Created python files for modules (schedule, tracker, display, archive) and main file
- Started working on "Legal, Social and Ethical Considerations"
- TODO: Legal, Social and Ethical Considerations

Wednesday 15 May
- Worked on part B documentation:
- Completed "Legal, Social and Ethical Considerations"

    Data Privacy & Security
    According to the 1988 Privacy Act, information systems containing personal information must legally be able to:
    - explain why personal information is being collected and how it will be used
    - provide individuals with access to their records
    - correct inaccurate information
    - divulge details of other organisations that may be provided with information from the system
    - describe to individuals the purpose of holding the information
    - describe the information held and how it is managed

    As part of this project, I will address these issues in my app. 

    Users will be asked to create an account to save and securely store their information within the app. This will be solely for the purpose of allowing users to access their records and past information; their information will not be shared with anyone else.
   
    Intellectual Property & Software Licensing
    A software licence is a document that provides legally binding guidelines for the use and distribution of software. The licence terms and conditions generally include:
    - how many times the software can be downloaded;
    - what the software will cost; and
    - what level of access users will have to the source code.

    My software will be classified with a public domain licence. This software is freely available, and anyone can use, change or incorporate code from it into an application. However, businesses should use caution as altered code may not meet enterprise quality and security standards. 

    Artificial Intelligence (AI) 
    The use of artificial intelligence (AI) has increased in the past year due to new innovations and technological advancements, including Chat-GPT and other open source software. This has led to a myriad of legal, social and ethical implications, especially in the education sector. Students and users have found AI to be a helpful tool in writing documents, however are now being accused of using it as a plagiarism tool and a breach of “All my own work” standards as they are not referencing it within their work. Other implications include areas surrounding responsibility, inclusion, social cohesion, autonomy, safety, bias, accountability, and environmental impacts.

    In this project, Chat-GPT will be used as a tool to help me code my software in Part A, as well as brainstorming ideas and writing responses for the Part B documentation. However, I will reference these within my work, and re-word responses when necessary. 

Thursday 16 May
- Worked on part B documentation:
- Completed "Project Management"

    Gantt Chart
    A Gantt chart is a horizontal bar chart used by project managers to visualise project tasks and the timeline required to complete each one. They usually consist of 3 components: The tasks of a project, the start date and end date of each task. They are helpful for tracking the progress of a project, ensuring that developers can complete it within the budget and time. It’s a useful tool developers can use alongside most techniques, especially for projects with a lot of dependencies. 

    Creating a Gantt chart has allowed me to break down the project into smaller, manageable modules and setting goals/completion dates. This has allowed me to maximise my time efficiently, and clearly visualise and track my progress. A copy of my Gantt chart is below:

    Agile Development 
    For this project, I have chosen to use the agile approach. The agile methodology is an iterative approach to managing software development projects that focuses on continuous releases (in the form of sprints) and customer feedback. This allows developers to work closely with their clients throughout the development phase. 

    The agile approach also responds well to changing user requirements and specifications, as it consists of working in sprints. This flexibility is vital, as this project must provide a working and user-friendly software application for my mum and other like-minded gardeners. 

    Other advantages to this approach include:
    - Increased quality of product: The agile approach is an iterative process, allowing for developers to continually grow with time and continually improve their products. 
    - Consumer satisfaction: In the traditional framework, the customer is only involved in the planning phase. By closely communicating with the customer and making changes according to their feedback, developers are able to better deliver the product to the customer and ensure that the final product is suitable according to their requirements. 
    Better control: The agile approach allows developers to have better control over the project due to its transparency, feedback integration and quality control features. 
    - Improved project predictability: The agile framework allows developers to identify and predict risks, thus increasing their ability to plan to ensure that the project runs smoothly
    - Reduced risks: Agile works in small sprints that focus on continuous delivery. Hence, there is always a salvageable part that can be used in the future, even if a particular approach doesn’t go as planned.
    
    Modular Programming
    Modular programming is a project management tool and software design technique that emphasises separating the functionality of a program into independent modules. Each module executes one aspect of the desired functionality.  

    I have utilised modules within my own project in order to break down the task and focus on specific functions, as shown below.

    - Schedule Module: Forecasts days to flip the bin
    - Tracking Module: Records bins when they are flipped
    - Display Module: Shows information to user on the app
    - Archive Module: Store transactions after bin cycle is completed
- Started working on "Schedule Module":

    #This module is given an input date from the user. Every 2 days from the given date, the bin must be flipped. These days must be recorded. 7 dates must be given back to the user. 

    #import
    import datetime

    #ask user for first date
    initial_date = input("Enter initial date in the format YYYY-MM-DD: ")

    #check that date is given in correct format   

    #calculate every 2 days from given date
    scheduled_date = datetime.datetime.today() + datetime.timedelta(days=2)
    print (scheduled_date)


    #repeat 7 times

    #print 7 dates 

### Term 2 Week 4
- Worked on part B documentation - collaborative approach
    Throughout the development of my software solution, I have involved key stakeholders. For example, I have consulted with my client (my mum) who is an avid gardener and composter, specifically in the different sections such as defining the problem, and the planning and designing of the software. This has allowed me to clearly identify and solve the problem, thus developing a solution that fits with the client’s needs and vision.  

    Another key stakeholder I have consulted is my teacher, Mr Groom. This has allowed me to gain information and help from someone with more coding/software experience, allowing me to make more informed decisions about my project. For example, I was initially planning on making a mobile application, as this would be most convenient and efficient for the user. However, I do not have the available time nor the skills to make the project in this format, so I decided to use pygame to make the user interface. 

    I have also collaborated with Ananya in the documentation of this project. This has sparked new ideas and allowed me to construct more cohesive responses. I have also used my Dad’s help in the front and back end development of my actual code, which has improved the quality of the software solution, increased efficiency (both through the run time of the code, and the time taken to build the software), and solving problems and bugs within the code.  

### Term 2 Week 5
- Work on part B documentation - user interface design
    Text Font & Size
    Fonts should be used appropriately within software solutions. The use of fancy fonts can decrease usability considerably, as well as multiple (more than 3) fonts on a single page. In my software solution, I have used fonts that are easy to read, and are consistent across the software.
