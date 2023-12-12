# InterviewGPT
Traditional video interview platforms that require candidates to record themselves speaking often leave them feeling awkward and uncomfortable. InterviewGPT will listen to your answers, and ask further questions that explore your strengths and weaknesses. Currently uses OpenAI models (Whisper, gpt-3.5-turbo, tts-1)

# Usage

### 1. Set Up Your Environment
- Ensure Python3 is installed on your system.

### 2. Clone the Repository
- Clone this repository to your local machine.
  ```bash
  git clone https://github.com/jalaneunos/InterviewGPT.git
  ```

### 3. Install Dependencies
- Optional: Create a virtual environment.
- Install the required python packages
  ```bash
  pip install -r requirements.txt
  ```

### 3. Set Environment Variables
- You must set your OpenAI API key as an environment variable.
- For Linux/Mac:
  ```bash
  export OPENAI_API_KEY='your_openai_api_key_here'
  ```
- For Windows:
  ```bash
  set OPENAI_API_KEY=<your_openai_api_key_here>
  ```

### 4. Running the applicaton
- Directly using python:
  ```bash
  python app.py
  ```
- On initialization, the application will scan for input devices and list them.
- Select the desired input device by its index number

### Conversation
- When 'recording...' appears on the CLI, the input recording has started and will record up to 30 seconds.
- To stop the audio recording, perform a keyboard interrupt (CTRL-C)
- To stop the conversation entirely, perform a keyboard interrupt (CTRL-C)
