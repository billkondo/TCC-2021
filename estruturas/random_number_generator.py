import sys
from pathlib import Path
from random import randint
from typing import Dict

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Empty filename")

    filename = sys.argv[1]
    N = int(sys.argv[2]) if len(sys.argv) >= 3 else 5000
    L = int(sys.argv[3]) if len(sys.argv) >= 4 else 64

    max_number = (1 << L) - 1
    generated: Dict[int, int] = {}
    for _ in range(0, N):
        x = randint(1, max_number)
        while generated.get(x) is not None:
            x = randint(1, max_number)
        generated[x] = 1

    generated_list = list(generated.keys())

    Path("./input").mkdir(parents=True, exist_ok=True)
    with open(f"./input/{filename}", "w") as f:
        for x in generated_list:
            f.write(f"{x}\n")
