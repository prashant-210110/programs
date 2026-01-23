from phi.agent import Agent
from phi.model.ollama import Ollama

# agent 1
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
# agent 2
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

# agent 3
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
# agent 4
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

#program
task=input("enter the programe you want")

#explining the program
explanation = explaining_agent.run(task)
data = explanation.content if hasattr(explanation, "content") else explanation.output_text
print(data)

# generating the python code
dev_response = coding_agent.run(task)
code = dev_response.content
print("\n--- Developer Output ---\n")
print(code)

#debugging the generated code
debug_response = debugger.run(f"Fix any issues in this code:\n{code}")
code = debug_response.content
print("\n--- Debugger Output ---\n")
print(code)

#giving review to the debugged code
review_response = reviewer.run(f"Review this code. Reply 'APPROVED' if valid:\n{code}")
print("\n--- Reviewer Output ---\n")
print(review_response.content)

#final code
print(code)