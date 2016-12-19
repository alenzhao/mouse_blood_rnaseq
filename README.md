# mouse_blood_rnaseq
* Cmp RSEM expression from three mouse erythroid cells
  * Use adrenal gland and thymus as controls
  * Two replicates each
  * MDS shows blood cells seperate from controls in the first component
  
### Methods
  * Rm ercc, Ignore non ENSMUSG genes, and translate ensembl IDs to gene names (ignore ensembl genes mapping to the same gene name)
  * Limit genes to those with at least a 35 expected count in two samples (go from 30K genes to 12K. Cutoff was taken as the dip between two expression modes)
  * Use voom-limma to find de between pairwise comparisons of cells
