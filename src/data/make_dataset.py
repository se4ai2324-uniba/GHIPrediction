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
validator = context.sources.pandas_default.read_csv('data/raw/FinaleBari.csv')
validator.expect_column_values_to_not_be_null("GHI")
validator.expect_column_values_to_not_be_null("Temperature")
validator.expect_column_values_to_not_be_null("DNI")
validator.save_expectation_suite()
checkpoint = context.add_or_update_checkpoint(
    name="my_quickstart_checkpoint",
    validator=validator,
)
checkpoint_result = checkpoint.run()
context.view_validation_result(checkpoint_result)
print(context.build_data_docs())

