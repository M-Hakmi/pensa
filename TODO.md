### In Progress

- [ ] Refactoring and fixes for release 0.2
  - [x] Restructure modules to subpackages
  - [x] Adapt README
  - [x] Adapt API documentation
  - [ ] Include SSI to example scripts?
  - [x] Numbering of principal component trajectories starts with 0, should start with 1
  - [x] Axis labels and legend name for distance matrix plot
  - [x] Function pca_features() does not have labels
  - [x] Function compare_projections() does not have labels or legend
- [ ] Tests
  - [x] Workflow test with example data
  - [ ] Trivial examples for each function
  - [ ] Unit tests for SSI 
  - [ ] Unit tests for density features
- [ ] Frame classification via CNN on features
  - [x] Prototype to classify simulation frames
  - [ ] Interpret weights as relevance of features
  - [ ] Write module
  - [ ] Write unit tests
- [ ] exploratory analysis via correlation coefficients of the features
  - [x] First tests (not very promising).
  - [ ] Try [different metric](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.correlation.html)
  - [ ] Find useful application or leave it out.
- [ ] Colab Tutorial
  - [x] Put Notebook on Colab and get it to run.
  - [x] Add visualizations.
  - [x] Fix installation via pip.
  - [ ] Fix animations (they only show white canvas).  

### Plans

- [ ] Write "getting started" for documentation 
- [ ] Unify tutorial format. Make one for each subpackage
  - [ ] preprocessing and featurization
  - [ ] comparison
  - [ ] dimensionality reduction
  - [ ] clusters
  - [ ] SSI
- [ ] Try using MDAnalysis instead of biotite for water featurization
- [ ] Integrate more options for features from PyEMMA (think carefully about how to make it more flexible)
- [ ] More example tcl scripts for VMD 
- [ ] Implement T-distributed Stochastic Neighbor Embedding (t-SNE)
  - [ ] First tests
  - [ ] write module
  - [ ] write unit tests
- [ ] Implement a clustering algorithem designed for structural ensembles
  - [ ] Read up about [CLoNe](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btaa742/5895303) 
  - [ ] First tests
  - [ ] write module
  - [ ] write unit tests
- [ ] Put shared functionality of PCA and TICA into shared functions.
- [ ] Include TICA in unit tests
- [ ] Make file format (png/pdf?) for matplotlib optional.

### Ideas

- [ ] Hydrogen bonds as features
- [ ] Position deviations as features (similar to components of RMSD)
- [ ] Calculate correlation times (and use them to estimate a threshold for significance)
- [ ] Wasserstein distance to compare ensembles
- [ ] Featurizers for other molecule types
  - [ ] ions
  - [ ] ligands
  - [ ] lipids
  - [ ] nucleic acids
- [ ] Simplify adding hand-crafted features 
- [ ] Implement conformational entropy calculations
  - [ ] Read papers, e.g, [1](https://www.pnas.org/content/111/43/15396), [2](https://www.mdpi.com/2079-3197/6/1/21/htm)
  - [ ] Test to find the best way to do it.
- [ ] Implement [multi-dimensional scaling](https://en.wikipedia.org/wiki/Multidimensional_scaling)
- [ ] Try to integrate [functional mode analysis](http://www3.mpibpc.mpg.de/groups/de_groot/fma.html).
- [ ] Try to integrate [VAMPnets](https://www.nature.com/articles/s41467-017-02388-1).
- [ ] Try to integrate [DiffNets](https://doi.org/10.1101/2020.07.01.182725).
- [ ] Try to integrate [network analysis](https://aip.scitation.org/doi/full/10.1063/5.0020974).

### Done  ✓