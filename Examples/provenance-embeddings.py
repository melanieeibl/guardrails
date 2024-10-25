# Import Guard and Validator
from guardrails.hub import ProvenanceEmbeddings
from guardrails import Guard
import numpy as np

import os
os.environ["AZURE_API_KEY"] = "a1414bc2ba834c5d85f235f026562b55" # "my-azure-api-key"
os.environ["AZURE_API_BASE"] = "https://meeopenai.openai.azure.com/" # "https://example-endpoint.openai.azure.com"
os.environ["AZURE_API_VERSION"] = "2023-03-15-preview" # "2023-05-15"

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    raise ImportError(
        "This example requires the `sentence-transformers` package. "
        "Install it with `pip install sentence-transformers`, and try again."
    )

# Setup text sources
SOURCES = [
    "The sun is a star.",
    "The sun rises in the east and sets in the west.",
    "Sun is the largest object in the solar system, and all planets revolve around it.",
]
# Load model for embedding function
MODEL = SentenceTransformer("paraphrase-MiniLM-L6-v2")
# Create embed function
def embed_function(sources: list[str]) -> np.array:
    return MODEL.encode(sources)

# Use the Guard with the validator
guard = Guard().use(
    ProvenanceEmbeddings,
    threshold=0.2,  # Lower the threshold to make the validator stricter
    validation_method="sentence",
    on_fail="exception",
)

# Test passing response
guard.validate(
    """
    The sun is a star that rises in the east and sets in the west.
    """,
    metadata={"sources": SOURCES, "embed_function": embed_function},
)

try:
    # Test failing response
    guard.validate(
        """
        Pluto is the farthest planet from the sun.
        """,  # This sentence is not "false", but is still NOT supported by the sources
        metadata={"sources": SOURCES, "embed_function": embed_function},
    )
except Exception as e:
    print(e)
