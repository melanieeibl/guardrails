from guardrails import Guard

import os
os.environ["AZURE_API_KEY"] = "a1414bc2ba834c5d85f235f026562b55" # "my-azure-api-key"
os.environ["AZURE_API_BASE"] = "https://meeopenai.openai.azure.com/" # "https://example-endpoint.openai.azure.com"
os.environ["AZURE_API_VERSION"] = "2023-03-15-preview" # "2023-05-15"

guard = Guard()

stream_chunk_generator = guard(
    messages=[{"role":"user", "content":"How many moons does Jupiter have?"}],
    model="azure/gpt-4", 
    stream=True
)

for chunk in stream_chunk_generator:
    print(f"{chunk.validated_output}")
