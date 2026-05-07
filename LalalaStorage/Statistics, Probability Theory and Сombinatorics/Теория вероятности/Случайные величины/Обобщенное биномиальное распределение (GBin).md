---
title: Обобщенное биномиальное распределение (GBin)
created: 2026-05-04
tags:
  - probability
links:
  - "[[Биномиальное распределение (Bin)]]"
  - "[[Дискретные случайные величины]]"
---
**Определение:** $\xi\thicksim\mathrm{GBin}(n,p_{1},\dots,p_{n}), \ n\in \mathbb{N}, p_{i}\in(0,1), \ i=\overline{1,n}$, если $\xi\overset{\text{def}}{=}\xi_{1}+\xi_{2}+\dots+\xi_{n}=\sum_{i=1}^{n}\xi_{i}$, где $\xi_{i}\thicksim\mathrm{Be}(p_{i}), \ i=\overline{1,n}$, причем д.с.в. $\xi_{1},\dots,\xi_{n}$ независимы в совокупности.

**Замечание:** Если $\xi\thicksim\mathrm{GBin}(n,p_{1},\dots,p_{n})$, то $\xi$ - число "успехов" в независимых опытах и вероятностью "успеха" в $i$-ом опыте ($i=\overline{1,n}$) (Обобщенная схема Бернулли)

**Следствие:** $M\xi=M\left( \sum_{i=1}^{n}\xi_{i} \right)=\sum_{i=1}^{n}M\xi_{i}=\sum_{i=1}^{n}p_{i}$, $\mathcal{D}\xi=\mathcal{D}\left( \sum_{i=1}^{n} \right)=\sum_{i=1}^{n}\mathcal{D}\xi_{i}=\sum_{i=1}^{n}p_{i}q_{i}$

**Утверждение:** Пусть $\mathcal{X}_{\xi_{i}}\subset \mathbb{N}\cup \{ 0 \}, \ i=\overline{1,n}$, д.с.в., $\xi_{1},\dots,\xi_{n}$, независимы в совокупности, $\xi=\sum_{i=1}^{n}\xi_{i}$. Тогда
$$
\varphi_{\xi}(z)=\varphi_{\xi_{1}}(z)\cdot\dots\cdot\varphi_{\xi_{n}}(z)=\prod_{i=1}^{n}\varphi_{\xi_{i}}(z).
$$

**Следствие:** Если $\xi\thicksim\mathrm{GBin}(n,p_{1},\dots,p_{n})$, то $\varphi_{\xi}(z)=(q_{1}+p_{1}z)\cdot\dots\cdot(q_{n}+p_{n}z)=\prod_{i=1}^{n}(q_{i}+p_{i}z), \ \xi_{i}\thicksim\mathrm{Be}(p_{i}), \ i=\overline{1,n}$.

Закон распределения:

| $\xi:$ | $0$           | $1$           | $\dots$ | $n$           |
| ------ | ------------- | ------------- | ------- | ------------- |
| $P:$   | $\hat{p}_{0}$ | $\hat{p}_{1}$ | $\dots$ | $\hat{p}_{n}$ |
$\hat{p}_{k}=P(\xi=k), \ k=\overline{0,n}$.

Вероятности $\hat{p}_{k}$ находятся с помощью $\varphi_{\xi}(z):$
$$
\varphi_{\xi}(z)=\prod_{i=1}^{n}(q_{i}+p_{i}z)\underset{\text{раскрытие скобок}}{=}\sum_{k=0}^{n}\hat{p}_{k}z^{k}
$$