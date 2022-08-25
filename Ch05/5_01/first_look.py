# %%
from pathlib import Path

csv_file = Path('taxi.csv')
mb = 2**20
csv_file.stat().st_size / mb

# %%
num_lines = 0
with csv_file.open() as fp:
    for lnum, line in enumerate(fp):
        if lnum < 5:
            print(line, end='')
        num_lines += 1

print(f'lines: {num_lines:,}')