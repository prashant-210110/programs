from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.tools.pandas import PandasTools
from fpdf import FPDF
from pathlib import Path
import pandas as pd

# Path to your Excel file
excel_file = r"c:\Users\prasa\OneDrive\Documents\Desktop\Project Sales Data.xlsx"

# Read Excel file
def read_powerbi_data(file_path: str) -> pd.DataFrame:
    """Read Excel/CSV file exported from Power BI."""
    df = pd.read_excel(file_path)
    return df

# Custom PDF generation tool
def create_professional_pdf(content: str, source_file: str, filename: str = "report.pdf") -> str:
    """Create a professional PDF report in the same folder as the source file."""
    folder = Path(source_file).parent
    pdf_path = folder / filename

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 15, "Data Analysis Report", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 6, content)
    pdf.output(str(pdf_path))

    return f"PDF saved as {pdf_path}"

# Data Analysis Agent using Ollama
data_analyst = Agent(
    name="Power BI Data Analyst",
    model=Ollama(id="llama3.2"),
    tools=[
        read_powerbi_data,
        create_professional_pdf,
        PandasTools(),
    ],
    instructions=[
        "Read the data file using read_powerbi_data tool",
        "Analyze trends, patterns, and anomalies",
        "Make predictions based on historical patterns",
        "Provide actionable insights and recommendations",
        "Generate a professional PDF report using create_professional_pdf",
        "Make some predictions to improve the sales",
        "Combine some of the items to get more profit"
    ],
    show_tool_calls=True,
    markdown=True,
)

# Usage - Export your PBIX to CSV/Excel first, then:
data_analyst.print_response(
    "Analyze Project Sales Data, identify trends, make predictions, and create a professional PDF report"
)

# Do your analysis here
df = read_powerbi_data(excel_file)
summary = df.groupby("Item")["Revenue"].sum().to_string()
df.columns = df.columns.str.strip()   # remove leading/trailing spaces
print(df.columns)


# Save PDF in the same folder as Excel file
print(create_professional_pdf(summary, excel_file, "Sales_Report.pdf"))
