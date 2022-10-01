# SVM（支持向量机）

 [MIT 6.034 Artificial Intelligence](https://youtu.be/_PwhiWxHK8o?t=1020) 

 [05 Object Recognition II.pdf](../../W4732 CV II/Slides/05 Object Recognition II.pdf) 

**support vectors** are vectors *closest* to the decision boundary (within the margin)

find the **decision boundary** that maximize the margin, i.e. distance between support vector and db

idea:  find the db s.t.  if preturb any of the example, the classification won't change(**->robustness**)

<img src="svm.assets/Screen Shot 2022-08-21 at 1.55.06 PM.png" alt="Screen Shot 2022-08-21 at 1.55.06 PM" style="zoom:25%;" />

<img src="svm.assets/Screen Shot 2022-08-21 at 1.55.44 PM.png" alt="Screen Shot 2022-08-21 at 1.55.44 PM" style="zoom:25%;" />

- **$\lambda ||w||_2^2$ - regularization term:** find the db that push the margin as far way as possible

  - margin distance is $\frac{2}{||\mathbf w||}$ 

    - [why margin equals $\frac{2}{\|\mathbf{w}\|}$](####margin)

  - convex: $\frac{2}{||\mathbf w||}$  is not convex, but $||\mathbf w||$ is

    so solve $\min ||\mathbf w||$ instead of  $\max \frac{2}{||\mathbf w||}$

  - use normal vector w to represent the plane

    w: vector perpendicular to the db plane

  

- **$\displaystyle \sum_i \max(0, 1-y_iw^Tx_i)$ - data term:** db should fit to the data

  (penalize mis-labeled examples within-margin)

  - $1-y_iw^Tx_i$:  want sign of $y_i$ and $w^Tx_i$ to agree, if don't agree then this example contribute to the error

  - $max(·,·)$: only the examples within the margin will contribute to the error(if preturbed, these examples will cause false classification)



## reference

#### margin

why margin equal to $\frac{2}{\|\mathbf{w}\|}$: 

[linear algebra - Why is the SVM margin equal to $\frac{2}{\|\mathbf{w}\|}$? - Mathematics Stack Exchange](https://math.stackexchange.com/questions/1305925/why-is-the-svm-margin-equal-to-frac2-mathbfw)  

[MIT OCW - 16.  Learning: Support Vector Machines - YouTube](https://youtu.be/_PwhiWxHK8o?t=1020) 
