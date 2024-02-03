# Purpose

1. Training a model to classify German search queries (short phrases) from a small dataset
2. Deploying final model using a FastAPI (and dockerized)

# Data

* Provided dataset is consisted of ~37k rows and 6 classes. You can find other exploratory insights about the data in the notebook file
* Dataset was preprocessed to remove duplicates, missing values, non-german characters and labels refactorized to integer values before the training

# Training 

* After splitting the data into train/valid/test sets, a pretrained language model is fine tuned. For this, an open source German BERT model of MDZ Digital Library team (dbmdz) at the Bavarian State Library is used.
* Using AutoModelForSequenceClassification class of transformers library we get our BertSequenceClassification model to be trained for downstream task of multiclass classification (rather than mask filling in its pretraining)
* Training arguments set to be in optimal ranges (i.e. batch size: 32, epochs: 3, learning rate: 1e-5, optimizer: Adam, and so on)
* Reported training and validation loss can be seen in outputs in the notebook file, training stopped before validation loss started increasing

# Evaluation Results

              precision    recall  f1-score   support

          ft       0.91      0.93      0.92       917
         pkg       0.91      0.88      0.90       943
          ch       0.90      0.89      0.89       325
          mr       0.87      0.82      0.84       440
         cnc       0.75      0.81      0.78       197
          ct       0.91      0.94      0.93       470

    accuracy                           0.89      3292
   macro avg       0.88      0.88      0.88      3292
weighted avg       0.89      0.89      0.89      3292

# Deploying with FastAPI and dockerization

# Future Work

* Techniques for better generalization in unknown data with different distribution than provided data will be explored such as: lowering batch size with trade off of longer training time, increasing data size either collecting more data or augmenting the set with synthetic data created by a large language model
* Multilanguage model can be implemented to have a more robost model in case of different future use cases
* Different REST API practices can be investigated as the projected application's needs may vary (event-based or two way communication, etc.)
