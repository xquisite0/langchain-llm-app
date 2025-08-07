from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    # temperature: 0 safe outputs, 1 creative outputs with risk of hallucination
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type} pet and I want a cool name for it. It is {pet_color} in color. Suggest me five cool names for my pet."
    )

    chain = prompt_template_name | llm
    response = chain.invoke({'animal_type': animal_type, 'pet_color': pet_color})
    return response

def langchain_agent():
    llm = OpenAI(temperature=0)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    # download ready to use prompt from langchain creator hwchase17
    prompt = hub.pull("hwchase17/react")

    # initialize agent. We use a basic agent type from documentation
    # verbose=True will print out the agent's thought process
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
    )


    result = agent_executor.invoke(
        {"input": "Use Wikipedia to find the average lifespan of a dog. Then use the calculator to multiply that number by 3."}
    )

    print(result)


if __name__ == "__main__":
    # print(generate_pet_name("hamster", "brown"))
    langchain_agent()