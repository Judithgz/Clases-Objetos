from sistema_empleados.empleado import Empleado
from sistema_empleados.empresa import Empresa

print('*** Sistema de Empleados ***')

# Crear una instancia de una empresa
empresa1 = Empresa('Global Mentoring')

# Contratar empleados
empresa1.contratar_empleado('Isaar', 'Ventas')
empresa1.contratar_empleado('Judith', 'Software')
empresa1.contratar_empleado('Manuela', 'Marketing')
empresa1.contratar_empleado('Jesus', 'Ventas')

# Obtener total de objetos de tipo empleados
print(f'Total de empleados: {Empleado.obtener_total_empleados()}')

# Obtener total de empleados por departamento
print(f'Empleados en departamento de ventas: {empresa1.obtener_numero_empleados_departamento('Ventas')}')

# Obtener total de empleados por empresa
empresa1.obtener_total_empleados()