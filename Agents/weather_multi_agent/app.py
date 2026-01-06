import streamlit as st
from agents.weather_agent import run_weather_agent
from agents.content_agent import generate_weather_summary
from agents.pdf_agent import run_pdf_agent

st.set_page_config(
    page_title="Multi-Agent Weather Report",
    layout="centered"
)

st.title("🌤️ Multi-Agent Weather Report System")

city = st.text_input("Enter City Name")

if st.button("Get Weather Report"):
    if city.strip() == "":
        st.error("Please enter a city name.")
    else:
        # Agent 1: Weather Agent
        weather_data = run_weather_agent(city)

        # Agent 2: Content Agent
        summary = generate_weather_summary(weather_data)

        if "error" in summary:
            st.error(summary)
        else:
            st.success("Weather Summary Generated")
            st.write(summary)

            # Agent 3: PDF Agent
            pdf_file = run_pdf_agent(summary)

            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="📄 Download PDF Report",
                    data=f,
                    file_name=pdf_file,
                    mime="application/pdf"
                )
