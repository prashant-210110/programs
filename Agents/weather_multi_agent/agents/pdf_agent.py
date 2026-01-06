from phi.agent import Agent
from content_agent import model)

pdf_agent = Agent(
    name="PDF Agent",
    role="Generate PDF report from weather summary",
    model=model
)

def run_pdf_agent(summary):
    return create_pdf(summary)
