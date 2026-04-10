import os

path = input("Enter full path: ").strip()

for i in range(1, 15):
    os.makedirs(os.path.join(path, f"WEEK{i}"), exist_ok=True)

print(f"Created WEEK1 through WEEK14 in {path}.")
