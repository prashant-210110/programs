import streamlit as st                  # Used to build the interactive web app UI.
import time                             # track execution time
from phi.agent import Agent             # define agents with roles and instructions
from phi.model.ollama import Ollama     # giving different model for different agents for fast execution


#agent 1: Coding Agent
coding_agent = Agent(
    model=Ollama(id="llama3.2"),
    instructions="Generate Python code with clear comments, beginner-friendly, final code in one block.",
    description="Provides simple Python code solutions", 
    markdown=True)

#agent 2: Debugger
debugger = Agent(
    name="Debugger", 
    role="Fixes errors",
    model=Ollama(id="llama3.2"),
    instructions="Fix problems in the given code and provide corrected version in one block.", 
    markdown=True)

#agent 3: Reviewer
reviewer = Agent(
    name="Reviewer", 
    role="Validates code",
    model=Ollama(id="tinyllama"),
    instructions="Review code for correctness, efficiency, readability. Reply 'APPROVED' if good, else provide formatted code.",
    markdown=True)

#agent 4: Use Case Generator
usecase_agent = Agent(
    name="UseCaseGenerator", 
    role="Generates use cases",
    model=Ollama(id="llama3.2"),
    instructions="Generate practical use cases with description, input, and expected output,dont give code just give the usecases and information about it,and also give the examples of that usecases",
    markdown=True)

#agent 5: Use Case Tester
usecase_tester = Agent(
    name="UseCaseTester", 
    role="Tests code",
    model=Ollama(id="tinyllama"),
    instructions="Test code against use cases. Report PASS or FAIL.", 
    markdown=True)

# Streamlit workflow
def main():
    st.title("🧑‍💻 Simple Multi-Agent Workflow")

    task = st.text_input("Enter your coding task:",
                        placeholder="write a python code to print first 10 fibonacci numbers")

    if st.button("Run Workflow"):
        start = time.time()

        code = coding_agent.run(task)
        st.subheader("Coding Agent Output")
        st.code(code.content, language="python")

        debug = debugger.run(code.content)
        st.subheader("Debugger Agent Output")
        st.code(debug.content, language="python")

        review = reviewer.run(debug.content)
        st.subheader("Reviewer Agent Output")
        st.write(review.content)

        usecases = usecase_agent.run(review.content)
        st.subheader("UseCase Generator Output")
        st.write(usecases.content)

        testing = usecase_tester.run(usecases.content)
        st.subheader("UseCase Tester Output")
        st.write(testing.content)


        end = time.time()
        st.markdown(f"### ⏱ Total Execution Time: {end - start:.2f} seconds")


main()
