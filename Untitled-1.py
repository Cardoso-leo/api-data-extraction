def extract_api_to_parquet(api_url: str, output_path: str):
    import requests
    import pandas as pd
    from datetime import datetime

    response = requests.get(api_url, timeout=10)
    response.raise_for_status()

    df = pd.DataFrame(response.json())
    df["extraction_date"] = datetime.now()

    df.to_parquet(output_path, engine="pyarrow", index=False)
    return df


extract_api_to_parquet(
    "https://jsonplaceholder.typicode.com/posts",
    "data/posts.parquet"
)
