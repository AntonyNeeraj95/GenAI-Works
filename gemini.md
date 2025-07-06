📧 Email Drafting Agent
📌 Overview
This project, an Email Drafting Agent, is developed as part of a Hackathon Challenge organized by the GenAI Works community.

Please Note: This project is a forked and extended version of the genai-agentos repository, available at https://github.com/genai-works-org/genai-agentos.git. It leverages the foundational framework provided by GenAI Works to build a specialized email drafting service.

The Email Drafting Agent is an LLM-powered service that transforms minimal, bullet-point-style input into polished professional emails. It is built on top of GenAI Works AgentOS, a powerful and developer-friendly framework for deploying AI agents with ease.

GenAI Works provides a robust infrastructure with seamless experience for building, configuring, and deploying intelligent agents using modern LLMs. With features like secure key management, agent-level JWT authentication, and a full-featured frontend UI, AgentOS makes it incredibly easy to go from idea to working prototype.

✨ Features
Bullet-Point to Professional Email: Seamlessly converts concise, bullet-point inputs into well-structured and grammatically correct professional emails.

LLM-Powered Intelligence: Leverages advanced Large Language Models to understand context and generate natural-sounding email drafts.

Built on AgentOS: Benefits from the robust and scalable infrastructure provided by GenAI Works AgentOS.

Secure & Scalable: Inherits AgentOS's features like secure key management and agent-level JWT authentication for secure deployments.

User-Friendly UI: Integrates with the full-featured frontend UI provided by AgentOS for easy interaction.

🚀 Getting Started
Follow these steps to set up and run the Email Drafting Agent.

Prerequisites
[cite_start]

Docker & Docker Compose: Ensure you have Docker Desktop running.   

Git: For cloning the repository.

uv (Recommended) or pip & Python: For managing project dependencies.

OpenAI API Key: You will need an API key for OpenAI to power the LLM.

Installation & Setup Flow
Clone the genai-agentos repository:

Bash

[cite_start]git clone https://github.com/genai-works-org/genai-agentos.git [cite: 1]
Navigate to the project directory:

Bash

[cite_start]cd genai-agentos/ [cite: 2]
Create a .env file:
Copy the example environment file. [cite_start]A 

.env file should be present for configuration. [cite_start]All variables in    

.env-example are commented. [cite_start]You can customize any environment setting by uncommenting the relevant line and providing a new value.   

Bash

[cite_start]cp .env-example .env [cite: 1]
Start the infrastructure:
[cite_start]Ensure Docker Desktop is running. [cite_start]Then, start the core AgentOS infrastructure using    

make up or docker-compose up:   

Bash

[cite_start]make up [cite: 3]
# or alternatively
[cite_start]docker-compose up [cite: 3]
Access the Frontend UI and configure your profile:

[cite_start]Open your web browser and go to the Frontend UI at 

http://localhost:3000/.   

[cite_start]Sign up if you are a new user or log in if you already have an account.   

[cite_start]Navigate to the settings page, in your profile.   

[cite_start]Add your OpenAI key and models.   

Generate and copy a JWT token:

[cite_start]Generate a JWT token from the Agents tab and copy it.   

Configure the Mail Drafting Agent's environment variables:

[cite_start]Navigate to 

genai-agentos\cli\agents\mail_drafting_agent.   

[cite_start]Edit the 

.env file located in this directory.   

[cite_start]Set the 

AGENT_JWT and OPENAI_API_KEY variables:   

Ini, TOML

[cite_start]AGENT_JWT = "<your_jwt_token_here>" [cite: 5]
[cite_start]OPENAI_API_KEY = "<your_openai_api_key>" [cite: 5]
Set up and run the Mail Drafting Agent:

[cite_start]Open your terminal.   

[cite_start]Navigate to the agent's directory: 

genai-agentos\cli\agents\mail_drafting_agent.   

[cite_start]Create a virtual environment using 

uv venv or python -m venv:   

Bash

uv venv
# or
python -m venv .venv
Activate the environment:

Bash

[cite_start].venv\Scripts\activate [cite: 5]
[cite_start]Install dependencies using 

uv sync:   

Bash

uv sync
Run the Mail Drafting Agent:

Bash

[cite_start]uv mail_drafting_agent.py [cite: 5]
[cite_start]You can see the agent running in your Frontend UI.   

Usage
Go to the chat section:

[cite_start]In the AgentOS Frontend UI (

http://localhost:3000/), go to the chat section.   

Paste your prompt:

Provide your request in a bullet-point format.

[cite_start]An ideal prompt would look like this:   

[cite_start]• Recipient: Priya Sharma (HR Manager) [cite: 6]
[cite_start]• Purpose: Request for leave [cite: 6]
[cite_start]• Details: [cite: 6]
   - [cite_start]Leave from July 15–19 [cite: 6]
   - [cite_start]Reason: personal travel [cite: 6]
   - [cite_start]Will complete handover [cite: 6]
   - [cite_start]Reachable for urgent issues [cite: 6]
• Approx. [cite_start]Word Count: 120 [cite: 7]
💻 Development
Project Structure
(Assuming a typical AgentOS setup, your specific agent code resides within the cli/agents/mail_drafting_agent directory.)

.
├── .env.example
├── docker-compose.yml
├── cli/
│   ├── agents/
│   │   ├── mail_drafting_agent/    # Your Email Drafting Agent code
│   │   │   ├── .env                # Agent-specific environment variables
│   │   │   ├── mail_drafting_agent.py  # Main agent logic
│   │   │   └── requirements.txt    # Agent dependencies
│   │   └── ... (other agents)
│   └── ... (cli tools)
├── frontend/                     # AgentOS Frontend
├── services/                     # Core AgentOS services
└── README.md
Making Changes
Edit Agent Logic: Modify the Python files within cli/agents/mail_drafting_agent/ (e.g., mail_drafting_agent.py) to refine the email drafting logic, add new features, or integrate different LLM models.

Rebuild and Restart: After making code changes to the core infrastructure, you might need to rebuild your Docker containers:

Bash

docker-compose down
docker-compose up --build -d
For changes only to the mail_drafting_agent.py script, you would typically just re-run the uv mail_drafting_agent.py command after activating your virtual environment.

🤝 Contributing
We welcome contributions to enhance the Email Drafting Agent!

Fork the original genai-agentos repository or this project's fork if available.

Create a new branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.

Please ensure your code adheres to good practices and includes appropriate tests.

📄 License
This project is licensed under the MIT License.
The underlying AgentOS framework is also open-source; refer to its specific license in the original repository.

🌐 Community & Resources
GenAI Works Community: Join our community to discuss, get support, and collaborate on GenAI projects.

GenAI Works Website

GenAI Works AgentOS GitHub: Explore the core framework documentation and source code.

genai-agentos GitHub Repository


Sources and related content







