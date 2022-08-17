# Convolution

 [02 Convolution.pdf](../../W4732 CV II/Slides/02 Convolution.pdf) 

## Convolution Operation

<img src="convolution.assets/Screen Shot 2022-08-05 at 3.52.54 PM.png" alt="Screen Shot 2022-08-05 at 3.52.54 PM" style="zoom:20%;" />
$$
(f*g)[x,y] = \sum_{i,j} f[x-i, y-j]g[i,j]
$$
Substraction makes some math properties consistent later on. In practice, convoution in TF and Pytorch use the plus-definition with cross-correlation which is the equivalent if you define a upside-down convolution kernel.



### Cross-Correlation Operation

Conceptually simpler, but not as nice properties:

<img src="convolution.assets/Screen Shot 2022-08-05 at 6.14.33 PM.png" alt="Screen Shot 2022-08-05 at 6.14.33 PM" style="zoom:20%;" />
$$
(f*g)[x,y] = \sum_{i,j} f[x+i, y+j]g[i,j]
$$
*This is basically what "convolution" in CV does in practice, but in theory some properties, such as *associative property*, don't hold.  



### Properties





## Filters

identical

$\begin{bmatrix}
0 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 0\\
\end{bmatrix}$



translation filter 

### 

### blur filter

(aka **box filter**, **moving average**)



### gaussian filter

$$
G_\sigma = \frac{1}{2\pi\sigma^2}exp(-\frac{(x^2+y^2)}{2\sigma^2})
$$



<img src="convolution.assets/Screen Shot 2022-08-05 at 8.22.04 PM.png" alt="Screen Shot 2022-08-05 at 8.22.04 PM" style="zoom:30%;" />

- commonly used in practice for **bluring**

- creating a filter using the pdf of gaussian distribution.

**intuition**: adjacent pixels are probably the same, further pixels less likely to be the same

**properties**: 

- symmetric

- zero-mean: most important pixel at the center

- has infinite support: value decays but never goes to 0.

  > in theory Gaussian is a infinitely large filter, in practice large enough

- standard deviation $\sigma$: control extent of smoothing<img src="convolution.assets/Screen Shot 2022-08-05 at 8.22.24 PM.png" alt="Screen Shot 2022-08-05 at 8.22.24 PM" style="zoom:30%;" />

**complexity**: 

- naively $O(n^2m^2)$, **very** expensive
- $O(n^2m)$ with separable convolution:

#### Separable Convolution

Two dimensional Gaussian is product of two Gaussians:
$$
\begin{align}

G_\sigma & = \frac{1}{2\pi\sigma^2} \exp(-\frac{(x^2+y^2)}{2\sigma^2}) \\
& = \Bigg( \frac{1}{2\pi\sigma^2} \exp ( -\frac{x^2}{2\sigma^2})\Biggr) \Biggl(\frac{1}{2\pi\sigma^2} \exp (-\frac{y^2}{2\sigma^2}) \Bigg)

\end{align}
$$
Take advantage of associativity: 

<img src="convolution.assets/Screen Shot 2022-08-05 at 10.04.01 PM.png" alt="Screen Shot 2022-08-05 at 10.04.01 PM" style="zoom:50%;" />

### human Visual system

>  Cat Visual System
>
> <img src="convolution.assets/Screen Shot 2022-08-05 at 11.25.49 PM.png" alt="Screen Shot 2022-08-05 at 11.25.49 PM" style="zoom:50%;" />
>
> <u>Gabor Filters</u>: 
>
> cosine wave multiple by a Gaussian, for edge detection?



### edge filter 

#### Image Gradient

Use convolution filter to calculate gradient map:

<img src="convolution.assets/Screen Shot 2022-08-05 at 11.39.40 PM.png" alt="Screen Shot 2022-08-05 at 11.39.40 PM" style="zoom:33%;" />

#### finding edges

change is measured by derivative in 1D

- biggest change in value -> 1st derivative has maximum magnitude 

or:

- 2nd derivative is <u>zero</u>

#### handling noise

**with noise:** derivative is high everywhere. Therefore must <u>smooth</u> before taking gradient.

- filter with an Gaussian to smooth, then take gradients

- but, convolution is linear 

  - can combine two direction's convolution operations:

    <img src="convolution.assets/Screen Shot 2022-08-05 at 11.49.12 PM.png" alt="Screen Shot 2022-08-05 at 11.49.12 PM" style="zoom:30%;" />

    <img src="convolution.assets/Screen Shot 2022-08-05 at 11.50.15 PM.png" alt="Screen Shot 2022-08-05 at 11.50.15 PM" style="zoom:50%;" />

- another definition:

  $\gradient I = \frac{\partial^2I}{\partial x^2} + \frac{\partial^2I}{\partial y^2}$, then apply Gaussian filter

> eg:  Einstein's picture
>
> **finding boundaries**
>
> **object detection**:
>
> - convolve Einstein with his own eye: works as a box filter<img src="convolution.assets/Screen Shot 2022-08-06 at 2.25.40 PM.png" alt="Screen Shot 2022-08-06 at 2.25.40 PM" style="zoom:25%;" />
>
> - response for one window:
>
>   $f^T_{ij}g = ||f_{ij}|| ||g|| \cos\theta_{ij}$ 
>
>   the norm terms $||f_{ij}||$ and $||g||$ dominate the term, instead of similarity term $\cos\theta_{ij}$





## Padding

**same**

**valid**

**full**





## Pooling

### Max Pooling

can think of cheap resize/nonlinear convolution

gradient doesn't make sense

> eg: if cat nose exists in filter area, don't care exactly where
>
> 
