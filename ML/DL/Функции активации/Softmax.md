---
title: Softmax
created: 2026-07-23
tags:
  - deep_learning
links:
  - "[[Функция активации]]"
---
**Определение:** Пусть $d\in \mathbb{N}$. $A$ - $d$-мерная softmax активации, если
$$
A(x)=\left( \frac{\exp(x_{1})}{\sum_{i=1}^{d}\exp(x_{i})}, \frac{\exp(x_{2})}{\sum_{i=1}^{d}\exp(x_{i})},\dots,\frac{\exp(x_{d})}{\sum_{i=1}^{d}\exp(x_{i})} \right) 
$$

**Лемма:** Пусть $d\in \mathbb{N}$, $A=(A_{1},\dots,A_{d})$ - $d$-мерная softmax функция активации. Тогда
- $\forall x\in \mathbb{R}^{d},k\in \{ 1,2,\dots,d \} \ \ A_{k}\in(0;1]$
- $\forall x\in \mathbb{R}^{d}$
$$
\sum_{k=1}^{d}A_{k}(x)=1
$$

