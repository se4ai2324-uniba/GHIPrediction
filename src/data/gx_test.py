"""module for great expectations testing"""
import great_expectations as gx
MAX = 981
MIN = 0
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

validator.expect_column_values_to_be_between("GHI", MIN, MAX)

validator.save_expectation_suite(discard_failed_expectations=False)
checkpoint = context.add_or_update_checkpoint(
    name="make_dataset_checkpoint",
    expectation_suite_name='make_dataset',
    validator=validator,
    run_name_template="time_%H_%M_%S-make_dataset",
)
checkpoint_result = checkpoint.run()
context.view_validation_result(checkpoint_result)


context = gx.get_context()
#datasource = context.sources.add_pandas('postProcessed_data')
datasource = context.datasources["postProcessed_data"]
#asset = datasource.add_csv_asset('postProcessed_asset',
# filepath_or_buffer='data/processed/PreprocessedData.csv')
asset = datasource.assets[0]
batch_request = asset.build_batch_request()

context.add_or_update_expectation_suite("preprocessed")

validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name='preprocessed',
)

validator.expect_column_values_to_not_be_null("Temperature")
validator.expect_column_values_to_not_be_null("DNI")
validator.expect_column_values_to_not_be_null("Relative Humidity")

validator.expect_column_values_to_be_of_type("Temperature", 'float')
validator.expect_column_values_to_be_in_type_list("DNI", ['float','int'])
validator.expect_column_values_to_be_of_type("Relative Humidity", 'float')

validator.save_expectation_suite(discard_failed_expectations=False)
checkpoint = context.add_or_update_checkpoint(
    name="preprocessed_checkpoint",
    expectation_suite_name='preprocessed',
    validator=validator,
    run_name_template="time_%H_%M_%S-preprocessed",
)
checkpoint_result = checkpoint.run()
context.view_validation_result(checkpoint_result)

print(context.build_data_docs())
