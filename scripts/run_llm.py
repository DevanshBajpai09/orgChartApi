import yaml
import subprocess
import sys

def call_llm(model_name, input_cpp, prompt_file):
    with open(input_cpp) as f: code = f.read()
    with open(prompt_file) as f: prompt = yaml.safe_load(f)['instruction']
    full_prompt = f"{prompt}\n\n```cpp\n{code}\n```"

    # Run with Ollama
    result = subprocess.run(["ollama", "run", model_name], input=full_prompt.encode(), capture_output=True)
    output = result.stdout.decode()

    test_file = f"tests/test_{input_cpp.split('/')[-1]}"
    with open(test_file, "w") as f: f.write(output)
    print(f"✅ Unit test generated at: {test_file}")

if __name__ == "__main__":
    model = "codellama"
    input_cpp = sys.argv[1]  # Example: "models/orgchart.cc"
    prompt_file = sys.argv[2]
    call_llm(model, input_cpp, prompt_file)
