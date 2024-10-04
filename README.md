# MCQ Generator using Hugging Face

This project is an **MCQ (Multiple Choice Question) Generator** powered by Hugging Face models, designed to automatically generate multiple-choice questions from any given text. The generator allows users to specify the difficulty level (simple or difficult) and the number of questions they want to generate. It leverages Natural Language Processing (NLP) models to comprehend the context and create meaningful questions along with their corresponding options.

## Features:
- Generates MCQs based on input text.
- Option to choose between simple or difficult question tone.
- Customizable number of MCQs to generate.
- Interactive interface built with Streamlit for ease of use.
- Uses Hugging Face for text processing and generation.

## Technologies Used:
- **Hugging Face API** for NLP models.
- **Langchain** for efficient prompt management.
- **LLM Chain** for creating prompt templates.
- **Streamlit** for building an interactive user interface.
- **Git Bash** for environment setup and management.

## How it Works:
The user inputs a passage or text.
The Hugging Face model processes the text, extracting important concepts.
Based on the tone (simple/difficult), the generator creates multiple-choice questions with 4 options each.
The MCQs are displayed in a user-friendly format via the Streamlit interface.

## Installation & Setup:

### Install the required packages:

```bash
pip install -r requirements.txt
```

### Run the Streamlit app:
```bash
streamlit run app.py
```

### Usage:
Input any text passage and specify the desired number of MCQs and difficulty level.
The generator will create questions and display them along with the possible answers.

### Future Enhancements:
- Add support for more languages.
- Implement a scoring system for generated MCQs.
- Improve the NLP model’s accuracy for better question quality.

Feel free to explore, modify, and contribute to this project!
## Contributing

Contributions are always welcome!

Find out an Error or give any suggestion to improve the project.

If you want to add any new features, make a pull request.

ThankYou for your attention.

