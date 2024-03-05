import pandas as pd
from datetime import date
# Исходные данные для отчета
employees = [
    (1, 'Шершуков', 'Виктор', 'Кузьмич'),
    (2, 'Битова', 'Анастасия', 'Юрьевна'),
    (3, 'Кириллов', 'Валентин', 'Владиславович'),
    (4, 'Игнатьев', 'Игорь', 'Дмитриевич'),
]

emails = [
    (1, 1, 'shershuko@mail.ru'),
    (2, 1, 'shershuko-v@mail.ru'),
    (3, 2, 'bitova@mail.ru'),
    (4, 2, 'bitova@mail.ru'),
    (5, 3, 'kirillov@mail.ru'),
    (6, 3, 'kirillov@mail.ru'),
]

salary = [
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

# Создание DataFrame для каждой таблицы
df_employees = pd.DataFrame(employees, columns=['Empl_ID', 'NAME1', 'NAME2', 'NAME3'])
df_emails = pd.DataFrame(emails, columns=['Email_ID', 'Empl_ID', 'Email'])

df_salary = pd.DataFrame(salary, columns=['Empl_ID', 'dt', 'Salary_Type', 'Amount'])



# # Объединение таблиц по соответствующим ключам
merged_df = pd.merge(df_employees, df_emails, on='Empl_ID', how = 'left')

# print(df_employees)
# merged_df.groupby('NAME1')

# #удаляем дубликаты
merged_df.drop_duplicates(subset=['Empl_ID', 'Email'], keep="first", inplace=True)
# print(merged_df)
merged_df = pd.merge(merged_df, df_salary, on='Empl_ID', how = 'left')
# print(merged_df)

# Преобразование столбца с датой в формат datetime
merged_df['dt'] = pd.to_datetime(merged_df['dt']) 

# Оставляем только 2020 год
merged_df = merged_df[merged_df['dt'].dt.year == 2020]

# print(merged_df)

# # Расчет средней заработной платы и бонусов
average_salary = merged_df[merged_df['Salary_Type'] == 'salary'].groupby('Empl_ID')['Amount'].mean()
average_bonus = merged_df[merged_df['Salary_Type'] == 'bonus'].groupby('Empl_ID')['Amount'].mean()

# # print(average_salary)
# # Вывод отчета
report = merged_df[['Empl_ID', 'NAME1', 'NAME2', 'NAME3', 'Amount', 'Salary_Type', 'Email']]
report['Average_Salary'] = report['Empl_ID'].map(average_salary)
report['Average_Bonus'] = report['Empl_ID'].map(average_bonus)

report = report[['Empl_ID', 'NAME1', 'NAME2', 'NAME3', 'Email', 'Average_Salary', 'Average_Bonus']].drop_duplicates()

print(report)
# print(report.groupby('Empl_ID', 'NAME1', 'NAME2', 'NAME3', 'Amount', 'Salary_Type', 'Email'))