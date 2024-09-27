
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
