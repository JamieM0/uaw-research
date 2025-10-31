import json
import copy
import datetime

def generate_json_objects(template, start, end, fields_to_update):
    """
    Generates a list of JSON objects based on a template and a range of numbers.

    Args:
        template (dict): The template for the JSON object.
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).
        fields_to_update (list): A list of tuples, where each tuple contains:
            - A tuple representing the path to the field to update.
            - A format string for the new value.

    Returns:
        list: A list of generated dictionaries.
    """
    generated_objects = []
    for i in range(start, end + 1):
        new_obj = copy.deepcopy(template)
        for path, format_string in fields_to_update:
            # Navigate to the dictionary to update
            d = new_obj
            for key in path[:-1]:
                d = d[key]
            # Update the value
            d[path[-1]] = format_string.format(i)
        generated_objects.append(new_obj)
    return generated_objects

# --- Configuration ---

# 1. The JSON object template
# The original number will be replaced.
template_object = {
    "id": "equipment_proofing_basket_151",
    "type": "proofing_basket",
    "name": "Proofing Basket (Banneton) #151",
    "emoji": "🧺",
    "properties": { "basket_id": "banneton_151", "shape": "oval", "diameter_inches": None, "length_inches": 10, "width_inches": 6, "height_inches": 3.5, "capacity_min_g": 800, "capacity_max_g": 1000, "capacity_optimal_g": 900, "state": "empty", "contents_loaf_id": None, "location": "banneton_storage_rack", "material": "natural_rattan", "liner_present": None, "liner_state": "clean", "flour_coating": "fresh", "flour_type_used": "rice_flour", "last_used_timestamp": None, "last_cleaned_timestamp": "2025-10-15T14:00:00Z", "uses_since_cleaning": 0, "cleaning_required_after_uses": 50, "last_sun_dried_timestamp": "2025-10-01T12:00:00Z", "sun_drying_interval_days": 30, "condition": "good", "wear_level": 15, "mold_risk": 0.02, "contamination_present": False, "purchase_date": "2023-02-20", "purchase_price_usd": 6.50, "replacement_threshold_wear": 80 }
  }

# 2. The range of numbers to generate
start_range = 151
end_range = 200

# 3. The fields to update
# Each item is a tuple: ( (path_to_key), "format_string" )
# The format string uses standard Python string formatting, e.g., {:03d} for a 3-digit zero-padded number.
fields_to_update_config = [
    (("id",), "equipment_proofing_basket_{:03d}"),
    (("name",), "Proofing Basket (Banneton) #{:03d}"),
    (("properties", "basket_id"), "banneton_{:03d}")
]


# --- Main Execution ---

if __name__ == "__main__":
    generated_list = generate_json_objects(template_object, start_range, end_range, fields_to_update_config)

    # Generate timestamp for the filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_filename = f"output-{timestamp}.json"

    # Save the JSON output to a file
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(generated_list, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated and saved to {output_filename}")
