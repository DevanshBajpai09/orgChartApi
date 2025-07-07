import os
import subprocess
import sys
import time
import itertools
import threading

# === FILE PATHS ===
source_file = "models/Dummy.cc"
initial_prompt_file = "prompts/initial_prompt.yaml"
refine_prompt_file = "prompts/refine_prompt.yaml"
generated_test_file = "tests/test_Dummy.cpp"

# === Read files ===
def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# === Spinner for loading effect ===
def spinner_task(stop_event, message="🧠 Working"):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if stop_event.is_set():
            break
        sys.stdout.write(f'\r{message} {c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r✅ Done!                      \n')

# === LLM Call using Ollama ===
def call_ollama(prompt):
    stop = threading.Event()
    spinner = threading.Thread(target=spinner_task, args=(stop,))
    spinner.start()

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        stop.set()
        spinner.join()
        return result.stdout
    except subprocess.CalledProcessError as e:
        stop.set()
        spinner.join()
        print("\n❌ Ollama failed:")
        print(e.stderr)
        sys.exit(1)

# === Step 1: Initial Test Generation ===
print("📥 Generating initial unit test...")
cpp_code = read_file(source_file)
initial_yaml = read_file(initial_prompt_file)

initial_prompt = f"""You are a professional C++ unit test generator.

Below is the YAML instruction to follow strictly:
---
{initial_yaml}

Below is the source code:
---
{cpp_code}

Please generate GoogleTest-based unit tests with no duplicate or redundant cases.
"""

initial_output = call_ollama(initial_prompt)

os.makedirs(os.path.dirname(generated_test_file), exist_ok=True)
with open(generated_test_file, 'w', encoding='utf-8') as f:
    f.write(initial_output)

print("📄 Initial test saved at:", generated_test_file)

# === Step 2: Refine the Generated Tests ===
print("\n🔁 Refining generated test cases...")
generated_test_code = read_file(generated_test_file)
refine_yaml = read_file(refine_prompt_file)

refine_prompt = f"""You are a C++ test code refiner.

Below is the YAML with strict refinement rules:
---
{refine_yaml}

Below is the initial test file:
---
{generated_test_code}

Refine the tests by removing duplicates, fixing includes, and improving formatting.
"""

refined_output = call_ollama(refine_prompt)

with open(generated_test_file, 'w', encoding='utf-8') as f:
    f.write(refined_output)

print("✅ Final refined test saved at:", generated_test_file)
