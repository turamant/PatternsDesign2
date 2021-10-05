# coding: utf-8

"""
Фабричный метод (Factory Method) - паттерн, порождающий классы.
Определяет интерфейс для создания объекта, но оставляет подклассам решение о том, какой класс инстанцировать.
Позволяет делегировать инстанцирование подклассам.
Абстрактная фабрика часто реализуется с помощью фабричных методов.
Фабричные методы часто вызываются внутри шаблонных методов.
"""


class CreatorDocument:
    def show(self):
        raise NotImplementedError()


class AdminForm(CreatorDocument):
    def show(self):
        print('Форма администратор')


class UserForm(CreatorDocument):
    def show(self):
        print('Форма юзер')


class Application:
    def create_document(self, type_):
        # параметризованный фабричный метод `create_document`
        raise NotImplementedError()


class MyApplication(Application):
    def create_document(self, type_):
        if type_ == 'admin':
            return AdminForm()
        elif type_ == 'user':
            return UserForm()
        else:
            return CreatorDocument()

if __name__=='__main__':
    app = MyApplication()
    app.create_document('admin').show()
    app.create_document('user').show()
    try:
        app.create_document('pdf').show()
    except:
        print("NotImplementedError")
