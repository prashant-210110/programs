import streamlit as st
from phi.agent import Agent
from phi.model.ollama import Ollama

# Combined agent 1: Explain + Code
explain_and_code_agent = Agent(
    name="ExplainAndCode",
    role="Explains and generates Python code",
    model=Ollama(id="tinyllama"),
    instructions=(
        "First, explain the program idea in simple beginner-friendly terms. "
        "Then generate Python code that solves it. "
        "Keep both explanation and code concise. "
        "Show the final code in one block."
    ),
    markdown=True,
)

# Combined agent 2: Debug + Review
debug_and_review_agent = Agent(
    name="DebugAndReview",
    role="Fixes errors and reviews code",
    model=Ollama(id="tinyllama"),
    instructions=(
        "Check the code for errors and fix them. "
        "Then review the corrected code for readability and correctness. "
        "Reply 'APPROVED' if valid, otherwise suggest improvements. "
        "Show the corrected code in one block."
    ),
    markdown=True,
)

# Combined agent 3: Use Cases + Testing
usecase_and_test_agent = Agent(
    name="UseCaseAndTest",
    role="Generates test cases and validates code",
    model=Ollama(id="tinyllama"),
    instructions=(
        "Generate multiple test cases with expected input and output. "
        "Include at least one detailed example with step-by-step reasoning. "
        "Then check the code against these test cases. "
        "Report results clearly: PASS or FAIL with explanation. "
        "Present all test cases and results in one block."
    ),
    markdown=True,
)

# --- Streamlit UI ---
st.title("⚡ Fast Multi-Agent Python Workflow")
st.write("This streamlined app explains, codes, reviews, and tests Python programs quickly.")

task = st.text_area("📌 Describe the program you want:", 
                    placeholder="e.g., Write a program to generate Fibonacci numbers")

if st.button("🚀 Run Workflow"):
    if task.strip():
        with st.spinner("Running agents..."):

            # Step 1: Explain + Code
            explain_and_code = explain_and_code_agent.run(task).content
            st.subheader("🔎 Explanation + 💻 Code")
            st.markdown(explain_and_code)

            # Step 2: Debug + Review
            debug_and_review = debug_and_review_agent.run(explain_and_code).content
            st.subheader("🛠 Debug + 📋 Review")
            st.markdown(debug_and_review)

            # Step 3: Use Cases + Testing
            usecase_and_test = usecase_and_test_agent.run(debug_and_review).content
            st.subheader("🧪 Use Cases + ✅ Test Results")
            st.markdown(usecase_and_test)

    else:
        st.warning("⚠️ Please enter a program requirement before running.")
