# VoiceMoneyFlow - Integração do ChatGPT com GitHub Actions

Este projeto integra a API do ChatGPT com o GitHub Actions para automação.

## 📌 Como Funciona?
1. O workflow do GitHub Actions executa o script `script.py`.
2. O script interage com a API da OpenAI e gera uma resposta do ChatGPT.
3. A resposta é exibida nos logs do GitHub Actions.

## 🚀 Como Rodar?
1. **Crie um Secret no GitHub**:
   - Vá para `Settings > Secrets > Actions`
   - Adicione `OPENAI_API_KEY` com sua chave da OpenAI.

2. **Rode o Workflow Manualmente**:
   - Vá para `Actions > ChatGPT Integration > Run Workflow`.

3. **Veja a Resposta** nos logs do GitHub Actions.

---
