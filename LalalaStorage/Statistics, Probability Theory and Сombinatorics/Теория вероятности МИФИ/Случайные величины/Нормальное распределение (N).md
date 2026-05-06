---
title: Нормальное распределение (N) (Гауссово распределение)
created: 2026-05-06
tags:
  - probability
links:
  - "[[Понятие случайной величины]]"
---
**Определение:** $\xi\thicksim\mathrm{N}(\mu,\sigma^{2}), \ \mu \in \mathbb{R}, \sigma>0$, если $\mathcal{X}_{\xi}=\mathbb{R}$ и 
$$
f_{\xi}(x)\equiv f(x)= \frac{1}{\sigma \sqrt{ 2\pi }}e^{ - \frac{(x-\mu)^{2}}{2\sigma^{2}} }
$$

![[Pasted image 20260506131240.png]]


**Напоминание:** 
$$
\int_{-\infty}^{+\infty}e^{ -x^{2} }\,dx=\sqrt{ \pi }
$$

**Замечание:** Если $\xi\thicksim\mathrm{N}(0,1)$, то *стандартное нормальное распределение*, у него 
$$
f_{\xi}(x)\equiv f(x)= \frac{1}{\sqrt{ 2\pi }}e^{ -\frac{x^{2}}{2} }=\varphi(x)\text{ - функция Гаусса}
$$

**Теорема:** Если $\xi\thicksim\mathrm{N}(\mu,\sigma^{2}), \ \mu \in \mathbb{R},\sigma>0$, то $M\xi=\mu,\ \mathcal{D}\xi=\sigma^{2}$.
$\blacktriangleleft$
$$
M\xi=\int_{-\infty}^{+\infty}xf(x)\,dx= \frac{1}{\sigma \sqrt{ 2\pi }}\int_{-\infty}^{+\infty}xe^{ -\frac{(x-\mu)^{2}}{2\sigma^{2}} }\,dx=\begin{vmatrix}
t= \frac{x-\mu}{\sigma \sqrt{ 2 }} \\
x=\sigma \sqrt{ 2 }t+\mu \\
dx=\sigma \sqrt{ 2 }\,dt
\end{vmatrix}= \frac{\sigma \sqrt{ 2 }}{\sigma \sqrt{ 2\pi }}\int_{-\infty }^{+\infty}(\sigma \sqrt{ 2 }t+\mu)e^{ -t^{2} }\,dt
$$
$$
= \frac{1}{\sqrt{ \pi }} \sigma \sqrt{ 2 }\underbrace{\int_{-\infty}^{+\infty}te^{ -t^{2} }\,dt}_{0\text{ (нечетная функция)}}+ \frac{\mu}{\sqrt{ \pi }}\underbrace{\int_{-\infty}^{+\infty}e^{ -t^{2} }\,dt}_{\sqrt{ \pi }}= \frac{\mu \sqrt{ \pi }}{\sqrt{ \pi }}=\mu
$$
$$
\mathcal{D}\xi=\int_{-\infty}^{+\infty}(x-M\xi)^{2}f(x)\,dx= \frac{1}{\sigma \sqrt{ 2\pi }}\int_{-\infty}^{+\infty}(x-\mu)^{2}e^{ - \frac{(x-\mu)^{2}}{2\sigma^{2}} }\,dx=
$$
$$
=\begin{vmatrix}
t=  \frac{x-\mu}{\sigma}, \ x-\mu=\sigma t \\
dx=\sigma\,dt
\end{vmatrix}= \frac{1}{\sigma \sqrt{ 2\pi }}\sigma \int_{-\infty}^{+\infty}\sigma^{2}t^{2}e^{  -\frac{t^{2}}{2} }\,dt= \frac{\sigma^{2}}{\sqrt{ 2\pi }}\underbrace{\int_{-\infty}^{+\infty}t^{2} e^{ - \frac{t^{2}}{2} }\,dt}_{\begin{array}
 \\
\text{четная функция} \\
\text{в симметричных пределах}
\end{array}}=
$$
$$
=  \frac{2\sigma^{2}}{\sqrt{ 2\pi }}\int_{0}^{+\infty}t^{2} e^{ -\frac{t^{2}}{2} }\,dt=\begin{vmatrix}
u= \frac{t^{2}}{2}, \ t^{2}=2u \\
t=\sqrt{ 2u }\implies dt= \frac{\sqrt{ 2 }\,du}{2\sqrt{ u }} \\
u_{1}=0, \ u_{2}=+\infty
\end{vmatrix}= \frac{2\sigma^{2}}{\sqrt{ 2\pi }}\int_{0}^{+\infty}2u\cdot e^{ -u }\cdot \sqrt{ 2 }\cdot \frac{du}{2\sqrt{ u }}=
$$
$$
= \frac{2\sigma^{2}}{\sqrt{\pi }}\int_{0}^{+\infty}\sqrt{ u }e^{ -u }\,du= \frac{2\sigma^{2}}{\sqrt{ \pi }}\int_{0}^{+\infty}u^{\frac{3}{2}-1}e^{ -u }\,du=
$$
$$
=\begin{pmatrix}
\text{напоминание: } \Gamma(p) =\int_{0}^{+\infty}x^{p-1}e^{ -x }\,dx, \ p>0, \\
\Gamma(p+1)=p\Gamma(p), \Gamma\left( \frac{1}{2} \right)=\sqrt{ \pi }
\end{pmatrix}=
$$
$$
= \frac{2\sigma^{2}}{\sqrt{ \pi }}\Gamma\left( \frac{3}{2} \right) = \frac{2\sigma^{2}}{\sqrt{ \pi }}\Gamma\left( \frac{1}{2} +  1\right)= \frac{2\sigma^{2}}{2\sqrt{ \pi }}\Gamma\left( \frac{1}{2} \right)= \frac{\sigma^{2}}{\sqrt{ \pi }}\cdot \sqrt{ \pi }=\sigma^{2}.
$$
**Итог:** $M\xi=\mu, \ \mathcal{D}\xi=\sigma^{2}$.
$\blacktriangleright$

**Теорема:** Если $\xi\thicksim\mathrm{N}(\mu,\sigma^{2}), \ \mu \in \mathbb{R}, \sigma >0$, то  $P(\xi \in \lfloor a,b \rceil)=\Phi_{0}\left(  \frac{b-\mu}{\sigma}  \right)-\Phi_{0}\left( \frac{a-\mu}{\sigma} \right)$
$\blacktriangleleft$
$$
P(\xi \in \lfloor a,b \rceil)=\int_{a}^{b}f(x)\,dx= \frac{1}{\sigma \sqrt{ 2\pi }}\int_{a}^{b} e^{ - \frac{(x-\mu)^{2}}{2\sigma^{2}} }\,dx=\begin{vmatrix}
t= \frac{x-\mu}{\sigma} \\
x=\sigma t+\mu \\
dx=\sigma\,dt \\
t_{1} = \frac{a-\mu}{\sigma} \\
t_{2}= \frac{b-\mu}{\sigma}
\end{vmatrix}= \frac{1}{\sigma \sqrt{ 2\pi }}\sigma \int_{\frac{a-\mu}{\sigma}}^{\frac{b-\mu}{\sigma}}e^{ - \frac{t^{2}}{2} }\,dt= 
$$
$$
= \int_{\frac{a-\mu}{\sigma}}^{ \frac{b-\mu}{\sigma}} \underbrace{\frac{1}{\sqrt{ 2\pi }}e^{ \frac{-t^{2}}{2} }}_{\varphi(t)}\,dt=\Phi_{0}\left(  \frac{b-\mu}{\sigma}  \right)- \Phi_{0}\left(  \frac{a-\mu}{\sigma}  \right),
$$
где $\Phi_{0}(x)=\int_{0}^{x}\varphi(t)\,dt, \ \Phi_{0}(\pm \infty)=\pm 0.5, \ \Phi_{0}(-x)=-\Phi_{0}(x)$
$\blacktriangleright$

**Функция нормального распределения:** $\xi\thicksim N(\mu,\sigma^{2}) ,F_{\xi}(x)=F(x)=P(\xi<x)=P(\xi \in(-\infty;x))=\Phi_{0}\left(  \frac{x-\mu}{\sigma}  \right) -\Phi_{0}\left(-\infty\right)=\Phi_{0}\left(  \frac{b-\mu}{\sigma}  \right) +0.5=\Phi\left( \frac{x-\mu}{\sigma} \right)$ 
![[Pasted image 20260421125910.png|518]]

### "Правило трёх сигм"

Пусть $\xi\thicksim N(\mu,\sigma^{2})$. Найдем $P(|\xi-\mu|<3\sigma):$
$$
|\xi-\mu|<3\sigma\Leftrightarrow -3\sigma<\xi-\mu<3\sigma\Leftrightarrow \mu-3\sigma<\xi<\mu+3\sigma\Leftrightarrow \xi \in(\mu-3\sigma ;\mu+3\sigma)\implies
$$
$$
\implies P(|\xi-\mu|<3\sigma)=P(\xi \in(\mu-3\sigma;\mu+3\sigma))=\Phi_{0}\left(  \frac{\mu+3\sigma-\mu}{\sigma}  \right)- \Phi_{0}\left(  \frac{\mu-3\sigma-\mu}{\sigma}  \right)=
$$
$$
=\Phi_{0}(3)-\Phi_{0}(-3)=2\Phi_{0}(3)\approx0.9973
$$
**Вывод:** $\{ |\xi-\mu|<3\sigma \}$ - практически достоверное событие

![[Pasted image 20260421130505.png|602]]
