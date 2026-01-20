import json
import httpx
import streamlit as st
from phi.agent import Agent
from phi.model.ollama import Ollama
from fpdf import FPDF

# agent1: Get Weather Data
def get_weather(city: str) -> str:
    """Fetch weather data for a given city."""
    api_key = "20943e1bce63bd27b938b4bd3154c404" 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = httpx.get(url)
    return json.dumps(response.json(), indent=2)

weather_agent = Agent(
    model=Ollama(id="llama3.1"),
    tools=[get_weather],
    instructions=["Use the get_weather tool to fetch current weather data."],
    description="Provides current weather information for a given location.",
    show_tool_calls=True,
    markdown=True,
)

#agent2: Summarize Weather Data
summarizer_agent = Agent(
    name="Summarizer Agent",
    model=Ollama(id="llama3.2"),
    instructions=["Summarize the weather data in a friendly, concise way."],
    markdown=True,
)

#agent3: Save to PDF
def save_to_pdf(content: str, filename: str = "weather_report.pdf") -> bytes:
    """Save content to a PDF file and return bytes."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    pdf_bytes = pdf.output(dest="S").encode("latin1")  # return as bytes
    return pdf_bytes

pdf_agent = Agent(
    name="PDF Agent",
    model=Ollama(id="llama3.2"),
    tools=[save_to_pdf],
    instructions=["Save the provided content to a PDF file using the save_to_pdf tool."],
)

#streamlit app
st.title("⛅ Weather PDF Generator")

city = st.text_input("Enter a city name:")

if st.button("Get Weather Report"):
    if city:
        # Step 1: Get weather data
        weather_response = weather_agent.run(city)
        weather_data = weather_response.content

        # Step 2: Summarize weather data
        summarized_data = summarizer_agent.run(f"Summarize this weather data: {weather_data}", stream=False)
        content_data = summarized_data.content

        # Step 3: Save to PDF
        pdf_bytes = save_to_pdf(content_data)

        # Display summary
        st.subheader("Weather Summary")
        st.write(content_data)

        # Download button
        st.download_button(
            label="Download Weather Report PDF",
            data=pdf_bytes,
            file_name=f"{city}_weather_report.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("Please enter a city name.")
