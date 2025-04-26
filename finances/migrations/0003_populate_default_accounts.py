
from django.db import migrations

def create_default_accounts(apps, schema_editor):
    Account = apps.get_model('finances', 'Account')
    default_accounts = [
        ('1.1', 'Caixa', 'asset'),
        ('1.2', 'Banco', 'asset'),
        ('1.3', 'Aplicações Financeiras', 'asset'),
        ('2.1', 'Contas a Pagar', 'liability'),
        ('2.2', 'Empréstimos', 'liability'),
        ('3.1', 'Patrimônio Social', 'equity'),
        ('4.1', 'Dízimos', 'revenue'),
        ('4.2', 'Ofertas', 'revenue'),
        ('4.3', 'Doações', 'revenue'),
        ('4.4', 'Eventos', 'revenue'),
        ('5.1', 'Pessoal', 'expense'),
        ('5.2', 'Administrativas', 'expense'),
        ('5.3', 'Manutenção', 'expense'),
        ('5.4', 'Ministérios', 'expense'),
        ('5.5', 'Ação Social', 'expense'),
        ('5.6', 'Missões', 'expense'),
    ]
    
    for code, name, type in default_accounts:
        Account.objects.get_or_create(
            code=code,
            defaults={'name': name, 'type': type}
        )

def remove_default_accounts(apps, schema_editor):
    Account = apps.get_model('finances', 'Account')
    Account.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('finances', '0002_remove_transaction_category_transaction_person_and_more'),
    ]

    operations = [
        migrations.RunPython(create_default_accounts, remove_default_accounts),
    ]
