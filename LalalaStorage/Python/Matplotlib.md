
**Установка:**
```bash
pip install matplotlib
```

**Импорт:**

```python

import matplotlib.pyplot as plt # Импорт самой библиотеки

import numpy as np # Импорт вспомогательной библиотеки NumPy

```

**Создание простого линейного графика

```python
# Создание 10 точек со случайными координатами
x = np.arange(10)
y = np.random.randit(1, 10, size=10)

print(f'x = {x}')
print(f'y = {y}')

# Задаём размер полотна, на котором будет отрисован график

plt.figure(figsize=(10, 7))

# Построение графика в виде диаграммы

plt.plot(x, y)

# Построение точечной диаграммы

plt.scatter(x, y)

# Создание заголовка графика

plt.title("Title Name")

# Имена осей

plt.xlabel("x-axis")
plt.ylabel("y-label")

# Результат
plt.show()
```


**Создание нескольких графиков в одной координатной плоскости:**

```python
#Создание координат точек
x = np.arange(10)
y = np.random.randit(1, 10, size=10)
z = np.random.randit(1, 10, size=10)

# Задаём размер полотна, на котором будет отрисован график 
plt.figure(figsize=(10, 7))

# Создание линейных графиков

plt.plot(x, y, label="plot_name") # Для понимания присвоим имена нашим графикам
plt.plot(x, z, color="color",label="lalala") # Также можно изменить цвет линии

# Отображение имён

plt.legend()

# Задаём заголовок

plt.title("Title")

# Имена осей

plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Ограничение осей

plt.xlim([-n, n])
plt.ylim([0, m])

# Добавление сетки

plt.grid()

# Отрисовка графиков

plt.show()

```


**Стилизация графиков:**

```python

plt.style.use("style_name")

```

## Создание диаграмм

При анализе данных, чтобы облегчить себе жизнь можно построить диаграмму. В данном блоке будет использована библиотека [[Pandas]] 

```python
data =  df.isnan().sum(axis=0)

plt.figure(figsize=(10, 7))

plt.bar(data.indexes, data.values) # Также есть метод barh, который выводит значение на горизонтальную ось

```


**Диаграммы:**

```python

plt.hist(df['Column']) # Строит диаграмму

# Добавление вертикальных линий
plt.axvline(x=n, color='color', linestyle='.', label="name")

...

plt.show()

```
