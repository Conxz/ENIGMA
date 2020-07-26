import os
import numpy as np

from vtk import vtkPolyDataNormals

from ..mesh.mesh_io import read_surface
from ..mesh.mesh_operations import combine_surfaces
from ..utils.parcellation import reduce_by_labels
from ..vtk_interface import wrap_vtk, serial_connect


def load_parcellation(name, scale=400, join=False):
    """ Load parcellation for conte69.

    Parameters
    ----------
    name : {'schaefer', 'vosdewael'}
        Parcellation name, either 'schaefer' for Schaefer (functional)
        parcellations or 'vosdewael' for a subparcellation of aparc.
    scale : {100, 200, 300, 400}, optional
        Number of parcels. Default is 400.
    join : bool, optional
        If False, return one array for each hemisphere. Otherwise,
        return a single array for both left and right hemisphere.
        Default is False.

    Returns
    -------
    parcellation : tuple of ndarrays or ndarray
        Parcellations for left and right hemispheres. If ``join == True``, one
        parcellation with both hemispheres.
    """

    root_pth = os.path.dirname(__file__)
    fname = '{name}_{np}_conte69.csv'.format(name=name, np=scale)
    ipth = os.path.join(root_pth, 'parcellations', fname)
    x = np.loadtxt(ipth, dtype=np.int)
    if join:
        return x
    return x[:x.size//2], x[x.size//2:]


def load_mask(name='midline', join=False):
    """ Load mask for conte69.

    Parameters
    ----------
    name : {'midline', 'temporal'} or None, optional
        Region name. If 'midline', load mask for all cortex.
        Default is 'midline'.
    join : bool, optional
        If False, return one array for each hemisphere. Otherwise,
        return a single array for both left and right hemispheres.
        Default is False.

    Returns
    -------
    mask : tuple of ndarrays or ndarray
        Boolean masks for left and right hemispheres. If ``join == True``, one
        mask with both hemispheres.
    """

    root_pth = os.path.dirname(__file__)
    ipth = os.path.join(root_pth, 'surfaces', 'conte69_32k_{0}{1}_mask.csv')
    if name == 'midline':
        name = ''
    else:
        name = '_' + name
    mask_lh = np.loadtxt(ipth.format('lh', name), dtype=np.bool)
    mask_rh = np.loadtxt(ipth.format('rh', name), dtype=np.bool)
    if join:
        return np.concatenate([mask_lh, mask_rh])
    return mask_lh, mask_rh


def load_conte69(as_sphere=False, with_normals=True, join=False):
    """ Load conte69 surfaces.

    Parameters
    ----------
    as_sphere : bool, optional
        Return spheres instead of cortical surfaces. Default is False.
    with_normals : bool, optional
        Whether to compute surface normals. Default is True.
    join : bool, optional
        If False, return one surface for left and right hemispheres. Otherwise,
        return a single surface as a combination of both left and right
        surfaces. Default is False.

    Returns
    -------
    surf : tuple of BSPolyData or BSPolyData
        Surfaces for left and right hemispheres. If ``join == True``, one
        surface with both hemispheres.
    """

    root_pth = os.path.dirname(__file__)
    if as_sphere:
        fname = 'conte69_32k_{}_sphere.gii'
    else:
        fname = 'conte69_32k_{}.gii'

    ipth = os.path.join(root_pth, 'surfaces', fname)
    surfs = [None] * 2
    for i, side in enumerate(['lh', 'rh']):
        surfs[i] = read_surface(ipth.format(side))
        if with_normals:
            nf = wrap_vtk(vtkPolyDataNormals, splitting=False,
                          featureAngle=0.1)
            surfs[i] = serial_connect(surfs[i], nf)

    if join:
        return combine_surfaces(*surfs)
    return surfs[0], surfs[1]


def load_fsa5(with_normals=True, join=False):
    """ Load fsaverage5 surfaces.

    Parameters
    ----------
    with_normals : bool, optional
        Whether to compute surface normals. Default is True.
    join : bool, optional
        If False, return one surface for left and right hemispheres. Otherwise,
        return a single surface as a combination of both left and right
        surfaces. Default is False.

    Returns
    -------
    surf : tuple of BSPolyData or BSPolyData
        Surfaces for left and right hemispheres. If ``join == True``, one
        surface with both hemispheres.
    """

    root_pth = os.path.dirname(__file__)
    fname = 'fsa5.pial.{}.gii'

    ipth = os.path.join(root_pth, 'surfaces', fname)
    surfs = [None] * 2
    for i, side in enumerate(['lh', 'rh']):
        surfs[i] = read_surface(ipth.format(side))
        if with_normals:
            nf = wrap_vtk(vtkPolyDataNormals, splitting=False,
                          featureAngle=0.1)
            surfs[i] = serial_connect(surfs[i], nf)

    if join:
        return combine_surfaces(*surfs)
    return surfs[0], surfs[1]


def load_subcortical(with_normals=False, join=False):
    """ Load subcortical surfaces.

    Parameters
    ----------
    with_normals : bool, optional
        Whether to compute surface normals. Default is False.
    join : bool, optional
        If False, return one surface for left and right hemispheres. Otherwise,
        return a single surface as a combination of both left and right
        surfaces. Default is False.

    Returns
    -------
    surf : tuple of BSPolyData or BSPolyData
        Surfaces for left and right hemispheres. If ``join == True``, one
        surface with both hemispheres.
    """

    root_pth = os.path.dirname(__file__)
    fname = 'sctx_{}.gii'

    ipth = os.path.join(root_pth, 'surfaces', fname)
    surfs = [None] * 2
    for i, side in enumerate(['lh', 'rh']):
        surfs[i] = read_surface(ipth.format(side))
        if with_normals:
            nf = wrap_vtk(vtkPolyDataNormals, splitting=False,
                          featureAngle=0.1)
            surfs[i] = serial_connect(surfs[i], nf)

    if join:
        return combine_surfaces(*surfs)
    return surfs[0], surfs[1]


def _load_feat(feat_name, parcellation=None, mask=None):
    root_pth = os.path.dirname(__file__)
    ipth = os.path.join(root_pth, 'matrices', 'main_group',
                        '{0}.csv'.format(feat_name))
    x = np.loadtxt(ipth, dtype=np.float)
    if mask is not None:
        x = x[mask]

    if parcellation is not None:
        if mask is not None:
            parcellation = parcellation[mask]
        x = reduce_by_labels(x, parcellation, red_op='mean')
    return x


def load_marker(name, join=False):
    """ Load cortical data for conte69.

    Parameters
    ----------
    name : {'curvature', 'thickness', 't1wt2w'}
        Marker name.
    join : bool, optional
        If False, return one array for each hemisphere. Otherwise,
        return a single array for both left and right hemispheres.
        Default is False.

    Returns
    -------
    marker : tuple of ndarrays or ndarray
        Marker data for left and right hemispheres. If ``join == True``, one
        array with both hemispheres.
    """

    feat_name = 'conte69_32k_{0}'.format(name)
    x = _load_feat(feat_name)
    if join:
        return x
    return x[:x.size//2], x[x.size//2:]

