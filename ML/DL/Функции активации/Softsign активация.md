---
title: Softsign активация
created: 2026-07-23
tags:
  - deep_learning
links:
  - "[[Функция активации]]"
---
**Определение:** $a(x)$ - функция активации softsign, если
$$
a(x)= \frac{x}{|x|+1}
$$

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle,
  width=8cm,height=5cm,
  xmin=-6,xmax=6,
  ymin=-1.2,ymax=1.2,
  xlabel={$x$},ylabel={$f(x)$},
  samples=150,
  domain=-6:6
]
\addplot[thick] {x/(1+abs(x))};
\end{axis}
\end{tikzpicture}
\end{document}
```
