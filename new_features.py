def create_feat(housing):
    housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]
    housing["bedrooms_per_room"] = housing["total_bedrooms"] / housing["total_rooms"]
    housing["population_per_household"] = housing["population"] / housing["households"]
    # corr_matrix = housing.corr()
    # corr_matrix["median_house_value"].sort_values(ascending=False)


# Consider removing this file instead, create features directly in main
