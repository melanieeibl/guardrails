# Import Guard and Validator
from guardrails.hub import ToxicLanguage
from guardrails import Guard

# Use the Guard with the validator
guard = Guard().use(
    ToxicLanguage, threshold=0.5, validation_method="sentence", on_fail="exception"
)

try:
    # Test passing response
    guard.validate("Love how you think and attack the problem. Great job!")

    # Test failing response
    guard.validate(
        "Please look carefully. You are a stupid idiot who can't do anything right."
    )
except Exception as e:
    print(e)
