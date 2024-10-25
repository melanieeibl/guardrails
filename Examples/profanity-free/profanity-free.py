# Import Guard and Validator
from guardrails.hub import ProfanityFree
from guardrails import Guard

# Use the Guard with the validator
guard = Guard().use(
    ProfanityFree, on_fail="exception"
)

try:
    guard.validate(
        """
        Director Denis Villeneuve's Dune is a visually stunning and epic adaptation of the classic science fiction novel.
        It is reminiscent of the original Star Wars trilogy, with its grand scale and epic storytelling.
        """
    ) # Test passing response

    guard.validate(
        """
        He is such a dickhead and a fucking idiot.
        """
    ) # Test failing response
except Exception as e:
    print(e)
