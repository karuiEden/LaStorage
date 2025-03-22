
## Подготовка

**Установка:**

```shell
pip install seaborn
```

**Импорт:**

```python

import seaborn as sns

```

## Использование

**Построение тепловой карты:

```python

array = np.random.randint(1, 100, size=(4, 4))

sns.heatmap(array, annot=True)

```

![[Pasted image 20240926221726.png]]

*P.S. Карта имеет ознакомительный характер*


**Использование на примере датасета Титаник**

```python

plt.figure(figuresize=(7,5))

sns.heatmap(df.isna().transpose())

```

![[Pasted image 20240926222152.png]]


### Графики взаимных распределений

```python
sns.set() # подключает встроенные темы
sns.pairplot(df[numerical_columns], height=2, kind="scatter", diag_kind='kde')

plt.show()
```

![[Pasted image 20240927113022.png]]

Пример графика взаимных распределений

### Матрица корреляций

```python
corr = df.corr() # взято из pandas

f, ax = plt.subplots(figsize=(12,9))

sns.heatmap(corrmat, vmax=.8, square=True);
```

![[Pasted image 20240927114438.png]]

Более красивая матрица:
```python
k = 10 # number of variables for heatmap

cols = corrmat.nlargest(k, 'Survived')['Survived'].index

cm = np.corrcoef(df[cols].values.T)

sns.set(font_scale=1.25)

hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)

plt.show()
```
![[Pasted image 20240927114737.png]]
