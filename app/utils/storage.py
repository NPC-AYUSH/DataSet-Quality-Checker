import uuid

# In-memory store (simple version)
DATASET_STORE = {}

def save_dataset(df):
    dataset_id = str(uuid.uuid4())
    DATASET_STORE[dataset_id] = df
    return dataset_id

def get_dataset(dataset_id):
    return DATASET_STORE.get(dataset_id)
