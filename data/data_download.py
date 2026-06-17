import os
import shutil
import kagglehub

print("Downloading dataset...")

# Download latest version
dataset_path = kagglehub.dataset_download(
    "berkanoztas/synthetic-transaction-monitoring-dataset-aml"
)

print(f"Downloaded to: {dataset_path}")

# Create local data directory
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

# Copy all files from kagglehub cache to data/
for file_name in os.listdir(dataset_path):
    src = os.path.join(dataset_path, file_name)
    dst = os.path.join(output_dir, file_name)

    if os.path.isfile(src):
        shutil.copy2(src, dst)
        print(f"Copied: {file_name}")

print(f"\nDataset files are now available in: {os.path.abspath(output_dir)}")