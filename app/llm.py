import os

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
load_dotenv()

import google.generativeai as genai
API_KEY = os.getenv("GEMNI_API_KEY")
genai.configure(api_key=API_KEY)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",google_api_key=API_KEY,)




from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain




async def check_if_beats(seed, guess,persona):

    # prompt = f"Does '{guess}' beat '{seed}' in a game of cleverness or power? Only answer YES or NO."
    prompt = """
    
    Be a very strict and logical judge.. you will be given {seed} and {guess} .  does {guess} beat {seed} ? Give only answer in yes or no .
   """

    response =   llm.invoke(prompt)


    verdict = response.content.strip().lower()
    return "yes" in verdict
