from crewai import Task
from agents import translator, summarizer


translator_task = Task(
    description="Translate the following paragraph to {target_language}: {paragraph}",
    expected_output="The complete translated text in {target_language}",
    agent=translator
)
translator_task

summarizer_task = Task(
    description="give some bullet points in {target_language} for the following paragraph: {paragraph}",
    expected_output="bullet poiont summary in {target_language}",
    agent=summarizer
)
summarizer_task