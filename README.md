# LLM Gateway Conversation — Home-Assistant-Integration

Conversation-Agent für Home Assistant, der über den hauseigenen
**`llm-gateway`**-Adapter (NAS, OpenAI-kompatibel, Failover-Kette
Claude→Mistral→GPT→Gemini + Circuit-Breaker) mit Claude spricht — inkl.
nativem Tool-Calling, also echter HA-Steuerung über die Assist-LLM-API.

Fork von [michelle-avery/openai-compatible-conversation](https://github.com/michelle-avery/openai-compatible-conversation),
zugeschnitten auf den Adapter: Default-`base_url` zeigt auf den Gateway, API-Key
optional (der Adapter prüft keinen), deutscher Default-Prompt, ohne den
dall-e-Bildservice der Vorlage.

## Voraussetzung

`llm-gateway` läuft erreichbar im LAN. Die Basis-URL im Einrichtungsdialog ist
für die lokale Installation auf `http://10.111.0.104:8081/v1` voreingestellt.

## Installation

**Via HACS (Custom Repository):** HACS → ⋮ → *Custom repositories* → URL dieses
Repos, Kategorie *Integration* → installieren → HA neu starten.

**Manuell:** `custom_components/llm_gateway/` nach `/config/custom_components/`
kopieren, HA neu starten.

## Einrichtung

*Einstellungen → Geräte & Dienste → Integration hinzufügen → „LLM Gateway"*

1. **Basis-URL** bestätigen (Default passt), API-Key-Feld leer lassen.
2. Unter *Konfigurieren*: **Instruktionen** (System-Prompt) anpassen,
   **Control Home Assistant** auf *Assist* stellen (Steuerung), Modell/Tokens
   nach Bedarf.
3. *Einstellungen → Sprachassistenten*: Pipeline auf diesen Agenten zeigen lassen.

## Modell

Default `claude-auto`: Der Adapter wählt für Home-Assistant-Anfragen ohne
zusätzlichen Judge anhand der Anfragekomplexität die passende Modellstufe.
Der Modellname ist in den Optionen frei änderbar.

Jede Anfrage trägt im OpenAI-kompatiblen `user`-Feld die feste Kennung
`homeassistant`. Der Gateway kann HA dadurch als Aufrufer anzeigen, statt den
Request unter `unknown` zu protokollieren.

## Umbenennung von „Claude Conversation (Proxy)" (Domain `claude_proxy`)

Diese Integration ist der Nachfolger von `ha-claude-conversation`
(Domain `claude_proxy`). Der Domain-Wechsel ist eine Breaking Change in
Home Assistant — bestehende Config-Einträge der alten Integration werden
**nicht** automatisch migriert. Vorgehen bei einem Umstieg:

1. Alte Integration(en) unter *Einstellungen → Geräte & Dienste* entfernen.
2. Diese Integration (neu, Domain `llm_gateway`) installieren und für jede
   vorher genutzte Pipeline neu einrichten (Titel, Prompt, Modell-Optionen
   erneut setzen — nichts wird übernommen).
3. Sprachassistenten-Pipelines auf die neuen Agenten umstellen.
