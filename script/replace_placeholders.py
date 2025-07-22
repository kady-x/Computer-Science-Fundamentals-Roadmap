import os

def replace_placeholders(file_path, replacements):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        for placeholder, value in replacements.items():
            content = content.replace(f"{{{{{placeholder}}}}}", value)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"Placeholders in {file_path} have been replaced successfully.")
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

if __name__ == "__main__":
    english_path = "README.md"
    arabic_path = "README_AR.md"

    english_replacements = {
        "center": "<div align=\"center\" style=\"background-image: url(''); background-size: cover; background-position: center; padding: 20px;\">",
        "project_name": "Computer Science Fundamentals Roadmap",
        "emoji_path": "<img src=\"https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis",
        "emoji_end": "\" width=\"25\" height=\"25\">",
        "author_name": "Ahmed M. Yahia",
        "author_github": "https://github.com/ahmedmahmoud72",
        "editor_name": "Mohamed Kady",
        "editor_github": "https://github.com/kady-x"
    }

    arabic_replacements = {
        "center": "<div align=\"center\" style=\"background-image: url(''); background-size: cover; background-position: center; padding: 20px;\">",
        "project_name": "خارطة طريق أساسيات علوم الحاسب",
        "emoji_path": "<img src=\"https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis",
        "emoji_end": "\" width=\"25\" height=\"25\">",
        "author_name": "أحمد م. يحيى",
        "author_github": "https://github.com/ahmedmahmoud72",
        "editor_name": "محمد قاضي",
        "editor_github": "https://github.com/kady-x"
    }

    replace_placeholders(english_path, english_replacements)
    replace_placeholders(arabic_path, arabic_replacements)
