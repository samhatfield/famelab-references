import pandas as pd


def print_results(datasource, year1, year2, emissions):
    land_use_change_scale_factor = 0.33
    emissions *= (1.0 + land_use_change_scale_factor)
    print(f"{datasource} emissions for {year1}-{year2} {emissions/3.667:.0f} GtC ({emissions:.0f} GtCO2)")


# Read in data
data = pd.read_csv("ceds_data/CO2_CEDS_emissions_by_country_v2017_05_18.csv")

# Sum CO2 emissions for world and convert to GtC
world_emissions = data.loc[:,"X1750":].sum().sum()/1000000
print_results("World", 1751, 2014, world_emissions)

# Compute world emissions in different centuries
for century in [("X1750","X1800"), ("X1800","X1900"), ("X1900","X2000"), ("X2000","X2014")]:
    century_data = data.loc[:,century[0]:century[1]]
    century_emissions = century_data.sum().sum()/1000000
    print_results("World", century[0], century[1], century_emissions)

# Select data for UK
uk_data = data[data["country"] == "gbr"]

# Sum CO2 emissions for UK and convert to GtC
uk_emissions = uk_data.loc[:,"X1750":].sum().sum()/1000000

print_results("UK", 1751, 2014, uk_emissions)
