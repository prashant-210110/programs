import os

os.environ["GOOGLE_API_KEY"]="AIzaSyBQqNGwQ8IwcaXy5Cy91hUkgggOpIhgK2s"

from langchain_google_genai import ChatGoogleGenerativeAI

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   # or "gemini-1.5-pro"
    temperature=0.7,
    verbose=True,
)


from langchain_community.chat_models import ChatOllama


'''ollama_llm = ChatOllama(
    model="llama3",   # or "llama3:8b", "gemma:2b", etc.
    temperature=0.7,
    verbose=True,
)'''





from crewai import Agent,Crew

translator = Agent(
    role="Language Translator",
    goal="Translate text to the user's requested language accurately",
    backstory="Expert linguist fluent in multiple languages.",
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)
translator


summarizer = Agent(
    role="summaring the text",
    goal="summarize the text into main points which contain 5 to 8 bullet points,and give the output in the user required langauge",
    backstory="Skilled at distilling complex information into clear summaries.",
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)
summarizer