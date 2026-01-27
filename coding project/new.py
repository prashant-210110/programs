from phi.agent import Agent
from phi.model.ollama import Ollama

# agent 1
explaining_agent = Agent(
    name="Explainer",
    role="Explains the program idea in simple terms",
    model=Ollama(id="tinyllama"),
    instructions=(
        "Explain the program idea clearly in beginner-friendly language. "
        "Break down technical terms into simple words. "
        "Provide background context if needed (e.g., what the algorithm does, why it matters). "
        "Give at least one small example to make the explanation practical. "
        "Keep the explanation concise but complete, so a beginner can understand without confusion."
    ),
    markdown=True,
)

# agent 2
coding_agent = Agent(
    name="Coder",
    role="Writes Python code",
    model=Ollama(id="tinyllama"),
    instructions=(
        "Write Python code that solves the program idea. "
        "Add clear comments explaining each step. "
        "Ensure the code is simple, efficient, and beginner-friendly. "
        "Use meaningful variable names and avoid unnecessary complexity. "
        "Include basic error handling if appropriate. "
        "At the end, present the complete code in one block for clarity."
    ),
    markdown=True,
)

# Agent 3
debugger = Agent(
    name="Debugger",
    role="Fixes errors in code",
    model=Ollama(id="tinyllama"),
    instructions=(
        "Check the code carefully for syntax errors, logic mistakes, and runtime issues. "
        "Fix all problems and provide the corrected version. "
        "Ensure the code runs successfully without errors. "
        "Keep the code beginner-friendly and well-commented. "
        "At the end, show the entire corrected code in one block so it can be copied directly."
    ),
    markdown=True,
)

# Agent 4
reviewer = Agent(
    name="Reviewer",
    role="Checks code quality",
    model=Ollama(id="tinyllama"),
    instructions=(
        "Review the code for correctness, efficiency, readability, and maintainability. "
        "Check if the code meets the requirements and follows best practices. "
        "If the code is valid, reply with 'APPROVED' and present the final code in one block. "
        "If there are issues, provide clear feedback and suggest improvements in simple, beginner-friendly language. "
        "Highlight any improvements for performance, readability, or structure."
    ),
    markdown=True,
)

# Agent 5
use_case_agent = Agent(
    name="UseCaseGenerator",
    role="Finds scenarios to test the code",
    model=Ollama(id="llama3.1"),
    instructions=(
        "Read the code carefully and generate multiple test scenarios (use cases),input and expected outputs. "
        "Each scenario should describe a specific input and the expected output or behavior. "
        "Make the scenarios clear and beginner-friendly. "
        "At the end, present all scenarios in one block so they can be easily read and understood."
    ),
    markdown=True,
)

# Agent 6
tester_agent = Agent(
    name="Tester",
    role="Runs tests on the code",
    model=Ollama(id="tinyllama"),
    instructions=(
        "Take the code and the scenarios. "
        "For each scenario, write a small test snippet that runs the code. "
        "Check whether the expected behavior is achieved. "
        "Report results clearly: PASS if the code works, FAIL if it does not. "
        "Include a short explanation for each result. "
        "At the end, present a summary table of all scenarios with their test results. "
        "Keep the output beginner-friendly and easy to understand."
    ),
    markdown=True,
)
task = input("Enter the program idea: ")

# task 1: Explain the program
print("\n--- Explanation ---\n")
print(explaining_agent.run(task).content)

# task 2: Write the code
code = coding_agent.run(task).content
print("\n--- Code Written ---\n")
print(code)

# task 3: Debug the code
code = debugger.run(code).content
print("\n--- Debugged Code ---\n")
print(code)

# task 4: Review the code
print("\n--- Review ---\n")
print(reviewer.run(code).content)

# task 5: Generate scenarios (use cases)
use_cases = use_case_agent.run(code).content
print("\n--- Scenarios to Test ---\n")
print(use_cases)

# task 6: Test the code against scenarios
print("\n--- Test Results ---\n")
print(tester_agent.run(f"Code:\n{code}\n\nScenarios:\n{use_cases}").content)

# Final Output
print("\n================ FINAL OUTPUT ================\n")
print(">>> Final Code:\n")
print(code)
print("\n>>> Scenarios:\n")
print(use_cases)
print("\n==============================================\n")