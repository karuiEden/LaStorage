---
title: Гипергеометрическое распределение (HGeom)
created: 2026-05-05
tags:
  - probability
links:
  - "[[Геометрическое распределение (Geom)]]"
---
**Определение:** $\xi\thicksim\mathrm{HGeom}(N,M,n)$, где $N,M\in \mathbb{N}:$ $M\leq N,n\leq N,$ если $\mathcal{X}_{\xi}=\{ 0;1;2;\dots;k;\dots;\min(n,M) \},$ $p_{k}=P(\xi=k)= \frac{C_{M}^{k}\cdot C_{N-M}^{n-k}}{C_{N}^{n}}, \ k=\overline{0,\min(n,M)}$ .

**Применение:** Случаи, подобные следующему: в урне $N$ шаров, из них $M$ белых и $(N-M)$ черных шаров; из урны выбирается $n$ шаров. Требуется найти вероятность того, что среди извлеченных шаров будет ровно $m$ белых шаров (остальные черные).

с.в. $\xi$ - число белых шаров среди извлеченных из урны $\implies$ $\xi\thicksim\mathrm{HGeom}(N,M,n)$.

**Теорема:** (Без док-ва) Если $\xi\thicksim\mathrm{HGeom}(N,M,n),$ где $N,M\in \mathbb{N}: \ M\leq N, n\leq N$, то 
$$
M\xi= \frac{nM}{N}, \ \mathcal{D}\xi= \frac{nM}{N-1}\cdot \frac{(N-M)\cdot(N-n)}{N^{2}}.
$$
