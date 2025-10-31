# Parkside Bakery Simulation Analysis

## 1. CUSTOM OBJECT TYPES NEEDED

### dough_batch
**Why separate type:** Dough has complex lifecycle states (mixed → bulk fermenting → shaped → proofing → baked) that generic "resource" can't capture. Need to track fermentation progress, temperature evolution, and quality indicators.

**Key properties:**
- `batch_id`: Unique identifier (e.g., "country_sourdough_batch_1_tue")
- `recipe_type`: Links to product (e.g., "country_sourdough")
- `state`: Enum (mixed, bulk_fermenting, shaped, proofing, baking, cooling, finished, spoiled)
- `temperature`: Current temp in °F (critical for fermentation)
- `mix_time`: Timestamp when mixing completed
- `fermentation_start`: When bulk fermentation began
- `fermentation_target_duration`: Minutes expected (e.g., 270 for 4.5 hours)
- `fold_count`: How many stretch-and-folds performed (0-4)
- `next_fold_time`: When next fold is due
- `shaped_time`: When shaping completed
- `proof_start`: When final proof began
- `proof_location`: "retarder" or "room_temp"
- `target_loaf_count`: How many loaves this batch makes
- `weight_kg`: Total dough weight
- `quality_score`: 0-100 (degrades if temps wrong, timing off)
- `over_proofed`: Boolean flag
- `under_proofed`: Boolean flag

**Why different from standard types:** 
- Resource is consumed/depleted linearly
- Dough transforms through states with time-dependent chemistry
- Quality degrades if constraints violated
- Requires active monitoring and interventions (folds)

### levain_culture
**Why separate type:** Starter/levain has biological lifecycle - needs regular feeding, has activity level, can be healthy or weak. Different from simple ingredient.

**Key properties:**
- `culture_id`: "mother_starter" or "production_levain_tue"
- `type`: "mother" or "production"
- `health`: 0-100 (affects fermentation reliability)
- `activity_level`: "peak", "rising", "falling", "dormant"
- `last_fed`: Timestamp
- `next_feeding_due`: Timestamp
- `temperature`: Current temp
- `volume_increase`: Percentage (indicates readiness)
- `location`: "walk_in" or "ambient"
- `weight_g`: Current weight
- `hydration_percent`: 100 for Parkside

**Why different:** 
- Self-perpetuating (small amount becomes more)
- Has health/vitality that affects all downstream production
- Requires maintenance tasks separate from production

### oven_deck
**Why separate type:** Each deck operates independently with own temp control, capacity, and state. Not just "equipment" - it's a spatial container with thermal properties.

**Key properties:**
- `deck_id`: "deck_1", "deck_2", "deck_3"
- `parent_oven`: "main_oven"
- `temperature_current`: °F
- `temperature_target`: °F
- `state`: "off", "preheating", "ready", "baking", "cooling", "door_open"
- `capacity_pans`: 3 (full-size sheet pans)
- `capacity_loaves`: 8-10 depending on size
- `contents`: Array of loaf IDs currently baking
- `bake_start_time`: When current bake began
- `bake_end_time`: When current bake completes
- `steam_available`: Boolean
- `last_steam_time`: Timestamp
- `recovery_time_minutes`: 10-15 (how long to return to temp after cold load)

**Why different from equipment:**
- Equipment is monolithic; oven has 3 independent sub-units
- Each deck has spatial capacity (number/arrangement of loaves)
- Thermal state changes continuously
- Requires individual monitoring and loading decisions

### proofing_basket
**Why separate type:** Bannetons are containers that hold individual loaves during proof, track which loaf is where, cleanliness state.

**Key properties:**
- `basket_id`: "banneton_001" through "banneton_200"
- `shape`: "round" or "oval"
- `capacity_g`: 900-1000
- `state`: "empty", "occupied", "dirty", "cleaning"
- `contents_loaf_id`: ID of loaf currently in basket (if occupied)
- `location`: "bench", "retarder", "staging"
- `flour_coating`: "fresh", "depleted" (needs re-flouring)

**Why different:**
- It's a spatial container that moves through workflow
- Tracks 1:1 relationship with individual loaves
- Has cleanliness state separate from contents

### fermentation_container
**Why separate type:** Large tubs that hold bulk-fermenting dough batches. Track fill level, temperature, cleanliness.

**Key properties:**
- `container_id`: "cambro_22qt_1" through "cambro_22qt_12"
- `capacity_liters`: 22
- `state`: "empty", "in_use", "dirty", "cleaning"
- `contents_batch_id`: Which batch is fermenting inside
- `fill_level_percent`: Visual indicator for volume increase
- `marked_volume`: Reference mark for "doubled"
- `temperature`: Current temp of contents

**Why different:**
- Temporary container (not consumed like resource)
- Multiple units that need tracking
- Visual volume indicators critical for fermentation assessment

### cooling_rack
**Why separate type:** Mobile racks with multiple positions, spatial capacity constraint, need to track what's on which shelf.

**Key properties:**
- `rack_id`: "cooling_rack_1" through "cooling_rack_4"
- `tier_count`: 20
- `tiers_occupied`: Array of tier numbers with contents
- `capacity_pans`: 20 full-size
- `current_load_pans`: How many pans currently on rack
- `location`: "cooling_zone", "packaging_area", "storage"
- `mobility`: "locked" or "mobile"

**Why different:**
- Multi-position container with spatial layout
- Loaves cool at different rates on different tiers
- Mobile asset that moves through workflow

### storage_location
**Why separate type:** Walk-in cooler, retarder, dry storage have different environmental properties and capacity limits.

**Key properties:**
- `location_id`: "walk_in_cooler", "proofing_retarder", "dry_storage"
- `type`: "refrigerated", "climate_controlled", "ambient"
- `temperature`: Current temp
- `temperature_target`: Set point
- `humidity_percent`: Current humidity
- `capacity_cubic_feet`: Physical volume
- `capacity_utilized_percent`: How full
- `contents`: Array of object IDs stored inside
- `state`: "normal", "malfunction", "door_open", "alarm"
- `power_consumption_kwh`: Current draw

**Why different:**
- Environmental controller (maintains temp/humidity)
- Spatial container with capacity limits
- Can malfunction (scenario 2 in complications)

## 2. STANDARD OBJECTS BY TYPE

### ACTORS

#### marcus_chen
```
type: "actor"
properties:
  - role: "owner_head_baker"
  - hourly_rate: null (salaried, $4333/month draw)
  - annual_salary: 52000
  - shift_start: "03:45"
  - shift_end: "14:00"
  - work_days: ["tuesday", "wednesday", "thursday", "friday", "saturday", "monday_admin"]
  - skills: ["starter_maintenance", "levain_building", "all_mixing", "oven_management", "quality_control", "shaping_expert", "scheduling", "wholesale_management", "equipment_maintenance"]
  - experience_years: 15
  - servesafe_certified: true
  - current_task: null
  - location: null
  - fatigue_level: 0-100
```

#### rachel_martinez
```
type: "actor"
properties:
  - role: "production_baker"
  - hourly_rate: 19.50
  - guaranteed_hours_weekly: 40
  - overtime_rate: 29.25 (time and half)
  - shift_start: "04:30"
  - shift_end: "14:30"
  - work_days: ["tuesday", "wednesday", "thursday", "friday", "saturday"]
  - skills: ["mixer_operation", "bulk_fermentation", "dough_dividing", "preshaping", "final_shaping_all", "baguette_specialist", "fold_cycles", "wholesale_packing"]
  - experience_years: 5
  - servesafe_certified: true
  - current_task: null
  - location: null
```

#### david_kim
```
type: "actor"
properties:
  - role: "baker_shift_supervisor"
  - hourly_rate: 18.00
  - guaranteed_hours_weekly: 38
  - shift_start: "05:00"
  - shift_end: "13:30"
  - work_days: ["wednesday", "thursday", "friday", "saturday", "sunday"]
  - skills: ["oven_monitoring", "focaccia_production", "ciabatta_production", "specialty_breads", "foh_restocking", "quality_checks", "backup_shaping", "sunday_opening"]
  - experience_years: 3
  - servesafe_certified: true
  - current_task: null
  - location: null
  - backup_training_level: 70 (can cover 70% of Rachel's duties)
```

#### sarah_thompson
```
type: "actor"
properties:
  - role: "foh_lead"
  - hourly_rate: 16.50
  - hours_weekly: 30
  - shift_start: "06:30"
  - shift_end: "12:30"
  - work_days: ["wednesday", "thursday", "friday", "saturday", "sunday"]
  - skills: ["customer_service", "pos_operation", "display_management", "bread_slicing", "packaging", "social_media", "online_orders", "inventory_counting", "wholesale_handoffs"]
  - experience_years: 2
  - current_task: null
  - location: "front_of_house"
```

### EQUIPMENT (using custom types where appropriate)

#### main_oven
```
type: "equipment"
properties:
  - equipment_id: "lbc_se932_3deck"
  - category: "oven"
  - decks: ["deck_1", "deck_2", "deck_3"] (references to oven_deck objects)
  - power_rating_kw: 33
  - voltage: 208
  - phase: 3
  - connected_load_kw: 33
  - operating_consumption_kw: 22-28 (varies)
  - preheat_time_minutes: 60-75 (to 500F)
  - state: "off", "preheating", "ready", "in_use", "cooling"
  - steam_system: true
  - steam_burst_seconds: 3 or 8
  - purchase_date: "2023-03-01"
  - purchase_price: 17738
  - installation_cost: 4200
  - maintenance_schedule: "quarterly"
  - last_maintenance: timestamp
  - next_maintenance_due: timestamp
  - maintenance_cost_per_visit: 180
  - monthly_energy_cost: 180
  - depreciation_years: 7
  - failure_probability: 0.02 (2% per simulation week)
```

#### spiral_mixer
```
type: "equipment"
properties:
  - equipment_id: "american_eagle_ae4030"
  - category: "mixer"
  - capacity_flour_kg: 11.8
  - capacity_dough_kg: 20
  - practical_batch_kg: 15-18
  - motor_hp_agitator: 1.5
  - motor_hp_bowl: 0.5
  - power_consumption_kw: 2.8
  - low_speed_rpm: 120
  - high_speed_rpm: 240
  - state: "idle", "mixing_low", "mixing_high", "resting", "cleaning", "malfunction"
  - bowl_attached: true
  - bowl_state: "clean", "dirty", "in_use"
  - cycle_time_minutes: 12-15 (average)
  - load_unload_time_minutes: 3-5
  - max_throughput_batches_per_hour: 3-4
  - maintenance_weekly: "belt_tension_check"
  - maintenance_monthly: "gear_lubrication"
  - maintenance_daily: "cleaning"
  - purchase_date: "2023-02-01"
  - purchase_price: 7200
  - condition: "used"
```

#### walk_in_cooler (using storage_location custom type)
```
type: "storage_location"
properties:
  - location_id: "walk_in_cooler"
  - subcategory: "refrigeration"
  - model: "amerikooler_qs0608"
  - interior_dimensions_ft: "6x8x7.5"
  - volume_cubic_feet: 360
  - temperature_setpoint: 38
  - temperature_range: "35-42"
  - current_temperature: 38
  - humidity_percent: 80
  - power_consumption_kw: 2.1
  - duty_cycle_percent: 40
  - alarm_threshold_temp: 42
  - alarm_state: "normal"
  - contents: [] (array of object IDs)
  - capacity_weight_lbs: 800 (dry goods)
  - capacity_perishables_lbs: 150
  - capacity_racks: 2 (20-pan rolling racks)
  - current_utilization_percent: 0
  - monthly_energy_cost: 65
  - purchase_price: 8400
  - installation_included: true
  - state: "operational", "malfunction", "door_open"
```

#### proofing_retarder (using storage_location custom type)
```
type: "storage_location"
properties:
  - location_id: "proofing_retarder"
  - subcategory: "climate_controlled"
  - model: "avantco_hpi1836"
  - capacity_pans: 36
  - pan_spacing_inches: 3
  - practical_capacity_loaves: 180-200 (in bannetons on pans)
  - temperature_range: "38-115"
  - proof_mode_temp: 85-115
  - retard_mode_temp: 38-50
  - current_mode: "retard"
  - current_temperature: 40
  - humidity_range: "30-100"
  - current_humidity: 85
  - power_consumption_kw: 1.575
  - insulated: true
  - energy_savings_percent: 35
  - monthly_energy_cost: 28
  - contents: [] (array of basket IDs)
  - capacity_utilized_percent: 0
  - state: "operational", "malfunction"
  - load_time: "18:00-21:00"
  - unload_time: "05:00-11:00"
```

#### reach_in_fridge_1
```
type: "equipment"
properties:
  - equipment_id: "true_t49hc_unit1"
  - category: "refrigeration"
  - capacity_cubic_feet: 49
  - sections: 2
  - shelves: 6
  - temperature_range: "33-38"
  - temperature_setpoint: 36
  - current_temperature: 36
  - power_consumption_kw: 1.2
  - energy_star: true
  - daily_kwh: 1.02
  - contents_typical: ["whole_milk", "butter", "eggs", "honey", "backup_yeast"]
  - location: "near_mixing_station"
  - state: "operational"
  - purchase_price: 1900 (half of 3800 for both units)
  - condition: "used"
```

#### reach_in_fridge_2
```
type: "equipment"
properties:
  - equipment_id: "true_t49hc_unit2"
  - category: "refrigeration"
  - capacity_cubic_feet: 49
  - sections: 2
  - shelves: 6
  - temperature_setpoint: 36
  - current_temperature: 36
  - contents_typical: ["kalamata_olives", "specialty_ingredients", "backup_perishables"]
  - location: "near_shaping_bench"
  - state: "operational"
  - purchase_price: 1900
```

#### primary_shaping_bench
```
type: "equipment"
properties:
  - equipment_id: "shaping_table_96x30"
  - category: "work_surface"
  - dimensions_inches: "96x30x34"
  - material: "16_gauge_stainless"
  - capacity_lbs: 600
  - surface_temp: "ambient" (68-72F, follows room)
  - state: "clean", "in_use", "dirty", "sanitizing"
  - current_occupant: null (actor ID using bench)
  - contents: [] (items currently on surface)
  - backsplash: true
  - undershelf: true
  - location: "production_zone"
  - purchase_price: 502
```

#### mixing_prep_table
```
type: "equipment"
properties:
  - equipment_id: "prep_table_60x24"
  - category: "work_surface"
  - dimensions_inches: "60x24x34"
  - material: "18_gauge_stainless"
  - capacity_lbs: 500
  - mobile: true
  - casters: true
  - state: "clean", "in_use", "dirty"
  - location: "mixing_zone"
  - purchase_price: 224
```

#### display_case
```
type: "equipment"
properties:
  - equipment_id: "structural_concepts_co57d"
  - category: "display"
  - type: "dry_bakery_case"
  - tiers: 3
  - dimensions_inches: "77x35x27"
  - capacity_cubic_feet: 21
  - capacity_loaves: 35-40
  - power_consumption_watts: 20 (LED lighting only)
  - state: "open", "closed"
  - current_contents: [] (array of product IDs)
  - contents_by_tier: {1: [], 2: [], 3: []}
  - location: "front_counter"
  - purchase_price: 2850
```

#### pos_system
```
type: "equipment"
properties:
  - equipment_id: "square_pos_terminal"
  - category: "point_of_sale"
  - hardware_components: ["ipad", "cash_drawer", "receipt_printer", "card_reader", "ups_battery"]
  - hardware_cost: 1092
  - software: "square_for_retail"
  - monthly_subscription: 60
  - transaction_fee_percent: 2.6
  - transaction_fee_fixed: 0.10
  - features: ["inventory_tracking", "customer_data", "sales_reporting", "employee_clock_in", "online_integration"]
  - state: "operational", "offline"
  - cash_drawer_float: 150
  - current_cash: 150
```

### RESOURCES (consumables)

#### bread_flour_organic
```
type: "resource"
properties:
  - resource_id: "flour_bread_organic"
  - category: "ingredient"
  - unit: "kg"
  - current_quantity: 100
  - reorder_point: 200 (when to trigger order)
  - reorder_quantity: 600 (weekly order)
  - unit_cost: 1.79
  - storage_location: "walk_in_cooler"
  - storage_container: "sealed_50kg_bags"
  - shelf_life_days: 180
  - supplier: "regional_flour_distributor"
  - delivery_day: "tuesday"
  - protein_percent: 12.5
  - organic: true
```

#### bread_flour_conventional
```
type: "resource"
properties:
  - resource_id: "flour_bread_conventional"
  - category: "ingredient"
  - unit: "kg"
  - current_quantity: 150
  - reorder_point: 200
  - reorder_quantity: 300
  - unit_cost: 1.19
  - storage_location: "walk_in_cooler"
  - protein_percent: 12.5
  - organic: false
```

#### whole_wheat_flour_organic
```
type: "resource"
properties:
  - resource_id: "flour_whole_wheat_organic"
  - unit: "kg"
  - current_quantity: 50
  - reorder_point: 50
  - reorder_quantity: 150
  - unit_cost: 1.87
  - storage_location: "walk_in_cooler"
```

#### rye_flour
```
type: "resource"
properties:
  - resource_id: "flour_rye"
  - unit: "kg"
  - current_quantity: 30
  - reorder_point: 20
  - reorder_quantity: 100
  - unit_cost: 2.21
  - storage_location: "walk_in_cooler"
  - specialty: true
```

#### water_filtered
```
type: "resource"
properties:
  - resource_id: "water_municipal_filtered"
  - category: "ingredient"
  - unit: "liters"
  - current_quantity: 1000 (effectively unlimited from tap)
  - unit_cost: 0.003
  - source: "municipal_water_filtered"
  - temperature_available: "variable" (can be heated/cooled)
```

#### sea_salt
```
type: "resource"
properties:
  - resource_id: "salt_fine_sea"
  - unit: "kg"
  - current_quantity: 25
  - reorder_point: 10
  - reorder_quantity: 50
  - unit_cost: 0.85
  - storage_location: "dry_storage"
```

#### instant_yeast
```
type: "resource"
properties:
  - resource_id: "yeast_instant_saf"
  - unit: "kg"
  - current_quantity: 2
  - reorder_point: 0.5
  - reorder_quantity: 3
  - unit_cost: 37.40
  - storage_location: "reach_in_fridge_1"
  - storage_requirement: "refrigerated_after_opening"
  - shelf_life_days: 180
```

#### whole_milk
```
type: "resource"
properties:
  - resource_id: "milk_whole_commercial"
  - unit: "liters"
  - current_quantity: 10
  - reorder_point: 5
  - reorder_quantity: 40
  - unit_cost: 2.55
  - storage_location: "reach_in_fridge_1"
  - perishable: true
  - shelf_life_days: 7
  - delivery_day: "tuesday"
```

#### butter_unsalted
```
type: "resource"
properties:
  - resource_id: "butter_unsalted_84percent"
  - unit: "kg"
  - current_quantity: 10
  - reorder_point: 5
  - reorder_quantity: 35
  - unit_cost: 12.75
  - storage_location: "reach_in_fridge_1"
  - perishable: true
  - shelf_life_days: 30
```

#### olive_oil_evoo
```
type: "resource"
properties:
  - resource_id: "olive_oil_bulk_evoo"
  - unit: "liters"
  - current_quantity: 15
  - reorder_point: 10
  - reorder_quantity: 35
  - unit_cost: 13.60
  - storage_location: "dry_storage"
  - container: "5_liter_tins"
```

#### kalamata_olives
```
type: "resource"
properties:
  - resource_id: "olives_kalamata_bulk"
  - unit: "kg"
  - current_quantity: 8
  - reorder_point: 5
  - reorder_quantity: 20
  - unit_cost: 11.05
  - storage_location: "reach_in_fridge_2"
  - preparation_required: "drain_pat_dry_chop"
```

#### fresh_rosemary
```
type: "resource"
properties:
  - resource_id: "rosemary_fresh_local"
  - unit: "kg"
  - current_quantity: 1
  - reorder_point: 0.5
  - reorder_quantity: 3
  - unit_cost: 34.00 (seasonal variation)
  - storage_location: "reach_in_fridge_2"
  - perishable: true
  - shelf_life_days: 7
  - source: "local_farm"
```

#### seeds_mixed
```
type: "resource"
properties:
  - resource_id: "seeds_sunflower_flax_sesame"
  - unit: "kg"
  - current_quantity: 5
  - reorder_point: 3
  - reorder_quantity: 10
  - unit_cost: 13.60
  - storage_location: "dry_storage"
  - preparation_required: "toast_and_cool"
  - mixture_ratio: {"sunflower": 0.45, "flax": 0.30, "sesame": 0.25}
```

#### brown_sugar
```
type: "resource"
properties:
  - resource_id: "sugar_brown_bulk"
  - unit: "kg"
  - current_quantity: 10
  - reorder_point: 5
  - reorder_quantity: 15
  - unit_cost: 3.74
  - storage_location: "dry_storage"
```

#### packaging_bread_bags
```
type: "resource"
properties:
  - resource_id: "bags_kraft_6x3x12"
  - unit: "count"
  - current_quantity: 5000
  - reorder_point: 2000
  - reorder_quantity: 10000
  - unit_cost: 0.14
  - storage_location: "packaging_area"
```

#### packaging_baguette_bags
```
type: "resource"
properties:
  - resource_id: "bags_baguette_long"
  - unit: "count"
  - current_quantity: 1500
  - reorder_point: 1000
  - reorder_quantity: 3000
  - unit_cost: 0.12
  - storage_location: "packaging_area"
```

#### packaging_labels
```
type: "resource"
properties:
  - resource_id: "stickers_branded_round"
  - unit: "count"
  - current_quantity: 8000
  - reorder_point: 5000
  - reorder_quantity: 15000
  - unit_cost: 0.05
  - storage_location: "packaging_area"
```

#### electricity
```
type: "resource"
properties:
  - resource_id: "utility_electricity"
  - unit: "kwh"
  - current_quantity: 999999 (effectively unlimited from grid)
  - unit_cost: 0.12
  - monthly_average_consumption: 4333
  - monthly_average_cost: 520
```

#### natural_gas
```
type: "resource"
properties:
  - resource_id: "utility_natural_gas"
  - unit: "therms"
  - current_quantity: 999999
  - unit_cost: 1.20 (estimated)
  - monthly_average_cost: 180
  - seasonal_variation: true
```

### PRODUCTS (finished goods)

#### country_sourdough
```
type: "product"
properties:
  - product_id: "country_sourdough_900g"
  - product_name: "Classic Country Sourdough"
  - shape: "batard"
  - target_weight_g: 900 (baked)
  - dough_weight_g: 1000 (pre-bake)
  - retail_price: 9.00
  - wholesale_price: 5.75
  - ingredient_cost: 2.72
  - gross_margin_retail: 0.698
  - gross_margin_wholesale: 0.527
  - production_days: ["tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  - tuesday_friday_quantity: 50
  - saturday_quantity: 75
  - sunday_quantity: 60
  - bake_temp_f: 500 (initial), 480 (during bake)
  - bake_time_minutes: 38
  - cooling_time_hours: 3
  - shelf_life_days: 3
  - scoring_pattern: "deep_cross"
  - requires_steam: true
  - levain_percent: 20
  - hydration_percent: 75
```

#### whole_grain_sourdough
```
type: "product"
properties:
  - product_id: "whole_grain_sourdough_900g"
  - product_name: "Whole Grain Sourdough"
  - shape: "boule"
  - target_weight_g: 900
  - dough_weight_g: 980
  - retail_price: 9.50
  - wholesale_price: 6.00
  - ingredient_cost: 3.21
  - tuesday_friday_quantity: 25
  - saturday_quantity: 35
  - sunday_quantity: 30
  - bake_temp_f: 490
  - bake_time_minutes: 40
  - cooling_time_hours: 4
  - scoring_pattern: "radial_star"
```

#### seeded_multigrain
```
type: "product"
properties:
  - product_id: "seeded_multigrain_850g"
  - product_name: "Seeded Multigrain"
  - shape: "batard"
  - target_weight_g: 850
  - dough_weight_g: 950
  - retail_price: 10.00
  - wholesale_price: 6.50
  - ingredient_cost: 3.76
  - tuesday_friday_quantity: 20
  - saturday_quantity: 30
  - sunday_quantity: 25
  - bake_temp_f: 490
  - bake_time_minutes: 38
  - seed_coating: "optional_top"
```

#### baguette
```
type: "product"
properties:
  - product_id: "baguette_300g"
  - product_name: "Classic Baguette"
  - shape: "traditional_baguette"
  - target_weight_g: 300
  - dough_weight_g: 325
  - retail_price: 4.00
  - wholesale_price: 2.60
  - ingredient_cost: 0.73
  - daily_quantity: 40
  - saturday_quantity: 50
  - production_method: "poolish_same_day"
  - bake_temp_f: 480
  - bake_time_minutes: 22-25
  - cooling_time_minutes: 30-45
  - peak_quality_hours: 4-8
  - scoring_pattern: "single_diagonal_slash"
  - requires_steam: "heavy"
```

#### ciabatta
```
type: "product"
properties:
  - product_id: "ciabatta_600g"
  - product_name: "Rustic Ciabatta"
  - shape: "slipper"
  - target_weight_g: 600
  - dough_weight_g: 650
  - retail_price: 7.50
  - wholesale_price: 4.90
  - ingredient_cost: 1.89
  - tuesday_saturday_quantity: 15
  - sunday_quantity: 20
  - production_method: "biga_method"
  - hydration_percent: 85
  - bake_temp_f: 480
  - bake_time_minutes: 28-30
  - cooling_time_hours: 1.5
  - scoring: "none" (natural cracking)
  - shaping: "minimal_handling"
```

#### whole_wheat_sandwich
```
type: "product"
properties:
  - product_id: "whole_wheat_sandwich_850g"
  - product_name: "Whole Wheat Sandwich Loaf"
  - shape: "pan_loaf"
  - target_weight_g: 850
  - dough_weight_g: 920
  - retail_price: 8.50
  - wholesale_price: 5.50
  - ingredient_cost: 5.29
  - gross_margin_retail: 0.378
  - gross_margin_wholesale: 0.038
  - tuesday_friday_quantity: 20
  - saturday_quantity: 30
  - sunday_quantity: 25
  - enriched: true
  - leavening: "commercial_yeast"
  - bake_temp_f: 360
  - bake_time_minutes: 35-38
  - cooling_time_hours: 3-4
  - requires_steam: false
  - pan_size: "9x5_inch"
  - slicing_requested_frequently: true
```

#### olive_rosemary_sourdough
```
type: "product"
properties:
  - product_id: "olive_rosemary_900g"
  - product_name: "Olive & Rosemary Sourdough"
  - shape: "boule"
  - target_weight_g: 900
  - dough_weight_g: 1000
  - retail_price: 10.50
  - wholesale_price: 6.75
  - ingredient_cost: 3.77
  - production_days: ["wednesday", "friday", "saturday"]
  - quantity_per_day: 15
  - saturday_quantity: 18
  - bake_temp_f: 490
  - bake_time_minutes: 38-40
  - scoring_pattern: "cross_or_decorative"
  - add_ins: ["kalamata_olives_12_percent", "fresh_rosemary"]
```

#### rye_sourdough
```
type: "product"
properties:
  - product_id: "rye_sourdough_40percent_900g"
  - product_name: "Rye Sourdough (40%)"
  - shape: "boule"
  - target_weight_g: 900
  - dough_weight_g: 1000
  - retail_price: 9.75
  - wholesale_price: 6.25
  - ingredient_cost: 2.98
  - production_days: ["thursday", "saturday"]
  - quantity_per_day: 12
  - rye_percent: 40
  - hydration_percent: 80
  - bake_temp_f: 475
  - bake_time_minutes: 45-50
  - cooling_time_hours: 6-8 (critical - DO NOT package early)
  - scoring_pattern: "simple_cross"
  - difficulty: "high"
  - primary_baker: "marcus_chen" (requires experience)
  - caraway_seeds_optional: true
```

#### rosemary_focaccia
```
type: "product"
properties:
  - product_id: "focaccia_rosemary_portion"
  - product_name: "Rosemary Focaccia"
  - shape: "sheet_cut_6_portions"
  - sheet_weight_g: 1200
  - portion_weight_g: 200
  - retail_price_per_portion: 4.50
  - wholesale_price_per_portion: 3.00
  - ingredient_cost_per_portion: 0.26
  - gross_margin_retail: 0.942
  - production_days: ["tuesday", "thursday", "saturday"]
  - sheets_per_day: 4
  - portions_per_day: 24
  - production_method: "cold_ferment_preferred"
  - bake_temp_f: 450
  - bake_time_minutes: 20-25
  - requires_steam: false
  - topping: ["olive_oil_generous", "flaky_sea_salt", "fresh_rosemary"]
  - primary_baker: "david_kim"
```

#### seasonal_sweet_focaccia
```
type: "product"
properties:
  - product_id: "focaccia_seasonal_portion"
  - product_name: "Seasonal Sweet Focaccia"
  - shape: "sheet_cut_6_portions"
  - portion_weight_g: 200
  - retail_price_per_portion: 5.00-5.50 (seasonal)
  - wholesale_price_per_portion: 3.25-3.50
  - ingredient_cost_per_portion: 0.34-0.51 (varies by topping)
  - production_days: ["wednesday", "friday", "sunday"]
  - sheets_per_day: 3
  - portions_per_day: 18
  - topping_seasonal: {
      "fall": "grape_thyme",
      "late_summer": "fig_honey",
      "winter": "caramelized_onion",
      "spring": "asparagus_lemon"
    }
  - bake_temp_f: 450
  - bake_time_minutes: 20-25
```

## 3. PROCESSES AND INTERACTIONS

### STARTER MAINTENANCE PROCESSES

#### daily_starter_feeding
**Timing:** Every production day, 4:00-4:30 AM
**Actor:** marcus_chen
**Duration:** 30 minutes

**Objects involved:**
- `mother_starter` (levain_culture)
- `flour_bread_organic` (resource)
- `flour_whole_wheat_organic` (resource)
- `water_filtered` (resource)
- `mixing_prep_table` (equipment)

**Interactions:**
```
starter_assessment:
  - Check mother_starter.health (0-100)
  - Check mother_starter.activity_level
  - If health < 60: flag for multiple refreshing feedings
  
discard_portion:
  - Remove 200g from mother_starter.weight_g
  - Set aside for experiments (not true waste)
  
feed_starter:
  - Add to mother_starter:
    - flour_bread_organic: -170g
    - flour_whole_wheat_organic: -30g
    - water_filtered: -200g (at 80F)
  - Mix until homogeneous
  - mother_starter.weight_g = 600g (200 old + 200 flour + 200 water)
  - mother_starter.last_fed = current_timestamp
  - mother_starter.next_feeding_due = current_timestamp + 8-12 hours
  - mother_starter.activity_level = "rising"
  - mother_starter.location = "ambient_68F"
  
cleanup:
  - mixing_prep_table.state = "dirty" → "cleaning" → "clean"
```

**Property changes:**
- mother_starter.weight_g: delta +200g (net after discard and feeding)
- mother_starter.last_fed: set to current_timestamp
- flour_bread_organic.current_quantity: delta -0.17kg
- flour_whole_wheat_organic.current_quantity: delta -0.03kg
- water_filtered.current_quantity: delta -0.2L

#### production_levain_build
**Timing:** 4:30-5:00 AM, for next day's production
**Actor:** marcus_chen
**Duration:** 30 minutes active work

**Objects involved:**
- `mother_starter` (levain_culture)
- `production_levain_tomorrow` (levain_culture) - new object created
- `flour_bread_organic` (resource)
- `flour_whole_wheat_organic` (resource)
- `water_filtered` (resource)
- `fermentation_container` (fermentation_container type)

**Interactions:**
```
calculate_needs:
  - Tomorrow's sourdough recipes need 4.5kg levain total
  - Build batch: 500g ripe starter + 2000g water + 2000g flour = 4500g
  
create_levain_object:
  - New levain_culture object: production_levain_tomorrow
  - type: "production"
  - weight_g: 4500
  - hydration_percent: 100
  - mix_time: current_timestamp
  - activity_level: "dormant" (just mixed)
  - target_peak_time: current_timestamp + 6-8 hours
  - location: "ambient_78F" (near oven exhaust)
  
resource_deductions:
  - mother_starter.weight_g: -500g
  - flour_bread_organic: -1700g (85% of 2000g)
  - flour_whole_wheat_organic: -300g (15% of 2000g)
  - water_filtered: -2000g at 80F
  
container_tracking:
  - Select fermentation_container where state = "clean"
  - container.state = "in_use"
  - container.contents_batch_id = "production_levain_tomorrow"
  - container.fill_level_percent = 40 (will rise to 80-100 at peak)
  - container.marked_volume = "double_reference"
  
monitoring_schedule:
  - production_levain_tomorrow.check_time_1 = timestamp + 4 hours
  - production_levain_tomorrow.check_time_2 = timestamp + 6 hours
  - production_levain_tomorrow.check_time_3 = timestamp + 8 hours
```

**Property changes:**
- Create new `production_levain_tomorrow` object
- mother_starter.weight_g: delta -500g
- flour_bread_organic.current_quantity: delta -1.7kg
- water_filtered.current_quantity: delta -2L
- fermentation_container.state: "clean" → "in_use"

### MIXING PROCESSES

#### autolyse_country_sourdough_batch1
**Timing:** 5:30 AM Tuesday-Friday, 5:45 AM Saturday
**Actor:** rachel_martinez
**Duration:** 2 minutes active, 40 minutes rest

**Objects involved:**
- `spiral_mixer` (equipment)
- New `dough_batch` object created
- `flour_bread_organic` (resource)
- `flour_whole_wheat_organic` (resource)
- `water_filtered` (resource)

**Interactions:**
```
pre_check:
  - Verify spiral_mixer.state = "idle"
  - Verify spiral_mixer.bowl_state = "clean"
  
create_batch:
  - New dough_batch object: country_sourdough_batch1_tue
  - recipe_type: "country_sourdough"
  - state: "autolyse"
  - weight_kg: 22.5 (half of 45kg total)
  - target_loaf_count: 25 (half of 50)
  
scale_ingredients:
  - flour_bread_organic: -9.11kg (85% of 10.72kg flour)
  - flour_whole_wheat_organic: -1.61kg (15%)
  - water_filtered: -8.04kg (calculated for 76F dough temp)
  - Water temperature calculated: 
    DDT_target = 76F
    water_temp = (76 * 3) - (room_70F + flour_68F + friction_22F) = 68F
  
mixing:
  - spiral_mixer.state = "mixing_low"
  - Add ingredients to bowl
  - Mix on low speed (120 RPM) for 2 minutes
  - Result: shaggy mass, just combined
  - spiral_mixer.state = "resting"
  
autolyse_rest:
  - dough_batch.state = "autolyse"
  - Leave in mixer bowl for 40 minutes
  - Enzymatic activity: gluten strands forming, dough becomes extensible
  - rachel_martinez moves to other tasks (stage next ingredients)
```

**Property changes:**
- Create `country_sourdough_batch1_tue` dough_batch object
- flour_bread_organic.current_quantity: delta -9.11kg
- flour_whole_wheat_organic.current_quantity: delta -1.61kg
- water_filtered.current_quantity: delta -8.04kg
- spiral_mixer.state: "idle" → "mixing_low" → "resting"
- country_sourdough_batch1_tue.state: set "autolyse"
- country_sourdough_batch1_tue.mix_time: set current_timestamp

#### final_mix_country_sourdough_batch1
**Timing:** 40 minutes after autolyse begins (6:10 AM)
**Actor:** rachel_martinez
**Duration:** 11 minutes (3 low + 8 high)

**Objects involved:**
- `country_sourdough_batch1_tue` (dough_batch)
- `spiral_mixer` (equipment)
- `production_levain_yesterday` (levain_culture from previous day)
- `salt_fine_sea` (resource)
- `fermentation_container` (fermentation_container type)

**Interactions:**
```
add_levain_salt:
  - production_levain_yesterday.weight_g: -4.5kg (20% of batch flour)
  - salt_fine_sea.current_quantity: -225g (2% of flour)
  - Add to mixer bowl with autolysed dough
  
final_mixing:
  - spiral_mixer.state = "mixing_low"
  - Low speed (120 RPM): 3 minutes (incorporate levain and salt)
  - spiral_mixer.state = "mixing_high"
  - High speed (240 RPM): 8 minutes
  - Gluten development: dough becomes smooth, elastic, pulls away from bowl
  - Total mixing time: 11 minutes
  - spiral_mixer.power_consumption_kw = 2.8 (draw during operation)
  
temperature_check:
  - country_sourdough_batch1_tue.temperature = measure_with_thermometer
  - Target: 76-78F
  - If temperature < 76F: flag for warm location
  - If temperature > 78F: flag for cool location
  - CRITICAL QUALITY CONTROL POINT
  
transfer_to_fermentation:
  - Select fermentation_container where state = "clean"
  - container.state = "in_use"
  - container.contents_batch_id = "country_sourdough_batch1_tue"
  - container.fill_level_percent = 50
  - container.marked_volume = "volume_reference_for_doubling"
  - Transfer dough from mixer to container
  - Cover container
  
batch_state_update:
  - country_sourdough_batch1_tue.state = "bulk_fermenting"
  - country_sourdough_batch1_tue.fermentation_start = current_timestamp
  - country_sourdough_batch1_tue.fermentation_target_duration = 270 minutes (4.5 hours)
  - country_sourdough_batch1_tue.fold_count = 0
  - country_sourdough_batch1_tue.next_fold_time = timestamp + 45 minutes
  
cleanup:
  - spiral_mixer.bowl_state = "in_use" → "dirty"
  - Mixer bowl must be cleaned before next batch
```

**Property changes:**
- production_levain_yesterday.weight_g: delta -4.5kg
- salt_fine_sea.current_quantity: delta -0.225kg
- country_sourdough_batch1_tue.temperature: set measured_value
- country_sourdough_batch1_tue.state: "autolyse" → "bulk_fermenting"
- country_sourdough_batch1_tue.fermentation_start: set current_timestamp
- fermentation_container.state: "clean" → "in_use"
- spiral_mixer.state: "mixing_high" → "idle"
- spiral_mixer.bowl_state: "in_use" → "dirty"

### BULK FERMENTATION PROCESSES

#### bulk_fermentation_fold
**Timing:** Every 45 minutes during bulk fermentation (4 folds total)
**Actor:** rachel_martinez or david_kim
**Duration:** 2 minutes per batch

**Objects involved:**
- `dough_batch` (any in state "bulk_fermenting")
- `fermentation_container` (containing the batch)

**Interactions:**
```
pre_check:
  - Verify dough_batch.state = "bulk_fermenting"
  - Check dough_batch.next_fold_time <= current_time
  - If not time yet: skip, wait
  
perform_fold:
  - Wet hands (prevent sticking)
  - Reach under dough, grab edge
  - Stretch up and fold over center
  - Rotate container 90 degrees
  - Repeat 4 times total (north, east, south, west)
  - Purpose: redistribute temperature, strengthen gluten, degas slightly
  
update_tracking:
  - dough_batch.fold_count: +1
  - If fold_count < 4:
    - dough_batch.next_fold_time = current_timestamp + 45 minutes
  - If fold_count = 4:
    - dough_batch.next_fold_time = null (no more folds)
  - fermentation_container.fill_level_percent: observe and record
  
visual_assessment:
  - Check for bubble formation on surface and sides
  - Assess volume increase (comparing to marked reference)
  - Note: These observations inform readiness assessment later
```

**Property changes:**
- dough_batch.fold_count: delta +1
- dough_batch.next_fold_time: set new_timestamp or null
- fermentation_container.fill_level_percent: update observed_value

#### bulk_fermentation_completion_check
**Timing:** After 4-5 hours bulk fermentation
**Actor:** marcus_chen or rachel_martinez
**Duration:** 5 minutes assessment

**Objects involved:**
- `dough_batch` (state "bulk_fermenting")
- `fermentation_container`

**Interactions:**
```
readiness_assessment:
  - Visual checks:
    - fermentation_container.fill_level_percent >= 75 (75-100% volume increase)
    - Domed surface visible (not flat or collapsed)
    - Bubbles visible on surface and through clear sides
  - Wobble test:
    - Shake container gently
    - Dough should jiggle (indicates gas retention)
  - Poke test:
    - Press finger into dough surface
    - Indentation should slowly spring back halfway
  
decision:
  - If ALL checks pass:
    - dough_batch.state = "ready_for_shaping"
    - Flag for marcus/rachel to begin shaping
  - If checks fail:
    - Extend bulk fermentation 30-60 minutes
    - Re-check later
  - If severely over-fermented (collapsed, no spring-back):
    - dough_batch.quality_score: set < 50
    - dough_batch.state = "over_fermented"
    - Batch may be salvageable with re-work or must be discarded
```

**Property changes:**
- dough_batch.state: "bulk_fermenting" → "ready_for_shaping" (if passed)
- dough_batch.quality_score: update based on assessment

### SHAPING PROCESSES

#### divide_and_preshape
**Timing:** 12:00-2:00 PM for next day's production
**Actor:** rachel_martinez (primarily) with marcus_chen assisting
**Duration:** Varies by batch size (50 loaves = 45 minutes)

**Objects involved:**
- `dough_batch` (state "ready_for_shaping")
- `primary_shaping_bench` (equipment)
- `digital_scale` (equipment - not previously listed, add to equipment)
- Multiple `proofing_basket` objects

**Interactions:**
```
setup:
  - Clear primary_shaping_bench
  - primary_shaping_bench.state = "in_use"
  - Lightly flour surface
  - Stage empty proofing_baskets (50 round or oval depending on recipe)
  - Verify baskets.flour_coating = "fresh"
  
turn_out_dough:
  - Transfer dough from fermentation_container to bench
  - Handle gently to preserve gas structure
  - fermentation_container.state = "in_use" → "dirty"
  
divide:
  - Use bench scraper and digital_scale
  - Cut dough into portions:
    - Country Sourdough: 1000g each (becomes 900g after bake)
    - Whole Grain: 980g each
    - Multigrain: 950g each
  - Precision critical for even baking
  - Create individual loaf tracking objects:
    - For each portion: create "loaf_object" with unique ID
    - loaf_object.batch_id = dough_batch.batch_id
    - loaf_object.weight_g = measured_weight
    - loaf_object.state = "divided"
    - loaf_object.target_product = "country_sourdough_900g"
  
preshape:
  - For each divided portion:
    - Shape into loose round (boule) or oval (batard) depending on final shape
    - Purpose: create initial tension, easier final shaping
    - Technique: gentle folding and tucking
    - Place on bench with space between pieces
    - loaf_object.state = "preshaped"
  
bench_rest:
  - All preshaped loaves rest on bench for 25 minutes
  - Gluten relaxes, making final shaping easier
  - Cover with plastic or cloth to prevent drying
  - rachel_martinez can start dividing next batch during this rest
```

**Property changes:**
- dough_batch.state: "ready_for_shaping" → "divided"
- Create 50 individual `loaf_object` items (custom type)
- fermentation_container.state: "in_use" → "dirty"
- primary_shaping_bench.state: "clean" → "in_use"

#### final_shape_and_proof
**Timing:** After 25-minute bench rest (12:45 PM onward)
**Actor:** rachel_martinez and marcus_chen working in parallel
**Duration:** 60-90 minutes for 50 loaves

**Objects involved:**
- Multiple `loaf_object` items (state "preshaped")
- Multiple `proofing_basket` objects
- `primary_shaping_bench`

**Interactions:**
```
final_shaping:
  For each loaf_object:
    - If shape = "batard" (oval):
      - Flatten preshape into rectangle
      - Fold top edge to center, press seal
      - Fold bottom edge to center, press seal
      - Fold in half (top to bottom), seal seam
      - Roll gently to create slight taper at ends
      - Result: 10-12 inch oval loaf
    
    - If shape = "boule" (round):
      - Place preshape top-side down on unfloured surface
      - Pull edges outward, fold toward center repeatedly
      - Flip over (seam on bottom)
      - Cup hands around dough
      - Drag across surface in circular motion (tighten skin)
    
    - loaf_object.state = "final_shaped"
    - loaf_object.shaped_time = current_timestamp
    - loaf_object.quality_score: assess shaping quality (80-100 for good technique)
  
load_into_baskets:
  - Select proofing_basket where state = "empty"
  - Dust basket interior with rice flour (prevents sticking)
  - Place shaped loaf SEAM-SIDE UP into basket
    - Important: seam up means scored pattern on top after flipping for bake
  - proofing_basket.state = "occupied"
  - proofing_basket.contents_loaf_id = loaf_object.loaf_id
  - loaf_object.location = proofing_basket.basket_id
  
transfer_to_retarder:
  - Place baskets on sheet pans (for structure during move)
  - Transfer pans to speed rack
  - Roll speed rack to proofing_retarder
  - Load into retarder shelves
  - Cover baskets with plastic wrap (prevent drying)
  - proofing_basket.location = "retarder"
  - loaf_object.state = "cold_proofing"
  - loaf_object.proof_start = current_timestamp
  - loaf_object.proof_location = "retarder"
  - proofing_retarder.contents: add basket_ids
  - proofing_retarder.capacity_utilized_percent: recalculate
```

**Property changes:**
- loaf_object.state: "preshaped" → "final_shaped" → "cold_proofing"
- loaf_object.shaped_time: set current_timestamp
- loaf_object.proof_start: set current_timestamp
- proofing_basket.state: "empty" → "occupied"
- proofing_basket.contents_loaf_id: set loaf_id
- proofing_basket.location: "bench" → "retarder"
- proofing_retarder.contents: add basket_ids
- proofing_retarder.capacity_utilized_percent: update

### BAKING PROCESSES

#### preheat_oven
**Timing:** 4:00 AM daily (60-75 min before first bake)
**Actor:** marcus_chen
**Duration:** 60-75 minutes

**Objects involved:**
- `main_oven` (equipment)
- `deck_1`, `deck_2`, `deck_3` (oven_deck custom type)
- `electricity` (resource)

**Interactions:**
```
startup:
  - main_oven.state = "off" → "preheating"
  - For each deck in [deck_1, deck_2, deck_3]:
    - deck.state = "preheating"
    - deck.temperature_target = 500F (standard sourdough preheat)
    - deck.temperature_current = ambient_70F (starting point)
  
heating_curve:
  - Temperature rises approximately 6-7F per minute
  - After 60 minutes: decks at ~490-500F
  - After 75 minutes: decks fully stabilized at 500F
  - main_oven.state = "preheating" → "ready" when all decks >= 495F
  
power_consumption:
  - electricity.current_quantity: delta -(33 kW * 1.25 hours) = -41.25 kWh
  - This is highest power draw period of day
  
steam_system_check:
  - Test steam injection: 3-second burst
  - Verify steam_available = true on all decks
```

**Property changes:**
- main_oven.state: "off" → "preheating" → "ready"
- deck_1/2/3.temperature_current: from 70F → 500F over 60-75 min
- deck_1/2/3.state: "off" → "preheating" → "ready"
- electricity.current_quantity: delta -41.25 kWh

#### pull_from_retarder_and_assess
**Timing:** 4:45 AM (15 min before first bake)
**Actor:** marcus_chen
**Duration:** 15 minutes

**Objects involved:**
- Multiple `loaf_object` (state "cold_proofing")
- Multiple `proofing_basket`
- `proofing_retarder`
- `speed_rack` (equipment - add to equipment list)

**Interactions:**
```
pull_first_batch:
  - Open proofing_retarder
  - proofing_retarder.state = "door_open" (temp will rise)
  - Select 20-24 loaves for first bake (deck capacity)
  - Transfer baskets from retarder to speed_rack
  - proofing_basket.location = "retarder" → "oven_staging_area"
  - Close retarder door
  - proofing_retarder.state = "operational"
  
warm_up_period:
  - Loaves at 40F from retarder
  - Allow 10-15 minutes at room temp (68-72F)
  - loaf_object.temperature: 40F → ~55F
  - Purpose: More accurate poke test, prevents thermal shock in oven
  
poke_test_each_loaf:
  - For each loaf_object:
    - Press finger gently into dough (1/2 inch depth)
    - Assess spring-back:
      - Springs back quickly/completely = UNDER-PROOFED
        - loaf_object.under_proofed = true
        - Action: Delay bake, allow 20-30 min more proof at room temp
      - Springs back slowly, halfway = PROPERLY PROOFED
        - loaf_object.quality_score: maintain or increase
        - Ready to bake immediately
      - No spring-back, indentation remains = OVER-PROOFED
        - loaf_object.over_proofed = true
        - loaf_object.quality_score: reduce by 20 points
        - Action: Bake immediately (cannot fix), accept lower quality
  
dust_with_flour:
  - Lightly dust loaf tops with rice flour
  - Prevents sticking to banneton during transfer
```

**Property changes:**
- loaf_object.temperature: 40F → ~55F
- loaf_object.under_proofed or over_proofed: set true if detected
- loaf_object.quality_score: adjust based on proof assessment
- proofing_basket.location: "retarder" → "oven_staging_area"

#### score_and_load_oven
**Timing:** 5:00 AM first bake (repeated every 40-60 min)
**Actor:** marcus_chen
**Duration:** 10 minutes per load

**Objects involved:**
- Multiple `loaf_object` (state "cold_proofing", ready to bake)
- Multiple `proofing_basket`
- Multiple `oven_deck`
- `oven_peel` (equipment - add to list)
- `lame` (equipment - scoring blade)

**Interactions:**
```
prepare_workspace:
  - Position oven_peel near oven
  - Have lame ready with fresh blade
  - Work in batches of 8 loaves (one deck capacity)
  
score_loaves:
  - For each loaf_object:
    - Turn loaf from basket onto oven_peel (flips seam-side down)
    - proofing_basket.state = "occupied" → "dirty"
    - Score pattern based on product_type:
      - Country Sourdough: deep cross (1/2" deep, perpendicular cuts)
      - Whole Grain: radial star (5 cuts from center)
      - Baguette: single diagonal slash (1/4" deep, 30-degree angle)
    - Scoring creates weak points for controlled oven spring
    - loaf_object.state = "cold_proofing" → "scored"
    - loaf_object.score_pattern = "cross" or "radial" or "diagonal"
  
load_deck:
  - Select oven_deck where state = "ready" or "recovered"
  - For each loaf on peel:
    - Slide loaf onto hot stone hearth using quick jerk motion
    - Position 8 loaves per deck (staggered arrangement for air flow)
    - loaf_object.state = "scored" → "baking"
    - loaf_object.bake_start_time = current_timestamp
    - loaf_object.location = deck.deck_id
  - deck.contents: add loaf_ids
  - deck.state = "ready" → "baking"
  
steam_injection:
  - IMMEDIATELY after loading (within 10 seconds):
    - Trigger steam system: 3-second initial burst
    - Then 8-second sustained burst
    - Purpose: Creates humid environment for crust development
  - deck.last_steam_time = current_timestamp
  - Close oven door
  - Close vents (trap steam for first 15 minutes)
  
set_timers:
  - Product-specific bake times:
    - Country Sourdough: 38 minutes
    - Baguette: 22-25 minutes
    - Rye: 45-50 minutes
  - deck.bake_end_time = current_timestamp + bake_time
  - Set alert/alarm for vent opening (15 minutes)
  - Set alert for bake completion
```

```
**Property changes:**
- loaf_object.state: "cold_proofing" → "scored" → "baking"
- loaf_object.bake_start_time: set current_timestamp
- loaf_object.location: set deck.deck_id
- oven_deck.contents: add array of loaf_ids
- oven_deck.state: "ready" → "baking"
- oven_deck.bake_start_time: set current_timestamp
- oven_deck.bake_end_time: set timestamp + bake_duration
- proofing_basket.state: "occupied" → "dirty"
```

#### oven_steam_phase_to_dry_phase
**Timing:** 15 minutes into bake
**Actor:** marcus_chen
**Duration:** 30 seconds

**Objects involved:**
- `oven_deck` (state "baking")

**Interactions:**
```
vent_control:
  - Open oven vents (dampers)
  - Purpose: Release steam, allow crust to dry and brown
  - Steam phase (0-15 min): Vents closed, humid
  - Dry phase (15-end): Vents open, crust caramelizes
  - This is critical timing - affects crust texture and color
  
no_state_change:
  - deck.state remains "baking"
  - Just operational adjustment within bake process
```

**Property changes:**
- (No object property changes, just operational state within oven)

#### unload_finished_bake
**Timing:** When deck.bake_end_time reached (timer goes off)
**Actor:** marcus_chen or david_kim
**Duration:** 10 minutes

**Objects involved:**
- `oven_deck` (state "baking")
- Multiple `loaf_object` (state "baking")
- `cooling_rack` (cooling_rack custom type)
- `oven_peel`

**Interactions:**
```
pull_loaves:
  - Open oven door
  - deck.state = "baking" → "door_open"
  - Use oven_peel to pull loaves one by one
  - For each loaf_object in deck.contents:
    - Visual quality check:
      - Crust color: Should be deep golden-brown to mahogany
        - Too pale: under-baked
        - Burnt spots: over-baked
      - Score marks: Check for "ear" formation (raised edge)
      - Shape: Even rise, no collapsed areas
    - Tap bottom of loaf: Should sound hollow (not solid thud)
    - If visual inspection passes:
      - loaf_object.quality_score: maintain or increase
    - If defects noted:
      - loaf_object.quality_score: reduce appropriately
      - loaf_object.defect_notes: "over_browned" or "flat" or "torn_score"
  
internal_temperature_spot_check:
  - Select 2-3 loaves from batch
  - Insert instant-read thermometer into center
  - Target temps:
    - Sourdough/lean breads: 205-210F
    - Enriched breads: 200-205F
    - Rye: 205-207F
  - If under temp: return entire batch to oven for 5-10 more minutes
  - If at temp: proceed to cooling
  
transfer_to_cooling:
  - Select cooling_rack with available capacity
  - Place loaves on rack tiers (spread out for air circulation)
  - Do not stack loaves (prevents proper cooling)
  - cooling_rack.current_load_pans: increment by number of loaves
  - loaf_object.state = "baking" → "cooling"
  - loaf_object.bake_end_time = current_timestamp
  - loaf_object.cooling_start = current_timestamp
  - loaf_object.location = cooling_rack.rack_id
  
deck_recovery:
  - deck.contents: clear array (all loaves removed)
  - deck.state = "door_open" → "cooling"
  - deck.temperature_current: drops to ~450F (door open)
  - Allow 10-15 minutes for deck to recover to target temp
  - After recovery period:
    - deck.state = "cooling" → "recovered" → "ready"
    - deck.temperature_current: back to 490-500F
```

**Property changes:**
- loaf_object.state: "baking" → "cooling"
- loaf_object.bake_end_time: set current_timestamp
- loaf_object.cooling_start: set current_timestamp
- loaf_object.location: set cooling_rack.rack_id
- loaf_object.quality_score: adjust based on visual/temp checks
- oven_deck.contents: clear array
- oven_deck.state: "baking" → "door_open" → "cooling" → "recovered" → "ready"
- oven_deck.temperature_current: 500F → 450F → 500F over recovery period
- cooling_rack.current_load_pans: delta + number_of_loaves

#### cooling_completion
**Timing:** Product-specific (2-8 hours after bake)
**Actor:** Passive process, checked by david_kim or sarah_thompson
**Duration:** Varies by product

**Objects involved:**
- `loaf_object` (state "cooling")
- `cooling_rack`

**Interactions:**
```
cooling_duration:
  - Baguettes: 30-45 minutes (thin, high surface area)
  - Country Sourdough: 3 hours minimum
  - Whole Grain/Multigrain: 3-4 hours
  - Sandwich Loaf: 3-4 hours (enriched, dense)
  - Rye: 6-8 hours MINIMUM (critical - gummy if sliced early)
  - Focaccia: 1.5 hours
  
temperature_check:
  - Touch test: Loaf should be barely warm or room temperature
  - Internal temp target: <90F (ideally room temp ~72F)
  
readiness_assessment:
  - If cooling_duration elapsed AND temp acceptable:
    - loaf_object.state = "cooling" → "cooled"
    - loaf_object.ready_for_packaging = true
    - Ready for FOH transfer or packaging
  - If still warm:
    - Wait longer (cannot rush this)
```

**Property changes:**
- loaf_object.state: "cooling" → "cooled"
- loaf_object.ready_for_packaging: set true
- loaf_object.temperature: ambient ~72F

### PACKAGING AND DISPLAY PROCESSES

#### package_for_retail
**Timing:** After cooling complete, before display or sale
**Actor:** sarah_thompson or david_kim
**Duration:** 30 seconds per loaf

**Objects involved:**
- `loaf_object` (state "cooled")
- `cooling_rack`
- `packaging_bread_bags` or `packaging_baguette_bags` (resource)
- `packaging_labels` (resource)

**Interactions:**
```
retrieve_loaf:
  - Select loaf from cooling_rack where ready_for_packaging = true
  - cooling_rack.current_load_pans: decrement by 1
  
package:
  - Select appropriate bag based on product:
    - Standard loaves: packaging_bread_bags (6x3x12)
    - Baguettes: packaging_baguette_bags (long narrow)
  - Place loaf in bag
  - If customer requested slicing:
    - Use electric slicer (equipment not yet listed - add)
    - Slice to requested thickness (thick or thin)
    - Return slices to bag in order
  - Apply branded sticker/label to bag
  - packaging_bread_bags.current_quantity: -1
  - packaging_labels.current_quantity: -1
  
update_loaf_state:
  - loaf_object.state = "cooled" → "packaged"
  - loaf_object.package_time = current_timestamp
  - loaf_object.location = "packaging_area"
```

**Property changes:**
- loaf_object.state: "cooled" → "packaged"
- loaf_object.package_time: set current_timestamp
- loaf_object.location: "packaging_area"
- cooling_rack.current_load_pans: delta -1
- packaging_bread_bags.current_quantity: delta -1
- packaging_labels.current_quantity: delta -1

#### stock_display_case
**Timing:** Throughout day as loaves become available
**Actor:** sarah_thompson or david_kim
**Duration:** 2 minutes per restocking trip

**Objects involved:**
- Multiple `loaf_object` (state "packaged")
- `display_case` (equipment)

**Interactions:**
```
assess_display_needs:
  - Check display_case.current_contents count
  - Check display_case.capacity_loaves (35-40 max)
  - Available space = capacity - current_count
  
arrange_by_tier:
  - Tier 1 (top shelf): Specialty/seasonal, higher-priced items
    - Olive & Rosemary, Rye, Seasonal Focaccia
  - Tier 2 (middle): Core sourdough varieties
    - Country Sourdough, Whole Grain, Multigrain
  - Tier 3 (bottom): Baguettes, Sandwich Loaves, Focaccia
  
transfer_loaves:
  - For each loaf selected for display:
    - loaf_object.location = "packaging_area" → "display_case"
    - loaf_object.state = "packaged" → "for_sale"
    - loaf_object.display_time = current_timestamp
    - display_case.current_contents: add loaf_id
    - display_case.contents_by_tier[tier_number]: add loaf_id
  
visual_merchandising:
  - Arrange attractively: larger loaves upright, baguettes angled
  - Ensure price tags visible
  - Face labels outward
```

**Property changes:**
- loaf_object.location: "packaging_area" → "display_case"
- loaf_object.state: "packaged" → "for_sale"
- loaf_object.display_time: set current_timestamp
- display_case.current_contents: add loaf_ids
- display_case.contents_by_tier[X]: add loaf_ids

#### customer_purchase_transaction
**Timing:** Throughout retail hours (7:00 AM - 6:00 PM / 2:00 PM / 4:00 PM depending on day)
**Actor:** sarah_thompson
**Duration:** 2-3 minutes per transaction

**Objects involved:**
- Multiple `loaf_object` (state "for_sale")
- `display_case`
- `pos_system`
- Customer object (could create "customer" type for tracking)

**Interactions:**
```
customer_selection:
  - Customer indicates desired products
  - sarah retrieves from display_case
  - For each loaf selected:
    - loaf_object.state = "for_sale" → "sold"
    - loaf_object.sale_time = current_timestamp
    - loaf_object.sale_channel = "retail"
    - display_case.current_contents: remove loaf_id
  
additional_packaging:
  - If customer wants multiple items, may use additional bag
  - Optional: tie with bakery twine (aesthetic touch)
  
transaction:
  - pos_system.state = "in_transaction"
  - Calculate total:
    - Sum of loaf_object.product.retail_price for all items
  - Customer payment method: cash or card
  - If card:
    - Transaction fee: total * 0.026 + 0.10
    - pos_system.transaction_fee_today: add fee
  - If cash:
    - pos_system.current_cash: add payment
  - Print receipt
  - pos_system.state = "idle"
  
inventory_tracking:
  - pos_system automatically deducts from inventory count
  - Daily sales data accumulated
  
revenue_tracking:
  - Add to daily_revenue (tracked in financial system)
```

**Property changes:**
- loaf_object.state: "for_sale" → "sold"
- loaf_object.sale_time: set current_timestamp
- loaf_object.sale_channel: set "retail"
- display_case.current_contents: remove loaf_ids
- pos_system.current_cash: delta + cash_payment (if cash)
- pos_system.transaction_fee_today: delta + calculated_fee (if card)
- Daily revenue counters incremented

#### prepare_wholesale_order
**Timing:** Morning (7:30-9:00 AM), orders fulfill specific delivery/pickup times
**Actor:** rachel_martinez or marcus_chen
**Duration:** 15-20 minutes per order

**Objects involved:**
- Multiple `loaf_object` (state "cooled" or "for_sale")
- `packaging_tissue` (resource - add to list)
- `packaging_wholesale_boxes` (resource)
- Wholesale customer object (track accounts)

**Interactions:**
```
retrieve_order_list:
  - Example: Cedar Street Café order
    - 10 Country Sourdough
    - 12 Baguettes
    - Pickup time: 8:00 AM
  
select_best_loaves:
  - Quality control: wholesale customers get consistent quality
  - Select loaves with quality_score >= 85
  - Avoid defective or lower-quality loaves for wholesale
  - For each loaf selected:
    - loaf_object.state = "cooled" → "wholesale_packed"
    - loaf_object.allocated_customer = "cedar_street_cafe"
  
pack_order:
  - Wrap each loaf in tissue paper (presentation)
  - packaging_tissue.current_quantity: -1 per loaf
  - Place in reinforced wholesale boxes
  - packaging_wholesale_boxes.current_quantity: -1 per box
  - Apply wholesale invoice/packing slip
  - loaf_object.sale_channel = "wholesale"
  
stage_for_pickup:
  - Place packed order in wholesale staging area
  - Or load into marcus's vehicle for delivery
  - Order ready for handoff
```

**Property changes:**
- loaf_object.state: "cooled" → "wholesale_packed"
- loaf_object.allocated_customer: set customer_id
- loaf_object.sale_channel: set "wholesale"
- packaging_tissue.current_quantity: delta - count
- packaging_wholesale_boxes.current_quantity: delta - count

### CLEANING AND MAINTENANCE PROCESSES

#### daily_equipment_cleaning
**Timing:** Throughout day after use, end of shift
**Actor:** All staff (assigned by item)
**Duration:** 5-30 minutes depending on equipment

**Objects involved:**
- `spiral_mixer`
- `primary_shaping_bench`
- `mixing_prep_table`
- `fermentation_container`
- `proofing_basket`
- Various equipment items

**Interactions:**
```
mixer_cleaning (rachel_martinez, after each use):
  - spiral_mixer.bowl_state = "dirty" → "cleaning"
  - Scrape out residual dough
  - Wash with warm soapy water
  - Sanitize with approved sanitizer
  - Dry thoroughly
  - spiral_mixer.bowl_state = "cleaning" → "clean"
  - Duration: 10 minutes
  
work_surface_cleaning (all staff, after each use):
  - primary_shaping_bench.state = "in_use" → "dirty" → "cleaning"
  - Scrape off flour and dough bits
  - Wipe with sanitizer solution
  - Dry with clean towel
  - primary_shaping_bench.state = "cleaning" → "clean"
  - Duration: 5 minutes
  
fermentation_container_cleaning:
  - fermentation_container.state = "dirty" → "cleaning"
  - Wash with hot soapy water
  - Sanitize
  - Air dry
  - fermentation_container.state = "cleaning" → "clean"
  - Duration: 5 minutes per container
  
banneton_maintenance:
  - proofing_basket.state = "dirty" → "cleaning"
  - Shake out excess flour (weekly)
  - Liners: Remove and wash every 2 weeks
  - Sun/air dry monthly (kills mold)
  - proofing_basket.flour_coating = "depleted" → "fresh"
  - proofing_basket.state = "cleaning" → "empty"
```

**Property changes:**
- Equipment.state: "dirty" → "cleaning" → "clean"
- proofing_basket.state: "dirty" → "cleaning" → "empty"
- proofing_basket.flour_coating: "depleted" → "fresh"

#### monday_deep_cleaning
**Timing:** Monday 10:00 AM - 2:00 PM (closed day)
**Actor:** marcus_chen
**Duration:** 4 hours

**Objects involved:**
- All equipment items
- All work surfaces
- Floors, walls, storage areas

**Interactions:**
```
equipment_deep_clean:
  - main_oven: 
    - Scrape deck surfaces
    - Clean door gaskets
    - Check steam system
    - State remains "operational" but receives maintenance
  - spiral_mixer:
    - Remove bowl, clean underneath
    - Check belt tension
    - Lubricate gears
  - refrigeration:
    - Wipe down interiors
    - Check door seals
    - Clean condenser coils (quarterly)
  
floor_and_walls:
  - Sweep all areas
  - Mop with sanitizer
  - Clean baseboards
  - Wipe down walls (splash zones)
  
administrative_work:
  - marcus performs bookkeeping
  - Reviews inventory
  - Places orders for upcoming week
  - Equipment maintenance scheduling
```

**Property changes:**
- All equipment.last_maintenance: update timestamp
- Cleanliness state refreshed across all objects

### SPECIALTY PRODUCT PROCESSES

#### baguette_same_day_production
**Timing:** 5:00-11:00 AM same day as sale
**Actor:** rachel_martinez (mixing, shaping), marcus_chen (baking)
**Duration:** 6 hours start to finish

**Process differences from sourdough:**
- Uses poolish (prepared previous afternoon)
- No cold retarding - room temp proof only
- Faster timeline: mix to bake in 3-4 hours
- Very specific shaping technique (taper, length)
- Heavy steam requirement
- Shorter bake time (22-25 min)
- Peak quality window short (4-8 hours)

**Objects involved:**
- `poolish_culture` (custom type, similar to levain_culture)
- `baguette_dough_batch` (dough_batch with special properties)
- Individual `baguette_loaf` objects
- `proofing_cloth_couche` (equipment - not baskets)

**Key interactions:**
```
poolish_prep_previous_day (4:00 PM):
  - Create poolish_culture object
  - Mix flour + water + tiny amount yeast (0.1%)
  - poolish.state = "fermenting"
  - poolish.location = "retarder" or "cool_area"
  - Ferment 12-14 hours until bubbly, domed
  
morning_mix (5:00 AM):
  - Check poolish.activity_level = "peak"
  - Mix final dough with poolish + flour + water + salt + malt
  - Bulk fermentation: only 90 minutes (vs 4-5 hours for sourdough)
  - 2 folds only
  
shaping (6:45 AM):
  - Divide into 325g portions
  - Preshape cylinders, 20 min rest
  - Final shape: very specific baguette technique
  - Place on linen proofing cloth (couche), not baskets
  - Pleat cloth between baguettes for support
  - baguette_loaf.proof_location = "couche_room_temp"
  - Proof 60-75 minutes until puffy
  
baking (8:00 AM):
  - Score: single diagonal slash at 30-degree angle
  - HEAVY steam (extra burst)
  - 480F oven
  - 22-25 minutes
  - Baguettes cool quickly (30-45 min)
```

#### focaccia_cold_ferment_method
**Timing:** Mix Tuesday AM, bake Tuesday PM or Wednesday AM
**Actor:** david_kim
**Duration:** 15 hours total (mostly passive fermentation)

**Process differences:**
- Very wet dough (85% hydration)
- Can ferment in walk-in 8-24 hours (flexibility)
- Shaped in oiled pans (not free-form)
- Dimpling creates signature texture
- No steam needed (pan baking)
- Highest margin product

**Objects involved:**
- `focaccia_dough_batch`
- `sheet_pan_9x13` (equipment)
- Olive oil (generous amounts)

**Key interactions:**
```
mixing (6:00 AM Tuesday):
  - Mix very wet dough with yeast + levain (optional)
  - Bulk ferment options:
    - Option A: 2-3 hours room temp with folds
    - Option B: Immediate cold ferment (PREFERRED)
  - focaccia_dough_batch.fermentation_method = "cold_8_24_hours"
  - Transfer to oiled container
  - Place in walk_in_cooler
  - focaccia_dough_batch.state = "cold_fermenting"
  
shaping (next day or later same day):
  - Pull from walk-in
  - Coat sheet pans generously with olive oil
  - Divide dough into 1200g portions
  - Place in pans, press toward edges
  - If dough resists: rest 20-30 min, press again
  - focaccia_dough_batch.state = "shaped_in_pans"
  
final_proof (1.5-3 hours):
  - Proof until puffy, nearly doubled
  - Room temperature
  
pre-bake_topping:
  - Drizzle surface with olive oil (2-3 tbsp)
  - Dimple with fingertips (push through to pan)
  - Sprinkle flaky salt
  - Press rosemary sprigs into surface
  
baking (4:00 PM):
  - 450F (no steam)
  - 20-25 minutes
  - Target: golden top and bottom, crispy edges
  - Cool 10 min in pan, then remove
  - Cut into 6 portions
```

## 4. TEMPORAL STRUCTURE

### DAILY SCHEDULE FRAMEWORK

#### Production Days (Tuesday-Saturday)
**Structure:**
- Pre-dawn startup (3:45-5:00 AM)
- Morning production peak (5:00-11:00 AM)
- Midday shaping session (12:00-2:00 PM)
- Afternoon cleanup and prep (2:00-4:00 PM)
- Evening shaping for next day (completed by 8:00 PM)

**Time-critical sequences:**
1. **4:00 AM: Oven preheat begins** (75-minute lead time before first bake)
2. **4:00-4:30 AM: Starter maintenance** (must happen every production day)
3. **4:30-5:00 AM: Levain build** (for tomorrow's production, 6-8 hour window)
4. **5:00 AM: First bake loads** (cold-proofed loaves from previous evening)
5. **5:00-7:30 AM: Main mixing window** (Rachel's primary mixing tasks)
6. **12:00-2:00 PM: Shaping session** (for next day's production, must happen)
7. **6:00-8:00 PM: Load retarder** (shaped loaves cold-proof overnight)

#### Sunday (Shorter Hours)
**Modified schedule:**
- Same morning production (baking loaves shaped Saturday)
- Retail closes 2:00 PM (vs 4:00-6:00 PM other days)
- No shaping for next day (Monday is closed)
- Reduced production volume

#### Monday (Admin/Cleaning Day - Bakery Closed)
**Structure:**
- Marcus only, 10:00 AM - 2:00 PM
- Deep cleaning (4 hours)
- Equipment maintenance
- Starter feeding (maintains culture through off day)
- Levain build for Tuesday production
- Administrative work (ordering, bookkeeping)
- No retail, no production

### PARALLEL vs SEQUENTIAL PROCESSES

#### Parallel Operations (can happen simultaneously)
- **Multiple actors working different tasks:**
  - Marcus managing oven while Rachel mixing
  - David restocking FOH while bakes happening
  - Sarah serving customers while production continues
  
- **Multiple batches in different states:**
  - Batch 1 baking in oven
  - Batch 2 bulk fermenting on bench
  - Batch 3 being mixed
  - Batch 4 cold-proofing in retarder
  
- **Multiple equipment items operating:**
  - Oven baking loaves
  - Mixer running new batch
  - Retarder holding tomorrow's loaves
  - Walk-in cooling ingredients

#### Sequential Dependencies (must happen in order)
- **Cannot skip:**
  1. Starter feed → Levain build → Mix dough → Bulk ferment → Shape → Proof → Bake → Cool → Package → Sell
  
- **Timing constraints:**
  - Autolyse must rest 40 minutes (cannot rush)
  - Bulk fermentation 4-5 hours (temperature-dependent, cannot compress)
  - Fold cycles every 45 minutes (4 folds required)
  - Cold proof 10-12 hours (8 minimum, 16 maximum)
  - Cooling 2-8 hours depending on product (cannot package hot bread)
  
- **Capacity bottlenecks create sequencing:**
  - Oven can only bake 25 loaves at once → must bake in batches
  - Mixer can only mix 18kg at once → 45kg batch requires 3 sequential mixes
  - Shaping bench limits how many people can shape simultaneously

### DAY TYPE VARIATIONS

#### Tuesday-Friday (Typical Weekday)
- Production: 170-185 loaves
- Staff: Marcus, Rachel, David (partial), Sarah
- Oven utilization: ~65%
- Retail hours: 7:00 AM - 6:00 PM

#### Saturday (Peak Day)
- Production: 250 loaves (maximum capacity)
- All staff working
- Oven utilization: 95% (at bottleneck)
- Retail hours: 7:00 AM - 4:00 PM
- **Critical path:** Any delay cascades, cannot recover

#### Sunday (Medium Volume, Short Hours)
- Production: 200 loaves
- Staff: David, Sarah (Marcus may assist)
- Oven utilization: ~75%
- Retail hours: 8:00 AM - 2:00 PM
- **Constraint:** No shaping for next day (Monday closed)

### CRITICAL TIMING WINDOWS

#### Window 1: Levain Readiness (10:00 AM - 2:00 PM)
- Production levain must reach peak activity
- If not ready by 2:00 PM: tomorrow's schedule delays
- Temperature-dependent (78F ambient speeds, 68F slows)

#### Window 2: Oven Availability Morning (5:00-11:00 AM)
- Highest value baking time (direct to retail display)
- Must complete sourdough, baguette, specialty breads
- Missing this window = revenue loss

#### Window 3: Shaping Session (12:00-2:00 PM)
- MUST shape tomorrow's loaves during this window
- If delayed past 3:00 PM: shortened cold proof (quality impact)
- Requires Marcus + Rachel both available

#### Window 4: Retarder Loading (6:00-8:00 PM latest)
- Shaped loaves must enter retarder by 8:00 PM
- 10-12 hour cold proof for 5:00 AM bake
- Loading at 9:00 PM = only 8 hours proof (under-proofed risk)

## 5. REALISTIC COMPLICATIONS

### CAPACITY CONSTRAINTS

#### Oven Bottleneck (Most Critical)
**Constraint:**
- 3 decks × 8-10 loaves per deck = 24-30 loaves per cycle
- Bake time: 25-50 minutes depending on product
- Recovery time: 10-15 minutes between loads
- **Maximum daily throughput:** ~250 loaves

**Impacts:**
- Saturday production at 95% capacity (no buffer)
- Cannot accept large special orders without displacing regular production
- Equipment failure on Saturday = catastrophic (\$2,200 revenue loss)

**Sim representation:**
- oven_deck.capacity_loaves property enforced
- bake_time + recovery_time creates scheduling constraint
- Saturday schedule must be precisely orchestrated

#### Retarder Capacity Limit
**Constraint:**
- 36 pans = ~180-200 loaves maximum
- Saturday needs 220+ loaves

**Current workaround:**
- Some Friday shaped loaves proof at room temp 3-4 hours
- Baked Friday night
- Sold Saturday as "12-hour old" (not ideal quality)

**Sim representation:**
- proofing_retarder.capacity_utilized_percent cannot exceed 100%
- Overflow loaves must use alternative proofing location
- Quality score reduced for room-temp overnight proof

#### Cooling Rack Space
**Constraint:**
- 4 racks × 20 positions = 80 loaf capacity
- Each loaf needs 2-4 hours cooling
- Saturday morning: all 80 positions full by 9:00 AM

**Impact:**
- Cannot continue baking until racks clear
- Forces pause in production mid-morning
- Some loaves cooled on sheet pans (takes work surface space)

**Sim representation:**
- cooling_rack.current_load_pans tracks capacity
- Cannot transfer from oven if no rack space available
- Cooling_time minimum enforced before packaging

### QUALITY REQUIREMENTS

#### Dough Temperature (DDT)
**Requirement:** 76-78°F after mixing
**Tolerance:** ±4°F (72-82°F acceptable but not ideal)
**Out of range impacts:**
- < 72°F: Sluggish fermentation, extended bulk time, schedule delays
- > 82°F: Too-fast fermentation, off flavors (acetic vs lactic balance)

**Sim representation:**
- dough_batch.temperature calculated based on ingredient temps
- If out of range: fermentation_target_duration adjusted
- quality_score reduced if significantly out of range

#### Proof Timing (Goldilocks Problem)
**Requirement:** Loaves must be "just right" proofed
**Assessment:** Poke test before baking
**Impacts:**
- Under-proofed: Dense crumb, tears in oven, poor rise
- Properly proofed: Optimal oven spring, open crumb, clean scores
- Over-proofed: Collapses in oven, flat loaves, gummy texture

**Sim representation:**
- loaf_object.under_proofed or over_proofed flags
- Cold proof duration 8-16 hours (10-12 ideal)
- Poke test at pull_from_retarder sets flags
- Quality_score impacted by proof state

#### Cooling Time Minimums
**Requirement:** Product-specific cooling before packaging
**Critical for rye:** 6-8 hours minimum (otherwise gummy)

**Sim representation:**
- loaf_object.ready_for_packaging only true after cooling_duration elapsed
- Attempting to package early: quality_score penalty, customer complaints
- Rye has longest cooling requirement (simulation should enforce)

### TIMING DEPENDENCIES

#### Bulk Fermentation Uncertainty
**Challenge:** Fermentation completion not clock-based
**Variables affecting duration:**
- Dough temperature
- Room ambient temperature
- Levain strength/health
- Flour protein content

**Typical range:** 4-5 hours, but can be 3.5-6 hours

**Sim representation:**
- Fermentation_target_duration has variance
- Must check dough_batch.state for "ready_for_shaping"
- Actors must monitor and assess (cannot just wait fixed time)

#### Cascade Delays
**Scenario:** Late levain build (started 5:00 AM instead of 4:30 AM)
**Cascade:**
- 30-minute delay in first mix
- → 30-minute delay in bulk fermentation start
- → 30-minute delay in shaping session
- → 30-minute delay loading retarder
- → Next morning: loaves under-proofed (only 9.5 hours vs 10-12)
- → Must allow extra room-temp proof before baking
- → First bake delayed 30-60 minutes
- → Retail display not stocked for 7:00 AM opening
- → Lost morning rush sales ($200-300)

**Sim representation:**
- Timing dependencies tracked through timestamps
- Each process checks prerequisite completion
- Delays propagate through dependent processes
- Revenue impact calculated for missed retail windows

### RESOURCE MANAGEMENT

#### Flour Inventory Triggers
**Monitoring:**
- Current flour stock checked daily
- Reorder point: 200kg remaining
- Weekly delivery: Tuesday morning

**Scenarios:**
- Normal: Order placed Friday, delivered Tuesday (3-day lead time)
- Delayed delivery: Scenario 4 (truck breakdown)
- Running low mid-week: Emergency purchase from local supplier at premium

**Sim representation:**
- flour_resource.current_quantity decremented with each mix
- When current_quantity < reorder_point: trigger_order_process
- If delivery_delayed: implement emergency_sourcing (higher cost)
- If inventory = 0: cannot_produce (block mixing processes)

#### Perishable Management
**Dairy products:**
- Shelf life: 7-30 days depending on item
- Storage requirement: <40°F
- If temperature exceeds 40°F for >2 hours: must discard (FDA)

**Fresh herbs:**
- Shelf life: 7 days
- Quality degrades (wilting, browning)
- Affects product quality if used past prime

**Sim representation:**
- resource.shelf_life_days and purchase_date tracked
- If current_date - purchase_date > shelf_life: resource.spoiled = true
- Spoiled resources cannot be used in recipes
- walk_in_cooler temperature excursion: spoil all perishables (scenario 2)

#### Packaging Depletion
**High-volume items:**
- Bread bags: 200-300 used daily
- Can run out mid-day if not monitored

**Impact:**
- Cannot package/sell loaves without bags
- Customer frustration (loaves available but can't purchase)

**Sim representation:**
- packaging_resource.current_quantity decremented per package
- If quantity < reorder_point: warning flag
- If quantity = 0: cannot_package (blocks packaging process)
- Emergency purchase option available (local store, premium cost)

### STATE TRACKING

#### Equipment State Machines
**Mixer states:**
- idle → mixing_low → mixing_high → resting → cleaning → idle
- malfunction (can occur from any state)

**Oven deck states:**
- off → preheating → ready → baking → door_open → cooling → recovered → ready
- malfunction (heating element failure)

**Refrigeration states:**
- operational → door_open → operational
- malfunction → alarm → repair_needed

**Sim representation:**
- Equipment.state property with defined state transitions
- Each state has allowed next states
- Process can only proceed if equipment in correct state
- State transitions have duration (preheating takes 75 minutes)

#### Dough Lifecycle Tracking
**Complete state progression:**
mixed → autolyse → bulk_fermenting → ready_for_shaping → divided → preshaped → final_shaped → cold_proofing → scored → baking → cooling → cooled → packaged → for_sale → sold

**Alternative paths:**
- over_fermented (bulk fermentation too long)
- over_proofed (proof too long)
- spoiled (time/temp abuse)
- defective (baking error)
- damaged (handling error)
- donated (day-old, quality OK but unsold)
- discarded (quality failure)

**Sim representation:**
- dough_batch and loaf_object.state tracks position in lifecycle
- Quality_score tracks cumulative quality impacts
- State gates certain processes (can't bake if not proofed)

#### Cleanliness Tracking
**States:**
- clean → in_use → dirty → cleaning → clean
- Applies to: work surfaces, mixing bowls, containers, baskets

**Impact:**
- Cannot use dirty equipment (health code violation)
- Cleaning takes time (removes actor from production)
- If cleaning neglected: failed health inspection (scenario 5)

**Sim representation:**
- Equipment and container.state includes cleanliness
- Using equipment transitions clean → in_use → dirty
- Cleaning process required before reuse
- Health_inspection_score based on cleanliness state of items

### FAILURE MODES

#### Equipment Failures
**Oven failure (scenario 1):**
- Probability: ~2% per simulation week
- Impact: Cannot bake (175 loaves lost, $1,700 revenue)
- Duration: 2-4 hours if repairable same-day, or 1-3 days if major
- Mitigation: Emergency repair call ($500-800), possible oven rental

**Walk-in cooler failure (scenario 2):**
- Probability: ~1.5% per simulation month
- Impact: Spoiled dairy ($150), over-proofed dough ($300-500 waste)
- Detection: Temperature alarm or morning discovery
- Mitigation: Emergency refrigeration repair ($600-1,200)

**Mixer breakdown:**
- Probability: ~1% per simulation month
- Impact: Cannot mix (blocks all production for day)
- Duration: Same-day repair if motor issue, 2-3 days if parts needed
- Mitigation: Hand mixing small batches possible but impractical for volume

**Sim representation:**
- Equipment.failure_probability checked each simulation day
- If failure occurs: equipment.state = "malfunction"
- All processes requiring equipment blocked
- Repair process initiated (cost, duration variable)
- Revenue_loss calculated based on blocked production

#### Staff Absences (scenario 3)
**Rachel sick (most impactful):**
- Probability: ~3% per simulation week (normal sick rate)
- Impact: Production capacity reduced to 70% (150 loaves vs 220)
- Mitigation: David arrives early, covers 70% of tasks, specialty items skipped
- Cost: Lost revenue ($600-700), David overtime ($81)

**Marcus sick (catastrophic):**
- Probability: ~2% per simulation week
- Impact: Bakery may need to close (Marcus has all critical skills)
- Mitigation: David/Rachel attempt reduced production, quality suffers
- Long-term risk: No succession plan

**Sarah sick (low impact):**
- Probability: ~3% per simulation week
- Impact: Marcus or David covers FOH (takes from production time)
- Revenue impact minimal (customers wait longer but still served)

**Sim representation:**
- actor.availability checked daily (random absence based on probability)
- If key actor unavailable: production_plan adjusted
- quality_score reduced if less-experienced actor covers
- Overtime costs calculated if coverage needed

#### Quality Failures
**Under-baked detection:**
- Occurs: ~2% of loaves
- Detection: Internal temp check, hollow sound test
- Action: Return to oven (5-10 min), or mark for staff/donation
- loaf_object.quality_score < 60

**Over-baked/burnt:**
- Occurs: ~1% of loaves
- Causes: Oven timer missed, temperature too high, forgotten in oven
- Action: Discount sale, breadcrumbs, or discard
- loaf_object.defect_notes = "over_browned"

**Collapsed loaves (over-proofed):**
- Occurs: ~3-5% of loaves if timing off
- Prevention: Proper poke test before baking
- Result: Flat loaf, dense crumb, poor appearance
- Sellable at discount or donated

**Sim representation:**
- Random quality check with probability of defects
- loaf_object.quality_score assigned at multiple checkpoints
- Defective loaves diverted to discount/donation/discard paths
- Ingredient cost wasted, no revenue recovery (or reduced)

## 6. NOTES ON REPRESENTATION CHALLENGES

### DIFFICULT TO MODEL ACCURATELY

#### 1. Fermentation as Biological Process
**Challenge:**
- Fermentation is living process with exponential growth curves
- Influenced by: temperature, time, yeast/bacteria health, pH, enzymes
- Real-world: observe visual/tactile cues (volume, bubbles, smell, texture)
- Simulation: Hard to model biological complexity

**Simplification approach:**
- Use time-based completion with temperature modifiers
- fermentation_target_duration adjusted by temperature variance
- quality_score reflects how close to ideal conditions
- "Ready" state based on time thresholds rather than biological simulation

**Trade-off:**
- Loses nuance of fermentation science
- Cannot model extreme scenarios (contamination, wild yeast issues)
- Adequate for operational simulation purpose

#### 2. Artisan Skill and Judgment
**Challenge:**
- Experienced bakers make hundreds of micro-decisions
- Marcus "knows" when dough is ready by feel, appearance, intuition
- Shaping quality varies by skill level (Rachel vs David)
- Cannot capture tacit knowledge in rules

**Simplification approach:**
- actor.skills array indicates capabilities
- quality_score affected by actor skill level
- Some tasks restricted to specific actors (Marcus only for rye)
- Use probability of success based on experience

**Trade-off:**
- Misses artisan expertise that distinguishes great from good
- Cannot model learning curve (baker improving over time)
- Adequate for capacity planning, less so for quality assessment

#### 3. Customer Behavior and Demand
**Challenge:**
- Customer demand varies by weather, day of week, holidays, random factors
- Word-of-mouth and reputation effects
- Substitution behavior (if Country Sourdough sold out, buy Whole Grain)
- Customer satisfaction affects repeat business

**Simplification approach:**
- Use historical averages for daily demand by product
- Add random variance (±10-15%)
- Special events flagged (holidays increase demand +20%)
- No customer agent modeling (too complex)

**Trade-off:**
- Cannot model marketing campaign effects
- Misses seasonality beyond simple multipliers
- Adequate for production planning, inventory management

#### 4. Equipment Degradation Over Time
**Challenge:**
- Equipment doesn't fail randomly - it degrades
- Oven performance degrades (temperature recovery slower, uneven heating)
- Mixer belt stretches, bearings wear
- Real maintenance history affects failure probability

**Simplification approach:**
- Fixed failure probabilities per time period
- Maintenance resets failure probability partially
- Age of equipment affects failure rate (older = higher probability)

**Trade-off:**
- Doesn't model cumulative wear
- Maintenance appears as discrete events, not continuous degradation
- Adequate for financial planning, risk assessment

#### 5. Sensory Quality Assessment
**Challenge:**
- Bread quality assessed by sight, smell, taste, touch, sound
- "Hollow sound when tapped" - how to model?
- Crust color spectrum from pale to burnt - visual assessment
- Crumb structure - open vs dense, holes distribution

**Simplification approach:**
- quality_score (0-100) as aggregate quality metric
- Specific defect flags: over_proofed, under_baked, burnt, collapsed
- Binary pass/fail for critical checkpoints
- Assume proper sensory assessment by experienced staff

**Trade-off:**
- Loses richness of quality dimensions
- Cannot distinguish subtle quality differences
- Adequate for operational decisions (sell/donate/discard)

### NECESSARY SIMPLIFYING ASSUMPTIONS

#### 1. Perfect Information
**Assumption:**
- Actors always know equipment state, inventory levels, current tasks
- In reality: information gaps, miscommunication, assumptions

**Justification:**
- Small team (4 people) with good communication
- Physical proximity (1500 sq ft space)
- Experienced team familiar with workflow
- Reasonable for this scale

#### 2. Instant Task Switching
**Assumption:**
- Actors can switch tasks immediately when needed
- No cognitive load, context switching penalty

**Reality:**
- Moving between tasks takes mental transition
- Actor might finish current step before switching

**Justification:**
- Simulation time step likely 5-15 minutes (switching within this acceptable)
- Errors from task switching reflected in quality_score variance
- Reasonable approximation for schedule modeling

#### 3. Consistent Recipe Execution
**Assumption:**
- Following recipe produces consistent results every time
- Ingredient variations (flour protein varies batch to batch) ignored
- Measurement errors minimal

**Reality:**
- Even experienced bakers have batch-to-batch variation
- Flour from different harvests behaves differently
- Small errors compound

**Justification:**
- Recipe specifications based on averages
- Quality_score variance captures some variation
- Parkside's 2.5 years experience = refined consistency
- Adequate for operational model

#### 4. Linear Resource Consumption
**Assumption:**
- 1 loaf = exactly specified ingredient amounts
- No spillage, waste, or overhead in scaling

**Reality:**
- Flour dusting benches, baskets (2-3% waste documented)
- Dough sticking to equipment
- Scaling inefficiencies

**Justification:**
- Waste factor built into COGS (18% includes waste)
- For simulation, track "sellable loaves" vs "total flour used"
- Adequate for financial modeling

#### 5. Uniform Product Quality
**Assumption:**
- All loaves of same product type interchangeable
- Individual loaf tracking for state, not for unique quality variations

**Reality:**
- Even in same batch, loaves vary (oven hot spots, shaping differences)
- Corner loaves bake different than center loaves

**Justification:**
- Quality_score per loaf allows some variation
- Defect probability captures random quality failures
- Customer generally cannot distinguish same-batch loaves
- Adequate for inventory and sales modeling

### CRITICAL FOR REALISM

#### 1. Time-Based Process Dependencies
**Must get right:**
- Fermentation cannot be rushed (minimum durations enforced)
- Cold proof window: 8-16 hours (out of range = quality impact)
- Cooling minimums before packaging (especially rye: 6-8 hours)
- Oven preheat: 60-75 minutes lead time

**Why critical:**
- These are hard biological/physical constraints
- Violating these = actual quality failure, not theoretical
- Core to why bakery can't just "go faster"

**Implementation:**
- State transitions gated by time elapsed
- Quality_score severely penalized for violations
- Some violations block subsequent processes

#### 2. Capacity Bottlenecks
**Must get right:**
- Oven: 25 loaves per cycle, bottleneck on Saturday
- Retarder: 200 loaf maximum
- Cooling racks: 80 loaf positions
- Shaping bench: 2-3 people maximum working simultaneously

**Why critical:**
- These drive business constraints (can't grow without investment)
- Scenario testing requires accurate capacity modeling
- Optimization decisions depend on where bottleneck is

**Implementation:**
- Capacity properties on equipment enforced
- Processes blocked when capacity full
- Queue management for constrained resources

#### 3. Labor Allocation and Skill
**Must get right:**
- Rachel handles 60% of hands-on production
- Marcus required for rye bread, oven management, quality control
- David cannot fully replace Rachel (70% capability)
- Staff absences have asymmetric impact

**Why critical:**
- Labor is highest cost (38% of revenue)
- Staff planning decisions require accurate model
- Succession planning, cross-training priorities depend on this

**Implementation:**
- Tasks specify required_skills
- Actors have skill arrays
- Task quality affected by actor skill level
- Some tasks restricted to specific actors

#### 4. Financial Accuracy
**Must get right:**
- Ingredient costs per loaf
- Revenue by channel (retail vs wholesale)
- Gross margins by product
- Operating costs (labor, utilities, rent)

**Why critical:**
- Business viability depends on profitability
- Product mix decisions driven by margin analysis
- Investment decisions require ROI calculation

**Implementation:**
- All financial properties based on actual model data
- Track costs accumulated throughout processes
- Revenue calculated at sale transaction
- Daily/weekly/monthly financial rollups

#### 5. Quality Gates and Consequences
**Must get right:**
- DDT (dough temperature) out of range = fermentation timing issues
- Poke test failure = quality problem in bake
- Over-proofed loaves collapse
- Under-cooled bread = soggy packaging, mold growth

**Why critical:**
- Quality failures have real costs (waste, donations, discounts)
- Health and safety implications
- Customer satisfaction affects repeat business
- These are actual operational pain points

**Implementation:**
- Quality checkpoints at key processes
- quality_score tracking cumulative impacts
- Failed quality gates divert loaves to alternative paths
- Financial impact of quality failures calculated

### WHAT CAN BE ABSTRACTED

#### 1. Exact Spatial Layout
**Can simplify:**
- Don't need precise X,Y coordinates of equipment
- "production_zone" vs "front_of_house" sufficient
- Movement time between areas negligible (small space)

**Just track:**
- Object.location as zone identifier
- Actor.location as current zone
- Capacity constraints within zones

#### 2. Detailed Recipe Chemistry
**Can simplify:**
- Don't need to model gluten strand formation
- Don't need pH tracking, enzyme activity curves
- Hydration percentage affects handling but not modeled mechanistically

**Just track:**
- Ingredient quantities
- Time and temperature (proxy for chemistry)
- Outcome quality (score)

#### 3. Individual Customer Tracking
**Can simplify:**
- No need for customer agents with preferences
- Aggregate demand by product sufficient
- Average transaction value adequate

**Just track:**
- Daily sales volume by product
- Revenue by channel
- Inventory depletion

#### 4. Micro-movements and Sub-tasks
**Can simplify:**
- "Shape loaf" as atomic action (don't model each fold, tuck, roll)
- "Mix dough" as single process (not each speed change)
- "Package loaf" includes bag, label, in one step

**Just track:**
- Process duration (aggregate time)
- Actor occupied during process
- Input and output states

#### 5. Ambient Conditions
**Can simplify:**
- Room temperature assumed stable 68-72°F (unless HVAC failure)
- Humidity not modeled (except in retarder)
- Air flow, drafts ignored

**Just track:**
- Temperature for cold storage (critical)
- Temperature deviations only when significant impact
- Assume normal conditions otherwise

## RECOMMENDATIONS FOR SIMULATION ENGINE

### Object Model Enhancements

1. **Support for custom object types with inheritance:**
   - Base types: actor, equipment, resource, product
   - Custom types inherit base properties, add specialized properties
   - Example: oven_deck extends equipment with thermal properties

2. **Time-based property evolution:**
   - Properties that change over time without explicit interactions
   - Example: levain.activity_level evolves from "dormant" → "rising" → "peak" → "falling"
   - Example: dough.temperature gradually equilibrates to ambient

3. **Composite objects and containment:**
   - Objects that contain other objects
   - Example: oven contains 3 oven_decks
   - Example: fermentation_container contains dough_batch
   - Enables capacity constraints, spatial reasoning

### Process Modeling Enhancements

1. **State-dependent process availability:**
   - Process can only execute if prerequisites met
   - Check object states, property values, resource availability
   - Example: "bake_loaves" requires oven.state = "ready" AND loaves.state = "proofed"

2. **Conditional duration and outcomes:**
   - Process duration affected by object properties
   - Example: fermentation_duration = base_duration * temperature_factor
   - Outcome quality affected by execution conditions

3. **Parallel process management:**
   - Multiple processes on different objects simultaneously
   - Resource contention (multiple processes want same actor)
   - Example: 3 batches in different fermentation stages at once

### Temporal Modeling

1. **Time-window constraints:**
   - Some processes must occur within specific time windows
   - Example: shaping_session must happen 12:00-14:00
   - Missed windows have consequences (cascade delays)

2. **Schedule templates by day type:**
   - Different schedules for weekday/Saturday/Sunday/Monday
   - Production quantities vary by day
   - Staffing patterns change

3. **Event-driven vs clock-driven:**
   - Some processes triggered by time (4:00 AM oven preheat)
   - Some triggered by state change (bulk_fermentation_complete → begin_shaping)
   - Mix of both in realistic operation

### Quality and Realism

1. **Quality score tracking:**
   - Cumulative quality impacts through lifecycle
   - Different paths for high/medium/low quality items
   - Financial implications of quality levels

2. **Failure modes and recovery:**
   - Random equipment failures with probabilities
   - Staff absences with mitigation strategies
   - Quality failures with corrective actions
   - Cost and time impacts of failures

3. **Resource management:**
   - Inventory depletion and reordering
   - Lead times for deliveries
   - Emergency procurement at premium cost
   - Spoilage and waste

This comprehensive analysis provides the foundation for converting the Parkside Bakery operational model into a working Universal Automation Wiki simulation. The level of detail enables realistic modeling while identifying where simplifications are acceptable versus where precision is critical for meaningful simulation results.