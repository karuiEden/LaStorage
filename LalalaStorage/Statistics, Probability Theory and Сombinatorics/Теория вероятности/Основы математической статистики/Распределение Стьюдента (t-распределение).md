---
title: Распределение Стьюдента (t-распределение)
created: 2026-06-28
tags:
  - statistics
links:
---
**Определение:** с.в. $\tau\thicksim t(n), \ n\in \mathbb{N}$ (распределение Стьюдента с $n$ степенями свободы), если 
$$
\tau= \frac{\eta}{\sqrt{ \frac{\xi}{n} }},
$$
где $\eta\thicksim\mathrm{N}(0;1), \ \xi\thicksim\mathcal{X}^{2}(n)$, $\xi$ и $\eta$ независимы.

**Замечание 1:** 
$$
f_{\tau}(t)= \frac{\Gamma\left(  \frac{n+1}{2}  \right)}{\Gamma\left( \frac{n}{2} \right)\sqrt{ \pi n }} \left( 1+ \frac{x^{2}}{n} \right)^{- \frac{n+1}{2}}, \ x\in \mathbb{R}
$$
![[Pasted image 20260628093731.png]]

**Замечание 2:** $M\tau=0, \ \mathcal{D}\tau= \dfrac{n}{n-2}, \ n\in \mathbb{N}, n>2$.

**Замечание 3:** $\tau \overset{d}{\underset{n\to \infty}{\longrightarrow}}\eta, \ \eta\thicksim\mathrm{N}(0;1)$.
При $n>30$ $t(n)\approx \mathrm{N}(0;1)$ (распределение почти совпадает с нормальным).

