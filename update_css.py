import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

replacements = {
    "#1b1b19": "#f4f6f8",
    "#2d2c29": "#ffffff",
    "#9b917c": "#a3c9c9",
    "#d4c5a9": "#6b8e8e",
    "#b4a88c": "#a3c9c9",
    "#e8e1d5": "#636e72",
    "#a7a195": "#b2bec3",
    "rgba(255, 255, 255, 0.02)": "rgba(163, 201, 201, 0.05)",
    "rgba(255, 255, 255, 0.04)": "rgba(163, 201, 201, 0.15)",
    "rgba(27, 27, 25, 0.9)": "rgba(244, 246, 248, 0.9)",
    "rgba(45, 44, 41, 0.95)": "rgba(255, 255, 255, 0.95)",
    "rgba(212, 197, 169": "rgba(163, 201, 201",
    "rgba(180, 168, 140": "rgba(163, 201, 201",
    "rgba(155, 145, 124": "rgba(163, 201, 201",
    "--text-primary: #ffffff;": "--text-primary: #2d3436;",
    "box-shadow: 0 0 50px rgba(0, 0, 0, 0.6);": "box-shadow: 0 10px 40px rgba(163, 201, 201, 0.2);",
    "box-shadow: 0 -15px 30px rgba(0, 0, 0, 0.3);": "box-shadow: 0 -15px 30px rgba(163, 201, 201, 0.15);",
    "text-shadow: 0 0 6px rgba(212, 197, 169, 0.8), 0 0 15px rgba(212, 197, 169, 0.4), 0 0 3px rgba(0, 0, 0, 0.9);": "text-shadow: none;",
    "text-shadow: 0 0 3px rgba(0, 0, 0, 0.9);": "text-shadow: none;",
    "color: var(--text-primary);": "color: var(--text-primary);",
    "background: rgba(0, 0, 0, 0.35);": "background: rgba(255, 255, 255, 0.8);",
    "background: rgba(255, 255, 255, 0.15);": "background: #ffffff;",
    "border: 1px solid rgba(255, 255, 255, 0.2);": "border: 1px solid rgba(163, 201, 201, 0.3);",
    "rgba(0, 0, 0, 0.2) 0%": "rgba(255, 255, 255, 0.1) 0%",
    "rgba(0, 0, 0, 0.1) 40%": "rgba(255, 255, 255, 0.3) 40%",
    "rgba(0, 0, 0, 0.6) 75%": "rgba(255, 255, 255, 0.8) 75%",
    "rgba(45, 44, 41, 0.95) 100%": "rgba(255, 255, 255, 1) 100%",
    "fill: rgba(255, 255, 255, 0.1);": "fill: #a3c9c9;",
    "#beb399": "#8bb4b5",
}

for old, new in replacements.items():
    css = css.replace(old, new)

# Special fix for highlight button text since text-primary changed to dark, but button text needs to be white
css = css.replace(".split-btn.gold-highlight .btn-title {\n    color: #ffffff;\n}", ".split-btn.gold-highlight .btn-title {\n    color: #ffffff;\n}")

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("CSS updated.")
