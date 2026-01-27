from phi.agent import Agent
from phi.model.ollama import Ollama

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

# agent 5
use_case_agent = Agent(
    name="UseCaseGenerator",
    role="Generates guiding use cases (hints) for writing code",
    model=Ollama(id="llama3.1"),
    instructions=(
        "Based on the user's program idea, generate multiple guiding use cases "
        "that act as hints or requirements for writing the code. "
        "Each use case should describe a specific scenario, input, or expected behavior "
        "that the final program must handle. "
        "Ensure the use cases are clear, beginner-friendly, and directly related to the program idea. "
        "At the end, present all use cases in one block so they can be easily read and understood."
    ),
    markdown=True,
)

# agent 6
tester_agent = Agent(
    name="Tester",
    role="Validates code against guiding use cases",
    model=Ollama(id="llama3.1"),
    instructions=(
        "Take the given Python code and the guiding use cases (hints). "
        "For each use case, write a small test snippet that runs the code "
        "and checks whether the expected behavior is achieved. "
        "Report results clearly: PASS if the code satisfies the use case, FAIL if it does not. "
        "Include a short explanation for each result. "
        "At the end, present a summary table of all use cases with their test results. "
        "Ensure the final output is beginner-friendly and easy to understand."
    ),
    markdown=True,
)


# Get user input for the task
task = input("Enter the program you want: ")

# task 1: Explain the program
explanation = explaining_agent.run(task)
data = explanation.content if hasattr(explanation, "content") else explanation.output_text
print("\n--- Explanation ---\n")
print(data)

# task 2: Generate Python code
dev_response = coding_agent.run(task)
code = dev_response.content
print("\n--- Developer Output ---\n")
print(code)

# task 3: Debug the generated code
debug_response = debugger.run(f"Fix any issues in this code:\n{code}")
code = debug_response.content
print("\n--- Debugger Output ---\n")
print(code)

# task 4: Review the debugged code
review_response = reviewer.run(f"Review this code. Reply 'APPROVED' if valid:\n{code}")
print("\n--- Reviewer Output ---\n")
print(review_response.content)

# task 5: Generate use cases for the code
use_case_response = use_case_agent.run(f"Generate use cases for this code:\n{code}")
use_cases = use_case_response.content
print("\n--- Use Case Generator Output ---\n")
print(use_cases)

# task 6: Test the code against use cases
test_response = tester_agent.run(f"Test this code against the following use cases:\n{code}\n\nUse Cases:\n{use_cases}")
print("\n--- Tester Output ---\n")
print(test_response.content)

# Final code output
print("\n--- Final Code ---\n")
print(code)


#all use cases
print("\n--- Use Case Generator Output ---\n")
print(use_cases)