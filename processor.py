import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class FinancialAdvisor:
    def __init__(self):
        # Simply swap OpenAI for Groq
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.bank_data = {
            "bank_name": "Suryoday Small Finance Bank",
            "regular_top_rate": "8.60%",
            "popular_tenor": "2 Years 1 Month"
        }

    def get_simplified_explanation(self, user_input, target_lang):
        system_prompt = f"Explain this banking info in {target_lang} simply: {self.bank_data}"
        
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content