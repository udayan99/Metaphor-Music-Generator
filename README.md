# Metaphor-Driven Music Therapy App

Welcome to the Metaphor-Driven Music Therapy App! This application combines the power of music and language processing to provide therapeutic music recommendations based on users’ emotional states or situations, using metaphor analysis.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This application allows users to input their emotions or situations and receive a personalized playlist based on metaphorical themes in song lyrics. The app uses a dedicated Metaphor API to extract metaphors from the song lyrics and match them to user input, creating a unique and personalized music therapy experience.

## Features

- **User Profile Management:** Users can create profiles to record their preferences, feedback, and interaction history.
- **Metaphor Analysis:** Utilizes the Metaphor API to analyze and extract metaphorical themes from song lyrics.
- **Matching Algorithm:** Matches user input with metaphorical themes to generate personalized playlists.
- **Interactive UI/UX:** Offers a user-friendly interface with smooth navigation and intuitive controls.
- **Feedback Processing:** Uses user feedback to refine the algorithm and improve recommendations.
- **Data Visualization:** Displays insights into the metaphorical content of recommended songs.

## Setup and Installation

1. **Clone the Repository**
    ```sh
    git clone <repository_url>
    ```
2. **Navigate to the Project Directory**
    ```sh
    cd <project_directory>
    ```
3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt  # Python Dependencies
    npm install  # JavaScript/Node.js Dependencies
    ```
4. **Initialize Database**
    ```sh
    python manage.py migrate  # Initializes the database
    ```

## Usage

1. **Start the Backend Server**
    ```sh
    python manage.py runserver  # Starts the Django/Flask server
    ```
2. **Start the Frontend Development Server**
    ```sh
    npm start  # Starts the React/Vue.js development server
    ```
3. **Access the App**
   - Open a web browser and navigate to [http://localhost:3000](http://localhost:3000) or the port you've configured.

## Contributing

For details on contributing to this project, please check the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
