import streamlit as st
from phi.agent import Agent
from phi.model.ollama import Ollama

# ---------------- Agents ----------------
explaining_agent = Agent(
    name="Explainer",
    role="Provides detailed explanations of questions",
    model=Ollama(id="llama2"),
    instructions=(
        "Explain the given question in a clear and detailed way. "
        "Break down complex terms into simple language for easy understanding. "
        "If the question contains specific keywords (e.g., 'fibonacci'), explain what they mean, "
        "give background context, and provide examples. "
        "Ensure the final explanation is beginner-friendly and presented in one block."
    ),
    markdown=True,
)

coding_agent = Agent(
    model=Ollama(id="llama2"),
    instructions=(
        "Generate Python code based on the user's requirement. "
        "Add clear and concise comments to explain each step. "
        "Ensure the final code is simple, easy to understand, and beginner-friendly. "
        "At the end, present the complete code in one block."
    ),
    description="Provides simple Python code solutions",
    show_tool_calls=True,
    markdown=True,
)

debugger = Agent(
    name="Debugger",
    role="Fixes errors and ensures runnable code",
    model=Ollama(id="llama2"),
    instructions=(
        "Check the given code for bugs, syntax errors, and logic issues. "
        "Fix all problems and provide the corrected version. "
        "Ensure the final code is complete, runnable, and beginner-friendly."
    ),
    markdown=True,
)

reviewer = Agent(
    name="Reviewer",
    role="Validates code quality and correctness",
    model=Ollama(id="llama2"),
    instructions=(
        "Carefully review the given code for correctness, efficiency, readability, and maintainability. "
        "If the code meets the requirements, reply with 'APPROVED'. "
        "If the code has issues, provide clear feedback and suggest improvements."
    ),
    markdown=True,
)

usecase_agent = Agent(
    name="UseCaseGenerator",
    role="Generates guiding use cases (hints)",
    model=Ollama(id="llama2"),
    instructions=(
        "by using the generated code ,generate a list of practical use cases for the given program idea."
        "Each use case should include a brief description,input and the expected output for each usecase."
    ),
    markdown=True,
)

usecase_tester = Agent(
    name="UseCaseTester",
    role="Tests code against generated use cases",
    model=Ollama(id="llama2"),
    instructions=(
        "Take the given code and the list of use cases. "
        "Run through each use case logically and check if the code would produce the expected output. "
        "Report results clearly: PASS if the output matches, FAIL if it does not."
    ),
    markdown=True,
)

import time
# ---------------- Streamlit UI ----------------
st.title("🤖 Multi-Agent Programming Assistant")

task = st.text_input("Enter the program idea (e.g., 'Fibonacci sequence generator')")

if st.button("Run Agents"):
    start_time = time.time()  # ⏱️ Start timer

    # Step 1: Explain
    explanation = explaining_agent.run(task)
    data = explanation.content if hasattr(explanation, "content") else explanation.output_text
    st.subheader("📘 Explanation")
    st.markdown(data)

    # Step 2: Generate Code
    dev_response = coding_agent.run(task)
    code = dev_response.content
    st.subheader("💻 Developer Output")
    st.code(code, language="python")

    # Step 3: Debug Code
    debug_response = debugger.run(f"Fix any issues in this code:\n{code}")
    code = debug_response.content
    st.subheader("🛠 Debugger Output")
    st.code(code, language="python")

    # Step 4: Review Code
    review_response = reviewer.run(f"Review this code. Reply 'APPROVED' if valid:\n{code}")
    st.subheader("✅ Reviewer Output")
    st.markdown(review_response.content)

    # Step 5: Generate Use Cases
    usecases_response = usecase_agent.run(task)
    usecases = usecases_response.content
    st.subheader("📊 Use Cases")
    st.markdown(usecases)

    # Step 6: Test Use Cases
    test_response = usecase_tester.run(f"Code:\n{code}\n\nUse Cases:\n{usecases}")
    st.subheader("🧪 Use Case Test Results")
    st.markdown(test_response.content)

    # Final Code
    st.subheader("🏁 Final Code")
    st.code(code, language="python")
    
    st.subheader("📊 Usecases")
    st.code(usecases, language="python")

    # ⏱️ End timer and show execution time
    end_time = time.time()
    execution_time = end_time - start_time
    st.subheader("⏱️ Execution Time")
    st.write(f"Total time taken: {execution_time:.2f} seconds")
