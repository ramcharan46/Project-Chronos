# Project Chronos: The AI Archeologist

## Student Name(s) and ID(s)
- Vunnam Ramcharan [SE25UDSC070] : Programming and GitHub Management
- Yuvraj Visen [SE25UCAM033] : Team Leading and Optimizing
- Utkrisht Pathak [SE25UCAM052] : Programming
- Ananya Pajini [SE25UCAM057] : Documentation and Optimizing

## Project Description
Project Chronos: The AI Archeologist is an application that reconstructs, analyses, and interprets fragmented or partial text artifacts using AI-assisted techniques. Given partially damaged or incomplete text (for example, archaeological inscriptions, damaged manuscripts, or fragmented transcripts), the application attempts to infer and reconstruct missing segments, provide confidence estimates, and offer contextual commentary to help researchers and students interpret recovered text.

## Features
- Accepts fragmented text input and attempts automated reconstruction.
- Uses Google Gemini AI API key for model-based inference.
- Prints reconstructed text and optional contextual links to refer to.
- Simple command-line interface for quick experimentation.

## Setup Instructions
Follow these steps to set up the project on a new machine.

Prerequisites:
- Python installed. Check with:
  ```
  python --version
  ```
- Git installed.

1. Clone the repository
   ```
   git clone https://github.com/ramcharan46/Project-Chronos.git
   cd Project-Chronos
   ```

2. Install required libraries and dependencies
   - If a requirements.txt file exists:
     ```
     pip install -r requirements.txt
     ```

3. Set up API keys
   - Create a `.env` file in the project root.
   - Add your Google Gemini API key as:
     ```
     GEMINI_API_KEY=your_google_gemini_api_key_here
     ```

## Usage Guide
Basic usage (example command-line):

- Example: Run the main script with a fragment to reconstruct
  ```
  python main.py "i loved it, i gotta go cya l8r!"
  ```
---
