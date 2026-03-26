# 📦 Bot Especialista - ExpressLog (Suporte Logístico)

Este repositório contém o projeto final da disciplina de Tópicos Especiais de Informática. Trata-se de um **Bot Especialista** desenvolvido em Python utilizando a API do Google Gemini (`gemini-2.5-flash`).

## 🎯 Objetivo do Projeto

O objetivo deste projeto é demonstrar a criação de um assistente virtual restrito a um **domínio específico e privado**, mitigando o risco de alucinações (quando a IA inventa informações). 

O bot atua como um especialista em logística da distribuidora fictícia **ExpressLog**, utilizando regras internas de recebimento de carga que não estão disponíveis publicamente na internet.

### ⚙️ Regras de Negócio Inseridas no Contexto (System Instructions)
- **Horário de Descarga:** Apenas das 07h às 11h para caminhões bitrem. Outros veículos até as 16h.
- **Documentação:** É obrigatória a apresentação da NF-e impressa e do canhoto de vistoria assinado.
- **Divergência:** Se faltar mais de 5% da carga, o recebimento total deve ser recusado.
- **Segurança (EPIs):** Uso obrigatório de colete refletivo e bota de bico de aço no pátio.

### 🔄 Fluxo de Interação
1. O bot responde a **exatamente três perguntas** do usuário, baseando-se estritamente nas regras acima.
2. Ao final da terceira resposta, o bot gera automaticamente um **Resumo do Atendimento**.
3. A conversa é encerrada pelo sistema.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Ambiente de Execução:** Google Colab
* **LLM:** Google Gemini 2.5 Flash
* **SDK:** `google-genai` (Nova biblioteca oficial do Google)

---

## 🚀 Passo a Passo: Como Executar o Projeto

Como o projeto foi otimizado para rodar no **Google Colab**, você não precisa instalar o Python ou configurar ambientes virtuais na sua máquina local. Siga os passos abaixo:

### 1. Acessar o Notebook
Abra o arquivo `.ipynb` presente neste repositório diretamente no [Google Colab](https://colab.research.google.com/). 

### 2. Configurar a Chave de API (Secret)
Para que o código se comunique com o Google Gemini, é necessário fornecer uma API Key segura:
1. No menu lateral esquerdo do Google Colab, clique no ícone de **Chave (🔑) chamado "Secrets"** (ou Segredos).
2. Clique em **"Add new secret"**.
3. No campo **Name** (Nome), digite exatamente: `GEMINI_API_KEY`.
4. No campo **Value** (Valor), cole a sua chave gerada no [Google AI Studio](https://aistudio.google.com/).
5. **Importante:** Ative o botão (toggle) ao lado da chave para liberar o acesso dela ao notebook (o botão deve ficar azul).

### 3. Executar o Código
1. Clique no botão de **Play** (Executar célula) localizado no canto superior esquerdo do bloco de código.
2. O Colab irá instalar a biblioteca `google-genai` silenciosamente e iniciar o chat.
3. Uma caixa de texto aparecerá abaixo da célula pedindo a sua "Pergunta 1/3".
4. Interaja com o bot testando as regras da ExpressLog. 
   > *Exemplo de teste funcional:* Pergunte sobre horários de bitrem, tente entrar sem botas no pátio ou relate a falta de 10% da carga na terceira pergunta para observar a geração do resumo final.

---

## 🎥 Apresentação em Vídeo

No vídeo abaixo, demonstro a explicação do código, a configuração do ambiente e a execução em tempo real das três interações obrigatórias.

🔗 **[LINK DO SEU VÍDEO DO YOUTUBE AQUI]**