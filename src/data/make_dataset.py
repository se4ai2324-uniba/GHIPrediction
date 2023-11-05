import pandas as pd
import great_expectations as gx
class Dataset:
  
#Create CSV
    def finalDf(self, df, df1, df2, name):
        data = [df, df1, df2]
        final = pd.DataFrame()
        final = pd.concat(data)
        final.to_csv(f"data/raw/{name}", index = False)
        df = pd.read_csv(f"data/raw/{name}", delimiter = ',')
        return df
    

dataset = Dataset()
dfB1 = pd.read_csv('data/raw/2017.csv', delimiter = ',')
dfB2 = pd.read_csv('data/raw/2018.csv', delimiter = ',')
dfB3 = pd.read_csv('data/raw/2019.csv', delimiter = ',')
dfBari = dataset.finalDf(dfB1, dfB2, dfB3, 'FinaleBari.csv')


context = gx.get_context()
#datasource = context.sources.add_pandas('finaleBari_data')
datasource = context.datasources["finaleBari_data"]
#asset = datasource.add_csv_asset('finaleBari_asset', filepath_or_buffer='data/raw/FinaleBari.csv')
asset = datasource.assets[0]
batch_request = asset.build_batch_request()

context.add_or_update_expectation_suite("make_dataset")

validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name='make_dataset',
)

validator.expect_column_to_exist("GHI")
validator.expect_column_to_exist("Temperature")
validator.expect_column_to_exist("DNI")
validator.expect_column_to_exist("Relative Humidity")

validator.expect_column_values_to_not_be_null("GHI")
validator.expect_column_values_to_not_be_null("Temperature")
validator.expect_column_values_to_not_be_null("DNI")
validator.expect_column_values_to_not_be_null("Relative Humidity")


validator.save_expectation_suite(discard_failed_expectations=False)
checkpoint = context.add_or_update_checkpoint(
    name="make_dataset_checkpoint",
    expectation_suite_name='make_dataset',
    validator=validator,
)
checkpoint_result = checkpoint.run()
context.view_validation_result(checkpoint_result)
print(context.build_data_docs())

