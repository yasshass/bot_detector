### Bot Detector

##### The project structure
 ```
.
├── README.md
├── bot_detector
│   ├── __init__.py
│   ├── apply_pipeline.py : the module tha calculates the predictions
│   ├── data.py
│   ├── fit_pipeline.py
│   ├── pipelines
│   │   └── pipeline.pkl
│   ├── pipelines.py
│   └── settings.py
├── bot_detector.toml
├── data
│   ├── fake_users.csv
│   └── fake_users_test.csv
├── notebooks
│   └── Bot\ detector.ipynb
├── requirements.txt
├── setup.py
├── tests
│   ├── __init__.py
│   └── bot_detector.py
└── tox.ini
 ```
#### Features Engineering and model training
- In the notebooks folder, there is a notebook gathering the features Engineering and the model training steps.
We could reach a perfect accuracy on test without trying different models and tuning the parameters.

 
 #### Configuration, tests and build
 - For configuration a settings.py is used with the decouple library to read variables set in an .env file or  as environment variables.
 - For tests, unittest is used for unit testing with tox to automate the testing. The written test is a simple example.
 - For build, setuptools is used to package the project, exposing 2 entrypoints 'calculate_bmi'.
    - apply_pipeline exposing the main function of apply_pipeline.py, it takes 2 arguments; the path to the input data csv and the path where to write predictions
    - fit_pipeline exposing the main function of fit_pipeline.py, it takes 2 arguments, the path to the input csv to fit and the path where to save the pipeline pickle  
    example : apply_pipeline data/fake_users.csv data/predictions.csv
 
 #### Use
 - Without installing the package : python bot_detector/apply_pipeline.py data/fake_users.csv data/predictions.csv
 - After building and installing the package : apply_pipeline data/fake_users.csv data/predictions.csv