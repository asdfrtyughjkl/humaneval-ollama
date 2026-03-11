import os
import pandas as pd
from difflib import SequenceMatcher

DATA_PATH = "data/test.csv"
GEN_PATH = "generated"
RESULT_PATH = "results/similarity_results.csv"

df = pd.read_csv(DATA_PATH)

results = []

for i, row in df.iterrows():
    ref = row["canonical_solution"]

    gen_file = f"{GEN_PATH}/llm_HumanEval_{i}.py"

    if os.path.exists(gen_file):
        with open(gen_file, "r", encoding="utf-8") as f:
            gen_code = f.read()

        similarity = SequenceMatcher(None, ref, gen_code).ratio()
    else:
        similarity = 0

    results.append({
        "task_id": row["task_id"],
        "similarity": similarity
    })

res_df = pd.DataFrame(results)

os.makedirs("results", exist_ok=True)
res_df.to_csv(RESULT_PATH, index=False)

print("Evaluation completed")
print(res_df)