---
title: Ортогональное дополнение подпространства
created: 2025-09-16
tags:
  - linear-algebra
links:
  - "[[Определение унитарного(евклидова) пространства]]"
  - "[[Прямая сумма подпространств]]"
---
$U_{1}$ - подпространство $U$ 
**Определение:** $x$ ортогонален $U_{1}$, если $x\perp y \ \ \forall y\in U_{1}$
**Обозначение:** $x\perp U_{1}$

**Определение:** $U_{1},U_{2}$ - подпространства $U$.
$U_{1},U_{2}$ - ортогональны, если $\forall x\in U_{1}, \ \forall y\in U_{2}:x\perp y$
**Обозначение:** $U_{1}\perp U_{2}$

**Лемма 1**: $U_{1}\perp U_{2}\implies U_{1}\cap U_{2}=\{ \varnothing \}$ 
*Док-во:* $\forall z\in U_{1}\cap U_{2}\implies z\in U_{1} \wedge z\in U_{2}\implies z\perp z\implies(z,z)=0\implies z=\theta$ 

**Определение:** *Ортогональное дополнение* $U_{1}$:
	$U_{1}^{\perp}=\{ x\in U\ | \ x\perp U_{1} \}$.
*Свойства:* ^11806d
1. $U_{1}^{\perp}$ - подпространство $U$
	*Док-во:* $\theta \in U_{1}^{\perp}\implies U_{1}^{\perp}\neq\theta$
	1. $\forall x',x''\in U_{1}^{\perp} \ \ \forall y\in U_{1}:(x'+x'',y)=(x',y)+(x'',y)=0+0=0\implies x'+x''\in U_{1}^{\perp}$
	2. $\forall x\in U_{1}^{\perp} \ \ \forall\lambda \ \ \forall y\in U_{1}: \  \ (\lambda x,y)=\lambda(x,y)=\lambda\cdot 0=0\implies\lambda x\in U_{1}^{\perp}$
2. $U_{1}\perp U_{1}^{\perp}$ (см. определение [[#^11806d|ортогонального дополнения]])
3. $(U_{1}^{\perp})^{\perp}=U_{1}$
	*Док-во:* самостоятельно, см [[#^6b6dcf|теорему 5]]

**Лемма 2:** $U_{1}=L(a_{1},\dots,a_{k})$.
$x\in U_{1}^{\perp}\Leftrightarrow x\perp a_{i}, \ \ i=\overline{1,k}$  ^50786b

*Док-во:* $\Longrightarrow$ $x\in U_{1}^{\perp}\implies x\perp y \ \forall y\in U_{1}\implies x\perp a_{i}(\in U_{1}), \ i=\overline{1,k}$
$\Longleftarrow$) $\forall y\in U_{1}:y=\sum_{i=1}^{k}\alpha_{i}a_{i}$ 
$$(x,y)=\sum_{i=1}^{k} \overline{\alpha}_{i}(x,a_{i})=0\implies x\perp y\implies x\perp U_{1}\implies x\in U_{1}^{\perp}$$

**Теорема 5:** $U$ - конечномерное, $U_{1}$- подпространство $U$. Тогда $$U=U_{1}\oplus U_{1}^{\perp}$$ ^6b6dcf

*Док-во:* Пусть $\dim U_{1}=k \neq 0$. Тогда по [[Ортогональность векторов. Метрические понятия В U(E). Ортонормированные системы и базисы#^38a0b4|теореме 3]] $\implies \exists e_{1},\dots,e_{k}$ - ОНБ
$$\forall x\in U \ \ \ z=x-(x,e_{1})e_{1}-\dots-(x,e_{k})e_{k}=x-(\sum_{i=1}^{k}(x,e_{i})e_{i})(=y\in U_{1})$$
$$(z,e_{j})=\left( x- \sum_{i=1}^{k}(x,e_{i})e_{i},e_{j} \right)=(x,e_{j})-\sum_{i=1}^{k}(x,e_{i})(e_{i},e_{j})(=\delta_{ij})=$$
$$=(x,e_{j})-(x,e_{j})\cdot1=0$$
Так как $U_{1}=L(e_{1},\dots,e_{k})$ по [[#^50786b|лемме 2]] $\implies z\in U_{1}^{\perp}$. 
Итого $\forall x\in U \ \  \ x = z + y$, где $z\in U_{1}^{\perp,}\ y\in U_{1}\implies U=U_{1}+U_{1}^{\perp}$
$U_{1}\perp U_{1}^{\perp}$ по лемме 1 $\implies U_{1} \cap U_{1}^{\perp}=\{ \theta \}$
Следовательно, $U=U_{1}\oplus U_{1}^{\perp}$

**Замечание:** Если $U_{1}=\{ \theta \}$, то $U_{1}^{\perp}=U\implies U=U\oplus \{ \theta \}$

**Замечание:** $\forall x\in U \ \ \ \exists!y\in U_{1},z\in U_{1}^{\perp}:$
$$x=y+z$$

**Определение:** Элемент $y\in U_{1}$ - ортогональная проекция $x$ на $U_{1}$.

**Определение:** $z\in U_{1}^{\perp}$ - ортогональная составляющая $x$ относительно $U_{1}$.


![[Pasted image 20250916134840.png]]

**Замечание:** $y=\sum_{i=1}^{k}(x,e_{i})e_{i}$, где $e_{1},\dots,e_{k}$ - ОНБ $U_{1}$ 

**Замечание 1:** *Задача* $\text{dist}(x_{0},U_{1})=\inf_{y\in U_{1}}\rho(x_{0},y)=\|z\|$
Ответ $\|z\|$ (проверить)

**Замечание 2:** *Задача* в $E$ 
Пусть $x_{0}=y_{0}+z_{0},  y_{0}\neq 0$
$$\sup_{y\in E_{1}, y\neq 0} \frac{(x_{0},y)}{\|x_{0}\|\|y\|}= \frac{(x_{0},y_{0})}{\|x_{0}\|\|y_{0}\|}$$
$$\widehat{x_{0},E_{1}}=\arccos\left(  \frac{(x_{0},y_{0})}{\|x_{0}\|\|y_{0}\|}  \right)$$
(проверить)

**Замечание 3:** $\|g_{1}\|\cdot\|g_{2}\|\cdot\dots\cdot\|g_{n}\|=V$ $n$-мерного паралипипеда  на векторах $f_{1},\dots,f_{k}$

