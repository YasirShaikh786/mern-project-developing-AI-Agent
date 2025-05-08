import os
import sys
from ollama import get_code_from_ollama  # Changed from openai to ollama
from file_manager import save_code_to_file, create_folder
import shutil

def setup_project(base_path):
    try:
        shutil.copytree("templates/frontend", os.path.join(base_path, "frontend"), dirs_exist_ok=True)
        shutil.copytree("templates/backend", os.path.join(base_path, "backend"), dirs_exist_ok=True)
        print("[✓] MERN boilerplate copied.")
        return True
    except Exception as e:
        print(f"[X] Error copying templates: {e}")
        return False

def main():
    print("MERN Project Setup Agent")
    print("------------------------")
    
    instruction = input("What do you want the agent to do? (e.g., Setup MERN with login system):\n").strip()
    project_path = input("Where should the project be created? (e.g., D:/projects/chat-app):\n").strip()

    if not os.path.exists("templates"):
        print("[X] Error: 'templates' directory not found!")
        return

    create_folder(project_path)
    if not setup_project(project_path):
        return

    print("[→] Generating code using AI...")
    prompt = f"""
    Create code for a MERN stack project that includes: {instruction}
    Important guidelines:
    1. Include comments with file paths (// server/controllers/authController.js)
    2. Use proper MERN architecture
    3. Include error handling
    """
    code = get_code_from_ollama(prompt)
    save_code_to_file(code, project_path)

if __name__ == "__main__":
    main()