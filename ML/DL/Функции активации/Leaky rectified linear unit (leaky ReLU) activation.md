---
title: Leaky rectified linear unit (leaky ReLU) activation
created: 2026-07-23
tags:
  - deep_learning
links:
  - "[[Функция активации]]"
---
**Определение:** Пусть $\gamma \in[0;+\infty)$. $a(x)$ - leaky ReLU активация, если
$$
a(x)=\begin{cases}
x,&:x>0 \\
\gamma x,&:x\leq 0
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
  ymin=-1,ymax=5,
  xlabel={$x$},ylabel={$f(x)$},
  samples=100,
  domain=-5:5
]
\def\alpha{0.1}
\addplot[thick] {x < 0 ? \alpha*x : x};
\end{axis}
\end{tikzpicture}
\end{document}
```
