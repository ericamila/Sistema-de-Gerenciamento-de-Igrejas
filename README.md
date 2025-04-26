
# Templo Digital

Sistema integrado de gestão para igrejas, desenvolvido em Django.

## Estrutura do Projeto

```
├── accounts          # Gerenciamento de usuários e autenticação
├── churches         # Gestão de igrejas
├── events          # Gestão de eventos
├── finances        # Controle financeiro
├── people          # Gestão de membros
├── reports         # Relatórios
├── schools         # Gestão de cursos e alunos
└── templates       # Templates HTML
```

## Funcionalidades Principais

- Gestão de Igrejas e Congregações
- Cadastro de Membros
- Controle Financeiro
- Gestão de Eventos
- Escola Bíblica (Cursos e Alunos)
- Relatórios e Dashboards

## Requisitos

- Python 3.10+
- Django 5.0+

## Instalação

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute as migrações: `python manage.py migrate`
4. Crie um superusuário: `python manage.py createsuperuser`
5. Inicie o servidor: `python manage.py runserver`

## Módulos

### Igrejas
- Cadastro de igrejas e congregações
- Gestão de membros por igreja

### Pessoas
- Cadastro de membros
- Histórico e informações pessoais

### Eventos
- Agenda de eventos
- Gestão de participantes

### Finanças
- Plano de contas
- Lançamentos financeiros
- Relatórios financeiros

### Escola
- Gestão de cursos
- Matrícula de alunos
- Acompanhamento de turmas

### Relatórios
- Relatórios personalizados
- Dashboard gerencial
- Indicadores e métricas
