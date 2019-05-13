"""
https://public.wmo.int/en/media/news/global-carbon-budget-released
"""

import pandas as pd


def print_results(datasource, year1, year2, emissions):
    land_use_change_scale_factor = 0.395
    emissions *= (1.0 + land_use_change_scale_factor)
    print(f"{datasource} emissions for {year1}-{year2} {emissions:.0f} GtC ({emissions*3.667:.0f} GtCO2)")


# Read in data
data = pd.read_csv("cdiac_data/nation.1751_2014.csv", skiprows=[1,2,3])

# Sum CO2 emissions for world and convert to GtC
col = "Total CO2 emissions from fossil-fuels and cement production (thousand metric tons of C)"
world_emissions = data[col].sum()/1000000
print_results("World", 1751, 2014, world_emissions)

# Compute world emissions in different centuries
for century in [1700, 1800, 1900, 2000]:
    century_data = data[(data["Year"] >= century) & (data["Year"] < century + 100)]
    century_emissions = century_data[col].sum()/1000000
    print_results("World", century, century+100, century_emissions)

# Select data for UK
uk_data = data[data["Nation"] == "UNITED KINGDOM"]

# Sum CO2 emissions for UK and convert to GtC
uk_emissions = uk_data[col].sum()/1000000

print_results("UK", 1751, 2014, uk_emissions)
