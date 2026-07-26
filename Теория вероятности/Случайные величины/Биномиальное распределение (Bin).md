---
title: Биномиальное распределение (Bin)
created: 2026-05-04
tags:
  - probability
links:
  - "[[Дискретные случайные величины]]"
  - "[[Распределение Бернулли (Be)]]"
  - "[[Повторение независимых испытаний. Схема Бернулли]]"
---
**Определение:** $\xi\thicksim\mathrm{Bin}(n,p), \ n\in \mathbb{N}, p\in(0,1)$, если $\mathcal{X}_{\xi}=\{ 0;1;\dots;n \}$, $p_{k}=P(\xi=k)=C_{n}^{k}p^{k}q^{n-k}, \ q=1-p, k=\overline{0,n}$.

**Замечание 1:** Если $\xi\thicksim\mathrm{Bin}(n,p)$, то $\xi$ - число "успехов" в $n$ испытаниях Бернулли и вероятностью успеха $p$ в одном опыте.
**Замечание 2:** $\mathrm{Bin}(1,p)=\mathrm{Be}(p)$.

**Закон распределения:**

| $\xi:$ | $0$     | $1$     | $2$     | $\dots$ | $n$     |
| ------ | ------- | ------- | ------- | ------- | ------- |
| $P:$   | $p_{0}$ | $p_{1}$ | $p_{2}$ | $\dots$ | $p_{n}$ |
$$
\varphi_{\xi}(z)\equiv\varphi(z)=\sum_{k=0}^{n}p_{k}z^{k}=\sum_{k=0}^{n}C_{n}^{k}p^{k}q^{n-k}z^{k}=\sum_{k=0}^{n}C_{n}^{k}(pz)^{k}q^{n-k}=(pz+q)^{n}\text{ - бином Ньютона}
$$
$$
\varphi_{\xi}(z)\equiv\varphi(z)=(pz+q)^{n}
$$
$$
\varphi'(z)=np(pz+q)^{n-1}
$$
$$
\varphi''(z)=n(n-1)p^{2}(pz+q)^{n-2}
$$
$$
M\xi=\varphi'(1)=np(p+q)^{n-1}=np
$$
$$
\mathcal{D}\xi=\varphi''(1)+\varphi'(1)-(\varphi'(1))^{2}=n(n-1)p^{2}(p+q)^{n-2}+np(p+q)^{n-1}-(np(p+q)^{n-1})^{2}=
$$
$$
=n(n-1)p^{2}+np-n^{2}p^{2}=n^{2}p^{2}-np^{2}+np-n^{2}p^{2}=np-np^{2}=np(1-p)=npq
$$
**Итог:** Если $\xi\thicksim\mathrm{Bin}(n,p), \ n\in \mathbb{N}, \ p\in(0,1)$, то $M\xi=np, \ \mathcal{D}\xi=npq$.

**Утверждение:** Пусть $\xi_{i}\thicksim\mathrm{Be}(p), \ p\in(0,1), \ i=\overline{1,n}$ причем д.с.в $\xi_{1},\xi_{2},\dots,\xi_{n}$ независимы в совокупности. Тогда д.с.в $\xi=\xi_{1}+\xi_{2}+\dots+\xi_{n}=\sum_{k=1}^{n}\xi_{i}\thicksim\mathrm{Bin}(n,p)$.