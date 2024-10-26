import pandas as pd

def load_arxiv_data(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            print("File content:\n", content)  # Log file content for debugging

        df = pd.read_csv(file_path)
        if df.empty:
            raise ValueError("The dataframe is empty.")

        print(f"Dataframe loaded successfully with {len(df)} rows.")
        return df

    except Exception as e:
        print(f"Error loading data: {e}")
        return None
