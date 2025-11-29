import os

# Define folder structure
structure = [
    "assets/css",
    "assets/js",
    "assets/images"
]

# Define files to create
files = {
    "assets/css/style.css": "/* Main CSS file */\n",
    "assets/js/app.js": "// Main JS file\n"
}

# Create folders
for path in structure:
    os.makedirs(path, exist_ok=True)
    print(f"Created folder: {path}")

# Create files
for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)
    print(f"Created file: {filepath}")

print("\nProject structure created successfully!")
