import re
with open("index.html", "r") as f:
    content = f.read()

content = content.replace(
    """grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));""",
    """grid-template-columns: repeat(4, 1fr);"""
)

with open("index.html", "w") as f:
    f.write(content)
