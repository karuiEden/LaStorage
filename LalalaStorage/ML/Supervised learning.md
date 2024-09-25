$X$ - множество объектов
$Y$ - множество ответов
$y: X → Y$ - истинная зависимость

Обучающий датасет - множество наборов из признаков и значений целевой переменной. Обозначим $X$<sub>train</sub> $⊂ X$
$$X_{train}=\begin{pmatrix}x_{11}&x_{12}&...&x_{1m}\cr&...&...\cr x_{n1}&x_{n2}&...&x_{nm}\end{pmatrix}$$
$$y_{train} = \begin{pmatrix}y_1\cr ... \cr y_n \end{pmatrix}$$ 
Типы признаков:
- Числовые (Numerical)
- Категориальные (Categorical)
- Порядковые (Ordinal)

Типы задач:
- Классификация (Classification)
  $Y = \{ 0, 1 \}, Y = \{1, 2, ..., n\}, Y = \{0, 1\}^n$
-  Регрессия (Regression)
  $$ Y = \mathbb{R} $$
-  Ранжирование
  $Y = \{1, 2, ..., n \}$ (числа упорядочены)

# KNN(K-Nearest Neighbors)


**Решение задачи классификации:**
*Обучение*: Просто запоминаем обучающую выборку.
*Предсказание:*
- Получаем точку **x**, в которой надо сделать предсказание.
- Ищем **k** ближайших соседей.
- В качестве ответа возвращаем класс, которого больше всех соседей.

## Curse of Dimensionality

В KNN мы делаем очень слабое предположение: близкие точки будут иметь близкие ответы.
При большой размерности данных в близкую область попадёт мало объектов.


## Feature Scale

Если в качестве метрики взять обычное расстояние между векторами, то возникает проблема масштаба признаков.

**Пример:**
- Расстояние до метро в метрах
- Кол-во комнат

Количество комнат почти не будет влиять на предсказание.

![Why do you need to scale data in KNN - Cross Validated](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeL_NmfjjN9uBcONT1LTPUy7B4eA3iPeUyfwGeNU0tayS9NcAEwuzq8cjfzYM3sVYQiOmXeWuNJTzN6AUO2o3fkReG2zN6mQJpqaWu8gekroMG8q8dIZUNuS3RzFnpt22iLRUfqlP79HnnR4QKi_YvadJSbL9nhvKZVHyLERD1n9VgjZAjW=s2048?key=lMBvtV1TQcZWVVgv7RjHYA)


# Обучение с учителем

Наша задача - найти функцию хорошо приближающую реальную зависимость $y(x)$.
Назовём такое решение  $ŷ: X → Y$ (эта функция должна быть вычислима на компьютере).

Обычно мы выбираем решение из некоторого параметризованного семейства.
 $$\mathcal{F} = \{ ŷ_\theta | \theta \in \Theta\}, \Theta - множество\spaceпараметров. $$

**Обучение** - процесс выбора параметра $\theta$, которому соответствует наиболее подходящее нам решение задачи $ŷ_\theta(x_1, x_2)$ . 

## Функции потерь (loss)

Определим функцию $L(y, ŷ(x))$, её значение показывает насколько сильно наше предсказание отличается от реального значения.

**Виды функций:**
- $L(y_{true}, ŷ(x)) = (y_{true} - ŷ(x))^2$ - квадратичная функция потери
- $L(y_{true}, ŷ(x)) = |y_{true} - ŷ(x)|$ - абсолютная функция потери
- $L(y_{true}, ŷ(x)) = (y_{true} - ŷ(x))^2 + 7$ - иные

## Эмпирический риск

Определим эмпирический риск как среднее значение функции потерь на обучающем датасете.
Часто функцию эмпирического риска также называют loss.
$$\theta_{best} =
\underset{\theta \in \Theta}{\mathrm{argmin}}\frac{1}{dataset\space size}\sum_i{L(y_{true}^i, ŷ(x^i))}
$$

## Линейная регрессия

$$\hat{y}(x_1, x_2, ..., x_n) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + ... + \theta_n x_n$$
**Обучение линейной регрессии:**
Классически в качестве лосса берут Mean Squared Error (среднее квадратов ошибок)

$$\underset{\theta_0, ... ,\theta_n}{\mathrm{argmin}}\sum_i(y_{true}^i - \theta_0 - theta_1 x_1^i - ... - \theta_n x_n^i)^2$$
### Polynomial Regression

Пусть у нас изначально есть только один признак $x$. Создадим новые:
$x_1 = x , x_2 = x^2, ..., x_n = x^n$ 

Тогда линейная регрессия от таких признаков называется полиномиальной:
$$\hat{y}(x_1, x_2, ..., x_n) =  \theta_0 + \theta_1 x + \theta_2 x^2 + ... + \theta_n x^n$$
Пример полиномиальной регрессии с n признаками, где можно заметить переобучение:

![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUf5DF498bc0OFt347SUIcT4Lea2C9UyimIE7rF5EA-agDey-dro0NPNANkmmJ5bgOhwaaDEdCWxBL_6ZJFmrSzWiAaaky3pRQiuM9CPHR6IBEYxR2dIViVC3XlXIsOO5AEhM0tKH6P8HyZ7_LJHU73bI4jXVQhuN4h_j4AJq4ZobF64RHL1=s2048?key=lMBvtV1TQcZWVVgv7RjHYA)

## Переобучение (KNN)

Если в алгоритме KNN мы возьмём $k=1$, то получим  идеальные предсказания на всем обучающем датасете и эмпирический риск будет равен 0. Это может являться не очень хорошим.

## Разделение на Train/Validation/Test

- Train - данные для обучения.
- Validation - данные для итеративной оценки качества.
- Test - данные для финальной оценки качества.
Часто можно опустить test часть. В этом случае название validation dataset и test dataset значат одно и то же.
![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdoZpNPWg6RNdxnsyC6c11eKWo6dPFCHazzQGjskr_LNLn8k1bws11-pNqFd2DplwLi2RA_KalpaYs1JqoUqhrrg5sRFSrVvmM06Rv2nejHXUSyYpyXRjsAiol8ki72XCayc3Ygfm0LH7RdS8BFjGcpIfr36Gvta01_4trRpayotNz19Ig=s2048?key=lMBvtV1TQcZWVVgv7RjHYA)

## Переобучение
**Переобучение** - ситуация, когда качество модели на train данных значительно лучше, чем на validation/test.

![[Pasted image 20240925151959.png]]

## Cross-validation

![[Pasted image 20240925152118.png]]
В данном примере для обучения нужно обучить модель 5 раз

**Не подходит для обучения нейронных сетей из-за n раз обучения моделей**

## Алгоритм решения задачи ML

**Result:** Модель ""закона природы"" $\hat{y}_\theta(x)$
Разделяем датасет на train, validation, test части;
Обрабатываем данные;
**while** *Качество на validation недостаточно высокое* **do**
	Выбираем семейство моделей $\mathcal{F}$ , выбрав тип модели и гиперпараметры;
	Обучаем, решая задачу $\theta_{best} = argmin_\theta \sum_iL(y_{true}^i, ŷ(x^i))$ ;
	Проверяем качество (лосс и метрики) на validation датасете;
**end**
Проверяем качество на test датасете.