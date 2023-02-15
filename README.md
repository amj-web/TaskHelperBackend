# The TaskHelper Todo List

The TaskHelper Todo List is a productivity app designed to help the user get organized by allowing them to create tasks and ToDo lists. 

## Technologies Used
Our productivity app is built using a variety of technologies, including:

- HTML, CSS, and JavaScript for the frontend
- React.js for building the user interface and managing the application's state
- Django REST framework for building the backend API
- ElephantSQL as the primary database management system
- Cloudinary for image and file storage
- JWT to securly share information
- Heroku for deployment

The live link can be found [here](https://task-helper.herokuapp.com/). 

## Website across different platforms
![Responsice Mockup](src/assets/images/screenshots/responsivemockup.png)


## User Stories

- As a user, I want to be able to create and manage tasks so that I can stay organized and on top of my to-do list.
- As a user, I want to be able to set deadlines for my tasks so that I can prioritize and plan my time effectively.
- As a user, I want to be able to categorize my tasks into different projects or groups so that I can easily find and access them.
-As a user, I want to be able to mark tasks as complete or incomplete so that I can track my progress and stay motivated.

###### User story functionality I would like to add in the future
- As a user, I want to be able to set reminders for my tasks so that I don't forget to complete them.
- As a user, I want to be able to view my tasks in a calendar view so that I can easily plan my week or month.
- As a user, I want to be able to share my task lists with others so that we can collaborate on projects together.

**First-Time Visitor Goals - As a first-time user, who has not created an account, I want to be able to:
* Understand what the purpose of the application is and how to use it.  
* Create an account. 

**Registered User Goals - As a registered user I want to be able to:**
* Create, Edit and Delete my own tasks
* Set a due date for a task
* Attach a file to a task
* Assign/unassign multiple owners
* Set a priority for a task
* Set a category for a task
* Filter tasks based on category and priority 

**Site Admin Goals - As an administrator, I want to be able to:**
* Create, Edit and delete my own and users' tasks
* Manage and authenticate user tasks

##  Design
I wanted to create a design that is both visually pleasing and functional, that helps users stay focused and motivated. The simplicity of the design allows users to navigate through the application with ease, and quickly access the features they need to get their tasks done efficiently. 

**Wireframes**

* [Home Page](src/assets/images/wireframes/Home.png)
* [Home Page With Tasks](src/assets/images/wireframes/homewtask.png)
* [Login](src/assets/images/wireframes/Login.png)
* [Register](/src/assets/images/wireframes/Register.png)
* [Create New Task](src/assets/images/wireframes/CreateANewTask.png)
* [viewtask](src/assets/images/wireframes/viewtask.png)

### Existing Features

- __Navigation Bar__

  - Featured on all three pages, the full responsive navigation bar includes links to the Home page, Categories, Create New Task, Documentation and of course a Log Out button it is identical on each page to allow for easy navigation.
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 

![Nav Bar](src/assets/images/screenshots/Navbar.png)

- __Home Page__

  - If the user is already register the home page is where they can see their on going tasks. 
  - If the user is not logged or register it displays an imput for them to do so. 
  - If the user has no task it displays a message congratulating them on having nothing to do. 
  - Each of the tasks has CRUD functionality where the user can view, update and delete thier tasks
  - Also displays information for each task such as state, category, priority and due date. 

![Home Page](src/assets/images/screenshots/homewtask.png)

![Home Page](src/assets/images/screenshots/Login.png)

![Home Page](src/assets/images/screenshots/Home.png)

- __View Task__

  - If the user clicks on the view button it will take them here where they can see all the information of their task. 
  - There is download button where the user can download files related to their task. 

  ![View](src/assets/images/screenshots/ViewTask.png)

  - __Update Task__

  - Here the user can update their tasks

  ![Update](src/assets/images/screenshots/updatetask.png)

- __Categories__

  - The Categories Page is where the user creates a category in which task have to assigned. 
  - Once a new catergory has been added it can be edited or deleted. 

![Categories](src/assets/images/screenshots/AddNewCategory.png)
![Categories](src/assets/images/screenshots/CategoryDeleteNot.png)

- __New Tasks__

  - This section will allow the user to create new tasks and assign them properties as follows:  
  - Assign a title
  - Give a description of the task
  - Add Task related files
  - Set a Due Date
  - Assign and owner of the task
  - Assign the Category
  - Assign the priority to High, Medium or Low
  - Change the state of the task to Open, In Progess or Completed

![New Tasks](src/assets/images/screenshots/CreateaNewTask.png)

- __Docs.__ 

  - Here I intend to put information found here in the readme. But due to time constraints is only has Lorem Ipsun dummy text. 
  - The side menu for navigating the documentation does work as does the hide menu functionality

![Docs](src/assets/images/screenshots/docs.png)

- __Login and Register__

  - Is where the user logs in or registers new accounts.  

![login](src/assets/images/screenshots/Login.png)
![Register](src/assets/images/screenshots/Register.png)

### Features Left to Implement

- A calander view to see tasks in days, weeks, months
- notifications of uncoming tasks

## Testing

## Manual Tests
### Login Form Submission

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Login Form | Submit empty form | Form doesn't submit, and displays error message| Pass |
| Login Form | Enter invalid Username | Form doesn't submit, and displays error message | Pass |
| Login Form | Enter User login credentials | Form doesn't submit, and displays error message | Pass | 
| Submit link | Click on link | User is redirected to category page | Pass | 

 ### Registration Form Submission (Register Page)

| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Registration Form | Try to submit empty form | Form doesn't submit, and displays error message | Pass |
| Registration Form | Try to submit a form where a username already exists | Form doesn't submit, and displays error message | Pass |
| Email input | Try to enter an invalid email address or random numbers, words etc. | Form doesn't submit, and displays error message | Pass |
| Login link | Click on link | User is redirected to Login Page | Pass |
| Registration Form | Create a new user | Success message displays as user is redirected to Login Page | Pass |

### Update Task

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Attempt to submit form without changing anything | Submit form without making any changes | Form doesn't submit, and displays error message | Fail |
| Cancling the update | click on link| Takes user back to Task page | Pass |

### Deleting Tasks

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Delete Task| Click on button | Warning alert asking is user is sure | Pass |
| Delete Successful Message | click yes on delete a task | Task successfully delted alert | Pass |
| Cancel Delete  | Click no on alert | Alert removed and nothing happens | Pass |

### Creating New Tasks

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Title | Try to submit empty form | Form doesn't submit, and displays error message | Pass |
| Description | Try to submit empty form | Form doesn't submit, and displays error message  | Pass |
| Files  | Try to submit empty form | Form doesn't submit, and displays error message  | Pass |
| Date  | Try to submit empty form | Form doesn't submit, and displays error message  | Pass |
| Owners | Try to submit empty form | Form doesn't submit, and displays error message  | Pass |
| Priority | Try to submit empty form | Form doesn't submit, and displays error message  | Pass |
| State | Try to submit empty form | Form doesn't submit, and displays error message  | Pass | Click no on alert | Form doesn't submit, and displays error message  | Pass |
| Category | Try to submit empty form | Form doesn't submit, and displays error message  | Pass |

### Creating New Category

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Category | Try to submit empty form | Form doesn't submit, and displays error message | Pass |
| Edit| Save changes | state changes and success alert  | Pass |
| Delte  | delete state | category deleted and success alert  | Pass |

### Filtering Tasks
| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Filter by Catergory | Use drop down | Filter by catergory | Pass |
| Filter by Priority | Use drop down  | Filter by priority  | Pass |
| Filter by Status | Use drop down  | Filter by status | Pass |


## HTML Validation:
- HTML Validation by W3C was used to check my HTML code: [W3C Markup Validation Link](https://validator.w3.org/)
- Testing conducted across all HTML Templates shows no errors but minor some warnings. 

---
## CSS Validation:
- CSS Validation by W3C was used to check my CSS: [W3C CSS Validation Link](https://jigsaw.w3.org/css-validator/)
- Testing conducted across all CSS Templates shows errors for the webkit -- is a vendor extension.  

---

## JS Validation:
- JS validation by JSHint was used to check my Javascript code: [JSHint Validation Link](https://jshint.com/)

---
## Python Validation:
- I relied on Linter for my Python Validation

## React
- I relied on eslint for my React Validation


---
## Lighthouse Performance Testing:
- Results of the Lighthouse Performance testing below:
- The performance is very low. I have been told this is due to smelly components. Something I will need to work on in the future. 

![Lighthouse Performance Test](src/assets/images/screenshots/Lighthouse.png)


## Responsiveness:
- The site has been tested at various screen sizes a demonstration of which can be found [here](http://www.responsinator.com/?url=https%3A%2F%2Ftask-helper.herokuapp.com%2F)

---

## Current Issues known but not yet resolved:
Making sure that I met my deadline there are a number of thing I will look to improve on in the future. I'm sure there are many more that I have not noticed. 
Some of the ones I have are: 
- Site loads to categories and not homepage
- User can only upload pictures
- The View Task page looks a bit naff
- The user can update the task without changing anything

---

## Personal Credits

- Danny Callaghan. My tutor and mentor, such an amazing teacher  with so much experience. I wish I had met him sooner. 
- The Code Insitute tutors as also their patience and knowledge knows no end.

## Final Thoughts

Portfolio Project 5 proved a real challenge for me. I really struggled with the initial learning curve and it forced me to find help from tutors and experienced react.js programmers. That said I thoroughly enjoyed creating the website from the ground up and had a few eureka moments that really helped my understanding of react. I still have a LONG way to go before I could say I am confident in what I am doing, but that's why we have people to teach us. 

I would like to thank The Code Institute for providing me with an excellent space to learn. 
I definitely struggle with imposter syndrome. But as one of my tutors said, “It never goes away and it can be a great motivator to keep learning”
