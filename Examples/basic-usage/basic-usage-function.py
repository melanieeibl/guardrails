# Buggy

from pydantic import BaseModel, Field
from typing import List
from guardrails import Guard

import os
os.environ["AZURE_API_KEY"] = "a1414bc2ba834c5d85f235f026562b55" # "my-azure-api-key"
os.environ["AZURE_API_BASE"] = "https://meeopenai.openai.azure.com/" # "https://example-endpoint.openai.azure.com"
os.environ["AZURE_API_VERSION"] = "2023-03-15-preview" # "2023-05-15"

class Fruit(BaseModel):
    name: str
    color: str

class Basket(BaseModel):
    fruits: List[Fruit]
    
guard = Guard.for_pydantic(Basket)

result = guard(
    messages=[{"role":"user", "content":"Generate a basket of 5 fruits"}],
    model="azure/gpt-4",
    tools=guard.add_json_function_calling_tool([]),
    tool_choice="required",
)

print(f"{result.validated_output}")
