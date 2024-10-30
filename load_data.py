
import pickle
import traceback

def load_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            print(f"Data loaded successfully from {file_path}, data size is {len(data)}")
            return data
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        traceback.print_exc()
        return None

normal_data = load_data('normal_traffic.pickle')