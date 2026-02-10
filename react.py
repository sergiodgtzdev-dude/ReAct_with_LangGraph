from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()


@tool
def triple(num: float) -> float:
    """
    Takes an input floating point number and triples its value, then returns the tripled number.
    :param num: floating point number to be tripled
    :return: tripled input number
    """

    return num * 3


tools = [TavilySearch(max_results=1), triple]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools=tools)
