# CIT 105 Capstone Proposal

## Project Title
Baseball Training Tracker

## 1. Problem Statement
Baseball players often complete many training sessions but do not have a simple way to keep track of what they practiced and how they performed. This application will help a baseball player record training sessions, review previous workouts, and identify areas that may need more practice.

## 2. Intended Users
The intended users are baseball players who want a simple way to organize and review their training. The user knows how to enter basic information about a workout, such as the date, type of training, duration, and notes about performance.

## 3. User Stories
1. As a baseball player, I can add a new training session so that I can keep a record of my workouts.
2. As a baseball player, I can view my previous training sessions so that I can review my training history.
3. As a baseball player, I can filter my sessions by training type so that I can focus on hitting, fielding, throwing, or conditioning.
4. As a baseball player, I can view a summary of my training time so that I can understand how much I have practiced.
5. As a baseball player, I can request an AI-generated training suggestion based on my recent sessions so that I can get an idea of what to practice next.

## 4. Data
The application will store the following information for each training session:

- session_id: unique identifier, required
- date: date of the training session, required
- training_type: hitting, fielding, throwing, or conditioning, required
- duration_minutes: length of the training session in minutes, required
- exercises: exercises completed during the session, required
- performance_rating: rating from 1 to 5, optional
- notes: additional comments about the session, optional

## 5. AI Feature
The application will include one generative AI feature that creates a short training suggestion based on the user's recent training sessions. The application will send a summary of recent training information to the AI model and display the returned suggestion.

If the AI service is unavailable or returns an unusable response, the application will display a message explaining that a suggestion could not be generated. The rest of the application will continue to work normally.

## 6. Framework Choice
I will use Streamlit because it allows me to build an interactive Python application with forms, buttons, filters, and displayed results without requiring a separate front-end framework. I also have experience using Streamlit in previous CIT 105 assignments.

## 7. Out of Scope
To keep the project small enough to complete during the capstone period, the following features will not be included:

1. User accounts, passwords, or authentication.
2. Social networking, messaging, or sharing workouts with other players.
3. Video upload or AI analysis of baseball videos.
4. Live integration with professional baseball statistics or external sports databases.
5. A mobile application for iOS or Android.

The goal is to create a focused application that can be demonstrated completely in a few minutes.