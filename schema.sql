-- CIT-105 Week 7 Assignment 2
-- Baseball Training Tracker
-- Created by Matthew Espinel
-- SQLite Database Schema

CREATE TABLE IF NOT EXISTS training_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    training_date TEXT NOT NULL,

    training_type TEXT NOT NULL
        CHECK (
            training_type IN (
                'Hitting',
                'Fielding',
                'Throwing',
                'Conditioning'
            )
        ),

    duration INTEGER NOT NULL
        CHECK (duration > 0),

    notes TEXT NOT NULL DEFAULT ''
);