import urllib.request
import json

url = "http://localhost:8000/api/interview/generate"
data = {
    "jobPosition": "Full Stack Developer",
    "jobDesc": "React, Next.js, FastAPI, Python",
    "jobExperience": "3",
    "userEmail": "demo@example.com"
}
req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers={"Content-Type": "application/json"})

try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode())
        mock_id = result.get("mockId")
        print(f"✅ Successfully generated new interview ID: {mock_id}\n")
        
        # Now fetch the stored interview details
        get_url = f"http://localhost:8000/api/interview/{mock_id}"
        get_req = urllib.request.Request(get_url)
        with urllib.request.urlopen(get_req) as get_response:
            interview_data = json.loads(get_response.read().decode())
            print("--- Generated AI Questions from Gemini ---")
            
            # The AI questions are stored as a JSON string inside jsonMockResp
            questions = json.loads(interview_data["jsonMockResp"])
            for idx, q in enumerate(questions):
                print(f"Q{idx+1}: {q.get('question')}")
                print(f"A{idx+1}: {q.get('answer')}\n")
except Exception as e:
    print(f"Error: {e}")
