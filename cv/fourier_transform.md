# Fourier Transform

 [02 Convolution.pdf](../../W4732 CV II/Slides/02 Convolution.pdf) 

## Sinusoids

$A -amplitude$ 
$\phi - phase$ 
$f - frequency$

<img src="fourier_transform.assets/Screen Shot 2022-08-06 at 4.24.02 PM.png" alt="Screen Shot 2022-08-06 at 4.24.02 PM" style="zoom:50%;" />
$$
f(t) = A \sin(2\pi ft + \phi) = A \sin(\omega x+\phi)
$$

## Joseph Fourier's Theroem

**A bold idea(1807)**: Any univariate function can be rewritten as a weighted sum of sines and cosines of different frequencies.

### 1D Fourier Transform

<img src="fourier_transform.assets/Screen Shot 2022-08-06 at 4.28.40 PM.png" alt="Screen Shot 2022-08-06 at 4.28.40 PM" style="zoom:50%;" />

(ignore the x labels)

map frequency(x) -> amplitude, phase(y)

center is 0

### 2D Fourier Transform

<img src="fourier_transform.assets/Screen Shot 2022-08-06 at 4.29.11 PM.png" alt="Screen Shot 2022-08-06 at 4.29.11 PM" style="zoom:50%;" />

**振幅 amplitude**: center is (0,0). black is 0, white $\infin$.==频域？==

**相位phase**: center is (0,0). grey is 0, white $\infin$, black $-\infin$.

- most information is stored in the phase
- amplitude is usually similar
  - reason: most natural photo is smooth, pixels is not changing much

## The Fourier Transform

<img src="fourier_transform.assets/Screen Shot 2022-08-06 at 6.35.37 PM.png" alt="Screen Shot 2022-08-06 at 6.35.37 PM" style="zoom:23%;" />

$$
G(f) = \int_{-\infin}^{\infin} g(t) e^{-2\pi ift} dt
$$

> $t$ - location in image(signal)
>
> $g(t)$ - function of image(signal)

> **How I think of it:**
> You wrap g(t) around the circle with frequency $f$, then calculate average position of $g(t)$

### Square Waves

<img src="fourier_transform.assets/Screen Shot 2022-08-06 at 6.40.27 PM.png" alt="Screen Shot 2022-08-06 at 6.40.27 PM" style="zoom:40%;" />

> **Fourier Transform** is essentially converting the original signal $g(t)$ into a new domain by frequency; for every frequency you are getting a complex number $G(f)$ back, from which you can extract things like amplitude and phase.

$G(f)$:  for a wave out of particular frequency, tells what the amplitude and phase should be 

**amplitude**: magnitude of  $G(f)$
$$
\sqrt{\mathfrak{R}[G(f)]^2 +  \mathfrak{I}[G(f)]^2}
$$
**phase**: angle of $G(f)$
$$
\tan ^{-1} \frac{\mathfrak{I}[G(f)]}{\mathfrak{R}[G(f)]}
$$
**Inverse Fourier Transform**

going back, is almost the same:
$$
g(t) = \int_{-\infin}^{\infin} G(f) e^{2\pi ift} df
$$

### Examples

#### Artificial Waves

<img src="fourier_transform.assets/Screen Shot 2022-08-06 at 7.07.16 PM.png" alt="Screen Shot 2022-08-06 at 7.07.16 PM" style="zoom:50%;" />

#### Repeated Patterns

FT has peaks at spatial frequencies of repeated structure

![Screen Shot 2022-08-06 at 7.07.31 PM](fourier_transform.assets/Screen Shot 2022-08-06 at 7.07.31 PM.png)

### Image Compresison

#### Removing high frequencies

image compression: only stores low-frequency information

> eg: jpeg

<img src="fourier_transform.assets/Screen Shot 2022-08-06 at 7.16.10 PM.png" alt="Screen Shot 2022-08-06 at 7.16.10 PM" style="zoom:33%;" />

<img src="fourier_transform.assets/Screen Shot 2022-08-06 at 7.18.10 PM-9827910.png" alt="Screen Shot 2022-08-06 at 7.18.10 PM" style="zoom:33%;" />

*this correspond to convolution with a big averaging filter.



#### Edge Detection

<img src="fourier_transform.assets/Screen Shot 2022-08-06 at 7.20.33 PM.png" alt="Screen Shot 2022-08-06 at 7.20.33 PM" style="zoom:33%;" />

<img src="fourier_transform.assets/Screen Shot 2022-08-06 at 7.20.42 PM.png" alt="Screen Shot 2022-08-06 at 7.20.42 PM" style="zoom:33%;" />

## Convolution

Convolution in time space is multiplication in frequency space:
$$
g(x) * h(x) == \mathscr{F}^{-1}\Big[\mathscr{F} [g(x)] \cdot \mathscr{F} [h(x)]\Big]
$$


Convolution in frequency space is multiplication in time space:
$$
\mathscr{F} [g(x)] * \mathscr{F} [h(x)] == \mathscr{F}\Big[ g(x) \cdot h(x) \Big]
$$

### Computation Efficiency

convolution vs FT:

- depends on how fast FT operations are

- if filter is huge, FT is faster.

### Gaussian Filter

<img src="fourier_transform.assets/image-20220806193345973.png" alt="image-20220806193345973" style="zoom:30%;" />



> **FT of Gaussian is Gaussian**
>
> $G(f) \sim Gaussian(0, \sigma')$
>
> - mean is the same(0), variance is different
>
> <img src="fourier_transform.assets/Screen Shot 2022-08-06 at 7.35.24 PM.png" alt="Screen Shot 2022-08-06 at 7.35.24 PM" style="zoom:30%;" />

### vs Box Filter

<img src="fourier_transform.assets/image-20220806194623366.png" alt="image-20220806194623366" style="zoom:25%;" />

**FT of box filter:**

<img src="fourier_transform.assets/Screen Shot 2022-08-06 at 7.46.54 PM.png" alt="Screen Shot 2022-08-06 at 7.46.54 PM" style="zoom: 25%;" />

# <img src="fourier_transform.assets/Screen Shot 2022-08-06 at 7.45.59 PM.png" alt="Screen Shot 2022-08-06 at 7.45.59 PM" style="zoom: 25%;" />



### Laplacian Filter

removes extremely low and extremely high frequency bits

<img src="fourier_transform.assets/Screen Shot 2022-08-06 at 9.49.52 PM.png" alt="Screen Shot 2022-08-06 at 9.49.52 PM" style="zoom:25%;" />



# Hybrid Images



<img src="fourier_transform.assets/Screen Shot 2022-08-07 at 12.17.10 AM.png" alt="Screen Shot 2022-08-07 at 12.17.10 AM" style="zoom:30%;" />

- red line - 150m away
- human eye cannot see waves above the redline
- can use this to hide things behind the grey



> example:
>
> low ref Marilyn Monroe + high ref Einstein:
>
> as walking far away, one can only see low ref (Monroe) images.
>
> <img src="fourier_transform.assets/Screen Shot 2022-08-07 at 12.22.51 AM.png" alt="Screen Shot 2022-08-07 at 12.22.51 AM" style="zoom:50%;" />
>
> http://cvcl.mit.edu/hybrid_gallery/gallery.html 





