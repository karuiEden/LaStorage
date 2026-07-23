---
title: Sine activation
created: 2026-07-23
tags:
  - deep_learning
links:
  - "[[Функция активации]]"
---
**Определение:** $a(x)$ - синус активация, если
$$
a(x)=\sin(x)
$$

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle,
  width=8cm,height=5cm,
  xmin=-6.5,xmax=6.5,
  ymin=-1.2,ymax=1.2,
  xlabel={$x$},ylabel={$f(x)$},
  xtick={-6.283,-3.142,0,3.142,6.283},
  xticklabels={$-2\pi$,$-\pi$,$0$,$\pi$,$2\pi$},
  samples=200,
  domain=-6.283:6.283
]
\addplot[thick] {sin(deg(x))};
\end{axis}
\end{tikzpicture}
\end{document}
```
