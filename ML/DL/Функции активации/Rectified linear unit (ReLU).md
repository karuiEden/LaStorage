---
title: Rectified linear unit (ReLU)
created: 2026-07-18
tags:
  - deep_learning
links:
  - "[[Функция активации]]"
  - "[[Покоординатное продолжение функции]]"
  - "[[Полностью связная прямая нейронная сеть]]"
---
**Определение:** Обозначим $\mathfrak{r}:\mathbb{R}\to \mathbb{R}$ как такую функцию, $\forall x\in \mathbb{R}$, что
$$
\mathfrak{r}(x)=\max\{ x,0 \}
$$
и назовем $\mathfrak{r}$ *выпрямленной линейным юнитом* (ReLU).

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}

\begin{document}

\begin{tikzpicture}
    \begin{axis}[
        axis lines=middle,
        xmin=-4,
        xmax=4,
        ymin=-1,
        ymax=4,
        xlabel={$x$},
        ylabel={$\mathrm{ReLU}(x)$},
        xtick={-3,-2,-1,0,1,2,3},
        ytick={0,1,2,3},
        width=9cm,
        height=6cm,
        samples=100,
        clip=false
    ]
        \addplot[
            very thick,
            domain=-4:0
        ] {0};

        \addplot[
            very thick,
            domain=0:4
        ] {x};

        \node[
            anchor=south east
        ] at (axis cs:3.7,3.7) {$y=x$};

        \node[
            anchor=south
        ] at (axis cs:-2,0) {$y=0$};
    \end{axis}
\end{tikzpicture}

\end{document}
```

**Определение:** Пусть $d\in \mathbb{N}$. Тогда обозначим $\mathfrak{R}_{d}:\mathbb{R}^{d}\to \mathbb{R}^{d}$ такую функцию
$$
\mathfrak{R}_{d}=\mathfrak{M}_{\mathfrak{r},d}
$$
и назовем $\mathfrak{R}_{d}$ $d$-мерной ReLU функцией активации.

**Лемма:** (ANN с ReLU). Пусть $W_{1}=w_{1}=1, \ W_{2}=w_{2}=-1, \ B=b_{1}=b_{2}=0$. Тогда выполняется следующее равенство:
$$
x=W_{1}\max\{ w_{1}x+b_{1},0 \}+W_{2}\max\{ w_{2}x+b_{2},0 \}+B
$$
**Доказательство:** 
$$
W_{1}\max\{ w_{1}x+b_{1},0 \}+W_{2}\max\{ w_{2}x+b_{2},0 \}+B=\max\{ x,0 \}-\max\{ -x,0 \}=
$$
$$
=\max\{ x,0 \}+\,\min\{ x,0 \}=x
$$
$\square$

**Лемма:** Пусть $\theta=(1,-1,0,0,1,-1,0)\in \mathbb{R}^{7}$. Тогда $\forall x\in \mathbb{R}$ выполняется, что 
$$
\mathcal{N}^{\theta,1}_{\mathfrak{R}_{2},\mathrm{id}_{\mathbb{R}}}(x)=x
$$
**Доказательство:** 
$$
(\mathcal{N}^{\theta,1}_{\mathfrak{R}_{2},\mathrm{id}_{\mathbb{R}}})(x)=(\mathrm{id}_{\mathbb{R}}\circ\mathcal{A}^{\theta ,4}_{1,2}\circ\mathfrak{R}_{2}\circ\mathcal{A}^{\theta,0}_{2,1})(x)=(\mathcal{A}^{\theta,4}_{1,2}\circ\mathfrak{R}_{2})(\begin{pmatrix}
1 \\
-1
\end{pmatrix}(x)+\begin{pmatrix}
0 \\
0
\end{pmatrix})=
$$
$$
=\mathcal{A}^{\theta,4}_{1,2}(\begin{pmatrix}
\max\{ x,0 \} \\
-\min\{ x,0 \}
\end{pmatrix})=\begin{pmatrix}
1&-1
\end{pmatrix}\begin{pmatrix}
\max\{ x,0 \} \\
-\min\{ x,0 \}
\end{pmatrix}+(0)=\max\{ x,0 \}+\min\{ x,0 \}=x
$$

$\square$

**Лемма:** Пусть $\theta=(1,-1,0,0,1,-1,-1,1,0,0,1,-1,0)\in \mathbb{R}^{13}$. Тогда утверждается, что $\forall x  \in \mathbb{R}$
$$
(\mathcal{N}^{\theta,1}_{\mathfrak{R}_{2},\mathfrak{R}_{2},\mathrm{id}_{\mathbb{R}}})(x)=x
$$
**Доказательство:** 
$$
(\mathcal{N}^{\theta,1}_{\mathfrak{R}_{2},\mathfrak{R}_{2},\mathrm{id}_{\mathbb{R}}})(x)=\begin{pmatrix}
1&-1
\end{pmatrix}\mathfrak{R}_{2}\left( \begin{pmatrix}
1&-1 \\
-1&1
\end{pmatrix}\mathfrak{R}_{2}\left( \begin{pmatrix}
1 \\
-1
\end{pmatrix}x + \begin{pmatrix}
0 \\
0
\end{pmatrix}\right)+\begin{pmatrix}
0 \\
0
\end{pmatrix}  \right) +0=
$$
$$
=\begin{pmatrix}
1&-1
\end{pmatrix}\mathfrak{R}_{2}\left( \begin{pmatrix}
\max\{ x,0 \}-\max\{ -x,0 \} \\
-\max\{ x,0 \}+\max\{ -x,0 \}
\end{pmatrix} \right) =\begin{pmatrix}
1&-1
\end{pmatrix}\mathfrak{R}_{2}\begin{pmatrix}
x \\
x
\end{pmatrix}=
$$
$$
=\max\{ x,0 \}-\max\{ -x,0 \}=x
$$
$\square$

