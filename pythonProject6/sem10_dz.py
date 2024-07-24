"""Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача
перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()"""

import pandas as pd
import random

# Создание DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание one-hot кодирования
unique_values = data['whoAmI'].unique()
one_hot_data = pd.DataFrame(0, index=data.index, columns=unique_values)

for i, value in enumerate(data['whoAmI']):
    one_hot_data.loc[i, value] = 1

# Объединение исходного DataFrame и one-hot кодирования
result = pd.concat([data, one_hot_data], axis=1)


print("Исходные данные:")
print(data.head())

print("\nOne-hot кодирование:")
print(one_hot_data.head())

print("\nРезультирующий DataFrame:")
print(result.head())  
