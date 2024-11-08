import agenteasy
from agenteasy.promptools import ai_template


@ai_template
def plain_translate(*, content: str, target: str, source: str | None = None):
    """System: {% if source is defined %}Source Language: {{source}}{% endif %}
    Task: Translate the user provided content into {{target}}. Return the translation only.||
    User: {{content}}"""
    ...


@ai_template
def context_translate(
    *, content: str, target: str, source: str | None = None, context: str | None = None
):
    """System:{% if source is defined %}Source Language: {{source}}{% endif %}
    {% if context is defined %}Context: {{context}}{% endif %}
    Task: Translate the user provided content into {{target}}. Return the translation only.||
    User:{{content}}
    """


agent = agenteasy.AIAgent(agenteasy.GPT())
print(
    agent.generate(
        messages=context_translate(
            content="这是一个平凡的早晨",
            target="Enslish",
            # context="就像很多故事开始那样，",
        )
    )
)
