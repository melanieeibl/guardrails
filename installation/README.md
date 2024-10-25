# Install Guardrails

Key from here: https://hub.guardrailsai.com/keys

```pwsh
pip install guardrails-ai
guardrails configure
```

Packages can be found here: `C:\Program Files\Python312\Lib\site-packages`

E.g.:
* guardrails
* guardrails_ai-0.5.13.dist-info
* guardrails_api
* guardrails_api-0.0.3.dist-info
* guardrails_api_client
* guardrails_api_client-0.3.13.dist-info
* guardrails_hub_types
* guardrails_hub_types-0.0.4.dist-info

# Installing validators from here

https://hub.guardrailsai.com

## Get started by installing RegexMatch validator/guard

### Example from command line

https://hub.guardrailsai.com/validator/guardrails/regex_match     

```shell
guardrails hub install hub://guardrails/regex_match
```

### From tutorial

```shell
guardrails create --validators hub://guardrails/gibberish_text --guard-name gibberish_guard
guardrails start --config config.py

# packages can be found here:
# C:\Program Files\Python312\Lib\site-packages\guardrails\cli\start.py

# Warning:
# C:\Program Files\Python312\Lib\site-packages\transformers\tokenization_utils_base.py
# 1617: FutureWarning: `clean_up_tokenization_spaces` was not set. It will be set to `True` by default. This behavior will be deprecated in transformers v4.45, and will be then set to `False` by default. For more details check this issue: https://github.com/huggingface/transformers/issues/31884 warnings.warn
```

# Uninstall Guardrails

```shell
pip uninstall guardrails-ai
```

Packages removed from here: `C:\Program Files\Python312\Lib\site-packages`
