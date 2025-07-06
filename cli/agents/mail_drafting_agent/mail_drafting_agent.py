import asyncio
import os
from typing import Annotated
from dotenv import load_dotenv
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
from openai import OpenAI
load_dotenv()
AGENT_JWT = os.getenv("AGENT_JWT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# ROUTER_WS_URL = os.getenv("ROUTER_WS_URL")

system_prompt  = """You are an Email Drafting Agent.

    Your job is to take minimal, bullet-point-style input from a user and return a polished, professional, and well-structured email draft.

    Follow these rules strictly:

    1. Return an email that includes:
       - A clear and relevant **Subject Line**
       - A natural and respectful **Greeting**:
         • If recipient’s name is given, use it (e.g., “Dear Jake,”)
         • If only role is given, use that (e.g., “Dear HR Manager,”)
         • If neither is given, use “Hello,”
       - A **Concise Email Body**:
         • Clearly state the purpose
         • Expand the bullet points into smooth, readable sentences
         • Maintain a neutral, courteous, and polished tone
         • Use natural transitions for flow
         • Adapt tone based on the purpose:
           - More formal for requests, applications, or business communication
           - Friendly-professional for internal or casual updates
       - A **Professional Closing**:
         • Use standard sign-offs like “Best regards,” or “Sincerely,”
         • If sender name is missing, end with “[Your Name]” as a placeholder

    2. Respect the **Approximate Word Count** given by the user (within ±10% range). If not specified, default to ~120 words.

    3. Never output raw bullet points — always return a complete and formatted email.

    4. If required information is missing, make a reasonable, professional default assumption.

    5. Always return a complete email draft, even if some details are missing.
       - Use placeholders like “[Your Name]” or “[Recipient’s Name]” where necessary.

    6. If the user provides a specific email format, follow it closely.

    7. If the user provides a specific tone or style, adapt to it.
    """

session = GenAISession(jwt_token=AGENT_JWT)                                                  ### , ws_url=ROUTER_WS_URL
openai_client = OpenAI(
    api_key=OPENAI_API_KEY,
)



@session.bind(
    name="mail_drafting_agent",
    description="Agent drafts mail from User Input"
)
async def mail_drafting_agent(
    agent_context: GenAIContext,
    text: Annotated[str,"User Input text to draft the email."],
)-> str:
    """Agent drafts mail from User Input"""
    agent_context.logger.info(f"Inside the mail_drafting_agent")

    response = openai_client.chat.completions.create(
        messages=[
            {"role": "system","content": system_prompt},
            {"role": "user", "content": text}
        ],
        model="gpt-4o-mini"
    )
    result = response.choices[0].message.content
    return result

async def main():
    print(f"Agent with token '{AGENT_JWT}' started")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
