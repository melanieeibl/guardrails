# Import Guard and Validator
from guardrails.hub import ProvenanceEmbeddings
from guardrails import Guard
import numpy as np

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    raise ImportError(
        "This example requires the `sentence-transformers` package. "
        "Install it with `pip install sentence-transformers`, and try again."
    )

# Setup text sources
SOURCES = [
    "Pasteurisation is a process of food preservation",
    "Pasteurisation is a process where packaged foods are treated with mild heat.",
    "The pasteurisation temperature is usually less than 100 °C (212 °F).",
    "Pasteurisation eliminates pathogens and extend shelf life.",
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

try:
    # Test passing response
    guard.validate(
        """
        The the pasteurisation process is treated with mild heat.
        """,
        metadata={"sources": SOURCES, "embed_function": embed_function},
    )

    # Test passing response
    guard.validate(
        """
        The temperature used for pasteurisation is less than 100 °C.
        """,
        metadata={"sources": SOURCES, "embed_function": embed_function},
    )

    # Test passing response
    guard.validate(
        """
        The temperature used for pasteurisation is more than 100 °C.
        """,  # This sentence is "false", but supported by the sources
        metadata={"sources": SOURCES, "embed_function": embed_function},
    )

    # Test passing response
    guard.validate(
        """
        Pasteurisation eliminates bacteria and extend shelf life.
        """,  # This sentence is "false", but supported by the sources
        metadata={"sources": SOURCES, "embed_function": embed_function},
    )
except Exception as e:
    print(e)
