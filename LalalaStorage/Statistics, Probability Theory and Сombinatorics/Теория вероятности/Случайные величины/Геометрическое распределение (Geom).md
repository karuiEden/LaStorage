---
title: Геометрическое распределение (Gem)
created: 2026-05-05
tags:
  - probability
links:
  - "[[Дискретные случайные величины]]"
  - "[[Повторение независимых испытаний. Схема Бернулли]]"
---
**Определение:** $\xi\thicksim\mathrm{Geom}(p), \ p\in(0;1)$, если $\mathcal{X}_{\xi}=\mathbb{N}=\{ 1;2;\dots;n;\dots \}$, если $p_{k}=P(\xi=k)=q^{k-1}\cdot p, \ k\in \mathbb{N}, \ q=1-p$.

**Замечание:** $\xi\thicksim\mathrm{Geom}(p)$, если $\xi$ - число опытов в схеме Бернулли, проведенных до первого "успеха", включая сам опыт с "успехом", $p$ - вероятность "успеха" в одном опыте.


| $\xi:$ | $1(=x_{1})$ | $2(=x_{2})$  | $3(=x_{3})$      | $\dots$ | $n(=x_{n})$      | $\dots$ |
| ------ | ----------- | ------------ | ---------------- | ------- | ---------------- | ------- |
| $P:$   | $p(=p_{1})$ | $qp(=p_{2})$ | $q^{2}p(=p_{3})$ | $\dots$ | $q^{n}p(=p_{n})$ | $\dots$ |

**Доопределение:** $\xi=0(=x_{0})$ с вероятностью $p_{0}=0$.

$$
\varphi_{\xi}(z)\equiv\varphi(z)=\sum_{k=0}^{\infty}p_{k}z^{k}=\sum_{k=1}^{\infty}pq^{k-1}z^{k}=pz\sum_{k=1}^{\infty}(qz)^{k-1}=pz\sum_{k=0}^{\infty}(qz)^{k}=
$$
$$
\underset{\left(\begin{array} \\ |z|\leq 1\text{ и }q\in(0;1)\implies \\
|qz|<1\implies \\
\text{ряд сходится}\end{array}\right)}{=}  pz\cdot \frac{1}{1-qz}= \frac{pz}{1-qz},
$$
т.е. $\varphi_{\xi}(z)\equiv\varphi(z)= \frac{pz}{1-qz}$.

**Контроль нормировки:**
$$
\sum_{k=0}^{\infty}p_{k}=\sum_{k=1}^{\infty}p_{k}=\sum_{k=1}^{\infty}pq^{k-1}=p\sum_{k=0}^{\infty}q^{k}= \frac{p}{1-q}= \frac{p}{p}=1\text{ - выполнено}
$$

**Теорема:** Если $\xi\thicksim\mathrm{Geom}(p), \ p\in(0;1), \ q=1-p$, то $M\xi= \frac{1}{p}, \ \mathcal{D}\xi= \frac{q}{p^{2}}$.
$\blacktriangleleft$
$$
\varphi(z)= \frac{pz}{1-qz}\implies
$$
$$
\varphi'(z)= \frac{p(1-qz)+qpz}{(1-qz)^{2}}= \frac{p-pqz+qpz}{(1-qz)^{2}}=\frac{p}{(1-qz)^{2}},
$$
$$
\varphi''(z)=\frac{2pq}{(1-qz)^3}
$$
$$
\varphi'(1)=\frac{p}{(1-q)^{2}}=\frac{p}{p^{2}}=\frac{1}{p}=M\xi
$$
$$
\varphi''(1)= \frac{2pq}{(1-q)^{3}}=\frac{2pq}{p^{3}}=\frac{2q}{p^{2}}
$$
$$
\mathcal{D}\xi=\varphi''(1)+\varphi'(1)-(\varphi'(1))^{2}= \frac{2q}{p^{2}}+\frac{1}{p}- \left( \frac{1}{p} \right)^{2}=\frac{2q-1+p}{p^{2}}=\frac{2q-q}{p^{2}}=\frac{q}{p^{2}}=\mathcal{D}\xi,
$$
т.е. $M\xi=\frac{1}{p}, \ \mathcal{D}\xi= \frac{q}{p^{2}}$.
$\blacktriangleright$
