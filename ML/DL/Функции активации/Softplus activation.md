---
title: Softplus
created: 2026-07-23
tags:
  - deep_learning
links:
  - "[[Функция активации]]"
---
**Определение:** $a$ - softplus функция активации, тогда и только когда $a:\mathbb{R}\to \mathbb{R}$ - функция, такая что
$$
a(x)=\ln(1+\exp(x))
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
  ymin=-0.5,ymax=5,
  xlabel={$x$},ylabel={$f(x)$},
  samples=100,
  domain=-5:5
]
\addplot[thick] {ln(1+exp(x))};
\end{axis}
\end{tikzpicture}
\end{document}
```
