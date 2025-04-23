import sys
import json

for line in sys.stdin:
    try:
        # Parse JSON line
        record = json.loads(line)
        # Extract the "text" field (or another field you need)
        text = record.get("text", "")
        # Tokenize and output key-value pairs
        words = text.split()
        for word in words:
            print(f"{word}\t1")
    except json.JSONDecodeError:
        # Handle invalid JSON
        continue
