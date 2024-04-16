import csv
import pickle
import numpy as np


def dynamic_classification():
    """
    Create the dict needed for the classification from the CSV files
    :return: dict
    """
    with open('model_classif/sous-categories.csv',
              newline='') as sous_categories:
        reader1 = csv.reader(sous_categories)
        # Lire les données et stocker dans un dictionnaire
        data_sous_categories = {row[0]: row[1] for row in reader1}

    # Ouvrir le deuxième fichier CSV
    with open('model_classif/categ.csv', newline='') as categories:
        reader2 = csv.reader(categories)
        # Lire les données et stocker dans un dictionnaire
        data_categories = {row[0]: row[1] for row in reader2}

    return data_categories, data_sous_categories


def classify_main_description(data, data_categories, data_sous_categories):
    """
    Classify all the main and the description from the weather data
    :param data: weather data
    :param data_categories: dict with all the main classified
    :param data_sous_categories: dict with all the description classified
    :return: weather data classified
    """
    data_classified = []
    for e, element in enumerate(data['main']):
        for cat in data_categories:
            if cat == element:
                data['main'][e] = float(data_categories.get(cat))
                break
    for e, element in enumerate(data['description']):
        for cat in data_sous_categories:
            if cat == element:
                data['description'][e] = float(data_sous_categories.get(cat))
                break

    for key, value in data.items():
        if key is not "pressure":
            for element in value:
                data_classified.append(element)
    return data_classified


def model_train(data_classified):
    """
    Use the model to get the class of the clothes and accessories
    :param data_classified:
    :return: list of the answer of the two model [VETEMENT,ACCESSOIRE]
    """
    num_samples = len(data_classified) // 240
    data_array = np.array(data_classified).reshape(num_samples, -1)
    with open('RF_V.pkl', 'rb') as f:
        model_V = pickle.load(f)
    with open('RF_A.pkl', 'rb') as f:
        model_A = pickle.load(f)
    return (model_V.predict(data_array).tolist() + model_A.predict(data_array).tolist())


def run_model(data):
    """
    Main function use to run every part of the model
    :param data: data from the weather_api
    :return: list of the answer of the two model
    """
    data_categories, data_sous_categories = dynamic_classification()
    data_classified = classify_main_description(data, data_categories, data_sous_categories)
    return model_train(data_classified)
