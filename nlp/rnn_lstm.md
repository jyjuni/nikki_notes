## encoder-decoder

encoder: input -> feature vector (feature representations)

decoder: feature vector -> output

*Simple terms , **ENCODER** folds the data to retain imp information and **DECODER** does the final task.

### training

The encoders are trained with the decoders. There are no labels (hence *unsupervised*). The loss function is based on computing the delta **between the actual and reconstructed input**. The optimizer will try to train both encoder and decoder to lower this reconstruction loss.

Once trained, the encoder will gives feature vector for input that can be use by decoder to construct the input with the features that matter the most to make the reconstructed input recognizable as the actual input.

It is important to know that in actual application, people donot try to reconstruct the actual input, but rather want to map/translate/associate inputs to certain outputs. For example translating french to english sentences, etc.



[What is an Encoder/Decoder in Deep Learning? - Quora](https://www.quora.com/What-is-an-Encoder-Decoder-in-Deep-Learning)  

[What is an encoder decoder model? | by Nechu BM | Towards Data Science](https://towardsdatascience.com/what-is-an-encoder-decoder-model-86b3d57c5e1a) 

