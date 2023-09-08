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

- Two group memebrs came across an issue withe the ticket booking system, specifically with the maximum amount of tickets able to be bought. This was an important issue to fix because if the user was able to buy too many tickets this could break the whole database.

## ERD (Entity Relationship Diagram)

### This entity relationship diagram was devised using the principles of relational databases and normalisation

![Entity Relationship Diagram](/Documentation-Screenshots/SQL/ERD.png)



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