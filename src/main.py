import pandas as pd
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "test.csv"
GENERATED_DIR = BASE_DIR / "generated"

df = pd.read_csv(DATA_FILE)

tasks = df.head(10)

instruction = """You are a Python coding assistant.
Complete the function exactly as specified.
Return only valid Python code.
Do not add explanations.
Do not change the function name or signature.
"""

for index, row in tasks.iterrows():

    task_id = row["task_id"]
    prompt = row["prompt"]

    full_prompt = instruction + "\n" + prompt

    print("Generating:", task_id)

    result = subprocess.run(
        ["ollama", "run", "llama3.1:8b", full_prompt],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    code = result.stdout

    filename = GENERATED_DIR / f"llm_{task_id.replace('/', '_')}.py"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    print("Saved:", filename)