<p align="center"><img src="https://bl6pap003files.storage.live.com/y4mndHVHqnpqVudLMiDZbho2Gi45g9sNnh1OzVkAY0MOwWH9Fm5keWXSrxCdfAum-K4yijPD3dSUTbxPHVeI9OHoa-EkMWfGn2d4XARNHqiGBVr25fCJUx0IWYZYgrDnW2nGtS0PuPDR1M-KvSmoSnC5tNuqH_KatsV68MFPr984_eUQWGk0GEjd5vtvpafqrGN?width=500&height=394&cropmode=none" />

## *SpectraMap (SpMap): Hyperspectral package for spectroscopists in Python*

<p align="justify">Hyperspectral imaging presents important applications in medicine, agriculture, pharmaceutical, space, food and many upcoming applications. The analysis of hyperspectral images requires advanced software. The upcoming developments related to fast hyperspectral imaging, automation and deep learning applications demand innovative software developments for analyzing hyperspectral data. The Figure 1 shows the hyperspectral imaging by a standard spectrometer instrument. More information regarding novel medical imaging is found in <a href= "https://advancesimaging.blogspot.com"> advances in imaging</a>.

<p align="center"><img src="https://bl6pap003files.storage.live.com/y4mFDcOdm5472CEwuu-1aCTB20ZzS5wxLSO9bMZer1YgIQE2ekouGnfET2yuRF4jQbr9MoxPhw4FLX7ZbpBTF4vrYUnnMK3WP3_bQg7oyFdxTTYJmX7bSvu6k3gjZoWJL2wToqf52Ga3dopLGuaGXqxu4LHhQjot9_8yGPowpjisnI8vpPQ-7URYfgRNNH5oJ8S?width=660&height=371&cropmode=none" />

<p align="center">Figure 1 Raman Imaging Instrument

## Features

<p align="justify">The package includes standard tools such as reading, preprocessing, processing and visualization. The designing was focused on working hyperspectral images from Raman datasets. The package is extended to other spectroscopies as long as the data follows the type data structure.  Some features are shown by the next figures.

- <p align="justify">Preprocessing: some tool such as smoothing, removal of spikes, normalization and advanced baseline corrections are included. Figure 2 illustrates a mean and standard deviation of a tissue signature.

<p align="center"><img src="https://bl6pap003files.storage.live.com/y4mplHFW8SLZNdnUpXqO6g4scKHgzE0F2HF-24bwCf5qTiZnX-S1WjV95CU_8PFufzzf2PeQewZTcuUyhAuFpOyMub5NCail6phkrkXjpldosPcdwTFOpAFhq8i0stGiEoUETcUKvnSMBFVp_R7bKl66-vU36itVQl5hdAntSP71hJ6qMXPbtDmnWacYo-YdBro?width=550&height=400&cropmode=none" />

<p align="center"> Figure 2 Visualization of tissue Raman signature

- <p align="justify">Processing: some tools such as unmixing, pca, pls, vca and hierarchical and kmeans clustering are included. Figure 3 displays application of clustering for locating microplastics on complex matrices.
  
  <p align="center"><img src="https://bl6pap003files.storage.live.com/y4mCv3oo8wnXEf1lEJiK01NOUET8Sbt3yMIlkReJ3CsKhBV2yaVJ43ZLUFEhW0i7vGdLAagLDJAlomRYrutpLl2mbg8oxa5QPCmHjP2Ktz1dzoRtkroi8vJWCtA67hbCC6sElL0LvyyKhwao7ZhqE5TZQQA_EV-tl3qctMSOalqcREcFyTXiULJXz-FtlpEBZdD?width=660&height=574&cropmode=none" />
  
  <p align="center"> Figure 3 Segmentation by clustering: (a) clustered image, (b) unmixing image, (c) image and (d) mean clusters

- <p align="justify">Visualization: the next examples shows the pca scores of several biomolecules.
  
  <p align="center"><img src="https://bl6pap003files.storage.live.com/y4m2IgtZawTrfzKz36eecSGjwkXsjp5Zp5vognNGr-v-VeNX4nLSWbid62R28cW6_gqsxS5JJfNBeF2pzQArOPDEsb3BqTYyyzGo2qA5CuXZaLCER_a6PiwVubWL2B9GB0n6hgHXkSXouTZKLYEHPve_TwUVOtYN9inEhgU3wH5kazukHsbqeyRar4fdgNUg6Bz?width=450&height=501&cropmode=none" />

<p align="center">Figure 4 PCA scores

## Further upcoming developments:

- [ ] Graphical User Interface

- [ ] Supervised tools

- [ ] Use of large language models

- [x] Optimizing speed and organizing main code 

- [x] More examples

## Installation

<p align="justify">The predetermined work interface is Python 3. The library comes with 8 different hyperspectral examples and analysis. A manual presents the relevant functions and examples <a href="https://github.com/MicroscopeMaestro/spectramap/tree/main/docs"> Manual</a>.
<p align="justify">Install the library and required packages: (admin rights):

```python
pip install spectramap
```

## License

<p style="text-align: center;">
    MIT

<p align="justify">Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

<p align="justify">The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

<p align="justify">THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## References

[1] F. Pedregosa, G. Varoquaux, and A. Gramfort, “Scikit-learn: Machine Learning in Python,” Journal of Machine Learning Research, vol. 12, pp. 2825-- 2830, 2011.

[2] J. M. P. Nascimento and J. M. B. Dias, “Vertex component analysis: A fast algorithm to unmix hyperspectral data,” IEEE Transactions on Geoscience and Remote Sensing, vol. 43, no. 4, pp. 898–910, 2005, doi: 10.1109/TGRS.2005.844293.

[3] Z. M. Zhang, S. Chen, and Y. Z. Liang, “Baseline correction using adaptive iteratively reweighted penalized least squares,” Analyst, vol. 135, no. 5, pp. 1138–1146, 2010, doi: 10.1039/b922045c.

[4] L. McInnes, J. Healy, S. Astels, *hdbscan: Hierarchical density based clustering* In: Journal of Open Source Software, The Open Journal, volume 2, number 11. 2017
