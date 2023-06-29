import os
import pandas as pd

root_directory = "/media/ege/DATA/bamboo/bamboo/RESAMPS"

def extract_ltp_column(csv_file_path):
    df = pd.read_csv(csv_file_path)
    ltp_column = df["ltp"]
    return ltp_column

def save_ltp_column(ltp_column, output_file_path):
    output_directory = os.path.dirname(output_file_path)
    os.makedirs(output_directory, exist_ok=True)

    output_file_name = "LTPS_" + os.path.basename(output_file_path)
    output_file_path = os.path.join(output_directory, output_file_name)

    ltp_column.to_csv(output_file_path, index=False)

def iterate_directories(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv") and file.startswith("SSE"):
                file_path = os.path.join(root, file)
                ltp_column = extract_ltp_column(file_path)
                output_directory = os.path.join(root, "ltps")
                output_file_path = os.path.join(output_directory, file)
                save_ltp_column(ltp_column, output_file_path)

main_folders = ["LastResamp_1Min", "LastResamp_5Min", "LastResamp_10Mins", "MeanResamp_1Min", "MeanResamp_5Min", "MeanResamp_10Mins"]
for main_folder in main_folders:
    main_folder_path = os.path.join(root_directory, main_folder)
    if os.path.isdir(main_folder_path):
        for day_folder in os.listdir(main_folder_path):
            day_folder_path = os.path.join(main_folder_path, day_folder)
            if os.path.isdir(day_folder_path):
                iterate_directories(day_folder_path)
