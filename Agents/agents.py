from dotenv import load_dotenv
from posthog import api_key
load_dotenv()
import os
os.environ["WEATHER_API_KEY"]=os.getenv("WEATHER_API_KEY")
os.environ["GOOGLE_API_KEY"]=os.getenv("GEMINI_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   # or "gemini-1.5-pro"
    temperature=0.7,
    verbose=True,
)


from crewai import Agent

weather_agent = Agent( 
        role="Weather Agent", 
        goal="Fetch real-time weather data for the user's requested city", 
        backstory="Specialist in retrieving accurate weather information from APIs.", 
        verbose=True, 
        allow_delegation=False, 
        llm=gemini_llm,
        api_key=os.getenv("GEMINI_API_KEY")

        )



'''weather_content_creator = Agent(
    role="Weather Content Creator",
    goal="Parse weather data and generate a clear, human-friendly paragraph summarizing the conditions.",
    backstory="Expert at interpreting raw weather data and turning it into easy-to-understand reports.",
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm  
)'''
