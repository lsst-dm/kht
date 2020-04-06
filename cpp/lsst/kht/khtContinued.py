
import numpy as np
from .pykht import find_satellites as fs


def find_satellites(image, cluster_min_size,
                    cluster_min_deviation, delta, kernel_min_height, n_sigmas, abs_kernel_min_height):

    im_copy = np.copy(image).astype(bool)
    image_height, image_width = image.shape
    image_height = int(image_height)
    image_width = int(image_width)

    fit_im = np.require(im_copy, bool, ['CONTIGUOUS', 'ALIGNED'])
    lines = fs(fit_im, image_width, image_height, cluster_min_size, cluster_min_deviation,
               delta, kernel_min_height, n_sigmas, abs_kernel_min_height)

    rhos, thetas = [], []
    for line in lines:
        rhos.append(line.rho)
        thetas.append(line.theta)
    res = [rhos, thetas]
    result = np.core.records.fromarrays(res, dtype=[('rho', float),
                                                    ('theta', float),
                                                    ])
    return result
