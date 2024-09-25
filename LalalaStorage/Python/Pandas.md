**Установка библиотеки:**
```pip install pandas```

**Импорт:**
```python
import pandas as pd
```

**Создание столбца:**
```python

a = [1,  7, 2]

series = pd.Series(a)

series

```


**Обращение к элементу строки:**
```python
series.loc[0] # Обращается по названию столбца

series.iloc[0] # Обращается по индексу массива
```

![[Pasted image 20240925205443.png]]
