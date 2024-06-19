import json
import pandas as pd

# Constants
DATA_FILE = "/content/drive/My Drive/MovieGenre/data/processed/primary_colors.json"
FEATURES_FILE = "/content/drive/My Drive/MovieGenre/data/processed/features.csv"

# Load data
def load_data(data_file):
    with open(data_file, 'r') as f:
        data = json.load(f)
    return data

# Generate labels based on primary colors
def generate_label(primary_colors):
    # Use the first primary color to generate a label
    return int(sum(primary_colors[0]) // 3)

# Process data to build features
def build_features(data):
    rows = []
    for dataset in ['train', 'test']:
        for item in data[dataset]:
            row = {"image": item["image"]}
            row["label"] = generate_label(item["primary_colors"])
            for i, color in enumerate(item["primary_colors"]):
                row[f"color_{i}_r"] = color[0]
                row[f"color_{i}_g"] = color[1]
                row[f"color_{i}_b"] = color[2]
            rows.append(row)
    return rows

# Save features to a CSV file
def save_features(features, features_file):
    df = pd.DataFrame(features)
    df.to_csv(features_file, index=False)
    print(f"Features saved to {features_file}")

# Main function
def main():
    data = load_data(DATA_FILE)
    features = build_features(data)
    save_features(features, FEATURES_FILE)

if __name__ == "__main__":
    main()
