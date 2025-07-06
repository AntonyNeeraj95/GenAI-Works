
# 📧 Email Drafting Agent — Documentation

## 📌 Overview

This project is developed as part of a **Hackathon Challenge** organized by the **GenAI Works community**.

The **Email Drafting Agent** is an LLM-powered service that transforms minimal, bullet-point-style input into polished professional emails. It is built on top of **GenAI Works AgentOS**, a powerful and developer-friendly framework for deploying AI agents with ease.

GenAI Works provides a robust infrastructure with seamless experience for building, configuring, and deploying intelligent agents using modern LLMs. With features like secure key management, agent-level JWT authentication, a full-featured frontend UI, **AgentOS** makes it incredibly easy to go from idea to working prototype.

> 🔄 **Note:** This implementation is a **forked version** of the official [genai-agentos repository](https://github.com/genai-works-org/genai-agentos.git). The codebase has been adapted to address the specific requirements of structured email generation.

🧩 GitHub Repository: [genai-agentos](https://github.com/genai-works-org/genai-agentos.git)  
🌐 Community: [GenAI Works](https://https://genai.works/)

## ✨ Features
* Bullet-Point to Professional Email: Seamlessly converts concise, bullet-point inputs into well-structured and grammatically correct professional emails.

* LLM-Powered Intelligence: Leverages advanced Large Language Models to understand context and generate natural-sounding email drafts.

* Built on AgentOS: Benefits from the robust and scalable infrastructure provided by GenAI Works AgentOS.

* Secure & Scalable: Inherits AgentOS's features like secure key management and agent-level JWT authentication for secure deployments.

* User-Friendly UI: Integrates with the full-featured frontend UI provided by AgentOS for easy interaction.


## ⚙️ Prerequisites

Ensure the following tools are available on your machine:

- **Git**
- **Python 3.10+**
- **[uv](https://github.com/astral-sh/uv)** (recommended Python package manager)
- **Docker Desktop**
- **OpenAI API Key**

> If `uv` is not installed, you can use `pip` as an alternative.

## 🚀 Getting Started
Follow these steps to set up and run the Email Drafting Agent.


## 🧪 1. Clone the Repository

```bash
git clone https://github.com/AntonyNeeraj95/genai-agentos.git
cd genai-agentos/
```

## 🔐 2. Configure Environment

Create your `.env` file for AgentOS configuration:

```bash
cp .env-example .env
```

- This `.env` file can be empty at first.
- All variables in `.env-example` are commented — uncomment and edit as needed.
- Example settings include ports, model defaults, and OpenAI keys.

## 🐳 3. Start Docker & Infrastructure

Make sure **Docker Desktop** is running.

Start infrastructure:

```bash
make up
# or alternatively
docker-compose up
```

Once started, access the platform at:

- **Frontend UI:** [http://localhost:3000](http://localhost:3000)
- **Swagger API Docs:** [http://localhost:8000/docs/](http://localhost:8000/docs/)

## 🔑 4. UI Setup & Authentication

1. Open the UI: [http://localhost:3000](http://localhost:3000)
2. Sign up or log in.
3. Go to your **profile settings**.
4. Add:
   - **OpenAI API Key**
   - **Preferred Model** (e.g., `gpt-4o`)

## 🔐 5. Agent JWT Configuration

1. Navigate to the **Agents tab** in the frontend.
2. Click **"Generate Token"**.
3. Copy the token and update the agent-specific `.env`:

```bash
cd genai-agentos/cli/agents/mail_drafting_agent/
```

Create your `.env` file for the agent:

```bash
cp .env-example .env
```

Edit the `.env` file in this folder:

```env
AGENT_JWT = "<your_jwt_token_here>"
OPENAI_API_KEY = "<your_openai_api_key>"
```

## 🐍 6. Python Environment for CLI Agent

In the `mail_drafting_agent/` directory:

```bash
# Create virtual environment
uv venv
# OR
python -m venv .venv

# Activate environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Install dependencies
uv sync
```

> If using `pip` instead of `uv`:
```bash
pip install -r requirements.txt
```

## 🚀 7. Run the Agent

From the same directory:

```bash
uv run mail_drafting_agent.py
#OR
python mail_drafting_agent.py
```

Once running, the agent will be visible and interactable in your **Frontend UI → Chat Section**.

## 💬 Example Prompt (Ideal Format)

Paste the following bullet-style input into the chat window:

```plaintext
• Recipient: Priya Sharma (HR Manager)  
• Purpose: Request for leave  
• Details:  
   - Leave from July 15–19  
   - Reason: personal travel  
   - Will complete handover  
   - Reachable for urgent issues  
• Approx. Word Count: 120
```

## 📝 Output Example

```plaintext
Subject: Leave Request for July 15–19

Dear Priya,

I hope you're doing well.  
I’m writing to request leave from July 15 to July 19 for personal travel. I’ll ensure all responsibilities are handed over before my absence and will remain reachable for urgent matters.

Thank you for your understanding.

Best regards,  
[Your Name]
```
## 🌐 Ngrok Setup 

Ngrok can be used to expose the local WebSocket endpoint to external clients or collaborators.

### 🔧 Install Ngrok

Choose your operating system:

- **macOS (Homebrew)**  
  ```bash
  brew install ngrok/ngrok/ngrok
  ```

- **Linux (Snap)**  
  ```bash
  sudo snap install ngrok
  ```

### 🔐 Authenticate Ngrok

1. Sign up or log in at the [Ngrok Dashboard](https://dashboard.ngrok.com/).
2. Navigate to **"Your Authtoken"** section and copy your personal token.
3. Run the following command in your terminal:

   ```bash
   ngrok config add-authtoken <YOUR_AUTH_TOKEN>
   ```

### 🚀 Start a Tunnel

To expose your local port run:

```bash
ngrok http 3000
```

This will generate a public WebSocket URL.
In my scenario, the AgentOS UI is deployed in the below URL.

```
https://1b27-2401-4900-8fdd-74da-9ccd-595f-85ec-e999.ngrok-free.app
```
**NOTE** : The above URL lasts live until the Docker container is up.

This link can be accessed by your clients or collabarators for testing purposes.
### 🔄 Update Configuration

Copy the generated WebSocket URL and update the `ws_url` field in the following module:

```
genai_session.session.GenAISession
```

---


## 🗂️ Project Structure

The repository follows a modular layout to separate concerns across core functionalities, CLI agent logic, backend services, and frontend UI.

```text
genai-agentos/
│
├── .github/                     # GitHub Actions & workflows
├── backend/                     # Backend services and APIs
├── cli/                         # Command-line interface for agents
│   ├── .venv/                   # Virtual environment (excluded from version control)
│   ├── agents/
│   │   └── mail_drafting_agent/  # Main agent logic
│   │       ├── .env
│   │       ├── mail_drafting_agent.py
│   │       ├── pyproject.toml
│   │       └── uv.lock
│   ├── src/                     # CLI utilities or scripts
│   ├── build_cli.ps1
│   ├── build_cli.sh
│   ├── cli.py
│   ├── get_release_version.sh
│   ├── install_cli.ps1
│   ├── install_cli.sh
│   ├── pyproject.toml
│   ├── uv.lock
│   └── README.md
│
├── frontend/                    # Frontend React-based UI
├── genai_agents_example/        # Sample/custom agents
├── master-agent/                # Master agent logic and dispatcher
├── router/                      # API routing and endpoint logic
├── tests/                       # Unit and integration tests
│
├── .env                         # Root-level environment configuration
├── .env-example                 # Sample env file
├── .gitignore                   # Git exclusions
├── docker-compose.yml          # Docker service definitions
├── Makefile                    # Build and orchestration commands
└── README.md                   # Project entry-point documentation
```
> 🛠️ **Note:** Some directories (like `.venv`) are environment-specific and may be excluded in version control using `.gitignore`.

## 🧠 Agent Design Highlights

- **Word Count Control**: Tries to stay within ±10% of specified word count.
- **Tone Adaptation**: Adjusts tone based on purpose (formal vs. friendly-professional).
- **Fallback Logic**: Uses defaults like “[Your Name]” or “Hello,” if inputs are missing.
- **No Raw Bullet Output**: Always returns polished prose.

## ❗Troubleshooting

| Issue | Solution |
|-------|----------|
| Agent not showing in UI | Ensure agent was started correctly using `uv run mail_drafting_agent.py` |
| OpenAI key not working | Recheck `.env` and model access |
| `uv` not found | Install `uv` or use `python` + `pip` as fallback |
| Token invalid | Regenerate JWT from UI and update the agent’s `.env` |

## 📦 Making Changes
Edit Agent Logic: Modify the Python files within cli/agents/mail_drafting_agent/ (e.g., mail_drafting_agent.py) to refine the email drafting logic, add new features, or integrate different LLM models.

Rebuild and Restart: After making code changes to the core infrastructure, you might need to rebuild your Docker containers