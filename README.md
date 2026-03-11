# HumanEval Code Generation Using Llama 3 (Ollama)

## Overview

This project evaluates Python code generation using a locally deployed language model.  
Programming tasks are loaded from the HumanEval dataset, solutions are generated using the model, and the generated code is compared with the reference implementations.

The workflow includes loading the dataset, generating Python solutions, saving them as separate files, and evaluating the generated outputs.

---

## Project Structure

project/

src/
main.py
similarity_eval.py

data/
test.csv

generated/
llm_HumanEval_0.py
llm_HumanEval_1.py
...

results/
similarity_results.csv

README.md  
requirements.txt  
.gitignore

---

## Dataset

The dataset used in this project is based on the HumanEval code generation benchmark.

Each dataset entry contains:

- task_id – identifier of the programming task  
- prompt – function signature and problem description  
- canonical_solution – reference implementation  
- test – unit tests  
- entry_point – expected function name  

For this experiment, the first 10 tasks from the dataset were used.

---

## Model

Code generation was performed using the Llama 3.1 (8B) model running locally through Ollama.

Example command:

ollama run llama3.1:8b

---

## Requirements

Install the required Python dependencies:

pip install -r requirements.txt

---

## How to Run

1. Install the required Python dependencies

pip install -r requirements.txt

2. Install Ollama on your system

3. Pull the model

ollama pull llama3.1:8b

4. Run the generation script

python src/main.py

---

## Output

The generation script creates Python files inside the generated directory.

Example files:

llm_HumanEval_0.py  
llm_HumanEval_1.py  
llm_HumanEval_2.py  

Each file contains a generated solution for one task from the dataset.

---

## Evaluation

The generated solutions are compared with the reference implementations from the dataset.

Similarity between the generated code and the canonical solution is computed using the Python difflib library.

The evaluation results are stored in:

results/similarity_results.csv

Each row contains the task identifier and the corresponding similarity score.

---

## Experiment Setup

The experiment was conducted using the Llama 3.1 (8B) model running locally through Ollama.

The HumanEval dataset was used as the evaluation source.  
For this study, the first 10 tasks from the dataset (HumanEval/0 – HumanEval/9) were selected.

For each task, the model generated a Python implementation based on the provided prompt.  
The generated code was stored as separate Python files and later compared with the reference implementations.

---

## Future Improvements

Possible improvements include:

- running unit tests for functional correctness evaluation
- computing the pass@k metric used in HumanEval benchmarks
- testing multiple language models
- scaling the experiment to the full HumanEval dataset

---

## Conclusion

This project demonstrates a workflow for evaluating code generation using a locally deployed language model.  
The generated solutions can be compared with reference implementations to analyze the performance of the model on programming tasks.