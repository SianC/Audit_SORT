import pandas as pd
pd.options.mode.chained_assignment = None

def ground_truth(df):
    a=0
    while a == 0:
        ground_truth = input("Please enter the name of the column containing your ground truth: ")
        if ground_truth in df.columns:
            a=1
        else:
            print("This is not the name of a column in the data. Please try again, ensuring that capital letters and spaces are correct.")
    return ground_truth

def model_result(df, ground_truth):
    a=0
    while a == 0:
        model_result = input("Please enter the name of the column containing your model results: ")
        if model_result in df.columns and model_result != ground_truth:
            a=1
        else:
            print("This is either not the name of a column in the data or you have already chosen it above. Please try again, ensuring that capital letters and spaces are correct.")
    return model_result

def protected_chara(df, ground_truth, model_result):
    a=0
    while a == 0:
        protected_chara = input("Please enter the name of the name of the column containing the characteristic you would like to audit: ")
        if protected_chara in df.columns and protected_chara != model_result and protected_chara != ground_truth:
            a=1
        else:
            print("This is either not the name of a column in the data or you have already chosen it above. Please try again, ensuring that capital letters and spaces are correct.")
    return protected_chara