import os, re, sys
from pathlib import Path

base_dir = r"C:\Users\msh897\Documents\Obsidian\trading-vault\transcripts"
output_file = r"C:\Users\msh897\Documents\Obsidian\trading-vault\transcripts\MENTAL_CLARITY_SEARCH_RESULTS.md"

patterns = {
    "Mental Clarity / Mind Clarity": [r'\bmental clarity\b', r'\bmind clarity\b', r'\bmental confusion\b'],
    "Confidence": [r'\bconfidence\b'],
    "Expertise": [r'\bexpertise\b'],
    "Deep Work / Cal Newport": [r'\bdeep work\b', r'\bCal Newport\b'],
    "FOMO": [r'\bFOMO\b'],
    "Crying / Stop Crying": [r'\bcrying\b', r'\bstop crying\b'],
    "Process Mindset": [r'\bprocess mindset\b', r'\btrading process\b', r'\bdaily process\b', r'\bprocess edge\b'],
    "Grinding": [r'\bgrinding\b'],
    "Home Run": [r'\bhome run\b'],
    "Expertise-Confidence / Comfort Confidence": [r'\bexpertise-confidence\b', r'\bcomfort confidence\b', r'\bbuild confidence\b'],
    "Willing to Execute": [r'\bwilling to execute\b'],
    "Wrong Understanding": [r'\bwrong understanding\b'],
    "5000 Example / Study Plan": [r'5000\s*example', r'5,000\s*example', r'\bstudy plan\b'],
    "Metaphors": [r'\btight pants\b', r'\bbell bottoms\b'],
}

def get_context(lines, idx, window=2):
    start = max(0, idx - window)
    end = min(len(lines), idx + window + 1)
    return "\n".join(lines[start:end])

results = []
seen = set()
md_files = list(Path(base_dir).rglob("*.md"))

for file_path in md_files:
    if file_path.name == "MENTAL_CLARITY_SEARCH_RESULTS.md":
        continue
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception:
        continue

    for concept, regex_list in patterns.items():
        for regex in regex_list:
            for i, line in enumerate(lines):
                if re.search(regex, line, re.IGNORECASE):
                    key = (str(file_path), i, line.strip())
                    if key in seen:
                        continue
                    seen.add(key)
                    context = get_context(lines, i, window=2)
                    results.append({
                        "concept": concept,
                        "file": str(file_path),
                        "line_num": i+1,
                        "match": line.strip(),
                        "context": context
                    })

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# Mental Clarity & Confidence Search Results\n\n")
    grouped = {}
    for r in results:
        grouped.setdefault(r["concept"], []).append(r)
    
    for concept, items in grouped.items():
        f.write(f"## {concept}\n\n")
        f.write(f"**Total matches:** {len(items)}\n\n")
        for item in items:
            rel_path = os.path.relpath(item["file"], base_dir)
            f.write(f"### Source: `{rel_path}` (Line {item['line_num']})\n")
            f.write(f"**Match:** {item['match']}\n\n")
            f.write(f"**Context:**\n```\n{item['context']}\n```\n\n")
            f.write("---\n\n")

print(f"Done. Found {len(results)} total matches. Saved to {output_file}")
