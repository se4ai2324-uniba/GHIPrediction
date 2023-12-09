# Dataset Card

## Dataset Summary:
The dataset contains three years of measurements at 30 minutes intervals from 2017 to 2019 in Bari. The data gathered concerns Humidity,
Temperature, Global Horizontal Irradiance (GHI) and Direct Normal Irradiance (DNI).

![Immagine 2023-12-09 132049](https://github.com/se4ai2324-uniba/GHIPrediction/assets/48125720/065c71ee-8081-4653-aaba-1fc8a12f254f)


## Data Source:
Data come from the [**National Solar Radiation Data Base**](https://nsrdb.nrel.gov/data-viewer). \
The NSRDB ([Sengupta et al., 2018](https://doi.org/10.1016/j.rser.2018.03.003)) is a high temporal and spatial resolution dataset consisting of the three most widely used measurements of solar radiation—*global horizontal, direct normal, and diffuse horizontal irradiance*—as well as other meteorological data. 


## Data Preprocessing:
In order to use the dataset, we should first clean the data and manipulate it, in particular: the most relevant features are selected ignoring the rest. These selected features, namely temperature, dni and relative humidity 
are the ones that are most correlated with GHI.
Then the rows with GHI equal to 0 are deleted, because these represent the night time, in which there is no solar irradiance, so it is not useful for our prediction.
Following this, any missing data points (NaN values) are replaced by zeros. Finally, a uniform scaling operation is applied to the data using the "robust scaler", that helps with the prediction. 
The resulting dataset, after the Pre-Processing, is presented in the table provided.


| Temperature  | DNI | GHI | Relative Humidity %
| --------- |:-------------:|:-------------:|:-------------:|
| 7.2      | 179    | 17     | 71.14 | 
| 10.8      | 767    | 289     | 58.44 | 
| 12.0      |  159   | 227     | 53.15 |
| 12.7     | 250     | 288     | 49.86 |
