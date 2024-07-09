# Text-Based Adventure Game

Welcome to the Text-Based Adventure Game! This project is a simple text-based adventure game built using Python and Flask.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Viewing Data](#viewing-data)

## Introduction

This project implements a text-based adventure game where players can navigate through different scenarios by making choices presented as buttons in a web interface. The game is built with Python using the Flask framework for the web server.

## Features

- Player registration and game start functionality.
- Interaction with different game scenarios (e.g., exploring a cave or entering a house).
- Outcome based on player choices (e.g., acquiring items, winning or losing encounters).
- Persistent player data storage using MongoDB.
- View and manage game data using Mongo-Express.

## Prerequisites

Before running the application, ensure you have the following installed:

- Docker (for containerization)
- Python (3.9 or higher) and Flask (2.0.2) if running without Docker
- MongoDB (4.4 or higher)

## Setup

### Using Docker

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd text-based-adventure-game
   ```

2. **Run the application with Docker:**

   ```bash
   docker-compose up
   ```

### Without Docker

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd text-based-adventure-game
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   Ensure MongoDB is running on your local machine at the default port 27017.

   ```bash
   python main.py
   ```

## Usage

- Open your web browser and navigate to `http://localhost:5000`.
- Follow the instructions on the screen to play the game.
- Make choices by clicking the buttons presented for different scenarios.

## Viewing Data

Mongo-Express is included in the setup for easy viewing and management of the game data stored in MongoDB.

- Open your web browser and navigate to `http://localhost:8081`.
- You will see the Mongo-Express interface where you can view the contents of your MongoDB database.

## App look like this:

![](./static/img/Image1.PNG)

![](./static/img/Image2.PNG)
