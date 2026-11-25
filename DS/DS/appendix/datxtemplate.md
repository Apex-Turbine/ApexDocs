# Datx Template

The datx template allows users to supply their own custom keyword/value pairs that will be included in the recorded .datx_index files.
These template files are simple text files with each line containing one keyword/value pair.
The keyword/value pairs are separated by a "=" character.

The datx template file may contain a global section and multiple per channel sections. The layout of these sections must follow the layout of a
regular datx file header or a datx index file.

example datx template file:

```
mykeyword1=valueA
mykeyword2=valueB
mykeyword3=valueC
```

And extension of the datx template file allows for user to map Data Point Setup fields to datx keywords.

Data Point Setup fields:

```
%dpFlags%
%dpInfo%
%testCell%
%testDate%
%testId%
%testLocation%
%testFacility%
%testArticle%
%testInfo%
%operatorName%
%operatorPhone%
%operatorEmail%
%organization%
%build%
%classify%
%engine%
%engineInfo%
%model%
%stand%
%maintainerName%
%maintainerPhone%
%maintainerEmail%
%systemName%
%extra%
%created%
%modified%
%fileVersion%
%programVersion%
```

datx keywords NOT mappable to Data Point Setup fields:

```
record_system_name
program_version
test_file_name
function_type
file_data_type
data_representation
test_date_time
test_date_time_IRIG
active_channels
```

Example Data Point Setup mapped to datx keywords:

```
data_owner=%operatorName%
engine_serial_number=%%
part_no/id=%engineInfo%
specimen_build=%build%
specimen_id=%dpFlags%
specimen_model=%model%
specimen_name=%testArticle%
structure_engr=%operatorName%
structure_test_engr=%operatorName%
test_description=%testInfo%
test_engr=%operatorName%
test_id=%testId%
test_location=%testLocation%
test_number=%dpNumber%
test_operator=%operatorName%
test_stand_number=%stand%
test_title=%organization%
test_type=%testId%
test_classification=%classify%
test_operator_email=%operatorEmail%
```

Datx keywords provided by APEX and not setable by datx template:

```
"C00_cal_conversion_coeffs"
"C00_cal_factor_type"
"C00_cal_factors"
"C00_cal_method"
"C00_chan_number"
"C00_dev_type"
"C00_id_tag"
"C00_mfgr_name"
"C00_model_name"
"C00_reference_delay"
"C01_cal_conversion_coeffs"
"C01_cal_factor_type"
"C01_cal_factors"
"C01_cal_method"
"C01_chan_number"
"C01_dev_type"
"C01_id_tag"
"C01_input_eu"
"C01_mfgr_name"
"C01_model_name"
"C01_output_eu"
"C01_reference_delay"
"acquisition_points"
"cal_coeff_1"
"cal_coeff_2"
"cal_corr_factor"
"channel_#"
"channel_label"
"data_representation"
"data_start_time"
"display_units"
"event_0001"
"event_0002"
"external_gain"
"file_data_type"
"function_type"
"internal_gain"
"measurement_type"
"program_version"
"record_system_name"
"response_units"
"sample_rate"
"tachometer_ratio"
"tachometer_threshold"
"tare_eu"
"tare_volts"
"test_date_time"
"test_date_time_IRIG"
"transducer_type"
"volts_per_count"
```
