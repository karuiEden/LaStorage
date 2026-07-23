---
title: Gaussian error linear unit (GELU) activation
created: 2026-07-23
tags:
  - deep_learning
links:
  - "[[Функция активации]]"
---
**Определение:** $a$ - GELU функция активации, если
$$
a(x)= \frac{x}{\sqrt{ 2\pi }}\left[ \int_{-\infty}^{x}\exp\left( - \frac{z^{2}}{2} \right)\,dz \right] .
$$

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle,
  width=8cm,height=5cm,
  xmin=-4,xmax=4,
  ymin=-0.5,ymax=4,
  xlabel={$x$},ylabel={$f(x)$},
  samples=150,
  domain=-4:4
]
\addplot[thick]
{x/2*(1+tanh(sqrt(2/pi)*(x+0.044715*x^3)))};
\end{axis}
\end{tikzpicture}
\end{document}
```
