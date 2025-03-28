# sahayak
submission to IIT Roorkee X peerhub ai/ml competition
- problem statement:2

  ![landing page](https://github.com/user-attachments/assets/a3e53d72-71d3-4a8b-a1d1-66c799f99172)
  ![landing page](https://github.com/user-attachments/assets/7396f994-975a-41e8-97bc-5feb514d123a)
  ![image](https://github.com/user-attachments/assets/aba9156b-01ee-4624-b821-9a4ab1fb929d)


# poshan
submission to AI/ML Multi-Track Competition By PeerHub x CIG IIT Roorkee
round 3 health_track_chatbot
1. diet suggestion based on age and gender: suggesting personalized diet plans based on calorie intake and health goals
2. Answer disease-related queries (database)
3. Send automated health reminders(need email:which triggers some python script to send a mail with the said reminder)


# Setting up locally
1. Prerequisites
Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).

## Installation Steps

1. Clone the Repository

2. Install Dependencies
   Run the following command to install the required libraries:
   ```sh
   pip install -r requirements.txt
   ```

3. Set Up Environment Variables
   Create a `.env` file in the root directory and add the following details:
   ```env
   EMAIL=email@domain.com
   PASSWORD=your_app_password  # Use an app-specific password, not a personal one
   API_KEY=your_gemini_api_key  # Obtain this from the Gemini API provider
   ```

4. Create FAQ Data File
   Ensure a JSON file named `internship_chatbot_conversations_only.json` exists in the root directory. Format it according to your specifications for FAQs.
   format:
   ```
     [  {
        "messages": [
            {
                "role": "user",
                "text": "What does this website do?"
            },
            {
                "role": "bot",
                "text": "This website is your personal guide to career and progress"
            }
        ]
    }, ]
   ```

6. Rename Response Model File
   Change the extension of `response_model.md` to response_model.py

7. Launch the UI
   Run the following command in the terminal:
   ```sh
   streamlit run landing.py
   ```
