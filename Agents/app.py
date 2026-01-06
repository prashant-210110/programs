from openai import api_key
import streamlit as st
from phi.agent import Agent
import requests
from fpdf import FPDF
from phi.model.google import Gemini
import google.generativeai as genai


# -----------------------------
# Agent 1: Weather Agent
# -----------------------------
def find_weather(city: str) -> dict:
    API_KEY ="16e4efd9bfa3105eb3557eb254318a26"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, 
              "appid": API_KEY, 
              "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "location": {
                "name": data.get("name"),
                "country": data.get("sys", {}).get("country"),
            },
            "current": {
                "temp_c": data.get("main", {}).get("temp"),
                "feelslike_c": data.get("main", {}).get("feels_like"),
                "condition": data.get("weather", [{}])[0].get("description"),
                "wind_kph": data.get("wind", {}).get("speed"),
                "humidity": data.get("main", {}).get("humidity"),
            },
        }
    except Exception as e:
        return {"error": str(e)}

weather_agent = Agent(
    name="Weather Agent",
    model = Gemini(model_name="gemini-1.5-flash",api_key="AIzaSyDV1MOInzriKCe9fxC4thPcnqTWZ3V_q_A"),
    tools=[find_weather],
    show_tool_calls=True,
    description="Fetches real-time weather data",
    instructions=["Always return normalized JSON with location and current weather details"],
    markdown=True,
)


# -----------------------------
# Agent 2: Content Agent
# -----------------------------
def summarize_weather(weather: dict) -> str:
    if "error" in weather:
        return f"Unable to retrieve weather: {weather['error']}"
    loc = weather.get("location", {})
    cur = weather.get("current", {})
    return (
        f"Weather update for {loc.get('name')} ({loc.get('country')}): "
        f"{cur.get('condition')}. Temperature {cur.get('temp_c')}°C, feels like {cur.get('feelslike_c')}°C. "
        f"Wind {cur.get('wind_kph')} kph, humidity {cur.get('humidity')}%."
    )

content_agent = Agent(
    name="Content Agent",
    model = Gemini(model_name="gemini-1.5-flash",api_key="AIzaSyDV1MOInzriKCe9fxC4thPcnqTWZ3V_q_A"),
    tools=[summarize_weather],
    show_tool_calls=True,
    description="Converts weather JSON into a readable paragraph",
    instructions=["Always respond with a single concise paragraph"],
    markdown=True,
)

# -----------------------------
# Agent 3: PDF Agent
# -----------------------------
def generate_pdf(summary: str, filename: str = "weather_report.pdf") -> str:
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Weather Report", ln=True)
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, summary)
        pdf.output(filename)
        return filename
    except Exception as e:
        return f"Error generating PDF: {e}"

pdf_agent = Agent(
    name="PDF Agent",
    model = Gemini(model_name="gemini-1.5-flash",api_key="AIzaSyDV1MOInzriKCe9fxC4thPcnqTWZ3V_q_A"),
    tools=[generate_pdf],
    show_tool_calls=True,
    description="Converts weather summary into a PDF file",
    instructions=["Always confirm PDF creation and return the filename"],
    markdown=True,
)


# -----------------------------
# Orchestrator Function
# -----------------------------
def run_pipeline(city: str):
    # Step 1: Weather Agent
    weather_result = weather_agent.run(f"Get weather for {city}")
    weather_json = weather_result.content

    # Step 2: Content Agent
    content_result = content_agent.run(weather_json)
    summary_text = content_result.content

    # Step 3: PDF Agent
    pdf_result = pdf_agent.run(summary_text)
    pdf_filename = pdf_result.content if isinstance(pdf_result.content, str) else "weather_report.pdf"

    return summary_text, pdf_filename

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Weather Report Generator", page_icon="⛅")
st.title("Multi-Agent Weather Reporter")

city = st.text_input("Enter a city name", "Hyderabad")
run_button = st.button("Generate Report")

if run_button and city.strip():
    with st.spinner("Fetching weather and generating report..."):
        summary_text, pdf_filename = run_pipeline(city.strip())

    st.subheader("Weather Summary")
    st.write(summary_text)

    st.subheader("Download PDF")
    try:
        with open(pdf_filename, "rb") as f:
            st.download_button(
                label="Download Weather Report PDF",
                data=f,
                file_name=pdf_filename,
                mime="application/pdf",
            )
    except Exception as e:
        st.error(f"Could not read the PDF: {e}")
