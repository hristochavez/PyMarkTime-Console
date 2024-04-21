from templates.banner import banner
from templates.commons import clean_screen
from views.actions import create_marktime

# Permisos que puede tener un empleado:
# 1 -> puede marcar.
# 2 -> puede registrar empleados.
# 3 -> puede inhabilitar empleados.
actions = {
    1: 'Realizar marcación.',
    2: 'Registrar a un empleado.',
    3: 'Inhabilitar a un empleado.'
}


# Retorna una lista de acciones que puede realizar un usuario donde cada
# acciónn es una tupla conformada por:
# (número de opción a mostrar, llave, valor).
def get_actions(permissions):
    # Lista de acciones permitidas.
    permitted_actions = []

    # Llenar la lista de acciones permitidas de acuerdo a los permisos que
    # tiene el usuario.
    num_opt = 1
    for key, value in actions.items():
        if key in permissions:
            permitted_actions.append((num_opt, key, value))
            num_opt += 1

    return permitted_actions


# Muestra el meńu principal del empleado.
def employee_menu(employee):
    clean_screen()
    banner()

    print(f'DNI: {employee["dni"]}')
    print(f'Bienvenido(a) {employee["first_name"]}')
    print('')

    # Muestra los permisos que tiene el usuario.
    print('Usted tiene los siguientes permisos:')
    actions = get_actions(employee['permissions'])

    for action in actions:
        print(f'{action[0]}.- {action[2]}')

    # Pregunta al usuario por la acción a realizar.
    valid_actions = [str(x) for x in range(1, len(actions) + 1)]
    print('')
    selected_action = input('Elija el número de acción a realizar: ')

    while selected_action not in valid_actions:
        selected_action = input('Elija el número de acción a realizar: ')

    # Ejecuta la acción elegida por el usuario.
    # Obtiene la acción a realizar de la lista de acciones que puede realizar
    # el usuario.
    action_to_do = 0
    for action in actions:
        if str(action[0]) == selected_action:
            action_to_do = action[1]
            break

    if action_to_do == 1:
        create_marktime(employee['dni'])