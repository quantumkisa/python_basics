class ExceptionInt:
    def __init__(self, *args):
        self.my_list = []

    def check_int(self):
        while True:
            try:
                val = input('введите число. для завершения ввода введите stop')
                if val == 'stop' or val == 'Stop':
                    break
                self.my_list.append(int(val))
            except:
                print('вы ввели недопустимое значение. введите число или stop для завершения программы')
                val_2 = input('введите число. для завершения ввода введите stop')
                if val_2 == 'stop' or val_2 == 'Stop':
                    break
                self.my_list.append(int(val_2))
        return f'ваш список : {self.my_list}'



kek = ExceptionInt(1)
print(kek.check_int())
