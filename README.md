# Metaphor-Music-Generator

Generate music compositions based on mood derived from textual input, leveraging OpenAI and Metaphor APIs.

## Table of Contents
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Metaphor-Music-Generator.git
    cd Metaphor-Music-Generator
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your API keys:
    ```bash
    export OPENAI_API_KEY='your-openai-api-key'
    export METAPHOR_API_KEY='your-metaphor-api-key'
    ```

## Usage

- Generate music without Metaphor API:
    ```bash
    python src/without_metaphor.py
    ```

- Generate music with Metaphor API:
    ```bash
    python src/with_metaphor.py
    ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
