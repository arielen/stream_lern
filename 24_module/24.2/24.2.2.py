# Задача 2. Однотипные объекты
# В офис заказали небольшую партию из четырёх мониторов и трёх наушников.
# У монитора есть четыре характеристики: название производителя, матрица, разрешение и частота обновления экрана.
# Все четыре монитора отличаются только частотой.
# У наушников три характеристики: название производителя, чувствительность и наличие микрофона.
# Отличие только в наличии микрофона.
#
# Для внесения в базу программист начал писать такой код:
#
# monitor_name_1 = 'Samsung'
# monitor_matrix_1 = 'VA'
# monitor_res_1 = 'WQHD'
# monitor_freq_1 = 60
# monitor_name_2 = 'Samsung'
# monitor_matrix_2 = 'VA'
# monitor_res_2 = 'WQHD'
# monitor_freq_2 = 144
# monitor_name_3 = 'Samsung'
# monitor_matrix_3 = 'VA'
# monitor_res_3 = 'WQHD'
# monitor_freq_3 = 70
# monitor_name_4 = 'Samsung'
# monitor_matrix_4 = 'VA'
# monitor_res_4 = 'WQHD'
# monitor_freq_4 = 60
# headphones_name_1 = 'Sony'
# headphones_sensitivity_1 = 108
# headphones_micro_1 = False
# headphones_name_2 = 'Sony'
# headphones_sensitivity_2 = 108
# headphones_micro_2 = True
# headphones_name_3 = 'Sony'
# headphones_sensitivity_3 = 108
# headphones_micro_3 = True
#
# Поправьте программиста: перепишите код, используя классы и экземпляры классов.

class Monitor:
    manufacturer = "Samsung"
    matrix = "VA"
    permission = "WQHD"
    frequency = 60


class Headphones:
    manufacturer = "Sony"
    sensitivity = 108
    micro = True


monitor_1, monitor_2, monitor_3, monitor_4 = Monitor()
monitor_2.frequency = 144
monitor_3.frequency = 70

headphones_1, headphones_2, headphones_3 = Headphones()
headphones_1.micro = False
