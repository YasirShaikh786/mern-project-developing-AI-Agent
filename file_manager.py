import os

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
        # Extract file path from first comment line
        lines = code.split("\n")
        file_path = "unsorted/generated_code.js"  # default
        
        for line in lines[:5]:  # Check first 5 lines for path hint
            if line.strip().startswith("//"):
                file_path = line.strip()[2:].strip()
                break

        full_path = os.path.join(base_dir, file_path)
        folder = os.path.dirname(full_path)
        
        if not create_folder(folder):
            return False

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(code)
        
        print(f"[✓] Code saved to {full_path}")
        return True
        
    except Exception as e:
        print(f"[X] Error saving code to file: {e}")
        return False