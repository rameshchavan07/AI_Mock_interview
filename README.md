# AI Mock Interview Platform 🚀

An AI-powered mock interview application that generates customized technical questions based on your job role, experience, and tech stack. It records your spoken answers using your webcam and microphone, transcribes them in real-time, and uses Google's Gemini AI to evaluate and provide targeted feedback on your performance!

## 🏗️ Technology Stack

This project uses a modern decoupled architecture:

### Frontend
- **Framework**: Next.js 14 (App Router) & React 18
- **Styling**: Tailwind CSS & Radix UI (shadcn)
- **Authentication**: Clerk
- **Media**: `react-webcam` and `react-hook-speech-to-text`

### Backend (Python API)
- **Framework**: Python FastAPI
- **Database**: Neon Serverless PostgreSQL
- **ORM**: SQLAlchemy
- **Artificial Intelligence**: Google Gemini 2.5 Flash (`google-generativeai`)

---

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed:
1. **Node.js** (v18 or higher)
2. **Python** (v3.9 or higher)
3. **API Keys**:
   - A [Clerk](https://clerk.com) account for authentication keys.
   - A [Neon](https://neon.tech) account for a PostgreSQL connection string.
   - A [Google AI Studio](https://aistudio.google.com/) account for a Gemini API key.

---

## 🚀 Getting Started

### 1. Environment variables
Create a `.env.local` file in the root directory and add your secret keys:

```env
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=your_clerk_publishable_key
CLERK_SECRET_KEY=your_clerk_secret_key

NEXT_PUBLIC_DRIZZLE_DB_URL=postgresql://user:password@endpoint.neon.tech/dbname?sslmode=require
NEXT_PUBLIC_GEMINI_API_KEY=your_google_gemini_api_key
NEXT_PUBLIC_INTERVIEW_QUESTION_COUNT=5
```

### 2. Setup the Python Backend
Open a terminal and navigate to the project root, then set up the Python virtual environment and run the FastAPI server:

```bash
cd backend
python -m venv venv
# On Windows use: .\venv\Scripts\activate
# On Mac/Linux use: source venv/bin/activate

pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```
The backend API should now be running locally at `http://localhost:8000`.

### 3. Setup the Next.js Frontend
Open a **new** terminal window, navigate to the project root, and install the Node modules:

```bash
npm install
npm run dev
```

### 4. Start Interviewing!
Open [http://localhost:3000](http://localhost:3000) in your browser. 
Log in using Clerk, navigate to the dashboard, and create your first mock interview. Ensure your browser is allowed to access your microphone and camera!

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.
