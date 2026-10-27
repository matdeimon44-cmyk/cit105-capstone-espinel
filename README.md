# Baseball Training Tracker

## CIT 105 Capstone Project

**Student:** Matthew Espinel  
**Course:** CIT 105

## Project Description

My project is a Baseball Training Tracker built with Python and Streamlit.

The purpose of this application is to help baseball players record their training sessions, review their progress, and track how much time they spend practicing.

## Features

- Add baseball training sessions
- View previous training sessions
- Filter sessions by training type
- View training-time summaries
- Generate AI training suggestions (planned)

## Project Status - Module 6 Checkpoint

### Completed
- [x] Main application screen
- [x] Add new training sessions
- [x] View training history
- [x] Filter sessions by training type
- [x] Display total training sessions
- [x] Display total training minutes
- [x] Display training summary chart
- [x] Save training data in a JSON file
- [x] Keep saved data after restarting the application

### In Progress
- [ ] Improve the user interface
- [ ] Test the application with more training records

### Not Started
- [ ] AI training suggestions
- [ ] SQLite database integration

## Technologies Used

- Python
- Streamlit
- JSON
- Generative AI (planned)

## How to Run the Application

1. Clone the GitHub repository.
2. Open the project folder.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Start the application:

```bash
python -m streamlit run main.py
```

5. Open the local URL displayed in the terminal.

## Scope Changes

For this checkpoint, I focused on the main features of the application.

I completed the training registration, history, filtering, and summary features.

The AI training suggestion feature and SQLite database will be developed in a later module.

## Author

Matthew Espinel

## Week 7 Assignment 2 - SQLite Data Layer

### Database Design

The Baseball Training Tracker uses SQLite to store
baseball training sessions persistently.

The database contains one table named
`training_sessions`.

### Table Structure

- id: Unique identifier and primary key.
- training_date: Date of the training session.
- training_type: Hitting, Fielding, Throwing,
  or Conditioning.
- duration: Training duration in minutes.
- notes: Additional performance notes.

### Database Constraints

The database includes the following constraints:

- PRIMARY KEY ensures each session has a unique ID.
- NOT NULL prevents required fields from being empty.
- CHECK restricts training types to valid categories.
- CHECK ensures training duration is greater than zero.

### Why This Table Exists

The training_sessions table stores the information
needed to display training history, filter sessions
by type, and calculate training summaries.

### SQLite Implementation

The application uses Python's sqlite3 module.

The database.py file manages database connections,
creates the table, migrates existing JSON records,
and performs database operations.

SQL INSERT statements use parameterized queries
to help prevent SQL injection.

### JSON Migration

The original training_data.json file was preserved
as a backup.

Existing training sessions were migrated into
training.db without losing the original data.

### Testing

The application was tested by adding a new
training session and checking Training History.

The existing session and the new session were
both displayed successfully.

After refreshing the application, both records
remained available.

### Application Features

- Add baseball training sessions.
- View training history.
- Filter sessions by training type.
- Display total sessions and training minutes.
- View a chart of training sessions by type.

### Author

Matthew Espinel
CIT-105 - Week 7 Assignment 2