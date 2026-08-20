# 🚗 DriveSense AI

### Intelligent Vehicle Diagnosis System

> An AI-powered multi-agent vehicle diagnosis assistant that helps drivers understand vehicle symptoms, identify possible causes, assess safety risks, and receive structured troubleshooting guidance.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.62.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-1.3.15-1C3C3C?style=for-the-badge)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-1.2.11-1C3C3C?style=for-the-badge)](https://www.langchain.com/langgraph)
[![Groq](https://img.shields.io/badge/Groq-Powered-F55036?style=for-the-badge)](https://groq.com/)

---

## 🚘 Overview

**DriveSense AI** is an intelligent vehicle diagnosis system designed to assist vehicle owners when they encounter common mechanical or performance-related problems.

Instead of simply asking an AI chatbot a generic automotive question, the system collects important vehicle information and the driver's reported symptoms before processing the problem through an AI-powered diagnostic workflow.

For example, a user can provide:

- Vehicle make and model
- Manufacturing year
- Engine capacity
- Fuel type
- Mileage
- Transmission type
- Warning lights
- Reported symptoms
- Additional observations

The system then analyzes the information and produces a structured diagnostic report.

---

## 🎯 Problem

Vehicle problems can be difficult for ordinary drivers to understand.

A symptom such as:

> "My car is jerking while accelerating."

could potentially be related to several different systems, including:

- Ignition
- Fuel delivery
- Air intake
- Sensors
- Throttle system
- Transmission
- Engine mechanical components

DriveSense AI aims to turn an unclear symptom into a structured starting point for investigation.

---

## 💡 Solution

DriveSense AI uses a **multi-agent AI workflow** rather than relying on a single response.

The system separates diagnostic responsibilities into specialized reasoning stages and combines their outputs into a final report.

### Core workflow

```text
                    ┌─────────────────────┐
                    │       Driver        │
                    │ Vehicle + Symptoms  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    DriveSense UI    │
                    │     Streamlit       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Coordinator     │
                    │   LangGraph Flow    │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
      ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
      │ Diagnostic  │   │    Safety   │   │ Troubleshoot│
      │    Agent    │   │    Agent    │   │    Agent    │
      └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │   Report / Summary  │
                    │  AI-powered Output  │
                    └─────────────────────┘
```

---

# 🧠 Multi-Agent Architecture

The project is designed around a multi-agent architecture powered by **LangGraph** and **LangChain**.

Each stage has a specific responsibility instead of asking one LLM call to perform the entire diagnostic process.

### 🔍 Diagnostic Reasoning

Analyzes the reported symptoms and vehicle information to identify potential causes.

### 🛡️ Safety Assessment

Evaluates whether the reported symptoms may indicate a situation where continued driving could be unsafe.

### 🔧 Troubleshooting Guidance

Provides structured diagnostic checks and possible next actions.

### 📋 Final Report

Combines the reasoning into a user-friendly vehicle diagnosis report.

---

# ⚙️ How It Works

### 1. Vehicle Information

The driver provides basic information about their vehicle.

Example:

```text
Make: Toyota
Model: Corolla
Year: 2018
Engine: 1.6L
Fuel: Petrol
Mileage: 120,000 km
```

### 2. Problem Description

The driver describes the problem using normal language.

Example:

```text
My car is jerking while accelerating and the Check Engine Light is on.
```

### 3. AI Processing

The request enters the DriveSense AI workflow.

The multi-agent system analyzes the symptoms and vehicle context.

### 4. Differential Diagnosis

Instead of claiming one confirmed fault, the system considers multiple possible causes and prioritizes them.

### 5. Safety Evaluation

The system evaluates potential driving risks and identifies situations where professional inspection may be appropriate.

### 6. Structured Report

The final result can contain:

- Vehicle summary
- Reported problem
- Possible causes
- Likelihood levels
- Recommended diagnostic checks
- Safety assessment
- Mechanic recommendations
- Follow-up questions
- Safety disclaimer

---

# 🧪 Example

### User Input

```text
Vehicle:
Toyota Corolla 2018
1.6L Petrol
120,000 km

Problem:
The car jerks during acceleration and the
Check Engine Light is on.
```

### DriveSense AI

The system may identify possibilities such as:

```text
HIGH
• Engine misfire
• Fuel delivery issue

MEDIUM
• Throttle body / air intake issue
• Vacuum leak

LOW
• Transmission-related issue
• Exhaust restriction
```

The system then recommends diagnostic checks and provides a safety assessment.

> These results are potential causes, not a confirmed mechanical diagnosis.

---

# 🖥️ User Experience

DriveSense AI is designed with a modern, responsive interface focused on simplicity and usability.

The interface is intended to make the diagnostic process easy for both desktop and mobile users.

### UX principles

- 📱 Mobile-friendly layout
- 🎯 Clear input flow
- 🚗 Vehicle-focused interface
- ⚡ Fast AI processing
- 📊 Structured diagnostic results
- 🚨 Prominent safety information
- 🧩 Easy-to-understand recommendations

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | Interactive web interface |
| LangChain | LLM application framework |
| LangGraph | Multi-agent workflow orchestration |
| Groq | LLM inference |
| Pydantic | Structured data validation |
| python-dotenv | Environment configuration |

---

# 📁 Project Architecture

The project follows a modular architecture so that individual agents and components can be developed and improved independently.

```text
DriveSenseAI/
│
├── agents/
│   ├── ...
│   └── ...
│
├── utils/
│   └── prompts.py
│
├── app.py
├── coordinator.py
│
├── test_workflow.py
├── test_groq.py
│
├── requirements.txt
├── .gitignore
├── README.md
│
└── .env
```

> `.env` is intentionally excluded from version control and must never contain a publicly exposed API key.

---

# 🔐 Environment Configuration

Create a `.env` file in the project root.

Example:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Never commit your real API key to GitHub.

The `.env` file should remain inside `.gitignore`.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/farmanullahsaif/DriveSense-AI.git
```

```bash
cd DriveSense-AI
```

## 2. Create a virtual environment

Windows:

```powershell
py -3.11 -m venv venv
```

## 3. Activate the environment

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

## 4. Install dependencies

```powershell
pip install -r requirements.txt
```

## 5. Configure your API key

Create `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## 6. Run the application

```powershell
streamlit run app.py
```

The application will then be available through the Streamlit local URL.

---

# 🧪 Testing

The project includes workflow and AI connection testing.

Example:

```powershell
python test_groq.py
```

and:

```powershell
python test_workflow.py
```

These tests help verify the AI connection and multi-agent workflow.

---

# 🛡️ Safety Philosophy

DriveSense AI is designed as an **assistive diagnostic tool**, not a replacement for a qualified automotive technician.

Vehicle symptoms can have multiple causes, and an AI-generated result cannot physically inspect a vehicle.

The system therefore emphasizes:

- Potential causes rather than guaranteed diagnoses
- Diagnostic checks rather than blind part replacement
- Safety warnings
- Professional mechanic recommendations
- Additional questions to improve diagnostic accuracy

### 🚨 Important

If a vehicle has severe symptoms such as:

- Sudden loss of power
- Engine stalling
- Severe overheating
- Smoke
- Burning smell
- Dangerous handling
- Severe braking problems

the driver should prioritize safety and seek professional assistance.

---

# 🗺️ Future Roadmap

DriveSense AI is designed to evolve beyond symptom-based diagnosis.

### Planned improvements

- [ ] OBD-II data integration
- [ ] Real-time vehicle sensor analysis
- [ ] Diagnostic trouble code interpretation
- [ ] Vehicle-specific knowledge base
- [ ] Maintenance recommendations
- [ ] Service history tracking
- [ ] Repair cost estimation
- [ ] Mechanic / workshop recommendations
- [ ] Voice-based symptom reporting
- [ ] Image-based component inspection
- [ ] Mobile application
- [ ] User accounts and diagnostic history
- [ ] Improved automotive knowledge retrieval
- [ ] Confidence scoring and evidence-backed diagnosis

---

# 📊 Project Vision

The long-term goal of DriveSense AI is to create an intelligent vehicle assistant that can combine:

```text
Driver Symptoms
       +
Vehicle Information
       +
OBD-II Data
       +
Automotive Knowledge
       +
Multi-Agent Reasoning
       ↓
Intelligent Vehicle Assistance
```

---

# 👨‍💻 Developer

**Farman Ullah Saif**

Artificial Intelligence Student

Interested in:

- Artificial Intelligence
- Generative AI
- Multi-Agent Systems
- LLM Applications
- AI Engineering
- Intelligent Automation

---

# 📄 License

This project is intended for educational and portfolio purposes.

---

## ⚠️ Disclaimer

DriveSense AI provides AI-generated informational guidance and does not provide a guaranteed mechanical diagnosis.

Always use appropriate caution when working on vehicles and consult a qualified automotive professional for inspection, repair, or safety-critical problems.

---

⭐ If you find this project interesting, consider starring the repository.