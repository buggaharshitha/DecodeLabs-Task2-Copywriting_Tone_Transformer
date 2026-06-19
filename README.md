# Automated Copywriting & Tone Transformer

## Project Overview

This project was developed as part of the **DecodeLabs Generative AI Internship**.

The application uses Google's Gemini AI model to generate customized marketing content based on user inputs such as product name, platform, tone, content length, and creativity level.

## Objective

The objective of this project is to demonstrate Prompt Engineering by creating an AI-powered marketing content generator that produces platform-specific promotional content.
## Features

- AI-powered marketing copy generation
- Dynamic prompt creation
- Multiple platform support
  - Instagram
  - LinkedIn
  - Email
- Multiple writing tones
  - Professional
  - Friendly
  - Formal
- Adjustable content length
- Adjustable creativity level using Temperature
- Secure API key management using `.env`
- Error handling for better user experience
## Technologies Used

- Python 3.10
- Google Gemini API
- Google GenAI SDK
- python-dotenv
- Prompt Engineering
## Project Structure

```
Project2_Copywriting_Tone_Transformer/
│
├── README.md
├── main.py
├── prompts.txt
├── sample_outputs.md
├── requirements.txt
├── .gitignore
└── screenshots/
```
## Installation

### Clone the repository

```bash
git clone <repository-link>
```

### Install dependencies

```bash
pip install -r requirements.txt
```
### Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```
## How to Run

Execute the following command:

```bash
python main.py
```

## Input Parameters

The application asks the user for:

- Product Name
- Platform
- Tone

## Sample Test Cases

### Test Case 1

**Product:** Nike Running Shoes

**Platform:** Instagram

**Tone:** Friendly
### Test Case 2

**Product:** MacBook Air M4

**Platform:** LinkedIn

**Tone:** Professional
### Test Case 3

**Product:** Organic Honey

**Platform:** Email

**Tone:** Formal
## Learning Outcomes

Through this project, I learned:

- Prompt Engineering
- Dynamic Prompt Templates
- Google Gemini API Integration
- Python Programming
- Environment Variable Management
- AI-powered Content Generation
- Error Handling
## Future Improvements

- Support for additional social media platforms
- Export generated content to PDF or Word
- Graphical User Interface (GUI)
- Content history and download options
## Author

**Bugga Harshitha**

Generative AI Intern – DecodeLabs
