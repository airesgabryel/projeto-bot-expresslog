{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "RK8hPoFdK6lX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e3f207c3-901c-43be-9dec-427b92f4112f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--- 🚛 SUPORTE EXPRESSLOG (MODO ESPECIALISTA) ---\n",
            "\n",
            "Pergunta 1/3: Qual é o horário permitido para descarregar um caminhão bitrem?\n",
            "\n",
            "Bot ExpressLog:\n",
            "Para caminhões bitrem, o horário permitido para descarregamento é das 07h às 11h.\n",
            "\n",
            "--------------------------------------------------\n",
            "\n",
            "Pergunta 2/3: Posso entrar no pátio de chinelo se for só para entregar um documento rápido?\n",
            "\n",
            "Bot ExpressLog:\n",
            "Não, a entrada no pátio exige o uso obrigatório de EPIs, que incluem colete e bota de aço. Não é permitido o acesso de chinelo, mesmo para entregas rápidas de documentos.\n",
            "\n",
            "--------------------------------------------------\n",
            "\n",
            "Pergunta 3/3: Chegou uma carga, mas o conferente disse que está faltando 10% do material. O que eu devo fazer?\n",
            "\n",
            "Bot ExpressLog:\n",
            "Se a divergência na carga for superior a 5% de falta, como no seu caso que é de 10%, a instrução é recusar a carga inteira.\n",
            "\n",
            "--- RESUMO DO ATENDIMENTO ---\n",
            "Neste atendimento, esclarecemos que o horário para descarregamento de caminhões bitrem é das 07h às 11h. Também informamos que o acesso ao pátio exige o uso obrigatório de EPIs (colete e bota de aço), não sendo permitido o uso de chinelos. Por fim, orientamos que em caso de divergência de carga com falta superior a 5% do material, a carga deve ser recusada integralmente.\n",
            "Atendimento encerrado por limite de interações.\n",
            "\n",
            "--------------------------------------------------\n"
          ]
        }
      ],
      "source": [
        "# 1. Instala a biblioteca do Google GenAI silenciosamente\n",
        "!pip install -q google-genai\n",
        "\n",
        "import os\n",
        "from google import genai\n",
        "from google.colab import userdata\n",
        "\n",
        "# 2. Resgata a sua chave de API configurada nos Segredos do Colab\n",
        "CHAVE = userdata.get('GEMINI_API_KEY')\n",
        "client = genai.Client(api_key=CHAVE)\n",
        "\n",
        "# 3. Define o contexto privado da empresa (ExpressLog)\n",
        "instrucoes = \"\"\"\n",
        "Você é o Especialista da ExpressLog.\n",
        "INFORMAÇÕES PRIVADAS:\n",
        "- Horário Bitrens: 07h às 11h. Outros: até 16h.\n",
        "- Documentos: NF-e impressa e canhoto assinado.\n",
        "- Divergência: Se >5% de falta, recuse tudo.\n",
        "- EPI: Colete e bota de aço obrigatórios.\n",
        "\n",
        "REGRAS DO BOT:\n",
        "1. Você deve responder a exatamente 3 perguntas do usuário.\n",
        "2. Na 3ª e última resposta, você DEVE obrigatoriamente escrever '--- RESUMO DO ATENDIMENTO ---', fazer um breve resumo de tudo que foi conversado nas 3 interações e finalizar dizendo 'Atendimento encerrado por limite de interações'.\n",
        "\"\"\"\n",
        "\n",
        "def executar_bot():\n",
        "    # 4. Inicializa o chat com o modelo gemini-2.5-flash e as instruções\n",
        "    chat = client.chats.create(\n",
        "        model=\"gemini-2.5-flash\",\n",
        "        config={\n",
        "            \"system_instruction\": instrucoes,\n",
        "            \"temperature\": 0.1 # Temperatura baixa para evitar alucinações\n",
        "        }\n",
        "    )\n",
        "\n",
        "    print(\"--- 🚛 SUPORTE EXPRESSLOG (MODO ESPECIALISTA) ---\")\n",
        "\n",
        "    # 5. Loop para limitar a 3 perguntas\n",
        "    for i in range(1, 4):\n",
        "        pergunta = input(f\"\\nPergunta {i}/3: \")\n",
        "\n",
        "        # Injeta uma instrução oculta na última pergunta para garantir o resumo\n",
        "        prompt_final = pergunta\n",
        "        if i == 3:\n",
        "            prompt_final += \" (Lembre-se da regra: gere o resumo completo do atendimento agora e encerre a conversa).\"\n",
        "\n",
        "        response = chat.send_message(prompt_final)\n",
        "        print(f\"\\nBot ExpressLog:\\n{response.text}\\n\")\n",
        "        print(\"-\" * 50)\n",
        "\n",
        "# Executa o programa\n",
        "executar_bot()"
      ]
    }
  ]
}