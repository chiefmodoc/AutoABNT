# AutoABNT
Automatize a configuração inicial de documentos acadêmicos no LibreOffice Writer.

Este script em Python automatiza a configuração inicial de documentos acadêmicos no **LibreOffice Writer**, aplicando as normas mais recentes da ABNT (NBR 14724:2024). Ele configura margens, fontes, espaçamentos e recuos de parágrafo com um único clique.

# AutoABNT - Automação de Formatação NBR 14724:2024

## 📋 Funcionalidades Automáticas

* **Margens Padronizadas**: Superior/Esquerda (3 cm) e Inferior/Direita (2 cm).
* **Tipografia**: Define a fonte padrão como Arial, tamanho 12.
* **Espaçamento**: Configura o entre linhas como 1,5.
* **Alinhamento**: Texto configurado como Justificado.
* **Recuo de Parágrafo**: Aplica automaticamente o recuo de 1,25 cm na primeira linha do corpo do texto.
* **Estilo de Títulos**: Remove o recuo de parágrafo dos títulos para alinhamento correto à esquerda.

---

## 🚀 Instruções de Instalação

### 1. Requisitos do Sistema
Certifique-se de que o suporte a scripts Python está instalado no seu sistema:
Opensuse base
```bash
sudo zypper up
sudo zypper install libreoffice-script-provider-python
```

Ubuntu base
```bash
sudo apt update
sudo apt install libreoffice-script-provider-python
```

Fedora base
```bash
sudo rpm update
sudo rpm install libreoffice-script-provider-python
```

### 2. Localização do Script
O LibreOffice reconhece macros de usuário em uma pasta específica. Crie o diretório se ele não existir:
```bash
mkdir -p ~/.config/libreoffice/4/user/Scripts/python/
```

Mova o arquivo `AutoABNT.py` para dentro desta pasta.

### 3. Configuração de Segurança (CRÍTICO)
Para que o script apareça e seja executado, você deve autorizar o local no LibreOffice:

1.  Abra o LibreOffice Writer.
2.  Vá em **Ferramentas > Opções > LibreOffice > Segurança**.
3.  Clique em **Segurança de Macros > Fontes confiáveis**.
4.  Clique em **Adicionar** e selecione a pasta: `~/.config/libreoffice/4/user/Scripts/python/`.

### 4. Criação do Atalho
1.  Vá em **Ferramentas > Personalizar > Barra de Ferramentas**.
2.  Em **Categoria**, selecione **Macros**.
3.  Navegue em: `Minhas macros > AutoABNT > AplicarFormatacaoABNT`.
4.  Adicione o comando à barra de ferramentas desejada. Nessa etapa você também pode escolher um ícone para o botão.

---

## 📖 Guia de Uso Acadêmico

Embora o script realize a configuração base, a norma ABNT exige cuidados manuais em seções específicas:

* **Quebras de Página**: Sempre utilize `Ctrl + Enter` para iniciar novos elementos (Resumo, Abstract, Sumário, Introdução).
* **Citações Longas**: Para trechos com mais de 3 linhas, utilize manualmente o tamanho 10, espaçamento simples e recuo de 4 cm à esquerda.
* **Paginação**: A contagem de páginas deve iniciar na Folha de Rosto, mas a exibição numérica deve começar apenas na Introdução.
* **Referências**: Devem ser alinhadas apenas à esquerda e possuir espaçamento simples entre linhas.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem**: Python 3.
* **API**: PyUNO (LibreOffice Bridge).

---
*Este script é um ponto de partida para produtividade acadêmica. Verifique sempre a versão final do seu documento com o manual oficial da sua instituição.*
---

## Autor

-   **chiefmodoc**

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K01KWCZW)
---
