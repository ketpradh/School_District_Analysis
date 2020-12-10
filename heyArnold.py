 # import dependencies
import pandas as pd  # Create a data frame with given columns and value
hey_arnold = pd.DataFrame(
    {"Character_in_show": ["Arnold", "Gerald", "Helga", "Phoebe", "Harold", "Eugene"],
     "color_of_hair": ["blonde", "black", "blonde", "black", "unknown", "red"],
     "Height": ["average", "tallish", "tallish", "short", "tall", "short"],
     "Football_Shaped_Head": [True, False, False, False, False, False]
     })

hey_arnold  # Rename columns to clean up the look  # Organize columns into a more logical order