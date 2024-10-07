import getpass
import os

from langchain_google_genai import ChatGoogleGenerativeAI

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass(
        "Enter your Google AI API key: "
    )

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
result = llm.invoke("Sing a ballad of LangChain.")
print(result.content)
