# Kernel-Based Hough Transform for Detecting Straight Lines in Images for the LSST Stack

This is the LSST stack code fork of the [KHT package](https://github.com/laffernandes/kht). Please see [Fernandes and Oliveira, 2008](http://www.ic.uff.br/~laffernandes/content/publications/journal/2008_pr_41(1)/fernandes_oliveira-pr-41(1)-2008-pre_print.pdf), for a full description of the algorithm.

Please cite the original paper if you use this code in your research:
```{.bib}
@Article{fernandes_oliveira-pr-41(1)-2008,
    author  = {Fernandes, Leandro A. F. and Oliveira, Manuel M.},
    title   = {Real-time line detection through an improved {H}ough transform voting scheme},
    journal = {Pattern Recognition},
    year    = {2008},
    volume  = {41},
    number  = {1},
    pages   = {299--314},
    doi     = {https://doi.org/10.1016/j.patcog.2007.04.003},
    url     = {http://www.ic.uff.br/~laffernandes/projects/kht},
}
```


This fork makes the following changes from the upstream package:

* Building the package with eups is now supported.
* A pybind11 python binding has been added as an alternative to the upstream boost python binding.
* An optional argument has been added to the main `run_kht` function, which allows a cut to be made on the absolute value of the kernel height. A cut was already implemented for the minimum kernel height as a fraction of the maximum kernel height in an image. However, in cases where there was no real line in the image, the tallest kernel height is not a meaningful quantity and it is helpful to set an absolute value.

Using the Pybind11 Python Implementation
----------------------------------------
After building, the python module can be used as follows:

```
import lsst.kht

lines = lsst.kht.find_lines(image, clusterMinimumSize, clusterMinimumDeviation, 
                            delta, minimumKernelHeight, nSigmas, absMinimumKernelHeight)
```
where the first six input parameters follow the conventions of the original [KHT](https://github.com/laffernandes/kht) and the last parameter `absMinimumKernelHeight` implements the absolute minimum kernel height cut described above.

