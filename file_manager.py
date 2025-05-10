import os
import re

def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as e:
        print(f"[X] Error creating folder {path}: {e}")
        return False

def save_code_to_file(code, base_dir):
    if not code or not code.strip():
        print("[X] No code provided to save")
        return False

    try:
        # Use regex to extract valid file paths and content blocks
        pattern = r'//\s+([^\n]+)\n([\s\S]*?)(?=//\s+[^\n]+\n|$)'
        matches = re.findall(pattern, code)

        if not matches:
            print("[X] No valid file sections found in the code.")
            return False

        for relative_path, file_content in matches:
            file_path = relative_path.strip()
            content = file_content.strip()

            if not file_path or not content:
                continue

            full_path = os.path.join(base_dir, file_path)
            folder = os.path.dirname(full_path)

            if not create_folder(folder):
                continue

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"[✓] Saved: {full_path}")

        return True

    except Exception as e:
        print(f"[X] Error saving code: {e}")
        return False
