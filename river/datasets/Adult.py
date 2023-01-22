from river import stream

from . import base


class Adult(base.FileDataset):

    def __init__(self):
        super().__init__(
            n_samples=20000,
            n_features=58,
            task=base.BINARY_CLF,
            filename="proccessed_adult.csv", 
        )

    def __iter__(self):
        return stream.iter_csv(
            self.path,
            target="Class-label",
            converters={ 'workclass_ Federal-gov': float, 'workclass_ Local-gov' : float,
       'workclass_ Private': float, 'workclass_ Self-emp-inc': float,
       'workclass_ Self-emp-not-inc': float, 'workclass_ State-gov': float,
       'workclass_ Without-pay': float, 'education_ 10th': float, 'education_ 11th': float,
       'education_ 12th': float, 'education_ 1st-4th': float, 'education_ 5th-6th': float,
       'education_ 7th-8th': float, 'education_ 9th': float, 'education_ Assoc-acdm': float,
       'education_ Assoc-voc': float, 'education_ Bachelors': float, 'education_ Doctorate': float,
       'education_ HS-grad': float, 'education_ Masters': float, 'education_ Preschool': float,
       'education_ Prof-school': float, 'education_ Some-college': float,
       'Maritial-status_ Divorced': float, 'Maritial-status_ Married-AF-spouse': float,
       'Maritial-status_ Married-civ-spouse': float,
       'Maritial-status_ Married-spouse-absent': float,
       'Maritial-status_ Never-married': float, 'Maritial-status_ Separated': float,
       'Maritial-status_ Widowed': float, 'occupation_ Adm-clerical': float,
       'occupation_ Armed-Forces': float, 'occupation_ Craft-repair': float,
       'occupation_ Exec-managerial': float, 'occupation_ Farming-fishing': float,
       'occupation_ Handlers-cleaners': float, 'occupation_ Machine-op-inspct': float,
       'occupation_ Other-service': float, 'occupation_ Priv-house-serv': float,
       'occupation_ Prof-specialty': float, 'occupation_ Protective-serv': float,
       'occupation_ Sales': float, 'occupation_ Tech-support': float,
       'occupation_ Transport-moving': float, 'relationship_ Husband': float,
       'relationship_ Not-in-family': float, 'relationship_ Other-relative': float,
       'relationship_ Own-child': float, 'relationship_ Unmarried': float,
       'relationship_ Wife': float, 'age': float, 'race': float, 'sex': float, 'Capital-gain': float,
       'Capital-loss': float, 'Hours-per-week': float, 'country': float,
                "Class-label": lambda x: x == "1",
            },
        )
