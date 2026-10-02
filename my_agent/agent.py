import pathlib

from google.adk import Agent
from google.adk.skills import load_skill_from_dir
from google.adk.tools import skill_toolset

weather_skill = load_skill_from_dir(
    pathlib.Path(__file__).parent / "skills" / "weather-skill"
)


def get_wind_speed(location: str) -> str:
    """Returns the current wind speed for a given location."""
    return f"The wind speed in {location} is 10 mph."


my_skill_toolset = skill_toolset.SkillToolset(
    skills=[weather_skill],
    additional_tools=[get_wind_speed],
)

root_agent = Agent(
    model="gemini-3.5-flash",
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
    tools=[
        my_skill_toolset,
    ],
)
