# Solver-for-Substitution-Cipher
This is a solver for substitution cipher based on n-gram Markov model, beam search and a formulation of CSP

To train model using files in 'data' folder, run:

	python train_model.py

The trained model in stored in 'model' folder.

To test the decipher function with default plaintext, run:

	python test_aicipher.py

To test with your own text, change the variable message in test_aicipher.py.

The pretrained model is stored in folder "model".
Datasets are stored in folder "data", which is specified in our report.
ai_cipher.py is the main decipher function.
csp_speller.py is the external tool to correct output.
narkov_model.py is the learning function.
