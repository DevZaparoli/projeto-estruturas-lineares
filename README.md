🗳️ Sistema de Votação e Simuladores - Atividades de Estruturas de Dados
📋 1. Qual problema o programa resolve?
Atividade 1 - Sistema de Votação:
Simula uma urna eletrônica para votação entre 3 candidatos (Lionel Messi, Alexandre de Moraes, Vinicius Rafacho). Recebe votos, valida candidatos, conta os votos e declara o vencedor (ou empate).

Atividade 2 - Editor de Texto com Pilha:
Implementa um editor de texto simples que permite adicionar palavras e desfazer a última adição usando estrutura de pilha (LIFO - Last In, First Out).

Atividade 3 - Sistema de Fila de Atendimento:
Simula um sistema de fila de atendimento para alunos, permitindo adicionar nomes na fila e atender o primeiro da fila (FIFO - First In, First Out).

🛠️ 2. Quais estruturas foram utilizadas?
Atividade 1 - Votação:


Copy code
- Lista (array dinâmico): `votos[]` - armazena todos os votos
- Lista de validação: `candidatos_validos[]` - candidatos permitidos
- Contadores variáveis: para totalizar votos de cada candidato
- Estrutura de controle: while, if/else, max()
Atividade 2 - Editor de Texto:


Copy code
- Pilha (LIFO): `pilha[]` - implementada com lista Python
- Operações: append() para empilhar, pop() para desempilhar
- Estrutura de controle: while, if/elif/else
Atividade 3 - Fila de Atendimento:


Copy code
- Fila (FIFO): `fila[]` - implementada com lista Python
- Operações: append() para enfileirar, pop(0) para desenfileirar
- Estrutura de controle: while, if/elif/else
🚀 3. Como executar o programa?
Pré-requisitos

Copy code
- Python 3.x instalado
- Nenhum pacote externo necessário (usa apenas biblioteca padrão)
Passos para execução:
Executar TODAS as atividades:

bash

Copy code
# Salve cada código em arquivos separados:
# 1. votacao.py
# 2. editor_pilha.py  
# 3. fila_atendimento.py

python votacao.py
python editor_pilha.py
python fila_atendimento.py
Ou execute tudo de uma vez (copie os 3 códigos em um arquivo atividades.py):

bash

Copy code
python atividades.py
📊 4. Exemplo simples de entrada e saída
Atividade 1 - Votação

Copy code
Entrada:
Lionel messi
Alexandre de moraes
vinicius rafacho
Lionel messi
fim

Saída:
Voto Confirmado (x3)
Vencedor: Lionel Messi

Resultado do embate Lionel= 2 , Alexandre= 1 e Vinicius= 1
Atividade 2 - Editor de Texto (Pilha)

Copy code
Entrada:
ola
mundo
python
desfazer
desfazer
fim

Saída:
Texto atual: ola mundo python
Última palavra removida: python
Texto atual: ola mundo
Última palavra removida: mundo
Texto atual: ola
Encerrando editor...
Atividade 3 - Fila de Atendimento

Copy code
Entrada:
João
Maria
Pedro
atender
atender
Carlos
fim

Saída:
Fila atual: João -> Maria -> Pedro
Aluno atendido: João
Aluno atendido: Maria
Fila atual: Pedro -> Carlos
Encerrando sistema...
📁 Estrutura do Projeto

Copy code
projeto-estruturas-dados/
├── votacao.py          # Atividade 1
├── editor_pilha.py     # Atividade 2  
├── fila_atendimento.py # Atividade 3
└── README.md
✨ Funcionalidades Extras
✅ Interface limpa com os.system("cls") (limpa tela)
✅ Validação de entrada robusta
✅ Tratamento de casos especiais (vazio, empate, inválido)
✅ Visualização em tempo real do estado das estruturas
