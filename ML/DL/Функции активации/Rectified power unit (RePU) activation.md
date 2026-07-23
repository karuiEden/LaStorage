---
title: Rectified power unit (RePU) activation
created: 2026-07-23
tags:
  - deep_learning
links:
  - "[[Функция активации]]"
---
**Определение:** Пусть $p\in \mathbb{N}$. Тогда $a(x)$ - RePU активация, если
$$
a(x)=(\max\{ x,0 \})^{p}
$$

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle,
  width=8cm,height=5cm,
  xmin=-3,xmax=3,
  ymin=-0.5,ymax=9,
  xlabel={$x$},ylabel={$f(x)$},
  samples=150,
  domain=-3:3
]
\def\s{2}
\addplot[thick] {(max(0,x))^\s};
\end{axis}
\end{tikzpicture}
\end{document}
```
