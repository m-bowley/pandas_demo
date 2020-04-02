from fl_data_downloader import FutureLearnData

fl = FutureLearnData("raspberry-pi")

dataset_df = fl.get_dataset(course="web-development", run=1, dataset="step-activity")

print(dataset_df)

dataset.to_csv('data.csv', index = False, header=True)
