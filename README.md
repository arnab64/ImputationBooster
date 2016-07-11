###Recursive partitioning spectral biclustering based Imputation boosting framework (RPSBImpute)

Introduction
---------------------------
RPSBImpute is a framework for boosting the performance of imputation for existing imputation algorithms. It was my undergraduate thesis. Not all code are provided here, however, I have included the code for KnnImpute and the one for boosting it with RPSBImpute. The detailed report is available [here](https://drive.google.com/open?id=0B-ZfncBkRrSUeE1MbTRhLU9pT3M)

Usage
------------
- 'rpsbknn.py' is the file for RPSB based Knn boosting. This is the code which is to be executed. It takes 'input_w_missing.txt' as input.
- 'knn.py' performs KNNimpute. It is called by rpsbknn.py
- 'getstuff.py' is used by rpsbknn.py for getting parameters.
- 'compare.py' computes the NRMSE of the imputation. It takes 'original.txt' and 'output.txt' as input.
