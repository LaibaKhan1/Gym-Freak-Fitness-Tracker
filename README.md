# Gym-Freak Fitness Tracker Project

Welcome to the Fitness Tracker Website, a comprehensive platform designed to help you achieve your fitness goals and lead a healthier lifestyle. This web application combines a range of features to support your fitness journey, making it easier than ever to stay on track and reach your objectives.

## Key Features:

### 1. BMI Calculator

Calculate your Body Mass Index (BMI) to assess your body weight in relation to your height. Understanding your BMI can help you set realistic fitness goals and monitor your progress over time.

### 2. Calorie Tracker

Effortlessly keep track of your daily calorie intake and monitor the calories burned during your workouts. This feature allows you to maintain a balanced and personalized diet while optimizing your fitness routines.

### 3. Exercise Library

Access a diverse library of exercises tailored to various fitness levels and preferences. Each exercise comes with detailed step-by-step instructions, ensuring you perform them correctly and effectively.

### 4. User Profiles

Create and personalize your user profile to keep a record of your fitness achievements and progress. Track your workout history, set goals, and celebrate milestones as you work towards a healthier you.

## Getting Started

To contribute to this project, follow these steps:

### 1. Install Requirements:

```bash
pip install -r requirements.txt
```

### 2. Clone the Repository

Clone your forked repository to your local machine using the following command in your terminal:

```bash
git clone https://github.com/SyedHassanUlHaq/Gym-Freak-Fitness-Tracker.git
```

### 3. Run the Django Development Server

Navigate to the project directory and start the Django development server:

```bash
cd Gym-Freak-Fitness-Tracker/GymFreak
```
```bash
python3 GymFreak/manage.py runserver
```

## Technologies Used:

- **Django:** A powerful web framework for building robust and scalable web applications.
- **HTML, CSS, JavaScript:** Frontend technologies for creating an interactive and visually appealing user interface.
- **SQLite:** A lightweight, serverless database engine for efficient data storage.
- **Edamam API:** Utilized for calculating calories consumed, enhancing the nutritional aspect of the Fitness Tracker.
- **Libraries:**
  - **Harris-Benedict Equation:** Employed for estimating calories burned during physical activity, considering factors such as weight, height, age, gender, and exercise intensity.
  - **django.shortcuts:** Part of the Django framework for providing high-level abstractions for common web development patterns.
  - **django.http:** Django module for handling HTTP requests and responses.
  - **.models:** Custom models defined in your project for database interaction.
  - **.forms:** Custom forms for user input handling.
  - **math:** Python's standard library for mathematical functions.
  - **requests:** An HTTP library for making API requests.
  - **django.contrib.auth:** Django module for user authentication.
  - **datetime:** Python's standard library for working with dates and times.
  - **django.contrib.auth.decorators:** Django decorators for restricting access to authenticated users.

## LICENSE
This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

Thank you for contributing to the Fitness Tracker project! 🏋️‍♂️

