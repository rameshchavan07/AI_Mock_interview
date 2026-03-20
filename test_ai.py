import sys
import os
import json
sys.path.append('backend')
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.local")
try:
    import ai_service
    result = ai_service.generate_interview_questions("Frontend Developer", "React, Next.js, UI/UX", 3)
    questions = json.loads(result)
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("--- Generated AI Questions ---\n\n")
        for i, q in enumerate(questions):
            f.write(f"Q{i+1}: {q.get('question')}\n")
            f.write(f"A{i+1}: {q.get('answer')}\n\n")
except Exception as e:
    import traceback
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("ERROR!\n")
        f.write(traceback.format_exc())
