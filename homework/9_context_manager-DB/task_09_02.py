from peewee import *
from datetime import datetime

# данные для таблиц
employees_data = [
(1, 'Шершуков', 'Виктор', 'Кузьмич',),
(2, 'Битова', 'Анастасия', 'Юрьевна',),
(3, 'Кириллов', 'Валентин', 'Владиславович',),
(4, 'Игнатьев', 'Игорь', 'Дмитриевич',),
]

salary_data = [
    (1, '2019-12-01', 'salary', 50000),
    (1, '2020-01-01', 'salary', 50000),
    (1, '2020-02-01', 'salary', 50000),
    (1, '2020-03-01', 'salary', 50000),
    (1, '2020-04-01', 'salary', 50000),
    (1, '2020-05-01', 'salary', 50000),
    (1, '2020-06-01', 'salary', 53000),
    (1, '2020-07-01', 'salary', 53000),
    (1, '2020-08-01', 'salary', 53000),
    (1, '2020-09-01', 'salary', 53000),
    (1, '2020-10-01', 'salary', 53000),
    (1, '2020-11-01', 'salary', 53000),
    (1, '2020-12-01', 'salary', 53000),
    (1, '2021-01-01', 'salary', 53000),
    (1, '2019-12-01', 'bonus', 10000),
    (1, '2020-01-01', 'bonus', 10000),
    (1, '2020-02-01', 'bonus', 9000),
    (1, '2020-03-01', 'bonus', 11000),
    (1, '2020-04-01', 'bonus', 10000),
    (1, '2020-05-01', 'bonus', 5000),
    (1, '2020-06-01', 'bonus', 10000),
    (1, '2020-07-01', 'bonus', 10000),
    (1, '2020-08-01', 'bonus', 10000),
    (1, '2020-09-01', 'bonus', 10000),
    (1, '2020-10-01', 'bonus', 10000),
    (1, '2020-11-01', 'bonus', 10000),
    (1, '2020-12-01', 'bonus', 10000),
    (1, '2021-01-01', 'bonus', 10000),
    (2, '2019-12-01', 'salary', 60000),
    (2, '2020-01-01', 'salary', 60000),
    (2, '2020-02-01', 'salary', 60000),
    (2, '2020-03-01', 'salary', 62000),
    (2, '2020-04-01', 'salary', 62000),
    (2, '2020-05-01', 'salary', 62000),
    (2, '2020-06-01', 'salary', 62000),
    (2, '2020-07-01', 'salary', 62000),
    (2, '2020-08-01', 'salary', 62000),
    (2, '2020-09-01', 'salary', 62000),
    (2, '2020-10-01', 'salary', 65000),
    (2, '2020-11-01', 'salary', 65000),
    (2, '2020-12-01', 'salary', 65000),
    (2, '2021-01-01', 'salary', 65000),
    (2, '2019-12-01', 'bonus', 10000),
    (2, '2020-01-01', 'bonus', 10000),
    (2, '2020-02-01', 'bonus', 9000),
    (2, '2020-03-01', 'bonus', 11000),
    (2, '2020-04-01', 'bonus', 10000),
    (2, '2020-05-01', 'bonus', 5000),
    (2, '2020-06-01', 'bonus', 10000),
    (2, '2020-07-01', 'bonus', 7000),
    (2, '2020-08-01', 'bonus', 7000),
    (2, '2020-09-01', 'bonus', 7000),
    (2, '2020-10-01', 'bonus', 7000),
    (2, '2020-11-01', 'bonus', 7000),
    (2, '2020-12-01', 'bonus', 7000),
    (2, '2021-01-01', 'bonus', 7000),
    (3, '2019-12-01', 'salary', 60000),
    (3, '2020-01-01', 'salary', 60000),
    (3, '2020-02-01', 'salary', 60000),
    (3, '2020-03-01', 'salary', 60000),
    (3, '2020-04-01', 'salary', 60000),
    (3, '2020-05-01', 'salary', 60000),
    (3, '2020-06-01', 'salary', 60000),
    (3, '2020-07-01', 'salary', 60000),
    (3, '2020-08-01', 'salary', 60000),
    (3, '2020-09-01', 'salary', 60000),
    (3, '2020-10-01', 'salary', 60000),
    (3, '2020-11-01', 'salary', 64000),
    (3, '2020-12-01', 'salary', 64000),
    (3, '2021-01-01', 'salary', 64000),
    (4, '2019-12-01', 'salary', 61000),
    (4, '2020-01-01', 'salary', 61000),
    (4, '2020-02-01', 'salary', 61000),
    (4, '2020-03-01', 'salary', 61000),
    (4, '2020-04-01', 'salary', 61000),
    (4, '2020-05-01', 'salary', 63000),
    (4, '2020-06-01', 'salary', 63000),
    (4, '2020-07-01', 'salary', 63000),
    (4, '2020-08-01', 'salary', 63000),
    (4, '2020-09-01', 'salary', 63000),
    (4, '2020-10-01', 'salary', 63000),
    (4, '2020-11-01', 'salary', 63000),
    (4, '2020-12-01', 'salary', 63000),
    (4, '2021-01-01', 'salary', 63000),
    (4, '2019-12-01', 'bonus', 7000),
    (4, '2020-01-01', 'bonus', 7000),
    (4, '2020-02-01', 'bonus', 7000),
    (4, '2020-03-01', 'bonus', 7000),
    (4, '2020-04-01', 'bonus', 7000),
    (4, '2020-05-01', 'bonus', 7000),
    (4, '2020-06-01', 'bonus', 7000),
    (4, '2020-07-01', 'bonus', 7000),
    (4, '2020-08-01', 'bonus', 7000),
    (4, '2020-09-01', 'bonus', 7000),
    (4, '2020-10-01', 'bonus', 7000),
    (4, '2020-11-01', 'bonus', 7000),
    (4, '2020-12-01', 'bonus', 7000),
    (4, '2021-01-01', 'bonus', 7000),
]

emails_data = [
    (1, 1, 'shershuko@mail.ru',),
    (2, 1, 'shershuko-v@mail.ru',),
    (3, 2, 'bitova@mail.ru',),
    (4, 2, 'bitova@mail.ru',),
    (5, 3, 'kirillov@mail.ru',),
    (6, 3, 'kirillov@mail.ru',),
]

db = SqliteDatabase('employees.db')

class BaseModel(Model):
    class Meta:
        database = db

class Employees(BaseModel):
    ID_emp = IntegerField(primary_key=True) # ID сотрудника
    NAME1 = CharField() # Фамилия сотрудника
    NAME2 = CharField() #Имя сотрудника
    NAME3 =  CharField() # Отчество сотрудника


class Salary(BaseModel):
    ID_emp = ForeignKeyField(Employees, backref='salary') # ID сотрудника
    dt = DateField() # Дата выплаты
    Salary_Type = CharField() #Тип суммы (salary, bonus)
    Amount_double =  IntegerField() # Сумма

class Emails(BaseModel):
    ID_email = IntegerField() # ID Email
    ID_emp = ForeignKeyField(Employees, backref='emails') # ID сотрудника
    Email = CharField() #Email адрес



# Создание таблиц в базе данных
with db:
    db.create_tables([Employees, Salary, Emails])

    # Наполнение таблиц данными из массивов

    with db.atomic():
        # Предварительная очистка таблиц
        for table in [Employees, Salary, Emails]:
            for row in table.select():
                row.delete_instance()

        Employees.insert_many(employees_data, fields=[Employees.ID_emp, Employees.NAME1, Employees.NAME2, Employees.NAME3]).execute()
        Salary.insert_many(salary_data, fields=[Salary.ID_emp, Salary.dt, Salary.Salary_Type, Salary.Amount_double]).execute()
        Emails.insert_many(emails_data, fields=[Emails.ID_email, Emails.ID_emp, Emails.Email]).execute()
        

        # print(Employees.get(Employees.ID_emp == 1))

    #     for empl in Employees.select():
    #         print(empl.NAME1)
        # for employee in Employees.select():
                # print(employee.ID_emp)
                # email = Emails.select().where(
                    # employee.ID_emp == Emails.ID_emp
                # )
                # for em in email:
                    # print(em.Email)
                # emails = Emails.select().where(
                #     Emails.ID_emp == employee.ID_emp,
                #     Salary.dt.year == 2020
                # )

    def calculate_average_salary():
        for employee in Employees.select():
            for email in employee.emails:
                salary_total = 0
                bonus_total = 0
                salary_count = 0
                bonus_count = 0
                salari_model = Salary.select().where(
                    Salary.ID_emp == employee.ID_emp,
                    Salary.dt.year == 2020
                )
                # email = set()
                # email_model = Emails.select().where(
                    # employee.ID_emp == Emails.ID_emp
                # )
                # for em in email_model:
                    # email.add(em.Email)

                for salary in salari_model:
                    if salary.Salary_Type == 'salary':
                        salary_total += salary.Amount_double
                        salary_count += 1
                    elif salary.Salary_Type == 'bonus':
                        bonus_total += salary.Amount_double
                        bonus_count += 1

                if salary_count > 0:
                    average_salary = salary_total / salary_count
                else:
                    average_salary = 0

                if bonus_count > 0:
                    average_bonus = bonus_total / bonus_count
                else:
                    average_bonus = 0

                # for em in email
                print(f"Empl_ID: {employee.ID_emp}, FIO: {employee.NAME1} {employee.NAME2} {employee.NAME3}, Salary: {average_salary}, Bonus: {average_bonus}, Email: {email.Email}")

    calculate_average_salary()
