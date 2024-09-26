
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


