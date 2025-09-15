import os
from functools import lru_cache
from typing import Any
from huggingface_hub import hf_hub_download
import joblib

HF_REPO_ID  = os.getenv("HF_REPO_ID",  "Marintosti/attrition")
HF_TOKEN    = os.getenv("HF_TOKEN")      

@lru_cache(maxsize=1)
def load_model(name) -> Any:
    local_path = hf_hub_download(
        repo_id=HF_REPO_ID,
        filename=f"{name}.joblib",
        token=HF_TOKEN,
        local_files_only=False,
    )
    return joblib.load(local_path)
