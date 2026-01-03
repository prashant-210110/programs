from crewai import Crew
from agents import translator, summarizer
from tasks import translator_task, summarizer_task


crew=Crew(
    agents=[translator,summarizer],
    tasks=[translator_task,summarizer_task],
    verbose=True
)


result = crew.kickoff(inputs={
    "paragraph": "Artificial intelligence is transforming how we work and live.",
    "target_language": "Telugu"
})

print("Final Result:", result)