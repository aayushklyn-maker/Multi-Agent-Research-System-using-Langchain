from dotenv import load_dotenv
import rich
from rich import print
from src.Agents.agents import build_search_agent,build_reader_agent,writer_chain,critic_chain
load_dotenv()

def run_research_pipeline(topic:str)-> dict:
    state = {}
    print("Search Agent is working....\n")
    search_result = build_search_agent().invoke({
        "messages" : [("user",f"Find recent and reliable information on {topic} along with URLs")]
    })
    state['search_result'] = search_result['messages'][-1].content
    print("Search Results :\n",state['search_result'])
    print()

    print("Reader Agent is working....\n")
    reader_result = build_reader_agent().invoke({
        "messages" : [("user",
                       f"Based on the following search results about {topic}"
                       f"Extract deeper information from relevant urls"
                       f"Search results : {state['search_result']}")]
    })
    state['scraped_content'] = reader_result['messages'][-1].content
    print("Scraped Content :\n",state['scraped_content'])

    print()
    print("Writer Agent is working....\n")
    research_results = {
        "SEARCH_RESULTS" : state['search_result'],
        "DETAILED_RESULTS" : state['scraped_content']
    }

    state['writer_content'] = writer_chain.invoke({
        'topic' : topic,
        'research' : research_results
    })

    print("Detailed Research Report : \n", state['writer_content'])
    print()

    print("Critic Agent is working....\n")
    state['critic_results'] = critic_chain.invoke({
        'research_paper' : state['writer_content']
    })
    print("Detailed Critic Analysis : \n" , state['critic_results'])
    print()

    return state

run_research_pipeline("History of Evolution of LLMs")