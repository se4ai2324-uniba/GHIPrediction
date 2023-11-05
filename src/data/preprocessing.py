
import pandas as pd
from sklearn.preprocessing import RobustScaler
import great_expectations as gx

#Clean csv
class Preprocessing:
  def preProcessing(self):
    df = pd.read_csv('data/raw/FinaleBari.csv', header=0) 
    i = df[((df.GHI == 0))].index
    df = df.drop(i)
    df = df.drop(columns = ['DHI','Year','Month','Day','Hour', 'Minute', 'Precipitable Water', 'Dew Point', 'Cloud Type', 'Surface Albedo','Wind Speed','Pressure'])
    df = df.fillna(0)
    return df

#Scalarization
  def scalarization(self):
    scaler = RobustScaler()
    tmp = df.drop('GHI', axis = 1)
    scaler.fit(tmp)
    dfTransformed = scaler.transform(tmp)
    return dfTransformed
  


preprocessing = Preprocessing()

df = preprocessing.preProcessing()
ghi = df.GHI

dfS = preprocessing.scalarization()

dfNew = pd.DataFrame(dfS)
dfNew.to_csv('data/processed/PreprocessedData.csv', header=['Temperature', 'DNI', 'Relative Humidity'])
ghi.to_csv('data/processed/GHI.csv')

context = gx.get_context()
#datasource = context.sources.add_pandas('postProcessed_data')
datasource = context.datasources["postProcessed_data"]
#asset = datasource.add_csv_asset('postProcessed_asset', filepath_or_buffer='data/processed/PreprocessedData.csv')
asset = datasource.assets[0]
batch_request = asset.build_batch_request()

context.add_or_update_expectation_suite("preprocessed")

validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name='preprocessed',
)

validator.expect_column_to_exist('Temperature')
validator.expect_column_values_to_not_be_null("Temperature")
validator.save_expectation_suite(discard_failed_expectations=False)
checkpoint = context.add_or_update_checkpoint(
    name="preprocessed_checkpoint",
    expectation_suite_name='preprocessed',
    validator=validator,
)
checkpoint_result = checkpoint.run()
context.view_validation_result(checkpoint_result)





