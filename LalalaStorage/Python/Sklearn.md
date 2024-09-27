
## Подготовка

**Установка:**

```shell
pip install sklearn
```

**Импорт:**

```python
import sklearn
```

### One hot Encoding

```python
from sklearn.preprocessing import OneHotEncoder

# Initialize encoder
encoder = OneHotEncoder(sparce_output=false)

#Apply encoder to the categorial column
one_hot_encode = encoder.fit_transform(df[unprocessed_cat_features])

#Create DataFrame with encode columns
	one_hot_df = pd.DataFrame(one_hot_encode, columns=encoder.get_feature_names_out(unprocessed_cat_features), index=df.index)

#Add one_hot columns to original df
df_encoded = pd.concat([df, one_hot_df], axis=1)

df_encoded.drop(unprocessed_cat_features, inplace=True)
```
 Результат:
Ниже показана таблица `one_hot_df`

![[Pasted image 20240927103210.png]]

### Label Encoding

```python
from sklearn.preprocessing import LabelEncoder

# Initialize Encoder
encode = LabelEncoder()

# Fit and transform the categorial data
for column in unprocessed_cat_features:
	df[column] = encode.fit_transorm(df[column])

```


### Scaling data

**Standart Scale:**
```python
from sklearn.preprocessing import StandardScaler

  

scaler = StandardScaler()

scaler.fit(X_train)

# Выход pca - numpy матрица, положим ее в новую переменную со всеми фичами

X_train_scaled = scaler.transform(X_train)

X_test_scaled = scaler.transform(X_test)
```

**MinMaxScale:**
```python
from sklearn.preprocessing import MinMaxScaler

  

scaler = MinMaxScaler()

scaler.fit(X_train)

# Выход pca - numpy матрица, положим ее в новую переменную со всеми фичами

X_train_scaled = scaler.transform(X_train)

X_test_scaled = scaler.transform(X_test)
```