from setuptools import setup, find_packages

setup(
    name='bot_detector',
    version='0.0.1',
    packages=['bot_detector'],
    install_requires=[
        'pandas==1.3.4',
        'sklearn==0.0',
        'joblib==1.1.0',
        'python-decouple==3.5'
    ],
    entry_points={
        "console_scripts": [
            "apply_pipeline = bot_detector.apply_pipeline:main",
            "fit_pipeline = bot_detector.fit_pipeline:main"
        ]
    },
    package_data={
        "": ["pipelines/pipeline.pkl"],
    }
)