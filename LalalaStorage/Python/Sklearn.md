
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

## KNN


```python
# Initialization
model = KNeighborsRegressor(n_neighbors = n) # For regression tasks
model = KNeighborsClassifier(n_neighbors = n) # For Classification tasks

model.fit(X_train, Y_train) # Learning model

y_pred = model.predict(X_test) # Prediction from model
```

### Метрики

```python
from sklearn.metrics import mean_squared_error

from sklearn.metrics import r2_score, mean_absolute_error

  

pred_train = model.predict(X_train)

pred_test = model.predict(X_test)

  

MSE_train = mean_squared_error(y_train, pred_train)

RMSE_train = np.sqrt(MSE_train)

R2_train = r2_score(y_train, pred_train)

MAE_train = mean_absolute_error(y_train, pred_train)

  

MSE_test = mean_squared_error(y_test, pred_test)

RMSE_test = np.sqrt(MSE_test)

R2_test = r2_score(y_test, pred_test)

MAE_test = mean_absolute_error(y_test, pred_test)
```
