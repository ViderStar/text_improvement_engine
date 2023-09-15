# Text Improvement Engine

This repository contains the code for the Text Improvement Engine project, developed by ViderStar. The Text Improvement Engine is a tool designed to enhance the quality and effectiveness of written text by providing suggestions and improvements based on predefined standard phrases and language patterns.

## Features

- Preloaded Standard Phrases: The engine comes with a comprehensive list of standard phrases that cover various domains, including business jargon, scientific terminology, and more.
- Text Enhancement: The engine analyzes input text and suggests alternative phrases or improvements to enhance its clarity, conciseness, and impact.
- Customization: Users can modify and expand the list of standard phrases according to their specific needs and domain requirements.
- Easy Integration: The Text Improvement Engine can be easily integrated into existing applications or used as a standalone tool through a user-friendly interface.

## Installation

To install and run the Text Improvement Engine locally, follow these steps:

1. Clone this repository: `git clone https://github.com/ViderStar/text_improvement_engine.git`
2. Navigate to the project directory: `cd text_improvement_engine`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the engine: `python engine.py`

## Implementation
The key steps in the implementation are:

- CLI text input via the input() function
- Loading phrases from txt file
- spaCy NLP pipeline to tokenize text and extract keywords
- Vector similarity comparison between extracted keywords and standard phrases
- Sorting and returning the top suggestions
- The suggestions are printed in a readable format with the original phrase, suggestion, and similarity score.

## Future Improvements
Some potential improvements for the future:

- More robust CLI with options and help text
- Ability to directly substitute suggested phrases into the original text
- Additional filtering for quality suggestions
- User feedback loop to refine suggestions over time
- Integration with GUI/web interface