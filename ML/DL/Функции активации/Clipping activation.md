---
title: Clipping activation
created: 2026-07-23
tags:
  - deep_learning
links:
  - "[[Функция активации]]"
---
**Определение:** Пусть $u\in(-\infty;+\infty),v\in[u;+\infty).$ Тогда обозначим $\mathfrak{c}_{u,v}:\mathbb{R}\to \mathbb{R}$ - функция, которая $\forall x\in \mathbb{R}:$
$$
\mathfrak{c}_{u,v}(x)=\max\{ u,\min\{ x,v \} \}
$$
и называется $\mathfrak{c}_{u,v}(x)$ - clipping активация.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}

\begin{document}

\begin{tikzpicture}
    \begin{axis}[
        axis lines=middle,
        width=10cm,
        height=7cm,
        xmin=-4,
        xmax=4,
        ymin=-2.5,
        ymax=2.5,
        xlabel={$x$},
        ylabel={$f(x)$},
        xtick={-2,0,2},
        xticklabels={$a$,$0$,$b$},
        ytick={-2,0,2},
        yticklabels={$a$,$0$,$b$},
        clip=false,
        every axis x label/.style={
            at={(current axis.right of origin)},
            anchor=west
        },
        every axis y label/.style={
            at={(current axis.above origin)},
            anchor=south
        }
    ]

        \addplot[
            thick,
            domain=-4:-2,
            samples=2
        ] {-2};

        \addplot[
            thick,
            domain=-2:2,
            samples=2
        ] {x};

        \addplot[
            thick,
            domain=2:4,
            samples=2
        ] {2};

        \addplot[
            only marks,
            mark=*,
            mark size=1.8pt
        ] coordinates {
            (-2,-2)
            (2,2)
        };

        \draw[dashed]
            (axis cs:-2,0) -- (axis cs:-2,-2);

        \draw[dashed]
            (axis cs:2,0) -- (axis cs:2,2);



    \end{axis}
\end{tikzpicture}

\end{document}
```
