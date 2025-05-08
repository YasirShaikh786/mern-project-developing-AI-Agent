import subprocess
import json

def get_code_from_ollama(prompt, model="mistral", timeout=120):
    try:
        # Structured prompt for better code generation
        structured_prompt = {
            "instruction": "Generate MERN stack code",
            "requirements": [
                "Include file path as first comment",
                "Use modern JavaScript/TypeScript",
                "Follow best practices",
                "Include error handling"
            ],
            "task": prompt
        }
        
        result = subprocess.run(
            ['C:\\Users\\yasir\\AppData\\Local\\Programs\\Ollama\\ollama.exe','run', model, json.dumps(structured_prompt)],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout
        )

        if result.stderr:
            print(f"[!] Ollama warning: {result.stderr.decode('utf-8').strip()}")

        output = result.stdout.decode("utf-8").strip()
        return output

    except subprocess.TimeoutExpired:
        return "[Error] Model took too long to respond."

    except Exception as e:
        return f"[Error] Failed to run ollama model: {e}"