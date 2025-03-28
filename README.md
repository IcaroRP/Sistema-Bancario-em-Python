# 💰 Sistema Bancário em Python

Este projeto é um sistema bancário simples desenvolvido em Python com base nos princípios da **Programação Orientada a Objetos (POO)**. Ele simula operações como criação de clientes, contas, saques, depósitos e exibição de extratos com histórico de transações.

---

## 📌 Funcionalidades

- Criar cliente (Pessoa Física)
- Criar conta corrente
- Realizar depósito
- Realizar saque (com limite de valor e de quantidade)
- Exibir extrato de movimentações
- Listar contas cadastradas

---

## 🛠️ Tecnologias e Conceitos Usados

- Python 3
- Programação Orientada a Objetos (POO)
- Herança
- Classes Abstratas
- Encapsulamento
- Histórico de transações com data e hora
- Modularização em pacotes
- Boas práticas com separação de responsabilidades

---

## 📁 Estrutura do Projeto

```bash
meu_banco/
│
├── main.py                   # Arquivo principal do programa (interface de menu)
│
├── models/                   # Contém as classes de domínio (modelo)
│   ├── __init__.py
│   ├── cliente.py            # Cliente e PessoaFisica
│   ├── conta.py              # Conta, ContaCorrente, Historico
│   └── transacoes.py         # Transacao, Saque, Deposito
│
├── services/                 # Funções de lógica do sistema
│   ├── __init__.py
│   └── menu.py               # Operações como sacar, depositar, extrato etc.
│
├── utils/                    # Funções auxiliares
│   ├── __init__.py
│   └── helpers.py            # Ex: recuperar conta, buscar cliente
│
└── README.md                 # Documentação do projeto
```

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/IcaroRP/Sistema-Bancario-em-Python
cd Sistema-Bancario-em-Python
```

2. Execute o programa principal:

```bash
python main.py
```

> ⚠️ Importante: execute o comando a partir da **pasta raiz do projeto** (onde está o `main.py`), para que os imports entre os pacotes funcionem corretamente.

