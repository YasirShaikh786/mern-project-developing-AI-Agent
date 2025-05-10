import os
import shutil
from code_generator import get_code_from_openai
from file_manager import save_code_to_file, create_folder

def setup_project(base_path, project_name):
    project_path = os.path.join(base_path, project_name)
    try:
        # Create main project folder
        create_folder(project_path)
        
        # Create client and server subfolders from templates
        shutil.copytree("templates/frontend", os.path.join(project_path, "frontend"), dirs_exist_ok=True)
        shutil.copytree("templates/backend", os.path.join(project_path, "backend"), dirs_exist_ok=True)
        print(f"[✓] MERN project '{project_name}' created at: {project_path}")
        return project_path
    except Exception as e:
        print(f"[X] Error setting up project: {e}")
        return None

def get_user_prompt():
    print("\nDescribe your MERN app requirements (e.g., 'Create a login system with admin dashboard'):")
    print("(Type your prompt, press Enter twice to finish)")
    lines = []
    while True:
        line = input()
        if not line.strip() and lines:
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    print("MERN Project Generator")
    print("----------------------")
    
    base_location = input("Where should the project be created? (e.g., D:/projects):\n").strip()
    project_name = input("What should the project be called? (e.g., my-mern-app):\n").strip()
    
    project_path = setup_project(base_location, project_name)
    if not project_path:
        return

    user_prompt = get_user_prompt()
    print("\n[→] Generating code using AI...")

    structured_prompt = f"""
You are to return production-ready code for the following MERN stack app requirement:

{user_prompt}

File structure:
// backend/controllers/authController.js
// backend/controllers/(othercontrollers)
// backend/models/user.js
// backend/models/(othermodels)
// backend/routes/authRoutes.js
// backend/routes/(otherroutes)
// backend/db/connectDB.js(MongoDB connection)
// backend/utils/generateToken.js(if needed)
// backend/middleware/auth.js(if needed)
// frontend/src/pages/Login.jsx
// frontend/src/pages/(otherpages)
// frontend/src/components/dashboard.jsx
// frontend/src/components/(othercomponents)
// frontend/src/(otherfiles)
// etc.

Format the output strictly like this:

// path/to/file.ext
<code for that file>

// another/path/file.ext
<code for that file>

Only return code in this format. Do NOT include any explanation or comments outside of code blocks.
"""

    code = get_code_from_openai(structured_prompt)
    save_code_to_file(code, project_path)

if __name__ == "__main__":
    main()
