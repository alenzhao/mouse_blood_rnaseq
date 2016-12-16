import os
PWD = os.getcwd().split('code')[0]
DATA = PWD + 'data/'
WORK = PWD + 'working/'

RSEM = '/home/evansj/me/condas/anaconda3/bin/'

# mel w/ dmos https://www.encodeproject.org/experiments/ENCSR000CWF/
# g1eer4 w/ estradiol https://www.encodeproject.org/experiments/ENCSR181KQJ/
# mouse erythroblast 14.5 days https://www.encodeproject.org/experiments/ENCSR000CHS/
#   not diff strain at 5 wks https://www.encodeproject.org/experiments/ENCSR661TLW/
#       'eryth.1':'https://www.encodeproject.org/files/ENCFF233KBA/@@download/ENCFF233KBA.tsv',
#       'eryth.2':'https://www.encodeproject.org/files/ENCFF054XRZ/@@download/ENCFF054XRZ.tsv',
# thymus https://www.encodeproject.org/experiments/ENCSR000BYV/
# adrenal gland https://www.encodeproject.org/experiments/ENCSR000BYX/

TSV = {'mel.2':'https://www.encodeproject.org/files/ENCFF474ALI/@@download/ENCFF474ALI.tsv',
       'mel.1':'https://www.encodeproject.org/files/ENCFF272ZXV/@@download/ENCFF272ZXV.tsv',
       'g1eer4.1':'https://www.encodeproject.org/files/ENCFF783TPN/@@download/ENCFF783TPN.tsv',
       'g1eer4.2':'https://www.encodeproject.org/files/ENCFF166TVS/@@download/ENCFF166TVS.tsv',
       'eryth.1':'https://www.encodeproject.org/files/ENCFF169TWH/@@download/ENCFF169TWH.tsv',
       'eryth.2':'https://www.encodeproject.org/files/ENCFF685KKI/@@download/ENCFF685KKI.tsv',
       'adrenal.1':'https://www.encodeproject.org/files/ENCFF038WVC/@@download/ENCFF038WVC.tsv',
       'adrenal.2':'https://www.encodeproject.org/files/ENCFF633PPD/@@download/ENCFF633PPD.tsv',
       'thymus.1':'https://www.encodeproject.org/files/ENCFF543RQD/@@download/ENCFF543RQD.tsv',
       'thymus.2':'https://www.encodeproject.org/files/ENCFF289YEA/@@download/ENCFF289YEA.tsv'
}

CELLS = list( TSV.keys() )
CELLS.sort()

