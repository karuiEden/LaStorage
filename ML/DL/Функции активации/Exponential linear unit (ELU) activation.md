---
title: Exponential linear unit (ELU) activation
created: 2026-07-23
tags:
  - deep_learning
links:
  - "[[Функция активации]]"
---
**Определение:** Пусть $\gamma \in(-\infty;0]$. Тогда $a(x)$ - ELU активация, если
$$
a(x)=\begin{cases}
x,&x>0 \\
\gamma(1-\exp(x)),&x\leq 0
\end{cases}
$$

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle,
  width=8cm,height=5cm,
  xmin=-5,xmax=5,
  ymin=-1.5,ymax=5,
  xlabel={$x$},ylabel={$f(x)$},
  samples=150,
  domain=-5:5
]
\def\alpha{1}
\addplot[thick] {x < 0 ? \alpha*(exp(x)-1) : x};
\end{axis}
\end{tikzpicture}
\end{document}
```
