---
title: Распределение Пуассона (Pois)
created: 2026-05-05
tags:
  - probability
links:
  - "[[Биномиальное распределение (Bin)]]"
  - "[[Дискретные случайные величины]]"
  - "[[Предельные теоремы в схеме Бернулли]]"
---
**Определение:** $\xi\thicksim\mathrm{Pois}(\lambda), \ \lambda>0$, если $\mathcal{X}_{\xi}=\mathbb{N}\cup \{ 0 \}=\{ 0;1;\dots;n;\dots \}, \ p_{k}=P(\xi=k)= \frac{\lambda^{k}}{k!}e^{ -\lambda }, \ k \in \mathbb{N}\cup \{ 0 \}$

**Замечание 1:** Распределение Пуассона является приближенно предельным для биномиального, когда $n\to \infty$ и $p\to 0$ так, что $np=\lambda=\mathrm{const}$ ($p$ - мало, $\lambda=np<10, \ n>50$).

**Замечание 2:** Закон Пуассона - закон редких событий (в частности, радиоактивный распад и т.д.)

**Контрольная нормировка:** 
$$
\sum_{k=0}^{\infty}p_{k}=\sum_{k=0}^{\infty} \frac{\lambda^{k}}{k!}e^{ -\lambda }=e^{ -\lambda }\sum_{k=0}^{\infty} \frac{\lambda^{k}}{k!}=e^{ -\lambda+\lambda }=e^{ 0 }=1
$$

$$
\varphi_{\xi}(z)\equiv\varphi(z)=\sum_{k=0}^{\infty}p_{k}z^{k}=\sum_{k=0}^{\infty} \frac{\lambda^{k}}{k!}e^{ -\lambda }z^{k}=e^{ -\lambda }\sum_{k=0}^{\infty} \frac{(\lambda z)^{k}}{k!}=e^{ -\lambda+\lambda z }=e^{ \lambda(z-1) }
$$
**Теорема:** Если $\xi\thicksim\mathrm{Pois}(\lambda), \ \lambda>0$, то $M\xi=\mathcal{D}\xi=\lambda$.
$\blacktriangleleft$
$$
\varphi_{\xi}(z)\equiv\varphi(z)=e^{ \lambda(z-1) }\implies
$$
$$
\varphi'(z)=\lambda e^{ \lambda(z-1) }, \ \varphi''(z)=\lambda^{2}e^{ \lambda(z-1) }\implies
$$
$$
\varphi'(1)=\lambda e^{ \lambda(1-1) }=\lambda=M\xi, \ \varphi''(1)= \lambda^{2}\cdot e^{ 0 }=\lambda^{2},
$$
$$
\mathcal{D}\xi=\varphi'(1)+\varphi''(1)-(\varphi'(1))^{2}=\lambda+\lambda^{2}-(\lambda)^{2}=\lambda,
$$
т.е. $M\xi=\mathcal{D}\xi=\lambda$.
$\blacktriangleright$

**Примерный вид $F_{\xi}(x)$, если $\xi\thicksim\mathrm{Pois}(\lambda), \ \lambda>0$**
![[Pasted image 20260505131537.png]]

