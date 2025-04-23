import sys
from collections import defaultdict

# Dictionary to store word counts
word_counts = defaultdict(int)

# Read input from mapper
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    # Aggregate counts
    word_counts[word] += count

# Sort by frequency in descending order
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Print sorted results
for word, count in sorted_word_counts:
    print(f"{word}\t{count}")
