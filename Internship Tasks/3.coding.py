from phi.agent import Agent
from phi.model.ollama import Ollama
"""
making 4 agents to explain, code, debug, and review python code based on user input
then integrating them into a streamlit app
we use ollama llama3.1 model for all agents
"""

# agent 1
explaining_agent = Agent(
    name="Explainer",
    role="Provides detailed explanations of questions",
    model=Ollama(id="llama3.1"),  
    instructions=(
        "Explain the given question in a clear and detailed way. "
        "Break down complex terms into simple language for easy understanding. "
        "If the question contains specific keywords (e.g., 'fibonacci'), explain what they mean, "
        "give background context, and provide examples. "
        "Ensure the final explanation is beginner-friendly and presented in one block "
        "so it can be read easily without confusion."
    ),
    markdown=True,
)

# agent 2
coding_agent = Agent(
    model=Ollama(id="llama3.1"), 
    instructions=(
        "Generate Python code based on the user's requirement. "
        "Add clear and concise comments to explain each step. "
        "Ensure the final code is simple, easy to understand, and beginner-friendly. "
        "At the end, present the complete code in one block for clarity."
    ),
    description="Provides simple, efficient, and easy-to-understand Python code solutions",
    show_tool_calls=True,
    markdown=True,
)
# agent 3
debugger = Agent(
    name="Debugger",
    role="Fixes errors and ensures runnable code",
    model=Ollama(id="llama3.1"),
    instructions=(
        "Check the given code for bugs, syntax errors, and logic issues. "
        "Fix all problems and provide the corrected version. "
        "Ensure the final code is complete, runnable, and beginner-friendly. "
        "At the end, show the entire corrected code in one block so it can be copied and executed directly."
    ),
    markdown=True,
)

# agent 4
reviewer = Agent(
    name="Reviewer",
    role="Validates code quality and correctness",
    model=Ollama(id="llama3.1"),
    instructions=(
        "Carefully review the given code for correctness, efficiency, readability, and maintainability. "
        "If the code meets the requirements, reply with 'APPROVED' and present the final code in one block "
        "so it can be copied and executed directly. "
        "If the code has issues, provide clear feedback and suggest improvements in a simple, beginner-friendly way."
    ),
    markdown=True,
)




import streamlit as st
from phi.agent import Agent
from phi.model.ollama import Ollama

# --- your agent definitions remain unchanged ---
# (Explainer, Coding Agent, Debugger, Reviewer)

# Streamlit UI
st.title("🧑‍💻 Multi-Agent Code Workflow")
st.write("Enter a program requirement below, and click the button to generate, debug, and review the code.")

# Text input for program requirement
task = st.text_input("Enter the program you want:")

# Button to trigger agent workflow
if st.button("🚀 Generate Code"):
    if task.strip() != "":
        # Explaining the program
        explanation = explaining_agent.run(task)
        data = explanation.content if hasattr(explanation, "content") else explanation.output_text
        st.subheader("📘 Explanation")
        st.markdown(data)

        # Generating the python code
        dev_response = coding_agent.run(task)
        code = dev_response.content
        st.subheader("💻 Developer Output")
        st.code(code, language="python")

        # Debugging the generated code
        debug_response = debugger.run(f"Fix any issues in this code:\n{code}")
        code = debug_response.content
        st.subheader("🛠 Debugger Output")
        st.code(code, language="python")

        # Reviewing the debugged code
        review_response = reviewer.run(f"Review this code. Reply 'APPROVED' if valid:\n{code}")
        st.subheader("✅ Reviewer Output")
        st.markdown(review_response.content)

        # Final code
        st.subheader("🏁 Final Code")
        st.code(code, language="python")
    else:
        st.warning("⚠️ Please enter a program requirement before generating.")
