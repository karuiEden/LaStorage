---
title: Дисперсия дискретной случайной величины xi
created: 2026-05-04
tags:
  - probability
links:
---
**Определение:** *Дисперсией* $\mathcal{D}\xi$ дискретной случайной величины $\xi$ с $\mathcal{X}_{\xi}=\{ x_{i} \}$ называется 
$$
\mathcal{D}\xi\overset{\text{def}}{=} \mu_{2}=M((\xi-M\xi)^{2})=M(\overset{\circ}{\xi}^{2})=\sum_{i}(x_{i}-M\xi)^{2}p_{i}
$$
**Замечание:** Всегда $\mathcal{D}\xi\geq0$.

**Определение:** $\sigma_{\xi}\overset{\text{def}}{=}\sqrt{ \mathcal{D}\xi }$ - среднее квадратическое отклонение.

**Замечание:** В иностранной литературе $\mathrm{Var}(\xi)$ - обозначение дисперсии.

**Теорема:** Если $\exists \nu_{2}=M(\xi^{2})$ и $\exists \nu_{1}=M\xi$, то
$$
\exists\mathcal{D}\xi=M(\xi^{2})-(M\xi)^{2}=\nu_{2}-\nu_{1}^{2}.
$$
$\blacktriangleleft$
$$
\mathcal{D}\xi=M((\xi-M\xi)^{2})=M(\xi^{2}-2\xi\cdot M\xi+(M\xi)^{2})=M(\xi^{2})-M(2\xi\cdot M\xi)+M((M\xi)^{2})=
$$
$$
=\nu_{2}-2\cdot \nu_{1}\cdot \nu_{1}+\nu_{1}^{2}=\nu_{2}-\nu_{1}^{2}
$$
$\blacktriangleright$

**Свойства дисперсии:** 
1. $\forall c\in \mathbb{R}\implies \mathcal{D}c=0$;
$1^{0}$. $\mathcal{D}\xi=0\Leftrightarrow\xi=c=\mathrm{const}$
$\blacktriangleleft$
$\xi$ - дискретная случайная величина $\mathcal{D}\xi=\sum_{i}(x_{i}-M\xi)^{2}p_{i}=0\Leftrightarrow x_{i}-M\xi=0$, так как $p_{i}>0$, если $p_{i}=0$, то $x_{i}\not\in \mathcal{X}_{\xi}$ $\Leftrightarrow x_{i}=M\xi \ \forall i$
Пусть $M\xi=c\in \mathbb{R}\implies x_{i}=c\ \forall i$, т.е. $\mathcal{X}_{\xi}=\{ c \}\implies \xi=c=\text{const}$, т.е. $\xi$ принимает только одно значение.
$\blacktriangleright$
2. $\forall c\in \mathbb{R}\implies \mathcal{D}(c\xi)=c^{2}\mathcal{D}\xi$.
3. Если $\xi$ и $\eta$ *независимы*, то $\mathcal{D}(\xi+\eta)=\mathcal{D}\xi+\mathcal{D}\eta$
$3^{0}$. Если $\xi_{1},\dots,\xi_{n}$ попарно независимы, то $\mathcal{D}\left( \sum_{i=1}^{n}\xi_{i} \right)=\sum_{i=1}^{n}\mathcal{D}\xi_{i}$;
4. $\forall c\in \mathbb{R}\implies \mathcal{D}(\xi+c)=\mathcal{D}\xi$
5. Если $\xi$ и $\eta$ независимы, то $\mathcal{D}(\xi\cdot \eta)=M(\xi^{2})\cdot M(\eta^{2})-(M\xi)^{2}(M\eta)^{2}$