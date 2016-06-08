# rpsb

'rpsbknn.py' is the file for RPSB based Knn boosting. This is the code which is to be executed. It takes 'input_w_missing.txt' as input.

'knn.py' performs KNNimpute. It is called by rpsbknn.py
'getstuff.py' is used by rpsbknn.py for getting parameters.
'compare.py' computes the NRMSE of the imputation. It takes 'original.txt' and 'output.txt' as input.
