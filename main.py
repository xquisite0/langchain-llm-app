from langchain_community.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name():
    # temperature: 0 safe outputs, 1 creative outputs with risk of hallucination
    llm = OpenAI(temperature=0.7)

    name = llm("I have a dog pet and I want a cool name for it. Suggest me five cool names for my pet.")

    return name

if __name__ == "__main__":
    print(generate_pet_name())