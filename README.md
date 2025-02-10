# Learned, Uncertainty-driven Adaptive Acquisition

The official PyTorch implementation of the [Learned, Uncertainty-driven Adaptive Acquisition for Photon-Efficient Multiphoton Microscopy paper](https://arxiv.org/abs/2310.16102)

<div align="center">
  <img src="./readme_graphics/teaser.gif" width="80%" />
  <br/>
  <div align="left" width="60%">
    <figcaption display="table-caption" width="60%"> <b>Image prediction and predicted uncertainty when denoising using 1 to 5 noisy multiphoton microscopy images. As the number of measurements increases, the predicted image more closely matches the ground truth, and the pixel-wise uncertainty decreases.</b></figcaption>
  </div>
</div>

# Setup: 

Clone this project using:

```
git clone https://github.com/cassandra-t-ye/Learned_Uncertainty_Quantification.git
```

Dependencies can be installed using

```
conda env create -f environment.yml
source activate learned_uncertainty
```

# Dataset:

The FMD dataset we used can be downloaded [here](https://github.com/yinhaoz/denoising-fluorescence) <br>
The Experimental MPM dataset we used can be downloaded [here](https://drive.google.com/drive/folders/1DYUYBe7rm--mcpPVPKBcuhgHmfooy9e7?usp=sharing)


# Getting Started:

To get started, download the weights and `model.config` for our finetuned model here:

- [Weights](https://drive.google.com/file/d/1t7hAASo-FFw1SOTXDozE5vhFgeDwk11s/view?usp=sharing)  
- [Model Config](https://drive.google.com/file/d/1a28mvw4ihhQh38cCNJEa_ciLdT0szpRn/view?usp=sharing)

Once finished, put these files in the main repo, open either quickstart_FMD.ipynb or quickstart_MPM and get started!


