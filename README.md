# h2o2.ai: DSA4263 (Sense-making Case Analysis: Business and Commerce) Project

Building a production-ready Voice of Customer (VOC) web application.

## Setup Instructions

### Option 1: Docker

#### Deployment

To build Docker image and container, run the following commands on h2o2.ai project folder:

```bash
docker compose up
```

#### Running Pipeline via Notebook

To run all pipelines via notebook, run the following commands on final_presentation folder:

```bash
python3 run_notebook.py
```

#### Running Pipeline via Terminal

To run all pipelines via terminal, run the following commands on h2o2.ai project folder:

```bash
# Preprocess training data. This step should be done before calling train functions.
python3 -m src.preprocessing.transformations

# Train sentiment analysis models
python3 -m src.models.sentiment_analysis.train.train

# Train topic modelling models
python3 -m src.models.topic_modelling.train.train

# Predict test data. Test file path should be supplied from config file.
python3 -m src.models.predict

# Execute unit testing.
python3 -m src.unittest.unit_testing
```

#### Running App

Open the app on http://127.0.0.1:8080/ or http://localhost:8080/

### Option 2: EC2 Instance

Unfortunately, it's not possible to run H2O Wave app on EC2 Instance given the limited access to AWS provided on RLCatalyst as it needs further setup on AWS to open the relative port of EC2 Instance (https://h2o.ai/blog/deploy-a-wave-app-on-an-aws-ec2-instance/).

Hence, EC2 Instance is only used for model training and test prediction purposes.

#### Prerequisites

You will need to have an ubuntu EC2 GPU instance running and connect to the instance via terminal.

Then, copy all files to the instance.

#### Environment Setup

To setup the EC2 instance, run the following commands on h2o2.ai project folder:

```bash
# Install pip for Python 3
sudo apt install python3-pip

# Install all libraries needed
pip install -r requirements.txt
```

#### Running Pipeline via Notebook

To run all pipelines via notebook, run the following commands on final_presentation folder:

```bash
python3 run_notebook.py
```

#### Running Pipeline via Terminal

To run all pipelines via terminal, run the following commands on h2o2.ai project folder:

```bash
# Preprocess training data. This step should be done before calling train functions.
python3 -m src.preprocessing.transformations

# Train sentiment analysis models
python3 -m src.models.sentiment_analysis.train.train

# Train topic modelling models
python3 -m src.models.topic_modelling.train.train

# Predict test data. Test file path should be supplied from config file.
python3 -m src.models.predict

# Execute unit testing.
python3 -m src.unittest.unit_testing
```

### Option 3: Local

#### Prerequisites

You will need to have a valid Python and Conda installation on your system.

#### Environment Setup

To avoid library dependency issues, run the following commands on h2o2.ai project folder:

```bash
# Create environment from file
conda env create -f environment.yml

# Activate created conda environment
conda activate voc_env
```

#### Running Pipeline via Notebook

To run all pipelines via notebook, run the following commands on final_presentation folder:

```bash
python run_notebook.py
```

#### Running Pipeline via Terminal

To run all pipelines via terminal, run the following commands on h2o2.ai project folder:

```bash
# Preprocess training data. This step should be done before calling train functions.
python -m src.preprocessing.transformations

# Train sentiment analysis models
python -m src.models.sentiment_analysis.train.train

# Train topic modelling models
python -m src.models.topic_modelling.train.train

# Predict test data. Test file path should be supplied from config file.
python -m src.models.predict

# Execute unit testing.
python -m src.unittest.unit_testing
```

#### Running App

To start app, run the following commands on h2o2.ai project folder:

```bash
wave run src.app.app
```

Open the app on http://localhost:10101/
