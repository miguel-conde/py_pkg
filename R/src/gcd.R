library(readr)

gcd <- function() {
  
  if (file.exists(HOUSING_DATA_FILE)) {
    housing_data <- read_csv(HOUSING_DATA_FILE)
  } else {
    housing_data <- read_csv(URI_DATASET)
    write_csv(housing_data, file = HOUSING_DATA_FILE)
  }
  
  return(housing_data)
}