def dump_timestamp_pickle(save_name, model):
    now_code = dt.datetime.now().strftime("%y%m%d%H%M")
    new_file_name = save_name + "_" + now_code + ".pickle"
    duplicate_counter = 1
    while os.path.exists(new_file_name):
        new_file_name = save_name + "_"  + now_code + f"_{str(duplicate_counter)}" + ".pickle"
        duplicate_counter += 1
    pickle.dump(model, open(new_file_name, 'wb'))

def dump_timestamp_csv(save_name, dataframe):
    now_code = dt.datetime.now().strftime("%y%m%d%H%M")
    new_file_name = save_name + "_" + now_code + ".csv"
    duplicate_counter = 1
    while os.path.exists(new_file_name):
        new_file_name = save_name + "_"  + now_code + f"_{str(duplicate_counter)}" + ".csv"
        duplicate_counter += 1
    dataframe.to_csv(new_file_name)

def load_timestamp_pickle():
    pass

def load_timestamp_csv():
    pass

    
