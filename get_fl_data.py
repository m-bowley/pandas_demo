from fl_data_downloader import FutureLearnData

fl = FutureLearnData("raspberry-pi")

dataset_df = fl.get_dataset(course="introduction-to-web-developmentmac@raspberrypi.org", run=1, dataset="comments")

print(dataset_df)

dataset_df.to_csv('data.csv', index = False, header=True)