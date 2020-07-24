.. ENIGMA TOOLBOX documentation master file, created by
   sphinx-quickstart on Wed Jul 15 16:09:38 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.




**ENIGMA TOOLBOX**
============================
*An open source repository for the sharing of neuroimaging and genetics data, analytical
codes, and visualization tools that are 100% ENIGMA-friendly and -focused.*



.. image:: ./pages/extrafigs/spinearth.gif
    :scale: 100%
    :align: left


| 

|

|

|

|

___________________________________________________________________________________________________

|


**Data sharing** 💌
--------------------------
   As part of the **ENIGMA TOOLBOX**, we are making several data matrices openly available! As of now, 
   these include :ref:`functional and structural connectivity data<hcp_connectivity>` as well as :ref:`transcriptomic data<gene_maps>`.

**Harmonization of analytical methods** 👯‍♀️
--------------------------------------------------------
   Why make all these codes and data available, you may ask? One key goal of the **ENIGMA TOOLBOX** is
   to harmonize analytical methods both *within* and *across* ENIGMA Working Groups, ultimately facilitating
   comparisons of imaging and genetic findings across diseases.

**Visualization tools** 🎨
-------------------------------------
   Tired of displaying your surface findings in tables? Look no further! The **ENIGMA TOOLBOX** has got you 
   covered! Check out our :ref:`visualization tools<surf_visualization>` and project your cortical and subcortical data to the surface!

**Step-by-step tutorials** 👣
------------------------------------
   The **ENIGMA TOOLBOX** has a *No data, No problem* policy! To make things easier, we provide :ref:`example data<load_ct>` that
   have been processed according to ENIGMA protocols. Using these example data, you can complete all of the  
   tutorials. Alternatively, easily replace our example data with other ENIGMA-derived datasets!

|


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Getting started
   
   pages/install


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Loading data 
   
   pages/loadct_doc/index
   pages/HCP_doc/index


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Network-based atrophy models
   
   pages/hubs_doc/index
   pages/epicenter_doc/index


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Structural covariance networks

   pages/covariance_doc/index
   pages/gt_doc/index


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Gene expression

   pages/genemaps_doc/index
   pages/epilepsygenes_doc/index


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Surface data visualization

   pages/visualization_doc/index


___________________________________________________________________________________________________


Contributors
-----------------

- **Sara Larivière**, *MICA Lab - Montreal Neurological Institute*
- **Raúl Rodríguez-Cruces**, *MICA Lab - Montreal Neurological Institute*
- **Bo-Yong Park**, *MICA Lab - Montreal Neurological Institute*
- **Jessica Royer**, *MICA Lab - Montreal Neurological Institute*
- **Boris Bernhardt**, *MICA Lab - Montreal Neurological Institute*