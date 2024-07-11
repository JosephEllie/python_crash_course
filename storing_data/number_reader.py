from pathlib import Path
import json

# Storing data in JSON format
numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

load_content = path.read_text()
display_content = json.loads(load_content)

print(type(display_content))
