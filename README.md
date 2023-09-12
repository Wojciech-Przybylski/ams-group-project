# ams-group-project
AMS group project repo for Team Metaelectric Space Llamas

## Project Case Study 

QA Cinemas is an industry-recognised cinema chain that has been in the cinema and film business for over 20 years after being founded in 2004. The cinemas specialize in both new releases and special showings of classics films from the 60’s until the 90’s and has seen large success in the Northwest of England. The business plan on branching out nationally within the next coming years, but they wish to ensure that their online presence has further investment prior to expansion; they would like their brand to be known and visited. 

Currently, the online presence of QA Cinemas relies entirely on social media-driven pages that are purely for promotion and marketing. However, with the lack of dedicated social media team, their socials have been cast to the wayside and subsequently ignored for the last 7-8 months. Due to this, they have seen a downtick in interest, especially on screenings for the classic film showing they host.
Before QA Cinemas re-launch their social media strategy, they have decided that they wish to foray into the online booking world, with a custom website for their business to be developed showcasing who they are and what they do, their screenings and opening times, and of course, the ability to book tickets online. 

QA Cinemas had a previous consultation with a business transformation group that suggested that a website for online booking was a key method of growth within region and has suggested the prioritisation of this project over all other business endeavours. This means that their other areas of expansion, such as the opening of a new café and indoor arcade, have paused. 
The previous consultants also mentioned the need of DevOps within the infrastructure of this site; the ability to quickly automate and roll out new versions of a tested application for changes that need to be made. Whilst QA Cinemas don’t fully understand the technical aspects of this, they have had the benefits of automated builds and containers explained to them and are very keen to have this implemented alongside the site.
 


## Installation

These are the basic installations statements need to connect to the group repoistory and to successfully launch the webpage. 
This is assuming that all members of the group have been invited as contributors to the Github repoistory. 
As this project will be utlising feature branches, git pull is a command that will need to be used regularly to ensure that each group members local machine is up to date with the repo.

```bash
git clone https://github.com/jamesbryer/ams-group-project
cd ams-group-project
pip3 install -r requirements.txt
python3 create.py
python3 app.py
git pull

```

## The MVP (The Minimum Viable Product) 

### This MVP contains the user stories and the acceptance criteria according to our projects specification.

- Home Page:
   
    - Should describe QA Cinemas as a brand as well as this the home page needs to be well-designed and aesthetically   pleasing/accessible. 
    - Home page must be the default for the entire site and other pages should be accessible from here.

- Login Page:
    
    - Login page should be accessible from the home page at the very minimum. 
    - Should be accessible at the top right of the screen on all pages.
    - existing accounts should be able to login and new accounts created via a signup form.

- Listing Gallery:
   
    - Gallery should be accessible via overall site navigation.
    - It must feature at least 4 different movie images.
    - Each Image should appear on its own page with information regarding the movie - Title, actors, director and showing times.

- Opening Times:

    - Must be part of overall site navigation.
    - Page must have details of the opening times of the cinema.

- New Releases Gallery:

    - New release gallery must be part of overall navigation.
    - Must confine to the same image and information rules as the listing gallery.

- Classification: 

    - Part of the overall site navigation. 
    - Must follow standard film classifications and icons.
    - page must include any other relevant facts to classification system.

- Screens:

    - Should include seating plan and decor of both standard and deluxe screens.

- Ticket Bookings:

    - When booking a ticket bookings should include, movie title, screening date, time, number of seats, name of booker and ticket type, as well as concession 

- Payment:

    - Payment page should gather - card holder name, card number, expiry date, CVC.

- Cinema Services:

    - Part of overall site navigation. 
    - Should include prices for food and drink. 
    - feature upcoming cafe and arcade.

- Discussion Board:

    - Users can comment on a forum part of the sites navigation. 
    - content of the forum must be moderated for innappropriate content.

- Search:

    - Search bar allowing users to search keywords - with relevant links being returned. 

- About Page:

    - Part of overall site navigation.
    - The name and a small paragraph on all the team members.
    - Basic contact information and information on who QA cinemas are.

### General Design Asks

- Background colour of site should not be white on any of the pages.
- Site navigation should be user friendly and availble on all pages of the site.

### Website Wishlist

- Page header and footer, available on all pages.
- A custom logo for QA Cinemas.

## Problems Faced

### 05/09/2023

- One group member had an emergency that meant that they had to leave early. This is something we accounted for in the risk assessment for this project. In order to tackle this issue, the group member who had to leave prepared a short handover to inform the rest of the group of the work that they had been doing, so that a seamless transfer of work could be made.

### 06/09/2023

- One Group member had a differing password for MySQL this meant that when running the app this member was considered unauthorised and could not get into the website. The current solution for this is for the group member to manually input their password to the __init__.py file and then run the create.py file. This then gave the group member access to the site. However, it is also vital that this password change is not pushed to Github as this will mean all other members will no longer have site access.

- One group member ran into issues with reverse proxying the docker-composed images during deployment. In order to fix this the group member exposed the ports in the docker-compose file in the cinema-app section. This issue has also been recorded on the trello board for the project.

### 07/09/2023

- Several group members during development have had issues with the create.py file not correctly dropping the tables within the SQL database. This seemingly occurs where certain relationships that weren't needed have been removed. This then stops certain tables from being dropped correctly. In order to fix this, the schema must be deleted from the MySQL workbench, then the create.py file can be executed again and the database will completely rebuild itself.

- One group member was having an issue getting some HTML and CSS code working for the Home and About pages of the website. In order to tackle this several group members peer-reviewed the work and came to the conclusion that their was an issue with the file structure within the home-page branch causing the HTML and CSS to not appear correectly. Furthermore the group members in the peer review concluded that their needed to be some image resizing within the home-page before it can be pushed to the main branch.

### 08/09/2023

- One group member came across an issue with the deployment of the database using several CI/CD tools. After a diiscussion with the group after our morning SCRUM meeting we came to the conclusion to move away from this issue for now. As a group we concluded that other areas of this project need to take priority, on top of this their is a risk that pursuing this issue could take us far out of scope for this project.

- Two group members came across an issue withe the ticket booking system, specifically with the maximum amount of tickets able to be bought. This was an important issue to fix because if the user was able to buy too many tickets this could break the whole database.

### 11/09/2023

- The group came across an issue with the footer. Whilst the footer was functioning as it should on most pages, the addition of the search page on the site raised an issue with the footer. Seemingingly tbe footer would sometimes not move around the page correctly and cover up certain search results, if their were enough in a certain search. In order to fix this, several group members discussed what caused this issue. After consideration, some minor changes were made to the HTML and CSS for the footer, this allowed for the positioning footer to adjust correctly, depending on the number of search results.

## Development Methodology 

### Kanban Board 

For this project our group used a Kanban board via Trello to more easily display and communicate our user stories and specification. Making this Kanban board was one of the first tasks that we undertook. In a group scenario this helped us easily distribute and prioritise different tasks. Each group member has made sure to keep up to date with the Trello board, by showing tasks as complete, adding comments or images to the individual tasks or user stories. There were some minor difficulties initially with the Kanban board. For this project the specification stated that we had to use Trello rather than Jira, none of the group members had used Trello before. However we quickly managed to figure out the interface of Trello and were able to put our Kanban board together. There are a number of examples of the progress of our Trello board within the documentation screenshots folder, however an example of this will be placed below:

![Example of Trellp Board](/Documentation-Screenshots/Trello/Trello%201.png)

### Scrum 

Scrum is an agile framework typically used for the completeion of complex work. It is typically considered the leading agile development methodology. Therefore as a group we saw it best to utilise Scrum during this project. Whilst we could technically integrate scrum into our individual projects for the sole purpose of experience, on an individual level scrum as a development methodology only really works in a group environment, therefore, our group has not had much if any experience utilising scrum. The first major implementation of scrum that the group has taken onboard is the daily standup meeting. Each morning we discuss with each other and the trainer, what we achieved the previous day and what we plan to achieve today. Problems faced or blockages can also be brought up during the daily standup where we can agree as a team on the best course of action.

### Sprint 1

During the intiial sprint for this this project we tackled three main tasks. Firstly we set up the first draft of the Trello board, splitting the different tasks into the MVP and website wishlist that were outlined in the project specification, we later added several more tasks to the board and made sure to keep up-to-date with the board, throughout all sprints. At the same time several group members began to design the basic file structure within Visual Studio Code. As we have been taguht best practice for a file structure when designing a website we were all able to utilise our file structures from our idividual projects to conclude what structure would work best in this group scenario. During later sprints we would add extra folders to the file structure from some of the feature branches that were also created later. The final task of our first srpint was the devise the risk assessment for the project this included risks for users and developers. We believed this was important to tackle during the first sprint, so we would have a much more in depth understanding of the risks we were facing during this project and how best to minimize them.

### Sprint 2

During the second sprint we began adding the basic content to several of the files that were previously added when creating the file structure. This included: app.py, create.py, requirements.txt, routes.py, models.py, __init__.py as well as adding the basic content to numerous html files that were to be worked on later. After this the group split in to three groups, two people were going to work on generating the first iteration of the database as well as working on other aspects of the backend, another group of two were beginning to work on the HTML files, starting with the homepage, and finally the final member of the group was to work on installing jenkins and setting up the necessary AWS instances. At several points during this sprint the group reconvened to discuss progress or any problems that they had ran into.

### Sprint 3 

During the third sprint we developed the majority of the back and front end of the code as well as integrating the automated deployment of the app. Our goal for this sprint was to reach the criteria of the MVP so we could focus on testing and the website wishlist. We wanted to reach this goal by the end of the first week of the project. We concluded as a group, that this was the best strategy to make sure that we would have time to go through thorough testing and bug fixes. Furthermore, by reaching this goal we would have more time to style the website up to the standard the specification requires, and beyond. In order to meet this goal, we discussed our strengths and weaknesses in the group and divided the tasks accordingly. On top of this, we concluded that, it would be best during this sprint to start, and keep on top of the write up for this project. Rather than it becoming a much more overwhelming task later down the line. 

### Sprint 4 



## ERD (Entity Relationship Diagram)

### This entity relationship diagram was devised using the principles of relational databases and normalisation

![Entity Relationship Diagram](/Documentation-Screenshots/SQL/ERD.png)

### An updated version of the ERD with the inclusion of the cart_item and ticket_type tables. This is to show the progress and development of our groups database:

![Entity Relationship Diagram 2](/Documentation-Screenshots/SQL/ERD%202.png)

### Update Three of ERD with the inclusion of Showings table:

![Entity Relationship Diagram](/Documentation-Screenshots/SQL/ERD%203.png)

## UML Diagram (Unified Modelling Language)

### A UML diagram is a diagram based on the UML (Unified Modeling Language) with the purpose of visually representing a system along with its main actors, roles, actions, artifacts or classes, in order to better understand, alter, maintain, or document information about the system.



## Risk Assessment 

| Facility/Activity            | Identify the hazards                                    | who/what may be harmed | risk likelihood | Severity of harm  | Overall risk | Existing control measures                                                                                                                             |
|------------------------------|---------------------------------------------------------|------------------------|-----------------|-------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technical Risks              | Data leaks                                              | Users                  | 3               | 5                 | 4            | Creating a proxy server to protect the data.                                                                                                          |
| Technical Risks              | data loss                                               | Users/Admins           | 3               | 5                 | 4            | Frequent Github pushes, good practice with data storage.                                                                                              |
| Technical Risks              | Infrastructure issues                                   | Admins                 | 4               | 5                 | 4.5          | Frequent manual check-ups for developers to minimise risk of introducing bugs.  Use available QA resources to guide us through the set-up of the app. |
| Technical Risks              | Tooling dependencies                                    | Admins                 | 3               | 5                 | 4            | Making sure the right tools are used in the right scenarios, and respective tools are to date.                                                        |
| Technical Risks              | integration challenges(software)                        | Admins                 | 2               | 4                 | 3            | Make sure the integration steps are implemented correctly.                                                                                            |
| Resource Risk                | Risk of availability                                    | Admins                 | 3               | 3                 | 3            | Hand over proceedures are in place.                                                                                                                   |
| Resource Risk                | Skill gap                                               | Admins                 | 3               | 3                 | 3            | Make sure the tasks are spread based on individual strengths. If there are any problems, ask for support from the team or trainer.                    |
| Resource Risk                | Risk of mental/Physical fatigue                         | Admins                 | 3               | 3                 | 3            | Making sure the team gets regular breaks.                                                                                                             |
| Quality and Testing          | Buggy code                                              | Admins                 | 4               | 2                 | 3            | Setting up a testing phase at the end of every sprint to make sure code is functional.                                                                |
| Quality and Testing          | Inadequate test coverage                                | Admins                 | 2               | 4                 | 3            | Try and maintain clean and coherent code.                                                                                                             |
| CI/CD Risks                  | Build failures                                          | Admins                 | 1               | 5                 | 3            | In case of build failure check the logs and sort the issues.                                                                                          |
| CI/CD Risks                  | Deployment failures                                     | Admins                 | 1               | 5                 | 3            | Testing the app functionality before deployment. or use previous working versions.                                                                    |
| External Dependencies        | Risk of external services being unavailable or changing | Admins                 | 2               | 2                 | 2            | Checking any external service beforehand. In order to know if it needs to be replaced.                                                                |
| External Dependencies        | Regulatory requirements                                 | Admins                 | 3               | 3                 | 3            | In case of any requirements not completed by the end of the sprint. The task can be extended into the next sprint.                                    |
| Scalability and Performance  | Scalability challenges                                  | Admins                 | 2               | 4                 | 3            | Do commits very often to aid in debugging.                                                                                                            |
| Scalability and Performance  | Performance bottlenecks                                 | User                   | 2               | 2                 | 2            | Follow good coding practices, avoiding repetitions of code.  Also keeping separation of concerns.                                                     |