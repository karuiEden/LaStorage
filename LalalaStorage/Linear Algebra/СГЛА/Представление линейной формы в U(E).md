---
title: Представление линейной формы в U(E)
created: 2025-09-23
tags:
  - linear-algebra
links:
---
**Определение:** $f(x);x\in V(\text{л.п.});f(x)\in \mathbb{C}(\mathbb{R})$ - линейная форма(функционал)
*Аксиомы:* $\forall x,y\in V,\forall\lambda \in \mathbb{C}(\mathbb{R})$:
1. $f(x+y)=f(x)+f(y)$
2. $f(\lambda x)=\lambda f(x)$

**Лемма (О сокращении на сомножитель в скалярном произведении):** 
Пусть $a,b\in U(E)$ и $\forall x\in U(E)$: $(x,a)=(x,b)$.
Тогда $a=b$.
*Док-во:* $\forall x\in U(E):(x,a)-(x,b)=0\implies(x,a-b)=0 \text{ для }x=a-b$
$$(x,a-b)=(a-b,a-b)=0\implies a-b=\theta\implies a=b$$

**Теорема 8 (О представлении линейной формы в $U(E)$):** 
Пусть $f(x)$ - линейная форма в $U(E)$. Тогда $\exists!h\in U(E):$
$$\forall x\in U(E) \ \ \ f(x)=(x,h)$$
*Док-во:* Пусть $\dim U=n\in \mathbb{N}$. Тогда $\exists$ОНБ $U  \ \ [e]$ 
$\forall x\in U \ \ \ x=[e]x_{\downarrow}=\sum_{i=1}^{n}x_{i}e_{i}$
$$f(x)=f\left( \sum_{i=1}^{n}x_{i}e_{i} \right)=\sum_{i=1}^{n}x_{i}f(e_{i})(=\overline{\eta_{i}})=\sum_{i=1}^{n}x_{i}\overline{\eta_{i}}$$
, где $\eta_{i}=\overline{f(e_{i})}$ 
Рассмотрим $h=[e]\eta_{\downarrow}=\sum_{i=1}^{n}\eta_{i}e_{i}$
$[e]$ - ОНБ $\implies \sum_{i=1}^{n}x_{i}\overline{\eta}_{i}=(x,h)$
Т.е. $\exists! h\in U \ \ \ \forall x \ \ f(x)=(x,h)$
Пусть $\exists h'\in U:f(x)=(x,h') \ \forall x\in U$
Тогда $\forall x\in U \ \ \ (x,h)=(x,h')\implies h=h'\implies !h$ 

$f(x)=(\theta,\theta(=\exists!h))$ для $\dim U=0$