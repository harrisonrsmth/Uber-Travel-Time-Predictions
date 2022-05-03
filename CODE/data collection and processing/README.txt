This folder contains links to the datasets we used and steps to process the data as we did.

To download Uber Movement Data and Atlanta Census Tract GeoJSON, go to https://movement.uber.com/explore/atlanta/travel-times/query?si=166&ti=&ag=censustracts&dt[tpb]=ALL_DAY&dt[wd;]=1,2,3,4,5,6,7&dt[dr][sd]=2020-03-01&dt[dr][ed]=2020-03-31&cd=&sa;=&sdn=&lang=en-US, click on "Download data", "ALL DATA", and then download "Travel Times By Date By Hour Buckets (All Days)". Then go to "GEO BOUNDARIES" and check the box and download ATLANTA_CENSUSTRACTS.JSON.

For weather data, go to https://www.ncei.noaa.gov/access/search/data-search/local-climatological-data?startDate=2020-01-01T00:00:00&endDate=2020-03-31T23:59:59&bbox=33.873,-84.516,33.623,-84.266, click "Select" next to the dataset, and then at the bottom click the radio button next to "csv" and click "Configure and Add." Now click "Edit Data Types" and only check "Daily Average Dry Bulb Temperature," "Daily Average Wind Speed," and "Daily Precipitation." Click "Accept" and "Add Order to Cart." Complete your checkout and wait for an email containing your data, which you will download. 

Now open OpenRefine (https://openrefine.org/download.html) and load this dataset into a new project. Then, under "Undo/Redo," click "Apply..." and load in the temp_precip_wind_ops.json file. Export the dataset. 

Follow the queries in uber_movement_processing.sql and load the Uber Movement data when prompted using MySQL Workbench (https://www.mysql.com/products/workbench/). Export the final table as data.csv.

Open the csv_to_parquet.ipynb notebook and run the cells in it to convert your csv dataset to a parquet file.

Open the data_processing_testing.ipynb file and run each cell to see the testing of several back end functions and how the dataset is processed to a version in which the neural network can be trained on.

Finally, run the cells in uber_regression_nn.ipynb to create and train the neural network. After the weights are saved in checkpoint.pt, be sure the move it over to the checkpoints folder in the "backend" directory.

The data is now properly processed!