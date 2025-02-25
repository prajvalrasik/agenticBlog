import os
from crewai_tools import SerperDevTool

class MySerperDevTool(SerperDevTool):
    """
    A subclass that overrides '_run' so we can handle if 'search_query' is a dict
    with a 'description' key (like { "description": "...", "type": "str" }).
    """
    def _run(self, search_query):
        # If the agent passes a dict, unwrap the 'description'
        if isinstance(search_query, dict):
            desc = search_query.get("description", "")
            if desc:
                search_query = desc
            else:
                search_query = str(search_query)  # fallback: convert entire dict to string

        # Now call parent's _run() with a pure string
        return super()._run(search_query=search_query)

# Initialize our custom search tool
google_search_tool = MySerperDevTool(
    api_key=os.getenv("SERPER_API_KEY")
)
