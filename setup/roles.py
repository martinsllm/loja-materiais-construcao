from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    avaible_permissions = {
        'cadastrar_produtos': True,
        'liberar_desconto': True,
        'cadastrar_vendedor': True
    }

class Gerente(AbstractUserRole):
    avaible_permissions = {
        'realizar_venda': True
    }