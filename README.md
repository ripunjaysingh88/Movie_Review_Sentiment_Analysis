# Movie Sentiment Analysis using LSTM
Build the model locally and exposed it as a REST API using Tensorflow Serving and Kubernetes on the Google Cloud Platform. The REST API was then integrated into the flask app to get the model prediction on the web. The flask app was hosted on the compute engine VM instance on GCP.
## Model Performance
. Accuracy: 0.83

. Specificity/True Negative Rate: 0.86

. Sensitivity/True Positive Rate: 0.80

![](images/classification_report.JPG)

## Learning Curve
### Training and Validation Accuracy
![](images/training_validation_accuracy.JPG)

### Training and validation loss
![](images/training_validation_loss.JPG)

## Model Prediction in a Flask App
### Review
![](images/review.png)
### Prediction
![](images/result.png)
