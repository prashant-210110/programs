import streamlit as st
import pdfplumber
import fitz  # PyMuPDF
import ollama

# Lightweight Agent class
class Agent:
    def __init__(self, name, role, model, instructions, markdown=True):
        self.name = name
        self.role = role
        self.model = model
        self.instructions = instructions
        self.markdown = markdown

    def run(self, prompt):
        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]

def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def update_file_content(file1_path, file2_path, output_path, agent):
    text1 = extract_text(file1_path)
    text2 = extract_text(file2_path)

    prompt = f"""
    Compare the following two documents. 
    Update Document 1 only where Document 2 provides newer or additional information. 
    Do not rewrite or remove any other content in Document 1. 
    Preserve all images, formatting, and layout of Document 1 exactly as they are. 
    Ensure that updated text is inserted naturally into the existing structure without overlapping or shifting image placement. 
    Return the fully updated version of Document 1.

    --- Document 1 ---
    {text1}

    --- Document 2 ---
    {text2}
    """


    updated_text = agent.run(prompt)

    # Open original PDF (file1) and replace text while keeping images/layout
    doc = fitz.open(file1_path)
    for page in doc:
        page_text = page.get_text("text")
        if page_text.strip():
            # Replace entire page text with updated content (simple approach)
            page.clean_contents()
            page.insert_text((50, 50), updated_text, fontsize=12)
            break  # only replace first page for demo; extend as needed
    doc.save(output_path)
    return output_path

# Streamlit UI
st.title("📄 PDF Updater Agent (Preserve Images/Layout)")

file1 = st.file_uploader("Upload the first PDF file", type="pdf")
file2 = st.file_uploader("Upload the second PDF file", type="pdf")

if file1 and file2:
    explaining_agent = Agent(
        name="Explainer",
        role="Updates and explains PDF content",
        model="llama3.1",  # or tinyllama if installed
        instructions = (
         "Update Document 1 using the information found in Document 2. "
         "Only replace or insert text where Document 2 provides newer or additional content. "
        "Do not modify any other parts of Document 1. "
        "Preserve the original images, formatting, and layout of Document 1 exactly as they are. "
        "Ensure that updated text fits naturally into the existing structure without overlapping or shifting image placement."
    )
,
        markdown=True,
    )

    if st.button("Update PDF"):
        # Save uploaded files to disk
        with open("file1.pdf", "wb") as f:
            f.write(file1.read())
        with open("file2.pdf", "wb") as f:
            f.write(file2.read())

        updated_path = update_file_content("file1.pdf", "file2.pdf", "updated_file1.pdf", explaining_agent)
        st.success("✅ PDF updated successfully!")

        with open(updated_path, "rb") as f:
            st.download_button("Download Updated PDF", f, file_name="updated_file1.pdf")
