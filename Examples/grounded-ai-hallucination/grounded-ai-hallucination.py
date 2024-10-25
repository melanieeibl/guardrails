# Buggy

from guardrails.hub import GroundedaiHallucination
from guardrails import Guard

guard = Guard().use(GroundedaiHallucination(quant=True))

try:
    # Tests passing response
    guard.validate("The capital of France is Paris.", metadata={
        "query": "What is the capital of France?",
        "reference": "The capital of France is Paris."
    })

    # with llm
    messages = [{"role":"user", "content":"What is the capital of France?"}]
    guard(
    messages=messages,
    model="gpt-4o-mini",
    metadata={
        "query": messages[0]["content"],
        "reference": "The capital of France is Paris."
    })

    # Test failing response
    guard.validate("The capital of France is London.", metadata={
        "query": "What is the capital of France?",
        "reference": "The capital of France is Paris."
    }) 
except Exception as e:
    print(e)
