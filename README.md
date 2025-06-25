# Projeto de Testes de Sistemas - Aplicação Bancária

## 👥 Equipe
- **Mateus Melo e Silva A de Figueiredo**
- **Amanda Mohring**
- **Bianca Fialho**

## 🌐 Aplicação Web Testada
**Link:** https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login

## 📋 Sobre o Projeto
Este projeto implementa testes automatizados para uma aplicação bancária web usando Selenium WebDriver e pytest. A aplicação permite duas funcionalidades principais:
- **Login de Cliente:** Seleção e login de clientes existentes
- **Login de Gerente:** Gerenciamento de clientes e contas (adicionar clientes, criar contas)

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Selenium WebDriver** - Automação de testes web
- **pytest** - Framework de testes
- **webdriver-manager** - Gerenciamento automático de drivers

## 📁 Estrutura do Projeto
```
trabalho-testes-sistemas/
├── pages/                 # Page Object Model (POM)
│   ├── BasePage.py       # Classe base para todas as páginas
│   ├── LoginPage.py      # Página de login inicial
│   ├── CustomerPage.py   # Página de seleção/login de cliente
│   ├── ManagerPage.py    # Página de gerenciamento bancário
│   └── AccountPage.py    # Página da conta do cliente
├── tests/                # Casos de teste
│   ├── conftest.py       # Configurações e fixtures do pytest
│   ├── test1.py          # CT-001: Login via botão Customer
│   ├── test2.py          # CT-002: Login com conta específica
│   ├── test3.py          # CT-003: Validação de lista de clientes
│   ├── test4.py          # CT-004: Login via botão Manager
│   ├── test5.py          # CT-005: Adicionar novo cliente
│   ├── test6.py          # CT-006: Criar conta para cliente
│   ├── test7.py          # CT-007: Fluxo completo de gerente
│   ├── test8.py          # CT-008: Fluxo end-to-end gerente→cliente
│   └── test9.py          # CT-009: Realizar depósito na conta
├── requirements.txt      # Dependências do projeto
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Este arquivo
```

## ⚙️ Configuração e Execução

### 1. Pré-requisitos
- Python 3.x instalado
- Navegadores Chrome, Edge e/ou Firefox instalados

### 2. Instalação de Dependências
```bash
# Criar ambiente virtual (recomendado)
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Executar Testes

#### Executar todos os testes:
```bash
pytest tests/ -v
```


## 🧪 Casos de Teste Implementados

| ID | Nome do Teste | Descrição |
|---|---|---|
| CT-001 | Login via Customer Button | Testa navegação do botão "Customer Login" |
| CT-002 | Login com Cliente Específico | Login com cliente "Harry Potter" |
| CT-003 | Validação Lista de Clientes | Verifica clientes disponíveis no sistema |
| CT-004 | Login via Manager Button | Testa navegação do botão "Bank Manager Login" |
| CT-005 | Adicionar Novo Cliente | Gerente adiciona cliente "John Doe" |
| CT-006 | Criar Conta para Cliente | Gerente cria conta em Dollar para cliente |
| CT-007 | Fluxo Completo de Gerente | Adicionar cliente + criar conta + verificar tabela |
| CT-008 | Fluxo End-to-End Completo | Gerente cria cliente → cliente faz login |
| CT-009 | Realizar Depósito | Cliente faz depósito de 1000 na conta |

## 🌐 Suporte Multi-Browser
Os testes são executados nos seguintes navegadores:
- **Chrome** 
- **Microsoft Edge**
- **Firefox**

O `webdriver-manager` gerencia automaticamente os drivers necessários.

## 📊 Funcionalidades Testadas

### 👤 Área do Cliente
- Seleção de cliente existente
- Login na conta
- Visualização de informações da conta
- Realização de depósitos
- Atualização de saldo

### 👨‍💼 Área do Gerente  
- Adição de novos clientes
- Criação de contas bancárias
- Verificação de dados na tabela de clientes
- Navegação entre diferentes funcionalidades

## 🔧 Arquitetura dos Testes

### Page Object Model (POM)
O projeto utiliza o padrão Page Object Model para:
- **Manutenibilidade:** Centralizar localizadores e ações de cada página
- **Reutilização:** Métodos podem ser usados em múltiplos testes
- **Legibilidade:** Testes mais limpos e fáceis de entender

### Fixtures e Configurações
- **conftest.py:** Contém fixtures para setup/teardown de browsers
- **Parametrização:** Testes executam automaticamente em múltiplos browsers
- **Isolamento:** Cada teste possui seu próprio contexto de browser

## 📝 Observações Importantes
- Os testes são independentes e podem ser executados em qualquer ordem
- Cada teste limpa seu próprio ambiente (setup/teardown automático)
- Logs detalhados são exibidos durante a execução para acompanhamento

