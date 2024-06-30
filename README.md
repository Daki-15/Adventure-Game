# Text-Based Adventure Game

Welcome to the Text-Based Adventure Game! This project is a simple text-based adventure game built using Python, Flask, and MongoDB.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [License](#license)

## Introduction

This project implements a text-based adventure game where players can navigate through different scenarios by making choices presented as buttons in a web interface. The game is built with Python using the Flask framework for the web server and MongoDB for data storage.

## Features

- Player registration and game start functionality.
- Interaction with different game scenarios (e.g., exploring a cave or entering a house).
- Outcome based on player choices (e.g., acquiring items, winning or losing encounters).
- Persistent player data storage using MongoDB.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python (3.9 or higher)
- Flask (2.0.2)
- pymongo (3.12.1)
- Docker (optional, for containerization)

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd text-based-adventure-game
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MongoDB:**

   - Ensure MongoDB is installed and running.
   - Set the `MONGODB_URI` environment variable in your shell or `.env` file.

4. **Run the application:**

   ```bash
   python app.py
   ```

   or using Docker:

   ```bash
   docker build -t adventure-game .
   docker run -p 5000:5000 adventure-game
   ```

## Usage

- Open your web browser and navigate to `http://localhost:5000`.
- Follow the instructions on the screen to play the game.
- Make choices by clicking the buttons presented for different scenarios.

## App look like this:

![](./static/img/Image1.PNG)


![](./static/img/Image2.PNG)