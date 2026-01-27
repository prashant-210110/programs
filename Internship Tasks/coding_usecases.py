import time
from phi.agent import Agent
from phi.model.ollama import Ollama

# Agent 1: Coding Agent
coding_agent = Agent(
    model=Ollama(id="tinyllama"),
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

# Agent 2: Debugger
debugger = Agent(
    name="Debugger",
    role="Fixes errors and ensures runnable code",
    model=Ollama(id="tinyllama"),  # can swap with qwen or mistral
    instructions=(
        "Check the given code and fix all problems. "
        "Provide the corrected version in one block."
    ),
    markdown=True,
)

# Agent 3: Reviewer
reviewer = Agent(
    name="Reviewer",
    role="Validates code quality and correctness",
    model=Ollama(id="tinyllama"),
    instructions=(
        "Review the given code for correctness, efficiency, readability, and maintainability. "
        "If the code meets the requirements, reply with 'APPROVED'. "
        "Provide code at last with proper formatting."
    ),
    markdown=True,
)

# Agent 4: Use Case Generator
usecase_agent = Agent(
    name="UseCaseGenerator",
    role="Generates guiding use cases",
    model=Ollama(id="llama3.2"),  # can swap with qwen or mistral
    instructions=(
        "Generate a list of practical use cases for the given program idea. "
        "Each use case should include a brief description, input, and expected output."
    ),
    markdown=True,
)

# Agent 5: Use Case Tester
usecase_tester = Agent(
    name="UseCaseTester",
    role="Tests code against generated use cases",
    model=Ollama(id="tinyllama"),
    instructions=(
        "Take the given code and the list of use cases. "
        "Check if the code would produce the expected output. "
        "Report results clearly: PASS if matches, FAIL if not."
    ),
    markdown=True,
)

# Normal workflow with total execution time
if __name__ == "__main__":
    task =input("enter the program you want :")

    start_time = time.time()  # start timer

    code = coding_agent.run(task)
    print("\n=== Coding Agent Output ===")
    print(code.content)

    debug = debugger.run(code.content)
    print("\n=== Debugger Agent Output ===")
    print(debug.content)

    review = reviewer.run(debug.content)
    print("\n=== Reviewer Agent Output ===")
    print(review.content)

    usecases = usecase_agent.run(review.content)
    print("\n=== UseCase Generator Output ===")
    print(usecases.content)

    testing = usecase_tester.run(usecases.content)
    print("\n=== UseCase Tester Output ===")
    print(testing.content)

    print("----final review of code-----")
    print(review.content)

    print("-----final usecases------")
    print(usecases.content)

    end_time = time.time()  # end timer
    total_elapsed = end_time - start_time
    print(f"\n⏱ Total Execution Time: {total_elapsed:.2f} seconds")
