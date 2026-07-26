---
title: Полутаролинейные формы в U
created: 2025-09-23
tags:
  - linear-algebra
links:
  - "[[Полуторалинейная форма]]"
---
**Определение:** *Полуторалинейной формой* в $U$ называется числовая функция

$$f(x,y);x,y\in U;f(x,y)\in \mathbb{C}\text{, если }\forall x,y,z\in U,\forall\lambda \in \mathbb{C}:$$
1. $f(x+y,z)=f(x,z)+f(y,z)$
2. $f(\lambda x,y)=\lambda(x,y)$
3. $f(x,y+z)=f(x,y)+f(y,z)$
4. $f(x,\lambda y)=\overline{\lambda}f(x,y)$

**Определение:** П.Ф $f(x,y)$ называется *эрмитовой*, если $\forall x,y\in U$
$$f(x,y)=\overline{f(y,x)}$$
Пусть $[a]$ - базис $U$. 
Тогда $x=[a]x_{\downarrow};y=[a]y_{\downarrow}$
$$f(x,y)=f\left( \sum_{i=1}^{n}x_{i}a_{i} ,\sum_{j=1}^{n}y_{j}a_{j}\right)=\sum_{i=1}^{n}\sum_{j=1}^{n}x_{i}\overline{y_{j}}f(a_{i},a_{j})=\sum_{i,j=1}^{n}f_{ij}x_{i}\overline{y_{j}}$$
**Определение:** $F_{a}=\|f_{ij}\|_{n\times n}=\|f(a_{i},a_{j})\|_{n\times n}$ - *матрица полуторалинейной формы $f(x,y)$* в $[a]$ 
$$x_{i}\overline{y_{j}}=x_{\downarrow}F_{a}\overline{y}_{\downarrow}$$

**Закон преобразования** $[a]\to^{T}[b]:$ $F_{a}=T^{T}F_{a}\overline{T}$ (проверить самому).

