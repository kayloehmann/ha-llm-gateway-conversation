"""Constants for the LLM Gateway Conversation integration."""

import logging

DOMAIN = "llm_gateway"
LOGGER = logging.getLogger(__package__)

CONF_RECOMMENDED = "recommended"
CONF_PROMPT = "prompt"
CONF_CHAT_MODEL = "chat_model"
CONF_MAX_TOKENS = "max_tokens"
CONF_TEMPERATURE = "temperature"
CONF_TOP_P = "top_p"
CONF_BASE_URL = "base_url"

# OpenAI-compatible caller identifier. The gateway records this as the agent
# name so Home Assistant requests are distinguishable from OpenClaw traffic.
GATEWAY_CLIENT_ID = "homeassistant"

# Defaults für einen llm-gateway-Adapter (OpenAI-kompatibel, mit Failover-Kette
# Claude→Mistral→GPT→Gemini). base_url im Einrichtungsdialog an die eigene
# Adapter-Adresse anpassen.
RECOMMENDED_CHAT_MODEL = "claude-auto"
RECOMMENDED_MAX_TOKENS = 1024
RECOMMENDED_TEMPERATURE = 1.0
RECOMMENDED_TOP_P = 1.0
RECOMMENDED_BASE_URL = "http://10.111.0.104:8081/v1"

# Persona-Default (in der UI frei überschreibbar). Die HA-LLM-API hängt die
# Tool-/Entity-Instruktionen automatisch an.
DEFAULT_PROMPT = (
    "Du bist der Sprachassistent in Kays Zuhause. Antworte kurz, natürlich und "
    "auf Deutsch — sprich gesprochene Sätze, keine Listen oder Markdown. Wenn du "
    "ein Gerät steuern sollst, tu es direkt und bestätige knapp. Bei Unklarheit "
    "(z. B. mehrdeutiger Raum) frag kurz nach."
)
