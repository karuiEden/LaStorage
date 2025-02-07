*Тэги:* ML

## Теория

![[Pasted image 20241001175157.png]]


**k-Nearest Neighbors** - простой алгоритм, который работает по принципу нахождения $k$ ближних соседей. Модель на таком алгоритме, по сути, не обучается, так как в неё просто загружаются все данные.
Алгоритм:
1. Считаем расстояние до всех "соседей".
2. Выбираем $k$ соседей.
3. Делаем предсказание.
Используется в задачах регрессии и классификации:
- В задачах классификации после нахождения соседей, смотрим их целевую переменную. Результатом предсказания будет тот целевой класс, который встретился больше всего.
- В задачах регрессии результат предсказания будет равен среднему значению целевых переменных ближайших соседей.
## Реализация

### Расчёт расстояния:

Традиционно в качестве расстояния берётся Евклидово расстояние:
$$Eucleadian\space dictance(x_1, x_2) = \sqrt{\sum_{i=1}^n}{(x^i_1 - x^i_2)^2}$$
Реализация на питоне:
```python
def eucleadian_distanse(vec1, vec2): 
	distance = 0
	for i in range(len(vec1)):
		distance += (vec1[i] - vec2[i])**2
	return sqrt(distance)
```

### Нахождения ближайших соседей

```python
def get_neighbors_dummy(train, test_row, num_neighbors):
	distances = []
	for train_id, train_row in enumerate(train):
		dist = eucleadian_distanse(train_row, test_row)
		distances.append((train_id, dist ))
	distances = distances.sort(key=lambda x: x[1])
	nearest_neighbors_ids = []
	for i in range(num_neighbors):
		nearest_neighbors_ids.append(distances[i][0])
	return nearest_neighbors_ids
```

### Получение предсказания

```python
def get_predict(X_train, X_test, Y_train, num_neighbors = 3):
	y_predict = []
	for x_test in X_test:
		nearest_neighbors_ids = get_neighbors_dummy(X_train, x_test, num_neighbors)
		y_pred = y_train[nearest_neighbor_ids]
		y_pred = y_pred.mean()
		y_predict.append(y_pred)
	return y_predict	
	
```

Также KNN модель доступна в библиотеке Sklearn