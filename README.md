# GymSo Fitness 💪
![Uploading WorkoutGymGIF.gif…]()


Welcome to GymSo Fitness – Your Virtual Gym Experience!

## Overview

GymSo Fitness is a revolutionary project that brings the gym experience to the comfort of your home, combining technology, gamification, and fitness. Our goal is to provide users with an engaging and effective way to stay fit and healthy.

## Features

### Virtual Fitness Experiences

Immerse yourself in a variety of virtual fitness experiences, ranging from VR workouts to gamified exercises. Explore different realms of exercise, each designed to make your fitness journey exciting and enjoyable.

#### VR Fitness Experiences

- **Curls Exercise**
  - Embark on a journey with VR Curls Challenge, an immersive virtual reality workout designed to enhance arm strength and endurance.

- **Shoulder Exercise**
  - Immerse yourself in the tranquility of VR Yoga Sessions, blending technology and mindfulness to promote a healthier lifestyle.

- **Pushups Exercise**
  - Dance your way to fitness with VR Zumba Fusion, a high-energy virtual reality dance workout that adds a fun and rhythmic twist to your exercise routine.

### Personalized Dieting Options

Tailor your diet to achieve specific muscle gains with personalized dieting options. Whether you're focusing on building shoulder strength, improving endurance, or working on core muscles, we've got you covered.

### Gamified Gym Experience

Transform your workout routine into a fun and interactive experience. Earn rewards, track your progress, and compete with friends in fitness challenges. Our gamification approach makes exercising at home enjoyable and motivating.
## Pages

### 1. [Homepage](#homepage)

Provide an overview of GymSo Fitness, its features, and how users can get started.

### 2. [Exercises Page](#exercises-page)

Explore the different exercises and virtual fitness experiences available in GymSo Fitness.

### 3. [Calorie Page](#calorie-page)

Learn about personalized dieting options and how GymSo Fitness helps you achieve your fitness goals.

### 4. [ML Models](#ml-models)

Discover the machine learning models used in GymSo Fitness to enhance the user experience.

# 1- LLM Chatbot

Sure, here's a basic README file for your Python script and the command to run it:

### Overview:
This project utilizes the LangChain library to create a language model chain that generates specific answers to questions related to exercise, workout, health, and fitness. The chain is built using Hugging Face's model from the repository "tiiuae/falcon-7b-instruct."

### Dependencies:
- Python 3.6 or higher
- Install dependencies using: `pip install langchain chainlit`

### Usage:
1. Set up your Hugging Face API token:
   - Get your Hugging Face API token from [Hugging Face](https://huggingface.co/settings/token).
   - Replace `'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'` with your actual API token in the `LLM.py` script.

2. Run the script:
   ```bash
   chainlit run LLM.py
   ```

### Input:
The script expects input questions related to health, fitness, exercise, and workout. It generates specific answers with references to exercises in an academic style suitable for an audience aged 18-25.

### Output:
The script outputs a paragraph-length response based on the provided question.

### Example Usage:
```bash
chainlit run LLM.py
```

### Additional Notes:
- Ensure you have proper permissions and access to the specified Hugging Face model repository.
- The script uses the `cl` and `langchain` libraries for chat-based language model chaining. Make sure they are installed using the provided `pip install` command.

## Getting Started

To start your virtual fitness journey with GymSo Fitness, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/manas/Gymso-VR-Fitness.git
