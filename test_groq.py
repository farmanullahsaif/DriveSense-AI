from utils.llm import llm


print("Testing DriveSense AI → Groq connection...")
print("")


response = llm.invoke(
    "You are DriveSense AI. Reply with exactly: "
    "DriveSense AI connection successful!"
)


print("AI Response:")
print(response.content)