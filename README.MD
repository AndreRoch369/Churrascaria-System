#  Sistema de Gestão - Churrascaria do Ronan

##  Descrição

Sistema web desenvolvido com o objetivo de automatizar os processos administrativos e operacionais da churrascaria, substituindo controles manuais baseados em papel por uma solução digital estruturada.

A aplicação visa melhorar a organização interna, reduzir erros operacionais e fornecer maior controle sobre pedidos, estoque e fluxo de caixa.

---

##  Objetivo

O sistema tem como principais objetivos:

* Controlar comandas de forma automatizada
* Gerenciar o estoque em tempo real
* Automatizar cálculos de pedidos e contas
* Gerar informações confiáveis para apoio à decisão
* Reduzir erros humanos no registro de pedidos

---

##  Paradigmas Utilizados

###  Programação Orientada a Objetos (POO)

Utilizada para representar as entidades do sistema como objetos do mundo real.

Classes implementadas:

* Produto → representa itens do cardápio
* Pedido → representa itens consumidos
* Comanda → agrupa pedidos por mesa
* Mesa → representa o local de atendimento
* Usuario → define perfis de acesso
* Caixa → controla abertura e fechamento financeiro

Benefícios:

* Organização do código
* Reutilização de componentes
* Facilidade de manutenção e expansão

---

###  Paradigma Imperativo

Responsável pelo controle do fluxo de execução das operações do sistema.

Aplicado em:

* Registro de pedidos
* Atualização de estoque
* Abertura e fechamento de comandas

Exemplo:
O sistema segue uma sequência lógica:

1. Receber pedido
2. Atualizar estoque
3. Registrar na comanda

---

###  Paradigma Funcional

Utilizado para funções específicas que realizam cálculos sem efeitos colaterais.

Aplicado em:

* Cálculo do total da comanda
* Cálculo de lucro diário
* Filtragem de dados

Benefícios:

* Maior previsibilidade
* Facilidade de testes
* Código mais limpo

---

##  Integração dos Paradigmas

O sistema utiliza uma abordagem híbrida onde cada paradigma desempenha um papel específico:

* POO → estrutura os dados e entidades do sistema
* Imperativo → controla o fluxo das operações
* Funcional → realiza cálculos e processamentos isolados

Essa integração garante:

* Modularidade
* Clareza na lógica do sistema
* Facilidade de manutenção

---

##  Arquitetura

O sistema segue o padrão MVC (Model-View-Controller)** com separação em camadas:

* Model → responsável pela estrutura dos dados (classes)
* View → representada pelas respostas da API (JSON)
* Controller → gerencia as rotas e requisições
* Service → implementa as regras de negócio

### Fluxo da aplicação:

1. O usuário realiza uma ação (ex: registrar pedido)
2. O Controller recebe a requisição
3. O Service executa a lógica de negócio
4. Os Models representam os dados manipulados
5. O sistema retorna uma resposta ao usuário

---

##  Roadmap

Funcionalidades implementadas e futuras evoluções:

* [x] Cadastro de produtos
* [x] Cadastro de mesas
* [x] Controle de comandas
* [x] Cálculo automático de pedidos
* [ ] Interface gráfica (frontend)
* [ ] Sistema de login e autenticação
* [ ] Relatórios avançados de vendas
* [ ] Controle completo de estoque

---

##  Equipe

Projeto desenvolvido por:

* André Rocha Figueredo
* Michel Guido Teixeira
* Mickael Sousa Miranda

---

##  Como executar

Siga os passos abaixo para rodar o projeto localmente:

```bash
git clone <repo>
cd churrascaria-system

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
venv\Scripts\activate  

# Instalar dependências
pip install -r requirements.txt

# Executar o sistema
python run.py
```

Após isso, acesse no navegador:

```
http://localhost:5000
```

---

##  Banco de Dados

O sistema utiliza SQLite como banco de dados relacional.

### Estrutura:

* Produto → armazena itens e estoque
* Mesa → controla mesas do estabelecimento
* Comanda → relaciona pedidos à mesa
* Pedido → registra os itens consumidos

### Normalização aplicada:

* 1FN (Primeira Forma Normal)** → dados atômicos, sem repetições
* 2FN (Segunda Forma Normal)** → dependência total da chave primária
* 3FN (Terceira Forma Normal)** → eliminação de dependências transitivas

Isso garante:
 
* Redução de redundância
* Integridade dos dados
* Melhor desempenho

---

##  Segurança

O sistema foi projetado com base em boas práticas de segurança:

* Estrutura para controle de usuários
* Possibilidade de níveis de acesso (garçom, caixa, administrador)
* Preparado para implementação de autenticação

Futuras melhorias:

* Criptografia de senha
* Controle de sessão
* Autenticação via token

---

##  Conclusão

O sistema desenvolvido atende às necessidades levantadas no levantamento de requisitos (TED 1), oferecendo uma solução digital eficiente para os problemas da churrascaria.

A aplicação apresenta:

* Organização estrutural baseada em MVC
* Integração de múltiplos paradigmas de programação
* Banco de dados normalizado
* Base sólida para expansão futura

Com isso, o projeto cumpre plenamente os objetivos propostos, servindo como uma solução escalável e de fácil manutenção.
