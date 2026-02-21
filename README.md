# Relatório — Mini Compilador CalcLang 2.0

**Aluno:** Caio Renato dos Santos Claudino
**Professor:** Amaury Nogueira Neto

---

## 1. Estrutura da Tabela de Símbolos

A tabela de símbolos foi implementada utilizando um dicionário (`dict`) em Python, onde o nome da variável é a chave e seu valor inicial é armazenado como conteúdo. Essa estrutura permite verificar rapidamente se uma variável foi declarada antes de seu uso.

---

## 2. Estratégia de Detecção de Erros Semânticos

O compilador lê o arquivo linha por linha. Após validar a estrutura dos comandos, é realizada a análise semântica, verificando:

* uso de variável não declarada;
* validade do nome das variáveis;
* utilização correta dos comandos.

Quando ocorre erro semântico, o programa informa o tipo do erro e o número da linha correspondente, interrompendo a compilação.

---

## 3. Organização das Fases do Compilador

O compilador foi dividido em três etapas:

* **Análise Sintática:** valida a estrutura dos comandos da linguagem.
* **Análise Semântica:** verifica declaração e uso correto das variáveis utilizando a tabela de símbolos.
* **Geração de Código:** traduz instruções CalcLang para código equivalente em Python.

---

## 4. Respostas Conceituais

**a)** Em qual fase do compilador ocorre a verificação de variável não declarada? Resposta: A verificação de variável não declarada ocorre na fase de **análise semântica**.

**b)** Qual a diferença entre erro sintático e erro semântico neste contexto? Resposta: Erro sintático refere-se à estrutura incorreta do comando; erro semântico ocorre quando a estrutura é válida, mas o significado é inválido.

**c)** Qual o papel da tabela de símbolos em compiladores reais? Resposta: A tabela de símbolos armazena informações sobre identificadores do programa, permitindo validações semânticas durante a compilação.

**d)** Como o projeto precisaria evoluir para suportar escopo (ex.: blocos ou funções)? Resposta: Para suportar escopo seria necessário utilizar múltiplas tabelas de símbolos organizadas em pilha, permitindo variáveis locais em blocos ou funções.
