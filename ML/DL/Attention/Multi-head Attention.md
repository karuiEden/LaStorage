---
title: Multi-head Attention
created: 2026-10-12
tags:
  - ml
  - deep_learning
  - attention
links:
  - "[[Attention]]"
  - "[[Масштабированный attention через скалярное произведение]]"
---
Отличие от обычного self-attention состоит в том, что используется линейное проецирование запросов, ключей и значений $h$ раз с помощью различных обученных линейных проекций на измерения $d_{k},d_{k}$ и $d_{v}$ соответственно. На каждую проекцию действуют attention параллельно, получая $d_{v}$-мерный результат. Затем они конкетируются и еще раз проецируются, что дает окончательные значения.

Multi-head attention позволяет модели совместно обрабатывать информацию из разных подпространств представления в разных позициях. При single head attention усреднение препятствует этому.

$$
\mathrm{MultiHead}(Q,K,V)=\mathrm{Concat}(\mathrm{head}_{1},\mathrm{head}_{2},\dots,\mathrm{head}_{h})W^{O},
$$
$$
\text{где } \mathrm{head}_{i}=\mathrm{Attention}(QW_{i}^{Q},KW^{K}_{i},VW^{V}_{i}) 
$$

Где проекции - матрицы параметров $W^{Q}_{i}\in \mathbb{R}^{d_{model}\times d_{k}},W^{K}_{i}\in \mathbb{R}^{d_{model}\times d_{k}}$, $W^{V}_{i}\in \mathbb{R}^{d_{model}\times d_{v}}$ и $W^{O}\in \mathbb{R}^{hd_{v}\times d_{model}}$. 

![[ModalNet-20.png|554]]


Реализация на TenserFlow:

```python
def MultiheadAttention(x, M, P_q, P_k, P_v, P_o):
"""
	Multi−head Attention on one query.
	Args:  
		x: a vector with shape [d]
		M: a matrix with shape [m, d]
		P_q: a tensor with shape [h, d, k]
		P_k: a tensor with shape [h, d, k]
		P_v: a tensor with shape [h, d, v]
		P_o: a tensor with shape [h , d , v] 
	Returns:  
		y: a vector with shape [d] 
""" 
	q = tf.einsum ("d , hdk−>hk", x, P_q)
	K = tf.einsum("md, hdk−>hmk", M, P_k) 
	V = tf.einsum("md, hdv−>hmv" , M, P_v)
	logits = tf.einsum ("hk, hmk−>hm", q , K)
	weights = tf.softmax(logits) 
	o = tf.einsum("hm, hmv−>hv", weights, V) 
	y = tf.einsum("hv, hdv−>d", o, P_o) 
	return y
```

