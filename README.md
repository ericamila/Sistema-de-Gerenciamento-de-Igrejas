
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
- Plano de contas estruturado
- Lançamentos financeiros
- Relatórios financeiros

#### Plano de Contas
1. Ativo
   - 1.1 Caixa
   - 1.2 Banco
   - 1.3 Aplicações Financeiras

2. Passivo
   - 2.1 Contas a Pagar
   - 2.2 Empréstimos

3. Patrimônio
   - 3.1 Patrimônio Social

4. Receitas
   - 4.1 Dízimos
   - 4.2 Ofertas
   - 4.3 Doações
   - 4.4 Eventos

5. Despesas
   - 5.1 Pessoal
   - 5.2 Administrativas
   - 5.3 Manutenção
   - 5.4 Ministérios
   - 5.5 Ação Social
   - 5.6 Missões

### Escola
- Gestão de cursos
- Matrícula de alunos
- Acompanhamento de turmas

### Relatórios
- Relatórios personalizados
- Dashboard gerencial
- Indicadores e métricas
