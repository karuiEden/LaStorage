**Установка библиотеки:**
```pip install pandas```

**Импорт:**
```python

import pandas as pd
```

**Создание столбца:**
```python

a = [1,  7, 2]

series = pd.Series(a) # Стандартный

series = pd.Series(a, index = ["x", "y", "z"]) # Кастомные индексы

print(series)
series

```


**Обращение к элементу строки:**
```python
series.loc[""] # Обращается по названию столбца

series.iloc[0] # Обращается по индексу массива
```

![[Pasted image 20240925205443.png]]

**Создание таблицы**

```python
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# можно создать таблицу из Python Dict
# keys словаря будут названиями столбцов
df = pd.DataFrame(data)
print(df)
df
```

Обращение к строкам данных такое же, как и к массиву 

**Чтение таблицы из файла:**

```python
df = pd.read_csv("titanic.csv")
print(df)
```