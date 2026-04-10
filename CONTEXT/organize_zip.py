import os
import re
import zipfile
import shutil
import glob

tmp_path = r"Z:\BCIT-FINALS\CONTEXT\tmp"
dest_path = input("Enter full path to destination folder (with WEEK# folders): ").strip().strip('"')

# --- Prompt for skipped weeks ---
skipped_weeks = set()
if input("Are any weeks skipped? (y/n): ").strip().lower() == 'y':
    while True:
        week_num = input("  Which week is skipped? Enter number: ").strip()
        if week_num.isdigit():
            skipped_weeks.add(int(week_num))
            print(f"  WEEK{week_num} marked as skipped.")
        else:
            print("  Invalid number, try again.")
            continue
        if input("  Any more skipped weeks? (y/n): ").strip().lower() != 'y':
            break
    print(f"  Skipping weeks: {sorted(skipped_weeks)}\n")

# --- Prompt for combined weeks ---
# combined_ranges: list of (start, end) tuples, e.g. [(1,2), (5,6)]
combined_ranges = []
if input("Are any weeks combined? (y/n): ").strip().lower() == 'y':
    while True:
        start = input("  Combined week start: ").strip()
        end = input("  Combined week end: ").strip()
        if start.isdigit() and end.isdigit() and int(start) < int(end):
            combined_ranges.append((int(start), int(end)))
            print(f"  WEEK{start}-{end} marked as combined.")
        else:
            print("  Invalid range, try again.")
            continue
        if input("  Any more combined weeks? (y/n): ").strip().lower() != 'y':
            break
    print(f"  Combined ranges: {[f'WEEK{s}-{e}' for s,e in combined_ranges]}\n")

# Build set of all week numbers consumed by combined ranges
combined_weeks = {}  # week_num -> (start, end) for every week in a range
for start, end in combined_ranges:
    for n in range(start, end + 1):
        combined_weeks[n] = (start, end)

# --- Build ordered slot list ---
# Each slot is a folder name that will receive one zip
week_folders_raw = sorted(
    [d for d in os.listdir(dest_path) if d.startswith("WEEK") and d[4:].isdigit()],
    key=lambda d: int(d[4:])
)
all_week_nums = [int(d[4:]) for d in week_folders_raw]

slots = []       # ordered folder names to fill with zips
seen = set()

for n in all_week_nums:
    if n in skipped_weeks:
        continue
    if n in combined_weeks:
        s, e = combined_weeks[n]
        slot_name = f"WEEK{s}-{e}"
        if slot_name not in seen:
            slots.append(slot_name)
            seen.add(slot_name)
    else:
        slots.append(f"WEEK{n}")

# --- Prepare folders: delete individuals that are part of combined ranges, create combined ---
for start, end in combined_ranges:
    for n in range(start, end + 1):
        individual = os.path.join(dest_path, f"WEEK{n}")
        if os.path.exists(individual):
            shutil.rmtree(individual)
    combined_dir = os.path.join(dest_path, f"WEEK{start}-{end}")
    os.makedirs(combined_dir, exist_ok=True)
    print(f"Created combined folder: WEEK{start}-{end}")

# Delete skipped week folders
for n in skipped_weeks:
    skip_dir = os.path.join(dest_path, f"WEEK{n}")
    if os.path.exists(skip_dir):
        shutil.rmtree(skip_dir)
        print(f"Deleted skipped folder: WEEK{n}")

# --- Get all files in tmp ---
all_files = sorted(
    [f for f in glob.glob(os.path.join(tmp_path, "*")) if os.path.isfile(f)],
    key=lambda f: os.path.getctime(f)
)

if not all_files:
    print("No files found in tmp folder.")
    exit()

assignment_files = []  # any format matching ASSIGNMENT#
lesson_zips = []       # non-assignment zips only

for file_path in all_files:
    name = os.path.splitext(os.path.basename(file_path))[0]
    if re.match(r"ASSIGNMENT\d+", name, re.IGNORECASE):
        assignment_files.append(file_path)
    elif file_path.lower().endswith(".zip"):
        lesson_zips.append(file_path)

print(f"\nFound {len(lesson_zips)} lesson zip(s), {len(assignment_files)} assignment file(s), {len(slots)} slot(s).")

if len(lesson_zips) > len(slots):
    print(f"Warning: more lesson zips ({len(lesson_zips)}) than slots ({len(slots)}). Extra zips will be skipped.")

# --- Extract lesson zips into slots ---
for i, zip_path in enumerate(lesson_zips):
    if i >= len(slots):
        print(f"No more folders for: {os.path.basename(zip_path)} — skipping.")
        break
    slot_dir = os.path.join(dest_path, slots[i])
    print(f"Extracting {os.path.basename(zip_path)} -> {slots[i]}/")
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(slot_dir)

# Delete leftover unused slots
for slot in slots[len(lesson_zips):]:
    slot_dir = os.path.join(dest_path, slot)
    if os.path.exists(slot_dir):
        shutil.rmtree(slot_dir)
        print(f"Deleted unused folder: {slot}")

# --- Handle assignment files (any format) ---
for file_path in assignment_files:
    name = os.path.splitext(os.path.basename(file_path))[0].upper()
    assign_dir = os.path.join(dest_path, name)
    os.makedirs(assign_dir, exist_ok=True)
    if file_path.lower().endswith(".zip"):
        print(f"Extracting {os.path.basename(file_path)} -> {name}/")
        with zipfile.ZipFile(file_path, 'r') as z:
            z.extractall(assign_dir)
    else:
        dest_file = os.path.join(assign_dir, os.path.basename(file_path))
        shutil.copy2(file_path, dest_file)
        print(f"Copied {os.path.basename(file_path)} -> {name}/")

print("\nDone.")
