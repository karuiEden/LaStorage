---
tags:
  - calculus
links:
  - "[[Предел последовательности]]"
---

1. $(a+b)^{n}=\sum_{k=0}^{n}C_{n}^{k}a^{k}b^{n-k}\quad C_{n}^{k}= \frac{n!}{k!(n!-k!)}= \frac{n(n-1)\dots(n-k+1)(n-k)!}{k!(n-k)!}= \frac{n(n-1)\dots(n-k+1)}{k!}$
	$$x_{n}:= \left( 1+ \frac{1}{n} \right)^{n}=1+n \frac{1}{n}+\frac{n(n-1)}{2} \left( \frac{1}{n} \right)^{2}+\dots+ \frac{n(n-1)\dots(n-k+1)}{k!} \frac{1}{n^{k}}+\dots+ \frac{n!}{n!} \frac{1}{n^n}$$
	$$=2+ \frac{n}{n} \frac{n-1}{n} \frac{1}{2!}+\dots+ \frac{1}{k!} \frac{n}{n} \frac{n-1}{n}\dots \frac{n-k+1}{n}+\dots+ \frac{1}{n!} \frac{n-1}{n} \frac{n-2}{n}\dots \frac{n-(n-1)}{n}$$
	$$=2+ \frac{1}{2!}\left( 1- \frac{1}{n} \right)+\dots+ \frac{1}{k!}\left( 1- \frac{1}{n} \right)\left( 1- \frac{2}{n} \right)\dots\left( 1- \frac{k-1}{n} \right)+ \frac{1}{n!}\left( 1- \frac{1}{n} \right)\dots\left( 1- \frac{n-1}{n} \right)$$
$x_{n}\longrightarrow x_{n+1}:$
2. Каждое слагаемое увеличивается:
	$$\frac{1}{k!}\left( 1- \frac{1}{n} \right)\dots\left( 1- \frac{k-1}{n} \right) < \frac{1}{k!}\left( 1- \frac{1}{n+1} \right)\dots\left( 1-\frac{k-1}{n+1} \right)$$
3. В конец добавлено положительное слагаемое:
	$$\frac{1}{(n+1)^{n+1}}>0\implies x_{n}<x_{n+1}$$
Ограниченность $\{ x_{n} \}$:
$$n! = 1\cdot 2 \cdot 3 \cdot\dots \ \cdot n\geq 2^{n-1}\implies \frac{1}{n!}< \frac{1}{2^{n+1}}$$
$$x_{n}=2+ \frac{1}{2!}\left( 1- \frac{1}{n} \right)+\dots+\frac{1}{n!}\left( 1- \frac{1}{n} \right)\dots\left( 1-\frac{n-1}{n} \right)<2+\frac{1}{2}+\frac{1}{4}+\dots+\frac{1}{2^{n-1}}<3\implies$$
$x_{n}\nearrow, \ x_{n}<3\implies \forall n\implies \ \{ x_{n} \}$ сходится и $e:=\lim_{ n \to \infty }\left( 1+\frac{1}{n} \right)^{n}$
4. $\sqrt[n]{a_{1}a_{2}a_{3}\dots a_{n}  }\leq \frac{a_{1}+a_{2}+\dots+a_{n}}{n} \quad \forall a_{j}>0 \ \text{"="} \Leftrightarrow a_{1}=a_{2}=a_{3}=\dots=a_{n}$
	$$\forall a>0,b>0 \sqrt[n+1]{ ab^{n }\leq \frac{a+nb}{n+1}}\quad \left( 1+\frac{1}{n} \right)^{n} \ a=1,b=1+\frac{1}{n}$$
	$$\sqrt[n+1]{ 1\left( 1+\frac{1}{n} \right)^{n} }< \frac{\left( 1+n\left( 1+\frac{1}{n} \right) \right)}{n+1}= \frac{n+2}{n+1}=1+ \frac{1}{n+1}\nearrow n+1$$
	$$\left( 1+\frac{1}{n} \right)^n<\left( 1+\frac{1}{n+1} \right)^{n+1}\implies x_{n}\nearrow$$
	Ограниченность сверху:
		$\left( 1-\frac{1}{n} \right)^{n} \nearrow$ проверим $a=1,b=1-\frac{1}{n}$
	$$\sqrt[n+1]{1\left( 1-\frac{1}{n} \right)^{n}  }< \frac{\left( 1 +n\left( 1-\frac{1}{n} \right) \right)}{n+1}=\frac{n}{n+1}=1-\frac{1}{n+1}\nearrow n+1\implies$$
	$$\implies\left( 1-\frac{1}{n} \right)^n<\left( 1-\frac{1}{n+1} \right)^{n+1}\implies\left( 1+\frac{1}{n} \right)^{n+1}=\left( \frac{n+1}{n} \right)^{n+1}=\frac{1}{\left( \frac{n}{n+1} \right)^{n+1}}=\frac{1}{\left( 1-\frac{1}{n} \right)^{n+1}}\searrow$$
	$$\left( 1+\frac{1}{n} \right)^{n}\nearrow, \ \left( 1+\frac{1}{n} \right)^{n+1}\searrow$$
	Проверим $\forall m,k:$
	$$\left( 1+\frac{1}{m} \right)^{m}<\left( 1+\frac{1}{k} \right)^{k+1}\quad n:=\max\{ m,k \}$$
	$$\left( 1+\frac{1}{m} \right)^{m}\leq\left( 1+\frac{1}{n} \right)^{n}<\left( 1+\frac{1}{n} \right)^{n+1}\leq\left( 1+\frac{1}{k} \right)^{n+1}\implies$$
	$\left( 1+\frac{1}{n} \right)^n\nearrow$ ограничена сверху, $\left( 1+\frac{1}{n} \right)^{n+1}\searrow$ ограничена снизу $\implies$ сходятся