# Import Guard and Validator
from guardrails import Guard
from guardrails.hub import ValidURL

import os
os.environ["AZURE_API_KEY"] = "a1414bc2ba834c5d85f235f026562b55" # "my-azure-api-key"
os.environ["AZURE_API_BASE"] = "https://meeopenai.openai.azure.com/" # "https://example-endpoint.openai.azure.com"
os.environ["AZURE_API_VERSION"] = "2023-03-15-preview" # "2023-05-15"

# Setup Guard
guard = Guard().use(ValidURL, on_fail="exception")
response = guard.validate("http://www.google.com")  # Validator passes

try:
    response = guard.validate("notalink.xyzq")  # Validator fails
except Exception as e:
    print(e)