from pyedflib import highlevel
import os
import pandas as pd


def search_annotations_edf(dirname): 
    filenames = os.listdir(dirname)
    filenames = [file for file in filenames if file.endswith("Hypnogram.edf")]
    return filenames

def search_signals_edf(dirname): 
    filenames = os.listdir(dirname)
    filenames = [file for file in filenames if file.endswith("PSG.edf")]
    return filenames

path = './sample/' 
signals_edf_list = search_signals_edf(path)
annotations_edf_list = search_annotations_edf(path)

file_path = os.path.join(path, signals_edf_list[0])
data = highlevel.read_edf(file_path)
labels = [item['label'] for item in data[1]]
df = pd.DataFrame(data[0]).T
df.columns = labels
df.to_csv("./sample/converted.csv")
print("완료:", signals_edf_list[0])


# 여러 EDF를 변환하고 싶을 때 사용
# for i in range(len(search_signals_edf)):
#     file_path = os.path.join(path, signals_edf_list[i])
#     data = highlevel.read_edf(file_path)
# labels = [item['label'] for item in data[1]]
# df = pd.DataFrame(data[0]).T
# df.columns = labels
# df.to_csv(f"./sample/converted{i}.csv")
# print("완료:", signals_edf_list[i])







# for i in range(len(signals_edf_list)):
#     file_path = os.path.join(path, signals_edf_list[i])
#     try:
#         with open(out_path, 'w', newline='') as csvfile:
#             csv_writer = csv.writer(csvfile)


#     except Exception as e:
#         print("error")


