provider "null" {}

data "null_data_source" "values" {
    inputs = {
        "roles" = "role1"
    }
}

output "null_data" {
    value = data.null_data_source.values.outputs
}