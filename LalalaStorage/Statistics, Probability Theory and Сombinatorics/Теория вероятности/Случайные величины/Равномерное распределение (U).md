---
title: Равномерное распределение (U)
created: 2026-05-06
tags:
  - probability
links:
  - "[[Понятие случайной величины]]"
  - "[[Геометрическая вероятность]]"
---
**Определение:** $\xi\thicksim \mathrm{U}[a,b], \ a,b\in \mathbb{R}$, если $\mathcal{X}_{\xi}=[a,b]$ и $f_{\xi}(x)\equiv f(x)=\begin{cases} \frac{1}{b-a},&x \in[a,b] \\ 0,&x\not\in[a,b] \end{cases}$
![[Pasted image 20260506124638.png]]

**Контроль:**
$$
\int_{-\infty}^{+\infty}f(x)\,dx=\int_{a}^{a}f(x)\,dx= \frac{1}{b-a}\int_{a}^{b}dx= \frac{b-a}{b-a}=1
$$


$$
F_{\xi}(x)\equiv F(x)=\int_{-\infty}^{x}f(t)\,dt:
$$
1. $x<a:$
$$
F(x)=\int_{-\infty}^{x}0\cdot\,dt=0
$$
2. $a\leq x\leq b:$
$$
F(x)=\int_{-\infty}^{a}0\cdot dt+\int_{a}^{x} \frac{1}{b-a}\,dt= \frac{x-a}{b-a}.
$$
3. $x>b:$
$$
F(x)=\int_{-\infty}^{a}0\cdot\,dt+\int_{a}^{b} \frac{1}{b-a}\cdot\,dt+\int_{b}^{x}0\cdot\,dt=1
$$

$$
F(x)=\begin{cases}
0,&x<a \\
\frac{x-a}{b-a},&a\leq x\leq b \\
1,&x>b
\end{cases}
$$

![[Pasted image 20260506125230.png]]

$F(x)\in C(\mathbb{R}), \ K=\{ a \}\cup \{ b \}, \ \mu(K)=0$
$\forall x\in \mathbb{R}\setminus K\implies f(x)=F'(x),$ т.е. $f(x)\overset{\text{п.в.}}{=}F'(x)$.

**Теорема:**  Если $\xi\thicksim \mathrm{U}[a,b]$, то $$M\xi= \frac{a+b}{2}, \ \mathcal{D}\xi= \frac{(b-a)^{2}}{12}.$$
$\blacktriangleleft$
$$
M\xi=\int_{-\infty}^{+\infty}xf(x)\,dx=\int_{a}^{b} \frac{x}{b-a}\,dx= \frac{1}{b-a}\int_{a}^{b}x\,dx= \frac{x^{2}}{2(b-a)}\bigg|_{a}^{b}= \frac{b^{2}-a^{2}}{2(b-a)}=
$$
$$
= \frac{(a+b)(b-a)}{2(b-a)}= \frac{a+b}{2}
$$
$$
M(\xi^{2})=\int_{-\infty}^{+\infty}x^{2} f(x)\,dx=\int_{a}^{b} \frac{x^{2}}{b-a}\,dx=\frac{x^{3}}{3(b-a)}\bigg|_{a}^{b}= \frac{b^{3}-a^{3}}{3(b-a)}= \frac{(b-a)(b^{2}+ab+a^{2})}{3(b-a)}=
$$
$$
=\frac{b^{2}+ab+a^{2}}{3}
$$
$$
\mathcal{D}\xi=M(\xi^{2})-(M\xi)^{2}= \frac{b^{2}+ab+a^{2}}{3}- \frac{(a+b)^{2}}{4}=
$$
$$
=\frac{4b^{2}+4ab+4a^{2}-3(a+b)^{2}}{12}= \frac{4b^{2}+4ab+4a^{2}-3a^{2}-6ab-3b^{2}}{12}=
$$
$$
= \frac{b^{2}-2ab+a^{2}}{12}= \frac{(b-a)^{2}}{12}
$$
Т.е. $M\xi = \frac{a+b}{2}, \ \mathcal{D}\xi= \frac{(b-a)^{2}}{12}$.
$\blacktriangleright$

**Замечание:** Равномерное распределение, в частности, применяется в геометрической вероятности на $\mathbb{R}\equiv \mathbb{R}^{1}$.
Пусть $[\alpha;\beta]\subset[a,b]$. Тогда 
$$
P(\xi \in[a,b])=\int_{\alpha}^{\beta}f(x)\,dx= \frac{1}{b-a}\int_{\alpha}^{\beta}f(x)\,dx= \frac{\beta-\alpha}{b-a}= \frac{\mu([\alpha,\beta])}{\mu([a,b])}\text{ - геометрическая вероятность}
$$
