# Physics Tutor

CITS3403 Assignment: Physics tutor built with jinja and Bootstrap on the frontend and Flask on the backend.

# Requirements

## Front End

| Objective  | Requirement                                                | Weighting |
| ---------- | ---------------------------------------------------------- | --------- |
| HTML5      | Style, Maintainability, Validation                         | 10%       |
| CSS3       | Style, Maintainability                                     | 10%       |
| Javascript | Code Quality, Validation of User Generated Data, Execution | 15%       |
| Style      | Look and Feel, Usability                                   | 10%       |
| Content    | Coherence, Effectiveness                                   | 5%        |

## Back End

| Objective                           | Description                                 | Weighting |
| ----------------------------------- | ------------------------------------------- | --------- |
| Code                                | Code quality, complexity of task, execution | 10%       |
| Persistence and User authentication | Database schema and models                  | 10%       |
| Testing                             | Unit tests and Selenium Tests               | 10%       |
| Design                              | Purpose and level of complexity             | 10%       |
| Collaboration                       | Git Logs and Agile Processes                | 10%       |

# Purpose

1. Instructional Web application teaching student classical physics, with formative assessments
2. Unit for CITS3403 unit at University of Western Australia 2021

# Design

## First Design

We drew up our wire frame using a free web application called [Figma](https://www.figma.com).

Screen shots of these are stored in the wireframes directory in the root of this repository.

These were for very basic structure of the site, and as such most of the content in the wireframes are placeholder, namely colour choices and text.

# Development

Our repository is on GitHub at https://github.com/Joel-Milligan/physics-tutor-assignment.

## Testing the application

- Launch app as described in the "Launching" section of this README
- python -m pytest

## Git Flow

For source control management, we used a stripped down version of the "Git Flow" methodology, as described in this [web page](https://www.gitkraken.com/learn/git/git-flow).
We used this as it is an industry standard and scales well to large teams and applications.

# Agile

## Project Management

To manage project development, we will be using GitHub's Projects feature.

This manages user stories, and issues in a Kanban style with To Do, In Progress, and Done columns, similar to Jira or Azure DevOps.

We have created 2 projects, one for front end development and one for backend development, for seperation of concerns.

Automation has been setup on these projects to automatically move cards between columns on certain events such as pull requests, merges, or issue creation.

# Structure

## Root Folder

The root of the repository contains the following:

- Project meta-data
  - README.md = Information about the project
  - Procfile = Heroku Deployment Requirement
  - commits.txt = Git Logs
  - .flaskenv = Environment variables for development
- Application entry point (physics-tutor.py)
- create-assessments.py = Script to create sample assessments
- app = Main application source code.
- migrations = Setting up the sqlite database
- tests
  - unit = Unit tests
  - integration = Selenium tests
- wireframes = Initial wireframing from design process

## Application Architecture

In this flask application we used an MVC structure.
The models are in models.py, using SQLAlchemy
The views are in the templates folder and forms.py, handled by jinja
The controllers are in routes.py.

# Launching

To launch the web application follow the below list, from top to bottom.

- using bash terminal in root of this repository
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- flask db upgrade
- flask run

## Heroku Deployment

Alternatively you can go to https://physics-tutor.herokuapp.com/ to view the web app.
Please note that this deployment is not working as well as running the application locally due to issues specific to deployment, so we would prefer to be marked on the local version.
