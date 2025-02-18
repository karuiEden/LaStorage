---
tags:
  - calculus
  - math
links:
  - "[[Рациональные дроби и их интегрирование]]"
  - "[[Расширенная таблица первообразных]]"
---
$$\text{I тип} \frac{A}{x-a} \to \int \frac{A}{x-a}dx=A\cdot \ln|x-a|+C$$
$$\text{II тип} \frac{A}{(x-a)^{p}}\to \int \frac{A}{(x-a)^{p}}dx= \frac{A(x-a)^{1-p}}{1-p}=\frac{A}{(1-p)(x-a)^{p-1}}+C$$
$$\text{III тип} \frac{Ax+B}{x^{2}+px+q}
\int \frac{Ax+B}{x^{2}+px+q}dx=\int \frac{\left( \frac{A}{2} (2x+p) +B - \frac{Ap}{2} \right)}{x^{2}+px+q}dx$$
1 шаг - выделение в числителе производной знаменателя
2 шаг - выделение целого квадрата
$$= \frac{A}{2}\int \frac{d(x^{2}+px+q)}{x^{2}+px+q}+\left( B-\frac{Ap}{2} \right)\cdot \int \frac{dx}{\left( x+\frac{p}{2} \right)^{2}+q-\frac{p^{2}}{4}}$$
$$=\frac{A}{2}\ln|x^{2}+px+q|+ \frac{1}{\sqrt{q-\frac{p^{2}}{4}}}\arctan \frac{\left( x + \frac{p}{2} \right)}{\sqrt{ q-\frac{p^{2}}{4} }}+C$$
$$\text{IV тип} \frac{Ax+B}{(x^{2}+px+q)^{r}}$$
1) выделение производной квадратного трёхчлена
$$\frac{Ax+B}{(x^{2}+px+q)^{r}}=\frac{ \frac{A}{2}(2x+p)+B-\frac{Ap}{2} }{(x^{2}+px+q)^{r}}=\frac{A}{2} \frac{2x+p}{(x^{2}+px+q)^{r}}+ \left( B-\frac{Ap}{2} \right)\cdot \frac{1}{\left[( x+\frac{p}{2} \right)^{2}+q-\frac{p^{2}}{4}]^{r}}$$
1) Степенной интеграл
2) $J_{n}=\int \frac{dx}{(x^{2}+a^{2})^{n}}$
### Доказательство реккурентной формулы для $J_{n}$
$$J_{n-1}=\int \frac{dx}{(x^{2}+a^{2})_{n-1}}=\bigg|\begin{array} \\
u= \frac{1}{(x^{2}+a^{2})^{n-1}} \ \ \ du=-(n-1) \frac{2x}{(x^{2}+a^{2})^{n}}dx \\
dv=dx \ \ \ v=x
\end{array}\bigg|= \frac{x}{(x^{2}+a^{2})^{n-1}}+$$
$$2(n-1)\int \frac{x^{2}+a^{2}-a^{2}}{(x^{2}+a^{2})^{n}}dx= \frac{x}{(x^{2}+a^{2})^{n-1}}+2(n-1)J_{n-1} -2(n+1)a^{2}J_{n}$$
$$2(n-1)a^{2}J_{n}=\frac{x}{(x^{2}+a^{2})^{n-1}}+(2n-3)J_{n-1}$$
### Как находить простейшие дроби
 $$\frac{P(x)}{Q(x)}=\frac{A_{1}}{(x-x_{1})}+\dots+ \frac{A_{r}}{(x-x_{r})^{r}}+\frac{B_{1}}{x-x_{2}}+\dots \frac{B_{r_{2}}}{(x-x_{2})^{r_{2}}}+\frac{C_{1}}{(x-x_{m})}+\dots+\frac{C_{r_{m}}}{(x-x_{m})^{r_{m}}}$$
	 $\frac{P(x)}{Q(x)}$ -правильная дробь
$$+ \frac{M_{11}x+N_{11}}{x^{2}+p_{1}x+q_{1}}+\dots+\frac{M_{1s_{1}}x+N_{1s_{1}}}{(x^{2}+p_{1}x+q_{1})^{s_{1}}}+\dots+\frac{(E_{s_{r}1}x+F_{s_{r}1})}{x^{2}+p_{s_{r}}+q_{s_{r}}}+ \frac{E_{s_{r}u}x+N_{s_{r}u}}{(x^{2}+p_{s_{r}}x+q_{s_{r}})^{u}}$$
#### Пример
Разложить рациональную дробь: $$\frac{P(x)}{Q(x)}= \frac{5x^{4}+8x^{3}+4x^{2}+2x+4}{(2x-1)(x+1)^{2}(x^{2}+2x+2)}$$
$$\text{1 шаг }\frac{P(x)}{Q(x)}=\frac{A}{2x-1}+\frac{B}{x+1}+\frac{C}{(x+1)^{2}}+\frac{Dx+E}{x^{2}+2x+2}$$
$$\text{2 шаг (метод неопределённых коэффициентов) }$$
$$(x+1)^{2}(x^{2}+2x+2)=(x^{2}+2x+1)(x^{2}+2x+2)=x^{4}+4x^{3}+7x^{2}+6x+2$$
![[Pasted image 20250214102410.png]]
$$(2x-1)(x+1)(x^{2}+2x+2)=2x^{4}+5x^{3}+5x^{2}-2$$
$$(2x-1)(x^{2}+2x+2)=2x^{3}+3x^{2}+2-2$$
$$(2x-1)(x+1)^{2}(Dx+E)=2Dx^4+(2E+3D)x^{3}+3Ex^{2}-Dx-E$$
$$x^{4}: \ \ A+2B+2D=5$$
$$x^{3}: \ \ \ 4A+5B+2C+2E+3D=8$$
$$x^{2}: \ \ \ 7A+5B+3C+3E=4$$
$$x:6A+2C-D=2$$
$$x^{0}: \ \ \ 2A-2B-2C-E=4$$
Т.е.$$\begin{cases}
A+2B+2D=5 \\
4A+5B+2C+2E+3D=8 \\
7A+5B+3C+3E=4 \\
6A+2C-D=2 \\
2A-2B-2C-E=4
\end{cases}$$
$$\begin{cases}
A=1 \\
B=0 \\
C=-1 \\
D=2 \\
E=0 \\
\end{cases}$$
### Метод подстановки
$$\frac{P(x)}{Q(x)}= \frac{5x^{4}+8x^{3}+4x^{2}+2x+4}{(2x-1)(x+1)^{2}(x^{2}+2x+2)} = \frac{A}{2x-1}+\frac{B}{x+1}+\frac{C}{(x+1)^{2}}+ \frac{Dx+E}{x^{2}+2x+2}$$
$$A= \frac{5x^{4}+8x^{3}+4x^{2}+2x+4}{(x+1)^{2}(x^{2}+2x+2)}\bigg|_{x=\frac{1}{2}} = \frac{117\cdot 4\cdot 4}{16\cdot 13 \cdot 9}=1$$ ![[Pasted image 20250214104801.png]]
По такой логике можем найти другие коэффициенты
$$\frac{5x^{4}+8x^{3}+4x^{2}+2x+4}{(2x-1)(x+1)^{2}}\bigg|_{x=-1+i}=Dx+E\bigg|_{x=-1+i}$$
$$\frac{-2+10i}{-3+2i}=E-D+Di$$
$$\frac{(-2+10i)(3+2i)}{13}=\frac{-26+26i}{13}=-2+2i=(E-D)+Di\to D=2, E=0$$
Вычисление интеграла:
$$\int\frac{5x^{4}+8x^{3}+4x^{2}+2x+4}{(2x-1)(x+1)^{2}(x^{2}+2x+2)}=\int\left( \frac{1}{2x-1} -\frac{1}{(x+1)^{2}} +\frac{2x}{x^{2}+2x+2}\right)dx=\frac{1}{2}\int  \frac{d(2x-1)}{2x-1}-$$
$$-\int \left( \frac{dx}{(x+1)^{2}} \right)+\int\frac{((2x+2)-2)}{x^{2}+2x+2}=$$
$$\frac{1}{2}\ln|2x-1|+\frac{1}{x+1}+\ln|x^{2}+2x+2|-2\arctan(x+1)+C$$
