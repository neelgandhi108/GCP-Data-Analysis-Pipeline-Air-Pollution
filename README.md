# GCP Data Analysis Pipeline : Air Pollution

## Project Overview

The objective of this data engineering initiative is to scrutinize air quality metrics across 100 cities in Poland. The data originates from the Weather API ([https://openweathermap.org/api](https://openweathermap.org/api)), which delivers real-time, forecasted, and historical air pollution metrics worldwide. The API reports on various pollutants like CO, NO, NO2, O3, SO2, NH3, as well as particulate matters PM2.5 and PM10.

### Technologies Utilized

-   Cloud Services: [Google Cloud](https://cloud.google.com/)
-   Infrastructure Provisioning: [Terraform](https://www.terraform.io/)
-   Data Orchestration: [Prefect](https://www.prefect.io/)
-   Data Storage: [Google Cloud Storage](https://cloud.google.com/storage)
-   Data Processing: [DBT](https://www.getdbt.com/)
-   Data Warehousing: [BigQuery](https://cloud.google.com/bigquery)
-   Data Visualization: [Google Looker Studio](https://cloud.google.com/looker)

## Architecture Diagram

![Air Pollution Data Flow](https://github.com/neelgandhi108/GCP-Data-Analysis-Pipeline-Air-Pollution/blob/main/Assets/GCP.png)

## Project Aim

This project seeks to identify the cities with the worst air quality using the Air Quality Index (AQI), which ranks air pollution levels based on the concentration of pollutants measured in μg/m3. The evaluation leverages data spanning from November 27, 2020, to assess air quality trends across these cities over time.

| Qualitative name | Index | SO2 (μg/m3) | NO2 (μg/m3) | PM10 (μg/m3) | PM2.5 (μg/m3) | O3 (μg/m3) | CO (μg/m3) |
|------------------|-------|-------------|-------------|---------------|----------------|------------|-------------|
| Good             | 1     | 0-20        | 0-40        | 0-20          | 0-10           | 0-60      | 0-4400    |
| Fair             | 2     | 20-80       | 40-70       | 20-50         | 10-25          | 60-100    | 4400-9400 |
| Moderate         | 3     | 80-250      | 70-150      | 50-100        | 25-50          | 100-140   | 9400-12400|
| Poor             | 4     | 250-350     | 150-200     | 100-200       | 50-75          | 140-180   | 12400-15400|
| Very Poor        | 5     | >350        | >200        | >200          | >75            | >180      | >15400    |

## Analysis Steps

![Dashboard1](https://github.com/neelgandhi108/GCP-Data-Analysis-Pipeline-Air-Pollution/blob/main/Assets/Air_Quality_Dashboard.png)
![Dashboard2](https://github.com/neelgandhi108/GCP-Data-Analysis-Pipeline-Air-Pollution/blob/main/Assets/Air_Quality_Leaderboard.png)


-   **Data Retrieval**: Obtaining air pollution data for the 100 cities from the Air Pollution API.
-   **AQI Calculation**: Computing the AQI for each city using the formula outlined in the API's documentation.
-   **City Ranking**: Assigning rankings to cities based on their AQI levels and identifying the most polluted.
-   **Visualization**: Displaying the findings using Google Looker Studio.

## Data Description

The Air Pollution API provides a comprehensive set of data about various air pollutants and particulate matters. This dataset includes measurements such as:

-   **dt**: Date and time of the measurements.
-   **Carbon_Monoxide_CO**: Carbon monoxide levels in ppm.
-   **Nitric_oxide_NO**: Nitric oxide levels in ppb.
-   **Nitrogen_Dioxide_NO2**: Nitrogen dioxide levels in ppb.
-   **Ozone_O3**: Ozone levels in ppm.
-   **Sulfur_Dioxide_SO2**: Sulfur dioxide levels in ppb.
-   **PM2_5**: Fine particulate matter (<2.5 micrometers) concentration in µg/m³.
-   **PM10**: Coarse particulate matter (<10 micrometers) concentration in µg/m³.
-   **NH3**: Ammonia levels in ppb.
-   **City_index**: Numeric identifier for each city.

## Technical Details

### Repository Structure

-   `/blocks`: Python scripts for Prefect blocks creation.
-   `/data`: Scripts and JSON files for city coordinates.
-   `/dbt`: DBT project configuration files and models.
-   `/flow`: Prefect workflow scripts.
-   `/images`: Repository images.
-   `/terraform`: Terraform configuration files for infrastructure setup.
-   `/README.md`: Overview of the project.
-   `/setup_gcp.md`: Guide for setting up Google Cloud Platform account.
-   `/setup_vm.md`: Instructions for configuring a virtual machine on GCP.

### Infrastructure as Code with Terraform

Terraform is used for setting up necessary cloud resources like storage buckets and BigQuery datasets.

### Orchestration with Prefect

Prefect manages data retrieval and processing workflows, integrating seamlessly with the cloud services.

### Data Transformation with DBT

DBT handles the transformation of raw data into structured formats suitable for analysis and reporting.

### Visual Insights with Looker Studio

The results are visualized in Google Looker Studio, providing interactive dashboards to explore the air quality data.

## Execution Steps

For detailed setup and operational instructions, refer to `setup_gcp.md` and `setup_vm.md`. The pipeline is designed to run efficiently within the Google Cloud environment, utilizing various services and tools for end-to-end data management and visualization.
