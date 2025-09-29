---
title: Предствавление полуторалинейной формы в U(БФ в E)
created: 2025-09-23
tags:
  - linear-algebra
links:
  - "[[Полуторалинейные формы в U]]"
---
**Теорема 9 (О представлении полуторалинейной формы в $U$): Пусть $f(x,y)$ - ПФ в $U$(БФ в $E$).**
Тогда $\exists!A\in L(U,U) \ \ (L(E,E)):$
$$\forall x,y\in U(E) \ \ f(x,y)=(x,Ay)$$
*Док-во:* Пусть $f(x,y)$ - П.Ф. в $U$. Фиксируем $y$ $\implies f(x,y)$ - линейная форма в $U$ $\implies$
По теореме 8 $\exists!h_{y}: \ \forall x\in U \ \ f(x,y)=(x,h_{y})$ 
Т.е. $\forall y\in U \ \ \exists!h_{y}$ или мы задали оператор $A$ в $U: Ay=h_{y}$
Итак, $\exists A:U\to U:$ $\forall x,y\in U \ \ f(x,y)=(x,Ay)(*)$ 
$\forall x,y,z\in U \ \forall\lambda \in \mathbb{C}:$
1. $f(x,y+z)=(x,A(y+z))$
	$f(x,y+z)=f(x,y)+f(x,z)=(x,Ay)+(x,Az)=(x,Ay+Az)$ 
	$\forall x\in U$ по лемме о сокращения сомножителя $A(y+z)=Ay+Az$
2. $f(x,\lambda y)=(x,A(\lambda y))$
	$f(x,\lambda y)=\overline{\lambda}f(x,y)=\overline{\lambda}(x,Ay)=(x,\lambda Ay)$
	$\implies(x,\lambda Ay)=(x,A(\lambda y))\implies$ по лемме о сокращении сомножителя $\forall x\in U$ $A(\lambda y)=\lambda Ay$ 
Исходя из п.1 и 2 $A\in L(U,U)$ - линейный оператор
Пусть $\exists A' \ \forall x,y\in U; \ f(x,y)=(x,A'y)(**)$ 
Тогда $(*),(**)\implies$ $(x,Ay)=(x,A'y) \ \forall x,y\in U\implies$ по лемме о сокращении на множитель $Ay=A'y; \ \forall y\in U\implies A=A'$ по определению операторов. $\implies !A$ 
