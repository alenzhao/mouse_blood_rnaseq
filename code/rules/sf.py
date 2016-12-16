import pandas
from functools import reduce
from sfConst import *
from collections import defaultdict

rule dl:
    output: DATA + 'counts/{cellrep}.tsv'
    run:
        url = TSV[wildcards.cellrep]
        shell('wget "{url}" -O {output}')

# normralized matrix for pcs
rule tpmMatrix:
    input: ls = expand( DATA + 'counts/{cellrep}.tsv', cellrep=CELLS )
    output: o = DATA + 'tpm.mat'
    run:
        useCols = ['gene_id', 'TPM']
        names = [ x.split('/')[-1].split('.tsv')[0] for x in input.ls ]
        dfs = [ pandas.read_csv(x, usecols=useCols, sep='\t') for x in input.ls ]
        dfLs2 = [ df.rename(index=str, columns={'TPM':name + '_tpm'}) for name, df in zip(names, dfs) ]
        dfM = reduce(lambda left, right: pandas.merge(left, right, on='gene_id', how='outer').fillna(0), dfLs2)
        dfM.to_csv(output.o, index=False, sep='\t')

rule addGenesNames:
    input:  i = DATA + '{afile}',
            t = '/mnt/isilon/gerdblobel_lab/perry/credwards_gene_alias/data/ensemblSyn.mm9'
    output: o = DATA + '{afile}.genes'
    run:
        with open(input.t) as f:
            trans = {}
            for line in f:
                sp = line.strip().split('\t')
                trans[ sp[1] ] = sp[2]
        
        counts = defaultdict(int)
        with open(input.i) as f:
            for line in f:
                sp = line.strip().split('\t')
                eg = sp[0].lstrip('"').strip('"').split('.')[0]
                if eg in trans:
                    g = trans[eg]
                    counts[g] += 1

        with open(input.i) as f, open(output.o, 'w') as fout:
            print(f.readline().strip(), file=fout)
            for line in f:
                sp = line.strip().split('\t')
                eg = sp[0].lstrip('"').strip('"').split('.')[0]
                if eg in trans:
                    g = trans[eg]
                    if counts[g] == 1:
                        print(g + '\t' + '\t'.join(sp[1:]), file=fout)

# exp count matrix for ebseq
rule matrix:
    input:  expand( DATA + 'counts/{cellrep}.tsv', cellrep=CELLS )
    output: DATA + 'mat.txt'
    shell:  '{RSEM}rsem-generate-data-matrix {input} > {output}'

rule ebseq:
    input:  DATA + 'mat.txt'
    output: DATA + 'mat.ebseq'
    shell:  '{RSEM}rsem-run-ebseq {input} 2,2,2,2,2 {output}'

rule fdr:
    input:  DATA + 'mat.ebseq'
    output: DATA + 'de.txt'
    shell:  '{RSEM}rsem-control-fdr {input} 0.05 {output}'

rule all:
    input: DATA + 'mat.ebseq.normalized_data_matrix.genes', DATA + 'tpm.mat.genes', DATA + 'de.txt' #expand( DATA + 'counts/{cellrep}.tsv', cellrep=TSV )
