# PARKSIDE BAKERY - COMPLETE OBJECT SPECIFICATION DOCUMENT

## TABLE OF CONTENTS
1. Staff (Actors)
2. Custom Type: Levain Culture
3. Custom Type: Dough Batch
4. Custom Type: Individual Loaf
5. Custom Type: Oven Deck
6. Custom Type: Proofing Basket
7. Custom Type: Fermentation Container
8. Custom Type: Cooling Rack Position
9. Custom Type: Storage Location
10. Custom Type: Ingredient (Bakery-Specific)
11. Equipment (Standard Type)
12. Products (Finished Goods)
13. Resources (Generic Consumables)
14. Locations (Spatial Zones)

---

## 1. STAFF (TYPE: ACTOR)

### OBJECT: marcus_chen
```
ID: actor_marcus_chen
Type: actor
Name: Marcus Chen (Owner/Head Baker)
Emoji: 👨‍🍳

Properties:
- role: "owner_head_baker" (string, defines primary function)
- employment_type: "salaried_owner" (string, compensation structure)
- annual_salary: 52000 (USD/year, numeric, base draw)
- hourly_rate: null (not hourly paid)
- guaranteed_hours_weekly: null (salaried, works as needed)
- typical_hours_weekly: 50 (hours/week, numeric, actual average)
- shift_start_time: "03:45" (24-hour time string, typical arrival)
- shift_end_time: "14:00" (24-hour time string, typical departure)
- work_days: ["tuesday", "wednesday", "thursday", "friday", "saturday", "monday_admin"] (array of strings)
- skills: ["starter_maintenance", "levain_building", "all_mixing", "dough_temperature_control", "oven_management", "steam_injection", "quality_control_expert", "shaping_all_styles", "baguette_scoring", "sourdough_scoring", "scheduling", "wholesale_account_management", "equipment_maintenance", "recipe_development", "financial_management", "rye_bread_specialist"] (array of strings, capabilities)
- experience_years: 15 (years, numeric, professional baking)
- skill_level_mixing: 100 (0-100 scale, expert)
- skill_level_shaping: 100 (0-100 scale, expert)
- skill_level_baking: 100 (0-100 scale, expert)
- skill_level_quality_assessment: 100 (0-100 scale, expert)
- servesafe_certified: true (boolean, food safety)
- current_task: null (string, references task_id when assigned)
- current_location: null (string, references location_id)
- fatigue_level: 0 (0-100 scale, increases with work duration)
- can_open_bakery: true (boolean, has keys and authority)
- can_close_bakery: true (boolean, has keys and authority)
- decision_making_authority: "full" (string, can make all operational decisions)
- phone_number: "+1-555-0101" (string, for emergency contact)
- emergency_contact_available: true (boolean, can be called in for issues)

Rationale: Marcus is the linchpin of the entire operation. His expertise enables quality control, troubleshooting, and all critical decision-making. His properties need to reflect his capability to perform any task and his availability patterns. The skill_level properties allow for quality differentiation when he performs tasks vs. other staff.
```

### OBJECT: rachel_martinez
```
ID: actor_rachel_martinez
Type: actor
Name: Rachel Martinez (Production Baker)
Emoji: 👩‍🍳

Properties:
- role: "production_baker" (string, primary production work)
- employment_type: "hourly_full_time" (string, compensation structure)
- annual_salary: null (not salaried)
- hourly_rate: 19.50 (USD/hour, numeric, base rate)
- overtime_rate: 29.25 (USD/hour, numeric, time-and-a-half for hours >40)
- guaranteed_hours_weekly: 40 (hours/week, numeric, minimum commitment)
- typical_hours_weekly: 44 (hours/week, numeric, actual average with OT)
- shift_start_time: "04:30" (24-hour time string, typical arrival)
- shift_end_time: "14:30" (24-hour time string, typical departure)
- work_days: ["tuesday", "wednesday", "thursday", "friday", "saturday"] (array of strings)
- skills: ["mixer_operation", "bulk_fermentation_management", "dough_dividing", "preshaping_all_styles", "final_shaping_batard", "final_shaping_boule", "final_shaping_baguette", "baguette_specialist", "fold_cycles", "banneton_loading", "retarder_management", "wholesale_packing", "ciabatta_handling", "enriched_dough_mixing"] (array of strings, capabilities)
- experience_years: 5 (years, numeric, professional baking)
- skill_level_mixing: 85 (0-100 scale, very competent)
- skill_level_shaping: 90 (0-100 scale, excellent, especially baguettes)
- skill_level_baking: 70 (0-100 scale, competent but less experienced)
- skill_level_quality_assessment: 75 (0-100 scale, good eye but learning)
- servesafe_certified: true (boolean, food safety)
- current_task: null (string, references task_id when assigned)
- current_location: null (string, references location_id)
- fatigue_level: 0 (0-100 scale, increases with work duration)
- can_open_bakery: true (boolean, has keys, can open if Marcus unavailable)
- can_close_bakery: true (boolean, can close production area)
- decision_making_authority: "production_only" (string, limited to production decisions)
- phone_number: "+1-555-0102" (string, for emergency contact)
- emergency_contact_available: false (boolean, cannot reliably come in on days off)
- specialization_notes: "Handles 60% of hands-on production volume, baguette expert" (string, key role descriptor)

Rationale: Rachel is the production workhorse. Her skill levels are high but not perfect - this creates variation in output quality. She's critical for volume production but has limitations that create dependencies (e.g., if she's absent, production drops significantly). Her baguette specialization is modeled explicitly.
```

### OBJECT: david_kim
```
ID: actor_david_kim
Type: actor
Name: David Kim (Baker/Shift Supervisor)
Emoji: 👨‍🍳

Properties:
- role: "baker_shift_supervisor" (string, secondary baker with supervisory duties)
- employment_type: "hourly_full_time" (string, compensation structure)
- annual_salary: null (not salaried)
- hourly_rate: 18.00 (USD/hour, numeric, base rate)
- overtime_rate: 27.00 (USD/hour, numeric, time-and-a-half)
- guaranteed_hours_weekly: 38 (hours/week, numeric, slightly less than full-time)
- typical_hours_weekly: 39 (hours/week, numeric, actual average)
- shift_start_time: "05:00" (24-hour time string, starts after Marcus/Rachel)
- shift_end_time: "13:30" (24-hour time string, typical departure)
- work_days: ["wednesday", "thursday", "friday", "saturday", "sunday"] (array of strings)
- skills: ["oven_monitoring", "focaccia_production_specialist", "ciabatta_production", "specialty_breads", "foh_restocking", "quality_checks_visual", "backup_shaping", "sunday_opening_procedures", "enriched_bread_assistance", "olive_rosemary_production", "seasonal_focaccia_topping"] (array of strings, capabilities)
- experience_years: 3 (years, numeric, professional baking)
- skill_level_mixing: 65 (0-100 scale, can assist but not primary)
- skill_level_shaping: 70 (0-100 scale, competent, learning from Rachel)
- skill_level_baking: 85 (0-100 scale, strong oven management skills)
- skill_level_quality_assessment: 70 (0-100 scale, good visual inspection)
- servesafe_certified: true (boolean, food safety)
- current_task: null (string, references task_id when assigned)
- current_location: null (string, references location_id)
- fatigue_level: 0 (0-100 scale, increases with work duration)
- can_open_bakery: true (boolean, has keys, handles Sunday opening)
- can_close_bakery: true (boolean, can close after Sunday shift)
- decision_making_authority: "shift_supervisor" (string, can make decisions during his shift, especially Sunday)
- phone_number: "+1-555-0103" (string, for emergency contact)
- emergency_contact_available: true (boolean, can sometimes come in early if emergency)
- backup_capacity_for_rachel: 70 (percentage, can cover 70% of Rachel's duties in emergency)
- specialization_notes: "Focaccia specialist, handles all focaccia production, Sunday supervisor" (string)

Rationale: David fills a critical middle-tier role - experienced enough to handle complex tasks (focaccia, oven management) but not at Marcus/Rachel's level for high-skill work (baguette shaping, precise mixing). His Sunday opening role and backup capacity for Rachel are critical for continuity modeling.
```

### OBJECT: sarah_thompson
```
ID: actor_sarah_thompson
Type: actor
Name: Sarah Thompson (FOH Lead)
Emoji: 👩‍💼

Properties:
- role: "foh_lead" (string, front-of-house customer service)
- employment_type: "hourly_part_time" (string, compensation structure)
- annual_salary: null (not salaried)
- hourly_rate: 16.50 (USD/hour, numeric, base rate)
- overtime_rate: 24.75 (USD/hour, numeric, time-and-a-half, rarely used)
- guaranteed_hours_weekly: 30 (hours/week, numeric, part-time commitment)
- typical_hours_weekly: 30 (hours/week, numeric, consistent)
- shift_start_time: "06:30" (24-hour time string, before store opening)
- shift_end_time: "12:30" (24-hour time string, typical departure weekdays)
- shift_end_time_sunday: "14:00" (24-hour time string, stays for close on Sunday)
- work_days: ["wednesday", "thursday", "friday", "saturday", "sunday"] (array of strings)
- skills: ["customer_service", "pos_operation", "display_case_management", "bread_slicing", "retail_packaging", "social_media_posting", "online_order_fulfillment", "inventory_counting", "wholesale_customer_handoff", "cash_handling", "product_knowledge", "customer_education"] (array of strings, capabilities)
- experience_years: 2 (years, numeric, in retail/food service)
- skill_level_customer_service: 90 (0-100 scale, excellent with customers)
- skill_level_product_knowledge: 80 (0-100 scale, well-informed about bread)
- skill_level_visual_merchandising: 85 (0-100 scale, good display arrangement)
- servesafe_certified: true (boolean, food safety for handling)
- current_task: null (string, references task_id when assigned)
- current_location: "front_of_house" (string, default location, rarely leaves FOH)
- fatigue_level: 0 (0-100 scale, increases with work duration)
- can_open_bakery: false (boolean, no keys to production area)
- can_close_bakery: false (boolean, Marcus or David close)
- decision_making_authority: "foh_only" (string, can make customer service decisions only)
- phone_number: "+1-555-0104" (string, for emergency contact)
- emergency_contact_available: false (boolean, part-time, not available outside scheduled hours)
- cash_drawer_responsibility: true (boolean, handles all cash)
- social_media_credentials: true (boolean, posts to Instagram/Facebook)

Rationale: Sarah is the customer-facing interface. Her properties focus on service and sales capabilities. She has no production skills and minimal authority, but is critical for revenue realization (no sales without her). Her social media role links to marketing/customer acquisition.
```

---

## 2. CUSTOM TYPE: LEVAIN_CULTURE

### OBJECT: mother_starter
```
ID: levain_mother_starter
Type: levain_culture
Name: Mother Starter (Sourdough Culture)
Emoji: 🫙

Properties:
- culture_id: "mother_starter_main" (string, unique identifier)
- culture_type: "mother" (string, indicates this is the perpetual starter)
- health: 95 (0-100 scale, current vitality, affects fermentation reliability)
- activity_level: "peak" (enum: ["dormant", "rising", "peak", "falling", "sluggish"], current fermentation state)
- weight_g: 600 (grams, numeric, current total mass)
- hydration_percent: 100 (percentage, numeric, equal parts flour and water by weight)
- last_fed_timestamp: null (ISO timestamp, when last feeding occurred)
- next_feeding_due_timestamp: null (ISO timestamp, when next feeding should occur)
- feeding_interval_hours: 10 (hours, numeric, typical time between feedings)
- temperature_current_f: 38 (degrees Fahrenheit, numeric, current storage temp)
- temperature_optimal_storage_f: 38 (degrees F, numeric, cold storage ideal)
- temperature_optimal_feeding_f: 70 (degrees F, numeric, room temp for feeding)
- location: "walk_in_cooler" (string, references location_id where stored)
- container_type: "sealed_plastic_tub" (string, descriptor)
- volume_increase_since_feeding: 0 (percentage, 0-200%, indicates rise)
- aroma: "pleasant_tangy" (enum: ["pleasant_tangy", "vinegary", "acetone", "neutral"], indicates health)
- flour_composition: {"bread_flour_organic": 0.85, "whole_wheat_organic": 0.15} (object, ratios by type)
- age_days: 912 (days, numeric, how long starter has been maintained, 2.5 years)
- discard_amount_per_feeding_g: 200 (grams, numeric, removed before feeding)
- feeding_flour_amount_g: 200 (grams, numeric, added during feeding)
- feeding_water_amount_g: 200 (grams, numeric, added during feeding)
- feeding_water_temp_target_f: 80 (degrees F, numeric, warm water accelerates fermentation)
- state: "healthy" (enum: ["healthy", "weak", "contaminated", "dead"], overall condition)
- contamination_risk: 0.01 (0-1 probability, chance of spoilage per day without feeding)
- can_be_used_for_production: true (boolean, quality gate)
- backup_culture_exists: true (boolean, indicates redundancy)

Rationale: The mother starter is the biological foundation of all sourdough production. Its health directly impacts every sourdough loaf. The activity_level and health properties drive fermentation timing - a weak starter creates cascade delays. Temperature tracking is critical because fermentation speed is exponentially temperature-dependent. The age property reflects that this is an established, stable culture (not a new, unpredictable one).
```

### OBJECT: production_levain_tuesday
```
ID: levain_production_tuesday
Type: levain_culture
Name: Production Levain (Tuesday Build)
Emoji: 🫙

Properties:
- culture_id: "production_levain_tuesday_20251022" (string, unique per build with date)
- culture_type: "production" (string, indicates this is a one-time build for specific day)
- health: 95 (0-100, inherited from mother starter)
- activity_level: "dormant" (enum, just mixed, not yet active)
- weight_g: 4500 (grams, numeric, total batch size for day's needs)
- hydration_percent: 100 (percentage, numeric, equal flour/water)
- build_timestamp: null (ISO timestamp, when mixed)
- target_peak_timestamp: null (ISO timestamp, when should reach peak activity, typically +6-8 hours)
- temperature_current_f: 78 (degrees F, numeric, warm ambient to speed fermentation)
- temperature_target_f: 78 (degrees F, numeric, optimal for 6-8 hour fermentation)
- location: "fermentation_ambient_warm_zone" (string, references location_id)
- container_id: "fermentation_container_22qt_1" (string, references container it's in)
- volume_increase_since_build: 0 (percentage, 0-200%, visual rise indicator)
- target_volume_increase: 100 (percentage, should double)
- aroma: "neutral_yeasty" (enum, changes as ferments)
- flour_composition: {"bread_flour_organic": 0.85, "whole_wheat_organic": 0.15} (object, ratios)
- mother_starter_amount_used_g: 500 (grams, numeric, how much mother went into this)
- flour_added_g: 2000 (grams, numeric)
- water_added_g: 2000 (grams, numeric)
- state: "building" (enum: ["building", "peak", "past_peak", "unusable"], fermentation state)
- peak_duration_window_hours: 2 (hours, numeric, how long it stays at peak before declining)
- amount_needed_for_production_g: 4500 (grams, numeric, matches total - entire batch will be used)
- check_timestamps: [] (array of ISO timestamps, when Marcus/Rachel should visually assess)
- readiness_for_production: false (boolean, quality gate, becomes true at peak)
- float_test_passed: null (boolean or null, test performed near peak time)

Rationale: Production levain is a time-critical intermediate. It must be ready exactly when needed (10 AM - 2 PM window) or the entire day's sourdough schedule delays. The activity_level progresses dormant → rising → peak → falling, and production can only proceed at peak. This creates a timing dependency. Unlike the mother starter which is perpetual, production levain is built fresh daily and fully consumed.
```

---

## 3. CUSTOM TYPE: DOUGH_BATCH

### OBJECT: country_sourdough_batch1_tuesday
```
ID: dough_country_sourdough_batch1_tue_20251022
Type: dough_batch
Name: Country Sourdough Batch 1 (Tuesday)
Emoji: 🍞

Properties:
- batch_id: "country_sourdough_batch1_tue_20251022" (string, unique identifier with date)
- recipe_type: "country_sourdough" (string, references product recipe)
- target_product_id: "product_country_sourdough_900g" (string, references final product)
- state: "not_started" (enum: ["not_started", "autolyse", "mixing", "bulk_fermenting", "ready_for_shaping", "divided", "over_fermented", "spoiled"], lifecycle state)
- weight_kg: 22.5 (kilograms, numeric, total dough mass for batch, enough for 25 loaves)
- target_loaf_count: 25 (integer, how many loaves this batch yields)
- loaf_weight_target_g: 1000 (grams, numeric, pre-bake weight per loaf)

- temperature_f: null (degrees F, numeric, actual measured dough temp after mixing, critical quality metric)
- temperature_target_f: 76 (degrees F, numeric, desired dough temp, DDT)
- temperature_tolerance_lower_f: 72 (degrees F, numeric, below this = slow fermentation)
- temperature_tolerance_upper_f: 82 (degrees F, numeric, above this = too fast, off flavors)

- autolyse_start_timestamp: null (ISO timestamp, when flour+water mixed)
- autolyse_duration_minutes: 40 (minutes, numeric, rest period before final mix)
- autolyse_complete: false (boolean, gate for next step)

- mix_start_timestamp: null (ISO timestamp, when final mixing began)
- mix_time_low_speed_minutes: 3 (minutes, numeric)
- mix_time_high_speed_minutes: 8 (minutes, numeric)
- total_mix_time_minutes: 11 (minutes, numeric, sum of speeds)
- mix_complete: false (boolean, gate for bulk fermentation)

- bulk_fermentation_start_timestamp: null (ISO timestamp, when bulk ferment began)
- bulk_fermentation_target_duration_minutes: 270 (minutes, numeric, 4.5 hours nominal)
- bulk_fermentation_actual_duration_minutes: null (minutes, numeric, actual elapsed time)
- fermentation_container_id: "fermentation_container_22qt_2" (string, references container)
- current_location: null (string, references location_id)

- fold_count: 0 (integer, 0-4, how many stretch-and-folds performed)
- fold_schedule: [45, 90, 135, 180] (array of minutes, when folds should occur)
- next_fold_due_timestamp: null (ISO timestamp, when next fold should happen)
- folds_complete: false (boolean, all 4 folds done)

- volume_increase_percent: 0 (percentage, 0-200%, observed rise in container)
- target_volume_increase_percent: 85 (percentage, minimum for "ready")
- surface_appearance: "shaggy" (enum: ["shaggy", "smooth", "domed", "collapsed"], visual indicator)
- bubble_formation: "none" (enum: ["none", "few", "moderate", "abundant"], visual indicator)
- wobble_test_passed: false (boolean, indicates gas retention)
- poke_test_result: null (enum: ["springs_back_fast", "springs_back_slow", "no_spring"], readiness test)

- quality_score: 100 (0-100 scale, degrades if conditions violated)
- quality_notes: [] (array of strings, issues encountered)

- ingredient_costs_usd: 61.20 (USD, numeric, calculated from recipe x quantities)
- labor_hours_invested: 0 (hours, numeric, cumulative actor time on this batch)

- over_fermented: false (boolean, flag if fermentation went too long)
- under_fermented: false (boolean, flag if rushed)
- discard_reason: null (string, if spoiled/wasted, why)

Rationale: Dough batch is the core production tracking object. Its state property drives workflow progression - tasks can only execute when dough is in correct state. The temperature property is critical: out-of-range temps cascade into timing issues. Fold tracking ensures proper gluten development. Quality_score accumulates impacts from all violations (temp, timing, handling). This batch object will spawn 25 individual loaf objects when divided.
```

### TEMPLATE FOR OTHER DOUGH BATCHES:
(Similar structure applies to whole_grain_sourdough_batch, seeded_multigrain_batch, baguette_batch, ciabatta_batch, etc. Each has recipe-specific properties like hydration_percent, add_ins (olives, seeds), and timing parameters.)

---

## 4. CUSTOM TYPE: INDIVIDUAL_LOAF

### OBJECT: country_sourdough_loaf_001
```
ID: loaf_country_sourdough_001_tue_20251022
Type: individual_loaf
Name: Country Sourdough Loaf #001
Emoji: 🥖

Properties:
- loaf_id: "country_sourdough_001_tue_20251022" (string, unique identifier)
- parent_batch_id: "dough_country_sourdough_batch1_tue_20251022" (string, references source batch)
- product_type: "country_sourdough_900g" (string, references product definition)
- state: "not_divided" (enum: ["not_divided", "divided", "preshaped", "bench_resting", "final_shaped", "cold_proofing", "warming", "scored", "baking", "cooling", "cooled", "packaged", "for_sale", "sold", "donated", "discarded"], lifecycle)

- weight_g: null (grams, numeric, actual measured weight when divided)
- weight_target_g: 1000 (grams, numeric, target pre-bake weight)
- weight_baked_g: null (grams, numeric, post-bake weight, ~10% loss)
- weight_variance_percent: null (percentage, how far from target)

- divided_timestamp: null (ISO timestamp, when cut from batch)
- preshaped_timestamp: null (ISO timestamp)
- bench_rest_start_timestamp: null (ISO timestamp)
- bench_rest_duration_minutes: 25 (minutes, numeric, required rest)
- final_shaped_timestamp: null (ISO timestamp)
- final_shape_style: "batard" (enum: ["batard", "boule", "baguette", etc.], shape type)

- proofing_basket_id: null (string, references proofing_basket when assigned)
- proof_start_timestamp: null (ISO timestamp)
- proof_location: null (enum: ["room_temp", "retarder"], where proofing)
- proof_duration_hours: null (hours, numeric, actual time)
- proof_target_duration_hours: 11 (hours, numeric, ideal for cold proof)
- temperature_during_proof_f: null (degrees F, numeric)

- poke_test_result: null (enum: ["under_proofed", "properly_proofed", "over_proofed"], pre-bake assessment)
- under_proofed: false (boolean, quality flag)
- over_proofed: false (boolean, quality flag)

- scoring_pattern: "deep_cross" (string, describes cuts made)
- scored_timestamp: null (ISO timestamp)
- scored_by_actor_id: null (string, who scored it)

- oven_deck_id: null (string, references oven_deck during bake)
- bake_start_timestamp: null (ISO timestamp)
- bake_end_timestamp: null (ISO timestamp)
- bake_duration_minutes: null (minutes, numeric, actual time)
- bake_target_duration_minutes: 38 (minutes, numeric)
- oven_temp_f: null (degrees F, numeric, actual during bake)
- steam_applied: null (boolean, whether steam was used)

- internal_temp_f: null (degrees F, numeric, measured post-bake for sample loaves)
- internal_temp_target_f: 209 (degrees F, numeric, ideal for sourdough)
- crust_color: null (enum: ["pale", "golden", "deep_golden", "dark_brown", "burnt"], visual assessment)
- crust_appearance: null (enum: ["perfect", "good", "acceptable", "defective"], overall)
- oven_spring_quality: null (enum: ["excellent", "good", "poor", "collapsed"], rise in oven)
- scoring_ear_formation: null (enum: ["prominent", "moderate", "minimal", "none"], visual quality)

- cooling_rack_id: null (string, references cooling_rack during cooling)
- cooling_start_timestamp: null (ISO timestamp)
- cooling_duration_hours: null (hours, numeric, actual)
- cooling_target_duration_hours: 3 (hours, numeric, minimum)
- ready_for_packaging: false (boolean, quality gate)

- package_timestamp: null (ISO timestamp)
- package_type: "kraft_bread_bag_6x3x12" (string, references packaging material)
- sliced: false (boolean, whether customer requested slicing)
- labeled: false (boolean, whether branded sticker applied)

- display_case_timestamp: null (ISO timestamp, when moved to display)
- display_tier: null (integer, 1-3, which shelf in display case)

- sale_timestamp: null (ISO timestamp, when purchased)
- sale_channel: null (enum: ["retail", "wholesale", "online"], where sold)
- sale_price_usd: null (USD, numeric, actual sale price)
- customer_id: null (string, if tracked, for loyalty or wholesale)

- quality_score: 100 (0-100 scale, cumulative quality impacts)
- defect_notes: [] (array of strings, issues found)
- defect_type: null (enum: ["under_baked", "over_baked", "torn_score", "collapsed", "cosmetic", "none"])

- ingredient_cost_usd: 2.72 (USD, numeric, COGS for this loaf)
- allocated_labor_cost_usd: null (USD, numeric, calculated share of labor)
- gross_margin_usd: null (USD, numeric, sale_price - costs)

- donated: false (boolean, if given to food bank)
- discarded: false (boolean, if wasted)
- discard_reason: null (string, why discarded if applicable)

Rationale: Individual loaf tracking enables quality control, sales tracking, and waste accounting. Each loaf has its own quality journey - two loaves from same batch can have different outcomes (one over-proofed, one perfect). The state progression maps to the production flow. Quality_score accumulates violations. This granularity allows simulation of defect rates and their financial impact.
```

---

## 5. CUSTOM TYPE: OVEN_DECK

### OBJECT: oven_deck_1
```
ID: equipment_oven_deck_1
Type: oven_deck
Name: Main Oven - Deck 1 (Top)
Emoji: 🔥

Properties:
- deck_id: "deck_1" (string, unique identifier)
- parent_oven_id: "equipment_main_oven_lbc_se932" (string, references parent oven)
- deck_position: "top" (enum: ["top", "middle", "bottom"], physical position)

- capacity_pans: 3 (integer, full-size sheet pans that fit)
- capacity_loaves_batard: 8 (integer, how many oval loaves fit)
- capacity_loaves_boule: 10 (integer, how many round loaves fit)
- capacity_baguettes: 8 (integer, how many baguettes fit)
- current_load_count: 0 (integer, how many items currently baking)
- contents: [] (array of loaf_ids, what's currently on this deck)
- contents_product_type: null (string, ensures single product type per bake)

- state: "off" (enum: ["off", "preheating", "ready", "baking", "door_open", "cooling", "malfunction"], operational state)
- temperature_current_f: 70 (degrees F, numeric, ambient when off)
- temperature_target_f: 500 (degrees F, numeric, set point)
- temperature_tolerance_f: 10 (degrees F, numeric, acceptable variance)
- heating_rate_f_per_minute: 6.5 (degrees F/min, numeric, how fast it heats)
- preheat_time_minutes: 70 (minutes, numeric, from cold to 500F)

- stone_hearth_thickness_inches: 2 (inches, numeric, thermal mass)
- interior_height_inches: 8 (inches, numeric, clearance for loaves)

- power_consumption_kw: 11 (kilowatts, numeric, when heating at full power)
- power_consumption_current_kw: 0 (kilowatts, numeric, current draw)
- duty_cycle_percent: 0 (percentage, 0-100, how often heating element is on)

- steam_system_available: true (boolean, whether deck has steam injection)
- steam_burst_duration_seconds: 3 (seconds, numeric, initial burst)
- steam_sustained_duration_seconds: 8 (seconds, numeric, sustained injection)
- last_steam_injection_timestamp: null (ISO timestamp)
- steam_reservoir_full: true (boolean, needs occasional refill)

- bake_start_timestamp: null (ISO timestamp, when current bake began)
- bake_end_timestamp: null (ISO timestamp, when current bake should complete)
- bake_target_duration_minutes: null (minutes, numeric, product-specific)
- steam_phase_duration_minutes: 15 (minutes, numeric, vents closed for steam)
- dry_phase_duration_minutes: null (minutes, numeric, calculated as total_bake - steam_phase)
- vents_state: "closed" (enum: ["closed", "open"], damper position for moisture control)
- vents_open_timestamp: null (ISO timestamp, when switched to dry phase)

- recovery_time_minutes: 12 (minutes, numeric, time to return to temp after cold load)
- last_door_open_timestamp: null (ISO timestamp)
- door_open_duration_seconds: 0 (seconds, numeric, cumulative time door was open)

- cycles_completed_today: 0 (integer, how many bakes finished on current day)
- cycles_completed_lifetime: 847 (integer, total since installation, for maintenance tracking)
- last_maintenance_timestamp: "2025-09-15T10:00:00Z" (ISO timestamp)
- next_maintenance_due_timestamp: "2025-12-15T10:00:00Z" (ISO timestamp)
- maintenance_interval_days: 90 (days, numeric, quarterly service)

- malfunction_probability_per_cycle: 0.0002 (0-1 probability, 0.02% per bake)
- malfunction_type: null (enum: ["heating_element", "thermostat", "steam_system", "door_seal", null])
- operational: true (boolean, can be used)

- heat_distribution_uniformity: 0.95 (0-1 scale, 1.0 = perfectly even, affects quality)
- hot_spots: ["rear_right"] (array of strings, areas that run hot)
- cool_spots: [] (array of strings, areas that run cool)

Rationale: Each oven deck is an independent resource with its own capacity, temperature, and state. The three decks can operate simultaneously at different temperatures for different products. State management prevents overloading (can't load if state != "ready"). Temperature recovery time creates scheduling dependencies. Steam system is critical for crust development. Malfunction probability creates realistic equipment failure scenarios.
```

### OBJECT: oven_deck_2
```
ID: equipment_oven_deck_2
Type: oven_deck
Name: Main Oven - Deck 2 (Middle)
Emoji: 🔥

Properties:
[Same structure as deck_1, with these differences:]
- deck_id: "deck_2"
- deck_position: "middle"
- cycles_completed_lifetime: 851 (slightly different wear)
- heat_distribution_uniformity: 0.97 (middle deck tends to be most even)
- hot_spots: [] (middle deck has best heat distribution)
- cool_spots: ["front_left"] (minor cool spot)

Rationale: Middle deck often has most consistent performance in stack ovens due to insulation from decks above/below.
```

### OBJECT: oven_deck_3
```
ID: equipment_oven_deck_3
Type: oven_deck
Name: Main Oven - Deck 3 (Bottom)
Emoji: 🔥

Properties:
[Same structure as deck_1, with these differences:]
- deck_id: "deck_3"
- deck_position: "bottom"
- cycles_completed_lifetime: 839 (slightly less used)
- heat_distribution_uniformity: 0.93 (bottom deck has more variation)
- hot_spots: ["rear_center"] (bottom deck runs hotter in back)
- cool_spots: ["front"] (heat rises, front cooler)
- recovery_time_minutes: 14 (slightly slower due to position)

Rationale: Bottom deck typically has longest recovery time and least uniform heating. These subtle differences affect product quality and scheduling decisions.
```

---

## 6. CUSTOM TYPE: PROOFING_BASKET

### OBJECT: proofing_basket_001
```
ID: equipment_proofing_basket_001
Type: proofing_basket
Name: Proofing Basket (Banneton) #001
Emoji: 🧺

Properties:
- basket_id: "banneton_001" (string, unique identifier)
- shape: "round" (enum: ["round", "oval"], determines loaf shape)
- diameter_inches: 9 (inches, numeric, for round baskets)
- length_inches: null (inches, numeric, for oval baskets, null for round)
- width_inches: null (inches, numeric, for oval baskets)
- height_inches: 3.5 (inches, numeric, depth)
- capacity_min_g: 800 (grams, numeric, minimum dough weight)
- capacity_max_g: 1000 (grams, numeric, maximum dough weight)
- capacity_optimal_g: 900 (grams, numeric, ideal for best shape)

- state: "empty" (enum: ["empty", "occupied", "dirty", "cleaning", "drying"], current status)
- contents_loaf_id: null (string, references loaf_id when occupied)
- location: "banneton_storage_rack" (string, references location_id)

- material: "natural_rattan" (string, construction material)
- liner_present: true (boolean, whether linen liner is installed)
- liner_state: "clean" (enum: ["clean", "needs_washing", "washing", "drying"])
- flour_coating: "fresh" (enum: ["fresh", "adequate", "depleted", "needs_refresh"], prevents sticking)
- flour_type_used: "rice_flour" (string, what flour used for dusting)

- last_used_timestamp: null (ISO timestamp)
- last_cleaned_timestamp: "2025-10-15T14:00:00Z" (ISO timestamp)
- uses_since_cleaning: 0 (integer, counter)
- cleaning_required_after_uses: 50 (integer, when liner should be washed)
- last_sun_dried_timestamp: "2025-10-01T12:00:00Z" (ISO timestamp)
- sun_drying_interval_days: 30 (days, numeric, prevents mold)

- condition: "good" (enum: ["excellent", "good", "fair", "poor", "damaged"], physical state)
- wear_level: 15 (0-100 scale, how worn/degraded, increases with use)
- mold_risk: 0.02 (0-1 probability per day if not maintained)
- contamination_present: false (boolean, food safety flag)

- purchase_date: "2023-02-20" (date string)
- purchase_price_usd: 5.90 (USD, numeric, per basket)
- replacement_threshold_wear: 80 (0-100 scale, when to retire)

Rationale: Bannetons are mobile containers that move through workflow and hold individual loaves during critical proof phase. State tracking prevents double-assignment (can't load occupied basket). Flour_coating state affects loaf release quality - depleted coating causes loaves to stick. Cleaning cycle tracking ensures food safety. 200 baskets create a capacity constraint for overnight cold proof.
```

### TEMPLATE: 199 more baskets (IDs banneton_002 through banneton_200)
- 150 round baskets (for boules)
- 50 oval baskets (for batards)
- Each with individual tracking for state, location, cleanliness
- Creates realistic constraint: max 200 loaves can proof simultaneously

---

## 7. CUSTOM TYPE: FERMENTATION_CONTAINER

### OBJECT: fermentation_container_1
```
ID: equipment_fermentation_container_22qt_1
Type: fermentation_container
Name: Bulk Fermentation Tub #1 (22-quart Cambro)
Emoji: 🫙

Properties:
- container_id: "cambro_22qt_1" (string, unique identifier)
- capacity_liters: 22 (liters, numeric, total volume)
- capacity_kg_dough: 25 (kilograms, numeric, practical maximum dough weight)
- dimensions_inches: "12x18x12" (string, L x W x H)

- state: "clean" (enum: ["clean", "in_use", "dirty", "cleaning", "sanitizing"], operational status)
- contents_batch_id: null (string, references dough_batch when in use)
- contents_weight_kg: null (kilograms, numeric, current dough mass inside)

- material: "clear_polycarbonate" (string, allows visual monitoring)
- transparency: "clear" (enum: ["clear", "translucent", "opaque"], affects visual monitoring)
- graduated_markings: true (boolean, has volume indicators on side)
- marked_volume_ml: null (milliliters, numeric, marked with tape for "doubled" reference)

- fill_level_percent: 0 (percentage, 0-100, visual estimate of how full)
- initial_dough_level_ml: null (milliliters, numeric, starting volume reference)
- current_dough_level_ml: null (milliliters, numeric, current volume estimate)
- volume_increase_percent: 0 (percentage, calculated rise, key fermentation indicator)

- temperature_f: null (degrees F, numeric, dough temperature inside)
- location: null (string, references location_id, indicates ambient temp zone)

- lid_present: true (boolean, has matching lid)
- lid_state: "on" (enum: ["on", "off", "loose"], affects moisture retention)
- seal_quality: "good" (enum: ["good", "fair", "poor"], affects CO2 retention)

- last_used_timestamp: null (ISO timestamp)
- last_cleaned_timestamp: "2025-10-21T20:00:00Z" (ISO timestamp)
- uses_since_cleaning: 0 (integer, counter)
- cleaning_required_after_uses: 1 (integer, must clean after each use)

- contamination_risk: 0.01 (0-1 probability per day if not cleaned)
- food_safe: true (boolean, quality gate)
- bpa_free: true (boolean, material safety)

- condition: "excellent" (enum: ["excellent", "good", "fair", "cracked"], physical state)
- wear_level: 5 (0-100 scale, minimal wear, new)
- purchase_date: "2023-02-15" (date string)
- purchase_price_usd: 38.00 (USD, numeric)

Rationale: These containers are temporary dough housing during bulk fermentation. Clear material enables visual monitoring of volume increase (key fermentation indicator). The marked_volume_ml property creates a reference point for "doubled" assessment. State management prevents reuse without cleaning (food safety). 12 containers total allows some batch overlap but can become constrained on heavy production days.
```

### TEMPLATE: 11 more containers (IDs cambro_22qt_2 through cambro_22qt_12)
- Each independently tracked
- Can be in different states simultaneously
- Creates realistic constraint: limited clean containers forces cleaning cycles

---

## 8. CUSTOM TYPE: COOLING_RACK_POSITION

### OBJECT: cooling_rack_1
```
ID: equipment_cooling_rack_1
Type: cooling_rack
Name: Cooling Rack #1 (20-Tier Sheet Pan Rack)
Emoji: 🗄️

Properties:
- rack_id: "cooling_rack_1" (string, unique identifier)
- tier_count: 20 (integer, number of shelf positions)
- tier_spacing_inches: 3.5 (inches, numeric, vertical space between shelves)
- capacity_pans_total: 20 (integer, one full-size pan per tier)
- capacity_loaves_per_pan: 4 (integer, typical, varies by size)
- capacity_loaves_total: 80 (integer, theoretical maximum)

- current_load_pans: 0 (integer, how many pans currently on rack)
- current_load_loaves: 0 (integer, how many loaves currently cooling)
- tiers_occupied: [] (array of integers, which tier numbers have loaves: [1,2,3,5,7...])
- contents_by_tier: {} (object, maps tier number to array of loaf_ids: {1: [loaf_001, loaf_002], 2: [loaf_003]})

- state: "empty" (enum: ["empty", "partially_loaded", "full", "in_use"], operational status)
- location: "cooling_zone_boh" (string, references location_id)
- mobility: "mobile" (enum: ["mobile", "locked"], whether currently movable)
- casters_locked: false (boolean, whether wheels are locked)

- material: "welded_aluminum" (string, frame construction)
- weight_capacity_lbs: 480 (pounds, numeric, maximum safe load)
- current_weight_lbs: 0 (pounds, numeric, estimated based on loaf count)
- weight_per_loaf_avg_lbs: 2.2 (pounds, numeric, used for capacity calculation)

- air_circulation: "good" (enum: ["excellent", "good", "fair", "poor"], affects cooling rate)
- tier_cooling_rate_variance: {"top": 1.15, "middle": 1.0, "bottom": 0.85} (object, top tiers cool faster)

- last_cleaned_timestamp: "2025-10-20T15:00:00Z" (ISO timestamp)
- cleaning_interval_days: 7 (days, numeric, weekly wipe-down)
- condition: "good" (enum: ["excellent", "good", "fair", "damaged"])
- rust_present: false (boolean, maintenance flag)

- purchase_date: "2023-02-28" (date string)
- purchase_price_usd: 185.00 (USD, numeric)

Rationale: Cooling racks are spatial constraints that limit production flow. When all 4 racks are full (320 loaf capacity), production must pause until loaves cool and are packaged/moved. The tiers_occupied array allows granular tracking of which shelves have space. Tier_cooling_rate_variance models realistic physics (top shelves cool faster due to heat rising). This creates scheduling pressure on Saturday when production hits capacity.
```

### OBJECTS: cooling_rack_2, cooling_rack_3, cooling_rack_4
[Same structure as cooling_rack_1, with unique IDs]
- Total 4 racks = 80 positions = practical capacity for 320 loaves cooling simultaneously
- Saturday morning: all racks at capacity by 9 AM, blocks further baking

---

## 9. CUSTOM TYPE: STORAGE_LOCATION

### OBJECT: walk_in_cooler
```
ID: location_walk_in_cooler
Type: storage_location
Name: Walk-In Cooler
Emoji: ❄️

Properties:
- location_id: "walk_in_cooler" (string, unique identifier)
- location_type: "refrigerated" (enum: ["refrigerated", "climate_controlled", "ambient", "hot_zone"])
- subcategory: "cold_storage" (string, descriptor)

- model: "amerikooler_qs0608" (string, equipment model)
- interior_dimensions_ft: "6x8x7.5" (string, L x W x H)
- volume_cubic_feet: 360 (cubic feet, numeric, total capacity)

- temperature_current_f: 38 (degrees F, numeric, actual temp)
- temperature_setpoint_f: 38 (degrees F, numeric, target)
- temperature_range_min_f: 35 (degrees F, numeric, acceptable low)
- temperature_range_max_f: 42 (degrees F, numeric, acceptable high)
- temperature_alarm_threshold_f: 45 (degrees F, numeric, triggers alarm)

- humidity_current_percent: 80 (percentage, 0-100)
- humidity_target_percent: 80 (percentage, optimal for most items)

- state: "operational" (enum: ["operational", "cooling", "malfunction", "door_open", "alarm", "defrost_cycle"], current status)
- compressor_state: "running" (enum: ["off", "running", "cycling"], actual operation)
- duty_cycle_percent: 40 (percentage, 0-100, how often compressor runs)

- door_state: "closed" (enum: ["closed", "open"], affects temp)
- door_open_count_today: 0 (integer, how many times accessed)
- door_open_duration_total_minutes: 0 (minutes, numeric, cumulative open time today)
- last_door_open_timestamp: null (ISO timestamp)

- power_consumption_kw: 2.1 (kilowatts, numeric, when running)
- power_consumption_current_kw: 0.84 (kilowatts, numeric, at 40% duty cycle)
- monthly_energy_cost_usd: 65 (USD, numeric, historical average)

- contents: [] (array of object IDs stored inside, multi-type)
- contents_by_type: {"ingredients": [], "dough_batches": [], "levain": [], "dairy": [], "misc": []} (object, categorized)
- capacity_weight_lbs: 800 (pounds, numeric, maximum safe load for dry goods)
- capacity_perishables_lbs: 150 (pounds, numeric, practical limit for perishables)
- capacity_rolling_racks: 2 (integer, how many 20-pan racks fit)
- current_utilization_percent: 35 (percentage, 0-100, estimated fullness)

- malfunction_probability_per_day: 0.0005 (0-1 probability, ~0.05%)
- malfunction_type: null (enum: ["compressor", "thermostat", "door_seal", "defrost_system", null])
- time_to_critical_temp_hours: 8 (hours, numeric, if compressor fails, how long until spoilage threshold)

- alarm_system: true (boolean, has temp alarm)
- alarm_state: "normal" (enum: ["normal", "alarm_sounding", "alarm_acknowledged"])
- alarm_audible_in_production_area: true (boolean, can be heard)
- alarm_remote_notification: false (boolean, no SMS alerts currently - identified gap)

- last_maintenance_timestamp: "2025-09-10T10:00:00Z" (ISO timestamp)
- maintenance_interval_days: 90 (days, quarterly condenser cleaning)
- next_maintenance_due_timestamp: "2025-12-10T10:00:00Z" (ISO timestamp)

- purchase_date: "2023-02-01" (date string)
- purchase_price_usd: 8400 (USD, including installation)
- depreciation_years: 10 (years, numeric, for financial modeling)
- current_value_usd: 6972 (USD, numeric, straight-line depreciation)

Rationale: Walk-in cooler is critical infrastructure that stores flour (prevents spoilage), dairy (food safety), and cold-fermented doughs. Temperature excursion = food safety crisis (Scenario #2). The contents array tracks what's inside for spoilage simulation. Malfunction_probability creates realistic equipment failure risk. Door_open tracking models temperature fluctuation from frequent access.
```

### OBJECT: proofing_retarder
```
ID: location_proofing_retarder
Type: storage_location
Name: Proofing Retarder
Emoji: 🧊

Properties:
- location_id: "proofing_retarder" (string, unique identifier)
- location_type: "climate_controlled" (enum)
- subcategory: "proof_box" (string, dual-mode: proof or retard)

- model: "avantco_hpi1836" (string)
- capacity_pans: 36 (integer, full-size sheet pans)
- pan_spacing_inches: 3 (inches, numeric, between slides)
- practical_capacity_loaves: 190 (integer, in bannetons on pans, realistic max)

- mode: "retard" (enum: ["proof", "retard"], current operating mode)
- temperature_current_f: 40 (degrees F, numeric, in retard mode)
- temperature_setpoint_f: 40 (degrees F, numeric)
- temperature_range_proof_min_f: 85 (degrees F, numeric, when in proof mode)
- temperature_range_proof_max_f: 115 (degrees F, numeric)
- temperature_range_retard_min_f: 38 (degrees F, numeric, when in retard mode)
- temperature_range_retard_max_f: 50 (degrees F, numeric)

- humidity_current_percent: 85 (percentage, 0-100, high humidity prevents drying)
- humidity_range_min_percent: 30 (percentage)
- humidity_range_max_percent: 100 (percentage)
- humidity_setpoint_percent: 85 (percentage, optimal for cold proof)

- state: "operational" (enum: ["operational", "malfunction", "door_open"])
- door_state: "closed" (enum: ["closed", "open"])
- insulated: true (boolean, reduces energy use)
- energy_savings_vs_non_insulated_percent: 35 (percentage, manufacturer spec)

- power_consumption_kw: 1.575 (kilowatts, numeric)
- monthly_energy_cost_usd: 28 (USD, numeric)

- contents: [] (array of proofing_basket IDs currently inside)
- contents_by_product: {} (object, {country_sourdough: [basket_ids], whole_grain: [basket_ids]})
- capacity_utilized_percent: 0 (percentage, 0-100, how full)
- loaf_count_current: 0 (integer, total loaves inside)

- typical_load_time_start: "18:00" (24-hour time, evening shaping complete)
- typical_load_time_end: "21:00" (24-hour time, all loaves loaded)
- typical_unload_time_start: "05:00" (24-hour time, morning bake begins)
- typical_unload_time_end: "11:00" (24-hour time, all loaves baked)

- malfunction_probability_per_day: 0.0003 (0-1 probability)
- malfunction_type: null (enum: ["cooling_system", "humidity_control", "thermostat", null])

- purchase_date: "2023-02-22" (date string)
- purchase_price_usd: 1499 (USD, numeric)

Rationale: Retarder is the bottleneck for overnight cold proof capacity. 190 loaf max caps Saturday production (need 220+ loaves). Contents tracking enables over-capacity detection. Temperature excursion during overnight proof = over-proofed loaves (Scenario #2). The load/unload time windows create workflow timing constraints.
```

### OBJECT: dry_storage_room
```
ID: location_dry_storage
Type: storage_location
Name: Dry Storage Room
Emoji: 📦

Properties:
- location_id: "dry_storage" (string)
- location_type: "ambient" (enum)
- subcategory: "ingredients_packaging" (string)

- temperature_current_f: 68 (degrees F, numeric, room temp)
- temperature_range_acceptable_min_f: 60 (degrees F, cool but not cold)
- temperature_range_acceptable_max_f: 75 (degrees F, not too warm)
- humidity_current_percent: 45 (percentage, low humidity for dry goods)
- climate_control: false (boolean, no active HVAC)

- contents: [] (array of ingredient/resource IDs)
- contents_by_category: {"flour": [], "salt": [], "seeds": [], "oil": [], "packaging": []} (object)
- capacity_cubic_feet: 200 (cubic feet, numeric)
- current_utilization_percent: 55 (percentage)

- shelving_units: 8 (integer, number of metal shelving units)
- shelving_capacity_lbs_per_unit: 600 (pounds, numeric)

- pest_control_traps: 6 (integer, number of bait stations)
- last_pest_inspection: "2025-10-10" (date string)
- pest_activity_detected: false (boolean, health department concern)

- state: "normal" (enum: ["normal", "needs_organization", "pest_issue"])

Rationale: Dry storage is where flour (primary ingredient) lives. Capacity constraint affects ordering frequency. Pest_control tracking ties to health inspection scenarios. Temperature/humidity affect ingredient shelf life.
```

### OBJECT: fermentation_ambient_warm_zone
```
ID: location_fermentation_warm_zone
Type: storage_location
Name: Warm Fermentation Zone (Near Oven)
Emoji: 🌡️

Properties:
- location_id: "fermentation_ambient_warm_zone" (string)
- location_type: "hot_zone" (enum)
- subcategory: "dough_fermentation" (string)

- temperature_current_f: 78 (degrees F, numeric, ambient near oven exhaust)
- temperature_range_min_f: 76 (degrees F, good for fermentation)
- temperature_range_max_f: 82 (degrees F, upper acceptable limit)
- temperature_source: "oven_radiant_heat" (string, passive heating)
- climate_control: false (boolean, temperature is ambient, not controlled)

- ideal_for: ["levain_building", "bulk_fermentation", "final_proof_enriched_doughs"] (array of strings)
- capacity_containers: 8 (integer, how many fermentation tubs fit in this zone)
- current_occupancy: 0 (integer, how many tubs currently here)
- contents: [] (array of dough_batch IDs or levain_culture IDs)

- air_circulation: "moderate" (enum: ["poor", "moderate", "good"], affects evenness)
- draft_risk: "low" (enum: ["none", "low", "moderate", "high"], affects dough skin formation)

Rationale: This "location" is a designated warm zone that accelerates fermentation. Placing levain here reduces build time from 10 hours to 6-8 hours. Temperature variance creates timing uncertainty. Multiple doughs can ferment here simultaneously. Positioning near oven is strategic use of waste heat.
```

---

## 10. CUSTOM TYPE: INGREDIENT (BAKERY-SPECIFIC)

### OBJECT: bread_flour_organic
```
ID: ingredient_flour_bread_organic
Type: ingredient
Name: Organic Bread Flour
Emoji: 🌾

Properties:
- ingredient_id: "flour_bread_organic" (string, unique identifier)
- category: "flour" (string, high-level grouping)
- subcategory: "bread_flour" (string, specific type)
- organic: true (boolean, certification status)

- current_quantity_kg: 180 (kilograms, numeric, current inventory)
- unit: "kg" (string, measurement unit)
- reorder_point_kg: 200 (kilograms, numeric, trigger for new order)
- reorder_quantity_kg: 600 (kilograms, numeric, weekly order size)
- container_size_kg: 50 (kilograms, numeric, comes in 50kg bags)
- containers_current: 4 (integer, calculated: current_quantity / container_size, rounded up)

- unit_cost_usd_per_kg: 1.79 (USD/kg, numeric, wholesale price)
- total_value_usd: 322.20 (USD, numeric, current_quantity * unit_cost)

- supplier: "regional_flour_mill_coop" (string, vendor name)
- supplier_contact: "+1-555-0200" (string, phone)
- supplier_lead_time_days: 1 (days, numeric, order to delivery)
- delivery_day_of_week: "tuesday" (string, regular schedule)
- last_delivery_date: "2025-10-15" (date string)
- next_delivery_scheduled: "2025-10-22" (date string)

- storage_location_id: "location_walk_in_cooler" (string, where stored)
- storage_requirement: "cool_dry" (enum: ["cool_dry", "refrigerated", "frozen", "ambient"])
- optimal_storage_temp_f: 38 (degrees F, numeric, extends shelf life)
- storage_container_type: "sealed_50kg_bags_poly" (string)

- protein_percent: 12.5 (percentage, numeric, affects gluten development)
- ash_content_percent: 0.55 (percentage, numeric, mineral content)
- moisture_content_percent: 13.0 (percentage, numeric, affects hydration calculations)
- falling_number: 350 (seconds, numeric, enzyme activity measurement)

- shelf_life_days: 180 (days, numeric, from production date if stored properly)
- production_date: "2025-09-01" (date string, from manufacturer)
- expiration_date: "2026-03-01" (date string, calculated)
- days_until_expiration: 133 (days, numeric, dynamic calculation)
- spoiled: false (boolean, quality gate)
- rancid_risk_factor: 0.02 (0-1, organic flour has higher fat content, spoils faster)

- batch_lot_number: "ORG-BF-2025-SEP-B" (string, traceability for recalls)
- country_of_origin: "USA" (string)
- mill_location: "Washington State" (string)

- weekly_consumption_avg_kg: 520 (kilograms, numeric, rolling average)
- monthly_consumption_avg_kg: 2080 (kilograms, numeric)
- days_of_supply_remaining: 2.5 (days, numeric, current_quantity / daily_avg_consumption)

- used_in_products: ["country_sourdough", "whole_grain_sourdough", "seeded_multigrain", "olive_rosemary", "baguette", "ciabatta"] (array of product_ids)
- percent_of_total_flour_usage: 60 (percentage, majority of production uses this)

Rationale: Ingredients need bakery-specific properties beyond generic resources. Protein_percent affects dough performance. Storage_location links to cold storage which can malfunction. Shelf_life creates spoilage risk. Reorder_point/quantity create ordering workflow and shortage scenarios (Scenario #4). Organic designation affects cost and product labeling. Days_of_supply calculates emergency/shortage risk.
```

### OBJECT: bread_flour_conventional
```
ID: ingredient_flour_bread_conventional
Type: ingredient
Name: Conventional Bread Flour
Emoji: 🌾

Properties:
[Similar structure to organic, with these key differences:]
- ingredient_id: "flour_bread_conventional"
- organic: false
- current_quantity_kg: 220
- unit_cost_usd_per_kg: 1.19 (cheaper than organic)
- protein_percent: 12.5 (same as organic)
- shelf_life_days: 240 (longer than organic due to lower fat content)
- rancid_risk_factor: 0.01 (lower risk)
- weekly_consumption_avg_kg: 340 (less used than organic)
- percent_of_total_flour_usage: 40
- used_in_products: ["sandwich_loaf", "focaccia", "some_baguette_batches"]

Rationale: Having both organic and conventional flour models the 60/40 blend strategy. Different costs and shelf lives affect financial modeling and ordering decisions.
```

### OBJECT: whole_wheat_flour_organic
```
ID: ingredient_flour_whole_wheat_organic
Type: ingredient
Name: Organic Whole Wheat Flour
Emoji: 🌾

Properties:
- ingredient_id: "flour_whole_wheat_organic"
- category: "flour"
- subcategory: "whole_wheat"
- organic: true

- current_quantity_kg: 75
- reorder_point_kg: 50
- reorder_quantity_kg: 150
- unit_cost_usd_per_kg: 1.87 (premium over white flour)

- protein_percent: 13.5 (higher than white flour)
- fiber_content_percent: 12.0 (key whole grain property)
- bran_content: "100_percent" (includes bran, affects texture)
- shelf_life_days: 120 (shorter than white flour, oils in bran go rancid faster)
- rancid_risk_factor: 0.04 (highest risk of all flours)

- storage_location_id: "location_walk_in_cooler"
- storage_requirement: "refrigerated_preferred" (more critical than white flour)

- used_in_products: ["whole_grain_sourdough", "seeded_multigrain", "sandwich_loaf", "starter_feeding"]
- weekly_consumption_avg_kg: 85

Rationale: Whole wheat has distinct properties (higher protein, shorter shelf life) that affect recipes and storage. Rancid_risk is highest, creating spoilage potential. Used in starter feeding (small quantity daily).
```

```
### OBJECT: rye_flour
```
ID: ingredient_flour_rye
Type: ingredient
Name: Rye Flour
Emoji: 🌾

Properties:
- ingredient_id: "flour_rye"
- category: "flour"
- subcategory: "specialty_rye"
- organic: false (conventional, limited organic availability)

- current_quantity_kg: 28
- reorder_point_kg: 20
- reorder_quantity_kg: 100
- unit_cost_usd_per_kg: 2.21 (most expensive flour, specialty item)

- protein_percent: 8.5 (low gluten protein)
- pentosan_content_percent: 8.0 (high, creates gummy texture, unique to rye)
- amylase_activity: "high" (enum: ["low", "moderate", "high"], affects dough handling)
- shelf_life_days: 150
- rancid_risk_factor: 0.03

- storage_location_id: "location_walk_in_cooler"
- handling_notes: "Minimal mixing required, over-mixing activates enzymes excessively" (string)
- specialty: true (boolean, not stocked by all suppliers)

- supplier: "specialty_grain_distributor" (string, different from main flour supplier)
- supplier_lead_time_days: 3 (longer lead time, specialty item)
- delivery_frequency: "biweekly" (string, not weekly like other flours)
- last_delivery_date: "2025-10-08"
- next_delivery_scheduled: "2025-10-22"

- used_in_products: ["rye_sourdough_40_percent", "whole_grain_sourdough", "rye_levain"] (array)
- weekly_consumption_avg_kg: 18 (low volume, produced Thu/Sat only)
- percent_of_total_flour_usage: 3 (small portion)

- production_challenge: "high" (enum: ["low", "moderate", "high"], Marcus only)
- requires_specialized_technique: true (boolean, different handling than wheat)

Rationale: Rye flour is specialty ingredient with unique properties (pentosans, high enzyme activity) that require different techniques. Higher cost and specialty supplier create ordering constraints. Low volume means longer inventory hold periods. Used exclusively by Marcus due to complexity.
```

### OBJECT: water_filtered
```
ID: ingredient_water_filtered
Type: ingredient
Name: Filtered Municipal Water
Emoji: 💧

Properties:
- ingredient_id: "water_municipal_filtered"
- category: "water"
- subcategory: "potable"

- current_quantity_liters: 999999 (liters, numeric, effectively unlimited from tap)
- unit: "liters" (string)
- unit_cost_usd_per_liter: 0.003 (USD/liter, includes water and sewer)

- source: "municipal_water_supply" (string)
- treatment: "carbon_filtration" (string, removes chlorine)
- filter_location: "mixing_station" (string, inline filter)
- filter_last_changed: "2025-09-01" (date string)
- filter_change_interval_months: 6 (months, numeric)
- chlorine_removed: true (boolean, chlorine affects yeast/bacteria)

- temperature_available_range_f: "50-120" (string, from cold tap to heated)
- temperature_typical_cold_f: 55 (degrees F, numeric)
- temperature_typical_hot_f: 110 (degrees F, numeric)
- temperature_mixing_calculation_required: true (boolean, DDT formula uses water temp)

- ph: 7.2 (numeric, 0-14 scale, slightly alkaline)
- hardness_ppm: 85 (ppm, numeric, calcium/magnesium content)
- mineral_content: "moderate" (enum: ["soft", "moderate", "hard"], affects dough)

- weekly_consumption_avg_liters: 1850 (liters, numeric)
- monthly_cost_usd: 5.55 (USD, numeric, minimal expense)

- used_in: ["all_doughs", "levain_building", "equipment_cleaning", "hand_washing"] (array)

- utility_meter_id: "water_meter_commercial" (string, for billing tracking)
- meter_reading_last: 47238 (liters, numeric, cumulative)
- meter_reading_date: "2025-10-01" (date string)

Rationale: Water seems simple but has critical properties. Temperature must be calculated for DDT. Chlorine removal via filter is necessary (chlorine kills yeast/bacteria). Hardness affects gluten development. Filter maintenance creates a maintenance task. Effectively unlimited supply but cost tracked for financial modeling. Temperature control is key to dough temperature management.
```

### OBJECT: sea_salt_fine
```
ID: ingredient_salt_fine_sea
Type: ingredient
Name: Fine Sea Salt
Emoji: 🧂

Properties:
- ingredient_id: "salt_fine_sea"
- category: "salt"
- subcategory: "fine_grain"

- current_quantity_kg: 22
- unit: "kg"
- reorder_point_kg: 10
- reorder_quantity_kg: 50
- unit_cost_usd_per_kg: 0.85 (inexpensive ingredient)
- container_size_kg: 25 (comes in 25kg sacks)

- storage_location_id: "location_dry_storage"
- storage_requirement: "dry_room_temp" (enum, must stay dry)
- storage_container_type: "sealed_plastic_bucket" (string, prevents humidity absorption)
- moisture_sensitivity: "high" (enum: ["low", "moderate", "high"], salt clumps if wet)

- grain_size: "fine" (enum: ["fine", "medium", "coarse"], affects dissolving rate)
- dissolves_easily: true (boolean, fine grain dissolves quickly in dough)
- iodized: false (boolean, no iodine added, better for bread)
- anti_caking_agent: false (boolean, pure salt)

- sodium_content_percent: 99.5 (percentage, pure sodium chloride)
- mineral_content_percent: 0.5 (percentage, trace minerals from sea)

- shelf_life_days: 999999 (days, effectively infinite if kept dry)
- spoilage_risk: 0.0 (no spoilage, but can clump)
- clumping_risk_factor: 0.02 (0-1, if humidity > 60%)

- supplier: "restaurant_supply_distributor"
- delivery_frequency: "monthly" (string, bulk order)
- last_delivery_date: "2025-10-01"

- used_in_products: ["all_breads"] (array, universal ingredient)
- typical_usage_percent_of_flour: 2.0 (percentage, standard baker's ratio)
- weekly_consumption_avg_kg: 10
- monthly_consumption_avg_kg: 40

- role_in_dough: "gluten_strengthening_flavor_fermentation_control" (string, multi-purpose)

Rationale: Salt is critical for gluten structure, flavor, and fermentation control. Storage in dry conditions prevents clumping. Low cost but essential. Universal ingredient (used in every bread). Stable shelf life eliminates spoilage concerns. Fine grain size matters for mixing.
```

### OBJECT: instant_yeast
```
ID: ingredient_yeast_instant_saf
Type: ingredient
Name: Instant Dry Yeast (SAF)
Emoji: 🦠

Properties:
- ingredient_id: "yeast_instant_saf"
- category: "leavening"
- subcategory: "commercial_yeast"
- brand: "SAF-Instant" (string, professional baker's choice)

- current_quantity_kg: 1.8
- unit: "kg"
- reorder_point_kg: 0.5
- reorder_quantity_kg: 3
- unit_cost_usd_per_kg: 37.40 (expensive per kg, but used in small quantities)
- container_size_kg: 0.5 (comes in 500g vacuum packs)

- storage_location_id: "equipment_reach_in_fridge_1"
- storage_requirement: "refrigerated_after_opening" (enum, critical for viability)
- optimal_storage_temp_f: 36 (degrees F, numeric)
- storage_container_type: "vacuum_sealed_foil_pack" (string, before opening)
- storage_after_opening: "airtight_container_refrigerated" (string)

- viability: 95 (0-100 scale, percentage of live yeast cells)
- activity_level: "high" (enum: ["low", "moderate", "high"], fermentation power)
- type: "instant" (enum: ["active_dry", "instant", "fresh"], no proofing needed)

- shelf_life_unopened_days: 730 (days, 2 years sealed)
- shelf_life_opened_days: 180 (days, 6 months in fridge)
- production_date: "2024-08-15" (date string)
- opened_date: "2025-09-22" (date string, when current pack opened)
- expiration_date: "2026-08-15" (date string, unopened)
- days_until_expiration: 300 (days, numeric)

- temperature_sensitivity: "extreme" (enum: ["low", "moderate", "high", "extreme"])
- viability_loss_rate_per_day: 0.001 (0-1, at proper refrigeration)
- viability_loss_rate_room_temp_per_day: 0.02 (0-1, rapid degradation if not refrigerated)
- killed_above_temp_f: 120 (degrees F, important for water temperature in mixing)

- used_in_products: ["baguette", "ciabatta", "sandwich_loaf", "focaccia"] (array, enriched/fast breads)
- not_used_in: ["sourdough_products"] (array, sourdough uses levain)
- weekly_consumption_avg_kg: 0.15 (kilograms, small quantities)

- dosage_typical_percent_of_flour: 1.0 (percentage, 1% of flour weight)

- supplier: "baking_specialty_distributor"
- delivery_frequency: "quarterly" (string, bulk order lasts long time)

Rationale: Yeast is living organism with strict storage requirements. Temperature excursion kills yeast, rendering it useless (creates production failure). Viability degrades over time even when stored properly. Used only in non-sourdough products. Small usage amounts but high per-kg cost. Refrigeration requirement links to reach-in fridge (equipment dependency).
```

### OBJECT: whole_milk
```
ID: ingredient_milk_whole_commercial
Type: ingredient
Name: Whole Milk (Commercial Dairy)
Emoji: 🥛

Properties:
- ingredient_id: "milk_whole_commercial"
- category: "dairy"
- subcategory: "fluid_milk"

- current_quantity_liters: 8
- unit: "liters"
- reorder_point_liters: 5
- reorder_quantity_liters: 40 (10 x 1-gallon jugs per weekly delivery)
- unit_cost_usd_per_liter: 2.55

- storage_location_id: "equipment_reach_in_fridge_1"
- storage_requirement: "refrigerated_mandatory" (enum, food safety critical)
- optimal_storage_temp_f: 36 (degrees F, numeric)
- max_safe_temp_f: 40 (degrees F, FDA requirement)
- time_above_40f_minutes: 0 (minutes, numeric, cumulative exposure tracker)
- spoilage_threshold_minutes_above_40f: 120 (minutes, FDA 2-hour rule)

- fat_content_percent: 3.25 (percentage, whole milk standard)
- protein_content_percent: 3.2 (percentage)
- lactose_content_percent: 4.8 (percentage)
- pasteurized: true (boolean, heat-treated for safety)
- homogenized: true (boolean, fat evenly distributed)

- perishable: true (boolean, critical flag)
- shelf_life_days: 7 (days, from delivery)
- delivery_date: "2025-10-15" (date string)
- expiration_date: "2025-10-22" (date string)
- days_until_expiration: 3 (days, numeric, urgent use)
- spoiled: false (boolean, becomes true if expired or temp-abused)

- temperature_abuse_event: false (boolean, flag if left at room temp >2 hours)
- aroma: "fresh" (enum: ["fresh", "sour", "spoiled"], quality indicator)

- used_in_products: ["sandwich_loaf"] (array, only enriched bread uses milk)
- weekly_consumption_avg_liters: 10
- used_on_days: ["tuesday", "wednesday", "thursday", "friday", "saturday"] (array, when sandwich loaves made)

- supplier: "regional_dairy_distributor"
- delivery_day_of_week: "tuesday" (string, weekly delivery)
- delivery_frequency: "weekly"

- fda_regulated: true (boolean, strict food safety rules)
- allergen: true (boolean, milk is top 8 allergen, requires labeling)

Rationale: Milk is highly perishable with strict temperature requirements. Temperature_abuse tracking models Scenario #2 (refrigeration failure = must discard). Shelf_life is short (7 days), creating ordering and waste risks. Used only in sandwich loaves. Allergen flag important for labeling. Time_above_40f tracker enforces FDA 2-hour rule for safety.
```

### OBJECT: butter_unsalted
```
ID: ingredient_butter_unsalted_84percent
Type: ingredient
Name: Unsalted Butter (84% Butterfat)
Emoji: 🧈

Properties:
- ingredient_id: "butter_unsalted_84percent"
- category: "dairy"
- subcategory: "solid_fat"

- current_quantity_kg: 12
- unit: "kg"
- reorder_point_kg: 5
- reorder_quantity_kg: 35
- unit_cost_usd_per_kg: 12.75 (expensive ingredient)
- container_size_kg: 0.454 (1 pound blocks)

- storage_location_id: "equipment_reach_in_fridge_1"
- storage_requirement: "refrigerated_mandatory"
- optimal_storage_temp_f: 36
- can_be_frozen: true (boolean, extends shelf life)
- frozen_shelf_life_months: 12 (months, if frozen)

- fat_content_percent: 84 (percentage, premium European-style)
- water_content_percent: 16 (percentage, remainder)
- salted: false (boolean, unsalted for baking control)
- cultured: false (boolean, sweet cream butter)

- perishable: true (boolean)
- shelf_life_days: 30 (days, refrigerated)
- delivery_date: "2025-10-15"
- expiration_date: "2025-11-14"
- days_until_expiration: 26 (days)

- rancidity_risk_factor: 0.015 (0-1, fats go rancid if temperature-abused)
- oxidation_sensitive: true (boolean, should minimize air exposure)
- aroma: "fresh_creamy" (enum: ["fresh_creamy", "slightly_off", "rancid"])

- melting_point_f: 90 (degrees F, important for dough incorporation)
- softened_ideal_temp_f: 65 (degrees F, for mixing into dough)

- used_in_products: ["sandwich_loaf"] (array, enriched bread only)
- weekly_consumption_avg_kg: 8
- monthly_consumption_avg_kg: 33

- supplier: "regional_dairy_distributor"
- delivery_day_of_week: "tuesday"

- allergen: true (boolean, milk allergen)
- cost_per_sandwich_loaf: 1.62 (USD, single highest ingredient cost in that product)

Rationale: Butter is expensive (\$12.75/kg) and perishable. Temperature sensitivity creates quality risk. High cost makes it significant in sandwich loaf COGS (which has lowest margin). Melting_point and softened_temp matter for mixing technique. Refrigeration failure affects this too.
```

### OBJECT: olive_oil_evoo
```
ID: ingredient_olive_oil_bulk_evoo
Type: ingredient
Name: Extra Virgin Olive Oil (Bulk)
Emoji: 🫒

Properties:
- ingredient_id: "olive_oil_bulk_evoo"
- category: "oil"
- subcategory: "olive_oil"
- grade: "extra_virgin" (string, highest quality)

- current_quantity_liters: 18
- unit: "liters"
- reorder_point_liters: 10
- reorder_quantity_liters: 35
- unit_cost_usd_per_liter: 13.60 (expensive, but bulk rate)
- container_size_liters: 5 (comes in 5-liter tins)

- storage_location_id: "location_dry_storage"
- storage_requirement: "cool_dark_place" (enum, light and heat degrade quality)
- optimal_storage_temp_f: 65 (degrees F, room temp acceptable but cool better)
- light_sensitive: true (boolean, UV degrades quality)
- container_type: "opaque_metal_tin" (string, protects from light)

- shelf_life_days: 540 (days, 18 months in unopened tin)
- shelf_life_opened_days: 180 (days, 6 months after opening)
- production_date: "2024-11-01" (date string)
- opened_date: "2025-09-01" (date string)
- expiration_date: "2026-05-01"
- days_until_expiration: 194 (days)

- rancidity_risk_factor: 0.008 (0-1, olive oil is relatively stable)
- oxidation_rate_increase_if_exposed_to_air: 3.0 (multiplier, oxidizes when exposed)
- aroma: "fruity_peppery" (enum: ["fruity_peppery", "flat", "rancid"])

- free_fatty_acid_percent: 0.5 (percentage, quality metric, <0.8% for EVOO)
- polyphenol_content: "high" (enum: ["low", "moderate", "high"], antioxidants)

- used_in_products: ["ciabatta", "focaccia_all_varieties", "olive_rosemary"] (array)
- weekly_consumption_avg_liters: 8
- monthly_consumption_avg_liters: 35

- supplier: "restaurant_supply_bulk_foods"
- delivery_frequency: "monthly"

- cost_impact: "high" (enum, expensive ingredient that affects COGS significantly)
- usage_generous_in_focaccia: true (boolean, focaccia uses lots of oil for texture)

Rationale: Olive oil is expensive (\$13.60/L) and quality-sensitive. Light/heat exposure degrades it. Used heavily in focaccia (highest-margin product). Rancidity affects flavor. Storage in dark, cool place important. Bulk purchasing in 5L tins is cost optimization.
```

### OBJECT: kalamata_olives
```
ID: ingredient_olives_kalamata_bulk
Type: ingredient
Name: Kalamata Olives (Bulk, Pitted)
Emoji: 🫒

Properties:
- ingredient_id: "olives_kalamata_bulk"
- category: "produce"
- subcategory: "prepared_vegetables"

- current_quantity_kg: 9
- unit: "kg"
- reorder_point_kg: 5
- reorder_quantity_kg: 20
- unit_cost_usd_per_kg: 11.05 (expensive specialty ingredient)
- container_size_kg: 2.5 (bulk tubs)

- storage_location_id: "equipment_reach_in_fridge_2"
- storage_requirement: "refrigerated_mandatory"
- optimal_storage_temp_f: 36
- storage_container: "brine" (string, packed in salty liquid)

- preparation_required: "drain_pat_dry_chop" (string, prep before adding to dough)
- preparation_time_per_kg: 15 (minutes, labor to prep)
- excess_moisture_issue: true (boolean, wet olives affect dough hydration)

- pitted: true (boolean, no pits, critical for food safety)
- cured: true (boolean, preserved olives)
- brine_concentration_percent: 8 (percentage, salt brine)

- perishable: true (boolean)
- shelf_life_days: 90 (days, in brine, refrigerated)
- opened_date: "2025-09-20"
- expiration_date: "2025-12-19"
- days_until_expiration: 61 (days)

- aroma: "briny_rich" (enum: ["briny_rich", "fermented", "spoiled"])
- texture: "firm" (enum: ["firm", "mushy"], quality indicator)

- used_in_products: ["olive_rosemary_sourdough"] (array, specialty product)
- usage_percent_of_dough: 12 (percentage, significant amount)
- weekly_consumption_avg_kg: 4
- produced_on_days: ["wednesday", "friday", "saturday"] (array, limited production)

- supplier: "specialty_foods_distributor"
- delivery_frequency: "biweekly"

- allergen: false (boolean, olives not top allergen)
- cost_per_loaf_olive_rosemary: 1.62 (USD, expensive add-in)

Rationale: Olives are expensive specialty ingredient used only in Olive & Rosemary Sourdough. Preparation labor (draining, drying, chopping) adds time. Excess moisture affects dough (must be patted dry). Storage in reach-in fridge #2 (equipment dependency). Limited production days (Wed/Fri/Sat only) means weekly consumption is low but significant when used.
```

### TEMPLATE FOR REMAINING INGREDIENTS:
Similar detailed specifications for:
- fresh_rosemary (perishable, expensive \$34/kg, local farm, 7-day shelf life)
- seeds_mixed (sunflower/flax/sesame, toasting required, \$13.60/kg)
- brown_sugar (\$3.74/kg, dry storage, infinite shelf life)
- honey (local, \$20.40/kg, sandwich loaf sweetener)
- malt_powder (diastatic, \$13.60/kg, enzyme activity for baguettes)
- caraway_seeds (optional for rye, \$20.40/kg)

---

## 11. EQUIPMENT (STANDARD TYPE)

### OBJECT: main_oven
```
ID: equipment_main_oven_lbc_se932
Type: equipment
Name: Main 3-Deck Electric Oven (LBC SE-932)
Emoji: 🔥

Properties:
- equipment_id: "lbc_se932_3deck" (string)
- category: "oven" (string)
- subcategory: "deck_oven_electric" (string)
- make_model: "LBC_Bakery_Equipment_SE-932" (string)

- decks: ["equipment_oven_deck_1", "equipment_oven_deck_2", "equipment_oven_deck_3"] (array, references to deck objects)
- deck_count: 3 (integer)
- configuration: "stacked_modular" (string)

- power_rating_kw: 33 (kilowatts, total connected load)
- voltage: 208 (volts)
- phase: 3 (integer, 3-phase commercial power)
- amperage: 72 (amps)
- electrical_requirements: "208V_3phase_72amp_dedicated_circuit" (string)

- operating_power_consumption_kw: 25 (kilowatts, typical when all decks at temp)
- operating_power_range_kw: "22-28" (string, varies by number of decks in use)
- standby_power_consumption_kw: 0.5 (kilowatts, controls and display only)

- state: "off" (enum: ["off", "preheating", "ready", "in_use", "cooling", "malfunction"])
- all_decks_ready: false (boolean, true when all decks at target temp)

- preheat_time_to_500f_minutes: 70 (minutes, cold start to full temp)
- energy_cost_per_preheat_usd: 1.40 (USD, 33kW * 1.17 hours * \$0.12/kWh)
- monthly_energy_cost_usd: 180 (USD, historical average)

- dimensions_inches: "72Wx42Dx78H" (string, footprint)
- weight_lbs: 1850 (pounds, massive thermal mass)
- requires_hood_ventilation: true (boolean, code requirement)
- hood_system_id: "ventilation_hood_6x4ft" (string, references exhaust hood)

- purchase_date: "2023-03-01" (date string)
- purchase_price_usd: 17738 (USD)
- installation_cost_usd: 4200 (USD, electrical upgrade + hood integration)
- total_investment_usd: 21938 (USD)
- depreciation_period_years: 7 (years, for financial modeling)
- current_book_value_usd: 18220 (USD, straight-line depreciation)

- warranty_years: 2 (years)
- warranty_expiration_date: "2025-03-01" (date string, expired)
- post_warranty: true (boolean, repairs now at owner's cost)

- maintenance_schedule: "quarterly" (string, professional service)
- last_maintenance_date: "2025-09-15" (date string)
- next_maintenance_due_date: "2025-12-15" (date string)
- maintenance_cost_per_visit_usd: 180 (USD, service call + labor)
- maintenance_tasks: ["deck_cleaning", "door_gasket_inspection", "thermostat_calibration", "steam_system_check"] (array)

- cycles_completed_lifetime: 2537 (integer, total bakes across all decks)
- operating_hours_lifetime: 4891 (hours, cumulative)
- expected_lifespan_hours: 35000 (hours, manufacturer spec)
- remaining_lifespan_percent: 86 (percentage, still relatively new)

- failure_probability_per_day: 0.0002 (0-1, ~0.02% daily risk, 2% annually)
- failure_modes: ["heating_element_burnout", "thermostat_failure", "steam_system_leak", "door_hinge_failure"] (array, possible issues)
- critical_equipment: true (boolean, production stops without this)

- backup_equipment_available: false (boolean, no second oven)
- downtime_impact_high: true (boolean, Saturday failure = \$2,200 loss)

Rationale: Main oven is the bottleneck for production capacity. Its three deck objects operate independently. Total power draw (33kW) is significant cost. Preheat time (70 min) creates scheduling constraint (must start by 4 AM for 5:15 AM first bake). Failure_probability models Scenario #1. No backup creates single point of failure. Maintenance tracking ensures realistic service intervals.
```

### OBJECT: spiral_mixer
```
ID: equipment_spiral_mixer_ae4030
Type: equipment
Name: Spiral Mixer (American Eagle AE-4030)
Emoji: 🌀

Properties:
- equipment_id: "american_eagle_ae4030" (string)
- category: "mixer" (string)
- subcategory: "spiral_dough_mixer" (string)
- make_model: "American_Eagle_AE-4030" (string)

- capacity_flour_kg: 11.8 (kilograms, maximum flour per batch)
- capacity_dough_kg: 20 (kilograms, maximum total dough)
- practical_batch_size_kg: 17 (kilograms, recommended max for best results, 85% of capacity)
- bowl_size_quarts: 40 (quarts)

- motor_hp_agitator: 1.5 (horsepower, spiral hook motor)
- motor_hp_bowl: 0.5 (horsepower, bowl rotation motor)
- power_consumption_kw: 2.8 (kilowatts, when both motors running)

- speed_settings: 2 (integer, low and high)
- low_speed_rpm: 120 (RPM, for incorporation and autolyse)
- high_speed_rpm: 240 (RPM, for gluten development)

- state: "idle" (enum: ["idle", "loading", "mixing_low", "mixing_high", "resting", "unloading", "cleaning", "malfunction"])
- bowl_state: "clean" (enum: ["clean", "dirty", "in_use"], cleanliness tracking)
- bowl_attached: true (boolean, safety interlock)
- bowl_guard_closed: true (boolean, safety interlock, won't run if open)

- current_batch_id: null (string, references dough_batch being mixed)
- mix_start_timestamp: null (ISO timestamp)
- mix_duration_current_seconds: 0 (seconds, running timer)

- cycle_time_minutes: 13 (minutes, average complete mix cycle: load + mix + unload)
- load_unload_time_minutes: 4 (minutes, manual labor time)
- max_throughput_batches_per_hour: 4 (integer, theoretical if run continuously)
- practical_throughput_batches_per_hour: 3 (integer, realistic with cleaning)

- vibration_level: "normal" (enum: ["normal", "elevated", "excessive"], wear indicator)
- noise_level_db: 75 (decibels, loud but acceptable)

- maintenance_daily: ["cleaning_bowl_and_spiral", "visual_inspection"] (array)
- maintenance_weekly: ["belt_tension_check"] (array)
- maintenance_monthly: ["gear_lubrication"] (array)
- last_maintenance_date: "2025-10-01"
- next_lubrication_due: "2025-11-01"

- condition: "used_good" (enum: ["new", "used_good", "used_fair", "worn"])
- purchase_date: "2023-02-01" (date string)
- purchase_price_usd: 7200 (USD, used equipment)
- purchase_condition: "used" (string, bought secondhand)
- expected_remaining_life_years: 12 (years, well-maintained used mixers last long)

- failure_probability_per_month: 0.01 (0-1, ~1% monthly risk)
- failure_modes: ["belt_breakage", "motor_burnout", "gearbox_failure", "bowl_lift_mechanism"] (array)
- typical_repair_cost_usd: 450 (USD, average repair)
- downtime_per_failure_hours: 6 (hours, same-day repair if parts available)

- backup_mixing_method: "hand_mixing" (string, possible but impractical for volume)
- critical_equipment: true (boolean, production severely limited without it)

Rationale: Mixer is second-most critical equipment. Capacity (17kg practical) means large batches must be split into 2-3 sequential mixes. Cycle_time creates scheduling - can't rush mixing. Bowl_state tracking enforces cleaning between batches (food safety). Power consumption significant when running. Maintenance tasks are regular (weekly belt, monthly lubrication). Used equipment means higher failure risk than new. No backup mixer means failure severely impacts production (Scenario #3 variant).
```

### OBJECT: reach_in_fridge_1
```
ID: equipment_reach_in_fridge_true_t49_1
Type: equipment
Name: Reach-In Refrigerator #1 (True T-49-HC)
Emoji: 🧊

Properties:
- equipment_id: "true_t49hc_unit1" (string)
- category: "refrigeration" (string)
- subcategory: "reach_in_commercial" (string)
- make_model: "True_T-49-HC" (string)
- capacity_cubic_feet: 49 (cubic feet)
- sections: 2 (integer, two-door unit)
- shelves_total: 6 (integer, 3 per section)
- shelves_adjustable: true (boolean)

- temperature_current_f: 36 (degrees F, numeric)
- temperature_setpoint_f: 36 (degrees F)
- temperature_range_acceptable_min_f: 33 (degrees F)
- temperature_range_acceptable_max_f: 38 (degrees F)
- temperature_alarm_threshold_f: 40 (degrees F)

- state: "operational" (enum: ["operational", "cooling_cycle", "defrost_cycle", "malfunction", "door_open"])
- compressor_state: "running" (enum: ["off", "running", "cycling"])
- defrost_cycle_frequency_hours: 8 (hours, automatic defrost)
- last_defrost_timestamp: "2025-10-22T02:00:00Z" (ISO timestamp)

- power_consumption_kw: 1.2 (kilowatts, when compressor running)
- energy_star_certified: true (boolean, efficient model)
- daily_kwh: 1.02 (kWh/day, manufacturer spec)
- monthly_energy_cost_usd: 9 (USD, efficient unit)
- duty_cycle_percent: 35 (percentage, compressor runs 35% of time)

- door_left_state: "closed" (enum: ["closed", "open"])
- door_right_state: "closed" (enum: ["closed", "open"])
- door_gasket_condition: "good" (enum: ["excellent", "good", "fair", "worn"])
- door_self_closing: true (boolean, spring-loaded hinges)

- contents: [] (array of ingredient IDs stored)
- contents_typical: ["ingredient_milk_whole_commercial", "ingredient_butter_unsalted_84percent", "eggs_large_dozen", "ingredient_yeast_instant_saf", "honey_local"] (array, what's normally stored here)
- organization: "top_shelf_dairy_middle_eggs_bottom_yeast" (string, layout description)

- location: "near_mixing_station" (string, placement in bakery)
- purpose: "high_use_perishables" (string, frequently accessed ingredients)

- last_cleaned_date: "2025-10-20" (date string)
- cleaning_interval_days: 7 (days, weekly interior wipe-down)
- next_cleaning_due: "2025-10-27" (date string)

- purchase_date: "2023-02-15" (date string)
- purchase_price_usd: 1900 (USD, half of \$3,800 for both units, used)
- purchase_condition: "used" (string)
- warranty_status: "none" (string, used equipment, no warranty)

- maintenance_interval_months: 6 (months, condenser coil cleaning)
- last_maintenance_date: "2025-08-15"
- next_maintenance_due: "2026-02-15"
- maintenance_task: "condenser_coil_cleaning_thermostat_calibration" (string)

- expected_lifespan_years: 15 (years, commercial refrigerators long-lasting)
- age_years: 6 (years, moderate age)
- remaining_lifespan_years: 9 (years)

- failure_probability_per_month: 0.008 (0-1, ~0.8% monthly)
- failure_modes: ["compressor_failure", "thermostat_malfunction", "door_seal_failure", "refrigerant_leak"] (array)
- typical_repair_cost_usd: 400 (USD, average repair)
- critical_equipment: true (boolean, milk/butter spoil without refrigeration)

- contents_value_if_spoiled_usd: 150 (USD, estimated loss if unit fails)

Rationale: Reach-in refrigerator is critical for perishables (milk, butter, yeast). Temperature excursion spoils contents (Scenario #2 variant). Contents tracking enables spoilage calculation. Door_state affects temperature (frequent opening in production environment). Energy-star efficient but still significant ongoing cost. Used equipment means moderate failure risk. Two units provide some redundancy but unit 1 holds most critical items.
```

### OBJECT: reach_in_fridge_2
```
ID: equipment_reach_in_fridge_true_t49_2
Type: equipment
Name: Reach-In Refrigerator #2 (True T-49-HC)
Emoji: 🧊

Properties:
[Same structure as fridge_1, with these differences:]
- equipment_id: "true_t49hc_unit2"
- contents_typical: ["ingredient_olives_kalamata_bulk", "ingredient_rosemary_fresh_local", "specialty_ingredients_misc", "backup_perishables"]
- location: "near_shaping_bench"
- purpose: "specialty_ingredients_backup_storage"
- critical_equipment: false (boolean, less critical than unit 1)
- contents_value_if_spoiled_usd: 85 (USD, lower value items)

Rationale: Second refrigerator provides redundancy and specialty storage. Less critical than unit 1 (doesn't hold daily-use dairy). Placement near shaping bench for convenient olive/herb access. Lower financial impact if fails.
```

### OBJECT: primary_shaping_bench
```
ID: equipment_shaping_table_96x30
Type: equipment
Name: Primary Shaping Bench (96"x30" Stainless Steel)
Emoji: 🔪

Properties:
- equipment_id: "shaping_table_96x30" (string)
- category: "work_surface" (string)
- subcategory: "stainless_steel_table" (string)

- dimensions_inches: "96Lx30Wx34H" (string, length x width x height)
- surface_area_sq_ft: 20 (square feet, working surface)
- material: "16_gauge_stainless_steel" (string, heavy-duty)
- finish: "brushed_4" (string, #4 brushed stainless)

- weight_capacity_lbs: 600 (pounds, evenly distributed)
- current_load_lbs: 0 (pounds, estimated based on items on surface)

- state: "clean" (enum: ["clean", "in_use", "dirty", "sanitizing"])
- current_occupant_actor_id: null (string, who is using it, null if available)
- contents: [] (array of loaf_ids or equipment_ids currently on surface)

- surface_temperature_f: 70 (degrees F, follows ambient room temp)
- surface_temperature_type: "ambient_passive" (string, no heating/cooling)
- ideal_shaping_surface_temp_f: 68 (degrees F, slightly cool surface preferred)

- backsplash: true (boolean, 1.5" rear splash guard)
- undershelf: true (boolean, storage shelf below surface)
- undershelf_capacity_lbs: 400 (pounds)
- undershelf_contents: ["bench_scrapers", "flour_container", "scale"] (array, tools stored below)

- adjustable_feet: true (boolean, can level on uneven floor)
- mobility: false (boolean, fixed position, heavy table)

- location: "production_zone_center" (string, central work area)
- adjacent_to: ["spiral_mixer", "fermentation_holding_area"] (array, nearby equipment)

- cleaning_frequency: "after_each_use" (string, must sanitize between batches)
- cleaning_method: "scrape_sanitizer_wipe_dry" (string, procedure)
- sanitizer_type: "quaternary_ammonium" (string, food-safe sanitizer)
- last_sanitized_timestamp: "2025-10-22T02:30:00Z" (ISO timestamp)

- food_contact_surface: true (boolean, must maintain sanitation)
- nsfansi_certified: true (boolean, commercial food equipment standard)

- condition: "excellent" (enum: ["excellent", "good", "fair", "worn", "damaged"])
- wear_level: 8 (0-100 scale, light wear, relatively new)
- scratches: "minor" (enum: ["none", "minor", "moderate", "severe"])
- rust_present: false (boolean, stainless resists rust)

- purchase_date: "2023-02-20" (date string)
- purchase_price_usd: 502 (USD)
- expected_lifespan_years: 20 (years, commercial stainless tables very durable)

Rationale: Primary work surface for all shaping operations. Surface_area (20 sq ft) limits how many loaves can be shaped simultaneously. State management prevents cross-contamination (must be clean before use). Current_occupant tracks which actor is using it (only 1-2 people can work on it at once). Surface_temperature is ambient (slightly cool is ideal for shaping). Cleaning after each use is food safety requirement. Very durable equipment with long lifespan.
```

### OBJECT: mixing_prep_table
```
ID: equipment_prep_table_60x24
Type: equipment
Name: Mixing Prep Table (60"x24" Mobile)
Emoji: 🔪

Properties:
[Similar structure to shaping bench, with these differences:]
- equipment_id: "prep_table_60x24"
- dimensions_inches: "60Lx24Wx34H"
- surface_area_sq_ft: 10 (square feet, half the size of shaping bench)
- material: "18_gauge_stainless_steel" (thinner gauge, lighter duty)
- weight_capacity_lbs: 500 (pounds)
- backsplash: false (no backsplash, allows flexible positioning)
- mobility: true (boolean, has locking casters)
- casters: 4 (integer, heavy-duty swivel casters)
- casters_locked: false (boolean, current state)
- location: "mixing_zone_flexible" (string, can be repositioned as needed)
- purpose: "ingredient_staging_autolyse_setup" (string)
- purchase_price_usd: 224 (USD, less expensive than fixed table)

Rationale: Mobile prep table provides flexible workspace. Can be moved to create different work zones. Used for ingredient staging before mixing. Lighter duty than shaping bench. Mobility is advantage for space management in small bakery.
```

### OBJECT: display_case
```
ID: equipment_display_case_co57d
Type: equipment
Name: Bakery Display Case (Structural Concepts CO57D)
Emoji: 🏪

Properties:
- equipment_id: "structural_concepts_co57d" (string)
- category: "display" (string)
- subcategory: "dry_bakery_case" (string)
- make_model: "Structural_Concepts_CO57D" (string)

- configuration: "countertop_three_tier" (string)
- tiers: 3 (integer, shelf levels)
- dimensions_inches: "77Lx35Dx27H" (string)
- capacity_cubic_feet: 21 (cubic feet, display volume)
- capacity_loaves: 38 (integer, realistic maximum display)

- glass_type: "tempered" (string, safety glass)
- glass_panels: "front_and_sides" (string, visibility)
- access: "sliding_rear_doors" (string, staff loading from back)

- lighting: "LED_interior" (string, illuminates products)
- power_consumption_watts: 20 (watts, LED only, no refrigeration)
- monthly_energy_cost_usd: 0.15 (USD, negligible)

- state: "open" (enum: ["open", "closed"], operational status)
- door_position: "unlocked" (enum: ["unlocked", "locked"], after hours security)

- current_contents: [] (array of loaf_ids currently displayed)
- contents_by_tier: {"1": [], "2": [], "3": []} (object, top/middle/bottom organization)
- tier_1_typical: ["specialty_breads", "seasonal_items", "highest_priced"] (array, merchandising strategy)
- tier_2_typical: ["core_sourdough_varieties"] (array)
- tier_3_typical: ["baguettes", "sandwich_loaves", "focaccia"] (array)

- current_display_count: 0 (integer, total loaves in case)
- restocking_frequency: "continuous" (string, replenished as sold)
- restock_threshold: 5 (integer, trigger restocking when count drops below this)

- location: "front_counter_centerpiece" (string, main customer interface)
- visibility_from_entrance: "high" (enum: ["low", "moderate", "high"], first thing customers see)

- cleanliness_state: "clean" (enum: ["clean", "needs_cleaning", "dirty"])
- last_cleaned_timestamp: "2025-10-22T06:00:00Z" (ISO timestamp)
- cleaning_frequency: "daily_morning" (string, before opening)
- cleaning_task: "glass_wipe_crumb_removal_shelf_wipe" (string)

- condition: "excellent" (enum, still new)
- wear_level: 5 (0-100, minimal wear)

- purchase_date: "2023-02-25" (date string)
- purchase_price_usd: 2850 (USD, significant investment)
- expected_lifespan_years: 15 (years)

Rationale: Display case is revenue-enabling equipment. Capacity (38 loaves) creates staging constraint - must continuously restock from cooling area as items sell. Contents_by_tier allows merchandising strategy modeling. No refrigeration means only day-old bread stays fresh (natural sales pressure). Visual centerpiece of FOH, affects customer experience. Cleanliness impacts health inspection and customer perception.
```

### OBJECT: pos_system
```
ID: equipment_pos_square_terminal
Type: equipment
Name: Point-of-Sale System (Square Terminal)
Emoji: 💳

Properties:
- equipment_id: "square_pos_terminal" (string)
- category: "point_of_sale" (string)
- subcategory: "integrated_payment_system" (string)

- hardware_components: ["ipad_10.2_inch", "cash_drawer_star_micronics", "receipt_printer_thermal_bluetooth", "card_reader_square_terminal", "ups_battery_backup"] (array)
- hardware_total_cost_usd: 1092 (USD)

- software_platform: "square_for_retail" (string)
- software_subscription_monthly_usd: 60 (USD/month)
- transaction_fee_percent: 2.6 (percentage, card transactions)
- transaction_fee_fixed_usd: 0.10 (USD, per card transaction)

- features: ["inventory_tracking_realtime", "customer_data_collection", "sales_reporting_daily_weekly_monthly", "employee_clock_in_function", "online_order_integration", "email_receipt_option"] (array)

- state: "operational" (enum: ["operational", "in_transaction", "offline", "malfunction"])
- current_transaction_id: null (string, if mid-transaction)

- cash_drawer_state: "closed" (enum: ["closed", "open"])
- cash_drawer_float_usd: 150 (USD, starting cash for change-making)
- current_cash_usd: 150 (USD, current cash in drawer)
- cash_over_short_usd: 0 (USD, discrepancy at day's end, should be 0)

- card_reader_state: "ready" (enum: ["ready", "processing", "error"])
- card_reader_connection: "bluetooth" (string, wireless to iPad)
- card_types_accepted: ["visa", "mastercard", "amex", "discover", "apple_pay", "google_pay"] (array)

- receipt_printer_state: "ready" (enum: ["ready", "printing", "paper_low", "paper_out", "error"])
- receipt_paper_rolls_remaining: 3 (integer, backup rolls)

- internet_connection_required: true (boolean, cloud-based POS)
- internet_connection_state: "online" (enum: ["online", "offline"])
- offline_mode_available: true (boolean, can process some transactions offline)
- offline_transaction_limit: 10 (integer, max transactions before must sync)

- inventory_sync_frequency: "realtime" (string, updates immediately on sale)
- sales_data_export: true (boolean, can export for accounting)

- employee_users: ["actor_sarah_thompson", "actor_marcus_chen", "actor_david_kim"] (array, who can use POS)
- employee_permissions: {"sarah": "full", "marcus": "full", "david": "limited"} (object, access control)

- daily_sales_today_usd: 0 (USD, running total, resets at close)
- daily_transaction_count_today: 0 (integer, resets at close)
- daily_card_transactions_today: 0 (integer)
- daily_cash_transactions_today: 0 (integer)

- average_transaction_value_usd: 18.50 (USD, historical average)
- typical_transaction_duration_seconds: 90 (seconds, avg checkout time)

- location: "front_counter_checkout_position" (string)

- last_software_update: "2025-10-01" (date string)
- software_version: "5.42.1" (string)

- backup_battery_charge_percent: 100 (percentage, UPS battery level)
- backup_battery_runtime_hours: 2 (hours, how long can run on battery)

- critical_equipment: true (boolean, can't process sales without it)
- failure_probability_per_day: 0.001 (0-1, low risk, but critical impact)
- failure_modes: ["internet_outage", "ipad_failure", "card_reader_malfunction", "printer_jam"] (array)
- workaround_if_failure: "manual_cash_only_backup_receipts" (string)

Rationale: POS is critical for revenue realization. Internet_connection required for card processing (most transactions). Offline_mode provides limited backup. Transaction_fees are significant ongoing cost (\$3,600/year). Inventory_tracking integrates with production (sales decrement displayed inventory). Cash_drawer tracking enables end-of-day reconciliation. Multiple failure modes (internet, hardware) can disrupt sales. Backup battery provides 2-hour cushion for power outages.
```

### OBJECTS: Cooling racks, packaging scales, slicing machine, etc.
[Additional equipment with similar detailed specifications]

---

## 12. PRODUCTS (FINISHED GOODS)

### OBJECT: country_sourdough_900g
```
ID: product_country_sourdough_900g
Type: product
Name: Classic Country Sourdough (900g)
Emoji: 🍞

Properties:
- product_id: "country_sourdough_900g" (string)
- product_name: "Classic Country Sourdough" (string, display name)
- product_category: "sourdough_bread" (string)
- signature_product: true (boolean, flagship item)

- shape: "batard" (enum: ["batard", "boule", "baguette", "pan_loaf", "sheet", "slipper"], final form)
- target_weight_baked_g: 900 (grams, post-bake target)
- target_weight_pre_bake_g: 1000 (grams, dough weight before oven)
- weight_loss_percent_baking: 10 (percentage, moisture loss during bake)

- recipe_id: "recipe_country_sourdough" (string, references detailed recipe)
- hydration_percent: 77.4 (percentage, true hydration including levain)
- levain_percent: 20 (percentage, of total flour)

- ingredient_cost_usd: 2.72 (USD, COGS per loaf)
- labor_cost_allocated_usd: 3.15 (USD, estimated labor per loaf, calculated)
- packaging_cost_usd: 0.19 (USD, bag + label)
- total_cost_usd: 6.06 (USD, full cost per loaf)

- retail_price_usd: 9.00 (USD, shelf price)
- wholesale_price_usd: 5.75 (USD, to wholesale partners)
- gross_margin_retail_usd: 2.94 (USD, retail_price - total_cost)
- gross_margin_retail_percent: 32.7 (percentage)
- gross_margin_wholesale_usd: -0.31 (USD, wholesale_price - total_cost, NEGATIVE)
- gross_margin_wholesale_percent: -5.4 (percentage, LOSS LEADER for wholesale)

- production_days: ["tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"] (array, daily production)
- tuesday_friday_quantity: 50 (integer, loaves per day)
- saturday_quantity: 75 (integer, peak day)
- sunday_quantity: 60 (integer)
- weekly_quantity_total: 310 (integer, sum across week)

- production_time_hours: 16 (hours, from mix to ready for sale, includes overnight proof)
- bake_temperature_f: 500 (degrees F, initial oven temp)
- bake_temperature_mid_f: 480 (degrees F, reduced after steam phase)
- bake_time_minutes: 38 (minutes, in oven)
- steam_required: true (boolean, heavy steam injection)
- steam_phase_duration_minutes: 15 (minutes, vents closed)

- cooling_time_hours: 3 (hours, minimum before packaging)
- shelf_life_days: 3 (days, optimal quality window)
- shelf_life_extended_days: 5 (days, still edible but staling)

- scoring_pattern: "deep_cross" (string, signature cuts)
- scoring_depth_inches: 0.5 (inches, blade depth)
- oven_spring_expected: "high" (enum: ["low", "moderate", "high"], rise in oven)

- crumb_structure_target: "open_irregular" (string, interior texture goal)
- crust_color_target: "deep_golden_to_mahogany" (string)
- crust_texture: "crispy_blistered" (string)

- customer_appeal: "very_high" (enum: ["low", "moderate", "high", "very_high"])
- customer_loyalty_driver: true (boolean, signature item that brings repeat customers)
- wholesale_demand: "high" (enum: ["low", "moderate", "high"])

- allergens: ["wheat_gluten"] (array, required labeling)
- organic_ingredients_percent: 60 (percentage, blend)
- vegan: true (boolean, no animal products)
- dietary_notes: "naturally_leavened_no_added_yeast" (string)

- slicing_requested_frequency_percent: 15 (percentage, how often customers ask for slicing)
- slicing_adds_labor_minutes: 2 (minutes, additional time if sliced)

- day_old_discount_percent: 30 (percentage, markdown for yesterday's loaves)
- donation_eligible: true (boolean, can donate unsold to food bank)

Rationale: Product objects define specifications, costs, pricing, and demand patterns. Gross_margin_wholesale is negative (loss leader) - this is realistic for volume wholesale. Production_days and quantities drive daily workflow scheduling. Bake parameters link to oven requirements. Shelf_life creates time pressure for sales. Customer_appeal and loyalty_driver affect demand modeling.
```

### TEMPLATE FOR OTHER PRODUCTS:
Similar detailed specifications for:
- whole_grain_sourdough_900g (higher ingredient cost \$3.21, \$9.50 retail)
- seeded_multigrain_850g (highest ingredient cost \$3.76, \$10.00 retail)
- baguette_300g (lowest cost \$0.73, \$4.00 retail, high volume)
- ciabatta_600g (\$1.89 cost, \$7.50 retail)
- sandwich_loaf_850g (highest total cost \$5.29, lowest margin 3.8%)
- olive_rosemary_900g (premium \$10.50, specialty item)
- rye_sourdough_40pct_900g (complex, Marcus only, \$9.75)
- rosemary_focaccia_portion (highest margin 94.2%, \$4.50 retail)
- seasonal_focaccia_portion (variable toppings, \$5.00-5.50)

---

## 13. RESOURCES (GENERIC CONSUMABLES)

### OBJECT: packaging_bread_bags
```
ID: resource_bags_kraft_6x3x12
Type: resource
Name: Kraft Bread Bags (6"x3"x12")
Emoji: 📦

Properties:
- resource_id: "bags_kraft_6x3x12" (string)
- category: "packaging" (string)
- subcategory: "bread_bags" (string)

- current_quantity: 4200 (integer, count)
- unit: "count" (string, individual bags)
- reorder_point: 2000 (integer, trigger new order)
- reorder_quantity: 10000 (integer, bulk order size)
- unit_cost_usd: 0.14 (USD, per bag, bulk rate)

- dimensions: "6x3x12_inches" (string, width x gusset x height)
- material: "kraft_paper" (string, brown paper)
- window: false (boolean, no clear window)
- food_safe: true (boolean, FDA approved for food contact)

- storage_location_id: "location_packaging_area" (string)
- storage_requirement: "dry_room_temp" (enum)
- storage_container: "original_carton_boxes" (string)

- supplier: "packaging_supply_company" (string)
- supplier_lead_time_days: 5 (days, order to delivery)
- delivery_frequency: "as_needed" (string, not regular schedule)
- minimum_order_quantity: 5000 (integer, supplier minimum)

- last_order_date: "2025-09-20" (date string)
- last_delivery_date: "2025-09-25" (date string)
- next_order_planned: null (date string, when quantity hits reorder_point)

- daily_consumption_avg: 170 (integer, bags used per day average)
- weekly_consumption_avg: 1020 (integer)
- days_of_supply_remaining: 24.7 (days, current_quantity / daily_avg)

- used_for_products: ["country_sourdough", "whole_grain_sourdough", "seeded_multigrain", "olive_rosemary", "rye_sourdough", "sandwich_loaf"] (array, standard loaves)
- percentage_of_daily_production: 85 (percentage, most loaves use this bag)

- biodegradable: true (boolean, environmentally friendly)
- recyclable: true (boolean)

- shelf_life_days: 999999 (days, stable packaging material)

Rationale: Packaging is consumable resource with high daily usage (170 bags/day). Running out blocks sales (can't package loaves). Reorder_point triggers ordering workflow. Days_of_supply tracks depletion risk. Daily_consumption drives usage rate in simulation. Used_for_products links to production volume.
```

### OBJECT: packaging_baguette_bags
```
ID: resource_bags_baguette_long
Type: resource
Name: Baguette Bags (Long, Narrow)
Emoji: 📦

Properties:
[Similar structure to bread bags, with these differences:]
- resource_id: "bags_baguette_long"
- current_quantity: 1350
- reorder_point: 1000
- reorder_quantity: 3000
- unit_cost_usd: 0.12 (USD, slightly cheaper, simpler bag)
- dimensions: "24x4_inches" (string, long and narrow)
- daily_consumption_avg: 40 (integer, baguettes per day)
- used_for_products: ["baguette_300g"] (array, baguettes only)

Rationale: Separate bag type for baguettes due to unique shape. Lower daily consumption than standard bags. Different reorder parameters.
```

### OBJECT: packaging_labels
```
ID: resource_stickers_branded_round
Type: resource
Name: Branded Logo Stickers (Round)
Emoji: 🏷️

Properties:
- resource_id: "stickers_branded_round" (string)
- category: "packaging" (string)
- subcategory: "labels_stickers" (string)

- current_quantity: 7200 (integer)
- unit: "count"
- reorder_point: 5000
- reorder_quantity: 15000
- unit_cost_usd: 0.05 (USD, per sticker)

- diameter_inches: 2.5 (inches, round sticker)
- design: "parkside_bakery_logo_brown_kraft" (string, branding)
- adhesive_type: "permanent" (string, sticks well to paper bags)

- storage_location_id: "location_packaging_area"
- storage_requirement: "dry_room_temp"

- supplier: "local_print_shop" (string)
- supplier_lead_time_days: 7 (days, custom printing)
- custom_design: true (boolean, bakery logo)

- daily_consumption_avg: 210 (integer, one per item sold)
- used_for: "all_products" (string, universal application)

Rationale: Labels are universal consumable for all packaged products. Running out means unbranded packaging (unprofessional). Higher daily usage than bags (some customers buy multiple items). Custom design means longer lead time for reordering.
```

### OBJECT: electricity
```
ID: resource_utility_electricity
Type: resource
Name: Electricity (Grid Power)
Emoji: ⚡

Properties:
- resource_id: "utility_electricity" (string)
- category: "utility" (string)
- subcategory: "energy" (string)

- current_quantity: 999999 (kWh, effectively unlimited from grid)
- unit: "kwh" (string, kilowatt-hours)
- unit_cost_usd: 0.12 (USD/kWh, commercial rate)

- supplier: "municipal_electric_utility" (string)
- account_number: "COM-847-PARK-001" (string)
- service_level: "commercial_208V_3phase" (string)
- service_capacity_kw: 200 (kilowatts, panel capacity)

- current_draw_kw: 0 (kilowatts, real-time consumption)
- peak_demand_today_kw: 0 (kilowatts, highest draw so far today)
- monthly_average_consumption_kwh: 4333 (kWh, historical average)
- monthly_average_cost_usd: 520 (USD)

- daily_consumption_tuesday_saturday_kwh: 180 (kWh, production days)
- daily_consumption_sunday_kwh: 120 (kWh, shorter hours)
- daily_consumption_monday_kwh: 15 (kWh, closed, minimal)

- major_consumers: ["equipment_main_oven_lbc_se932", "location_walk_in_cooler", "equipment_spiral_mixer_ae4030", "location_proofing_retarder", "equipment_reach_in_fridge_true_t49_1", "equipment_reach_in_fridge_true_t49_2", "lighting_led_all", "hvac_system"] (array, equipment that draws power)

- billing_cycle_start_date: 1 (integer, day of month)
- last_billing_date: "2025-10-01" (date string)
- last_bill_amount_usd: 498 (USD)
- next_billing_date: "2025-11-01" (date string)

- meter_reading_current_kwh: 142378 (kWh, cumulative lifetime)
- meter_reading_last_bill_kwh: 138228 (kWh)
- consumption_since_last_bill_kwh: 4150 (kWh)

- power_outage_risk_factor: 0.001 (0-1, ~0.1% daily, rare but possible)
- backup_power_available: false (boolean, no generator)
- ups_battery_backup_limited: true (boolean, only POS system has battery)

Rationale: Electricity is consumable utility tracked for cost modeling. Current_draw aggregates all active equipment power consumption. Major_consumers array links to equipment power properties. Monthly_average enables financial projections. Billing_cycle tracking for accounting. Power_outage_risk creates potential disruption scenario (would stop production mid-day).
```

### OBJECT: natural_gas
```
ID: resource_utility_natural_gas
Type: resource
Name: Natural Gas (Heating/Hot Water)
Emoji: 🔥

Properties:
- resource_id: "utility_natural_gas" (string)
- category: "utility" (string)
- subcategory: "fuel" (string)

- current_quantity: 999999 (therms, effectively unlimited from pipeline)
- unit: "therms" (string, 100,000 BTU)
- unit_cost_usd: 1.20 (USD/therm, estimated commercial rate)

- supplier: "municipal_gas_company" (string)
- account_number: "GAS-847-PARK-001" (string)
- service_type: "commercial_heating" (string)

- current_consumption_rate_therms_per_hour: 0 (therms/hour, real-time)
- monthly_average_consumption_therms: 150 (therms, historical average)
- monthly_average_cost_usd: 180 (USD)

- seasonal_variation: true (boolean, higher in winter)
- winter_monthly_avg_therms: 234 (therms, Dec-Feb, heating demand)
- summer_monthly_avg_therms: 79 (therms, Jun-Aug, minimal use)
- fall_spring_monthly_avg_therms: 150 (therms, moderate)

- used_for: ["space_heating_hvac", "hot_water_heater_demand", "backup_oven_pilot_if_applicable"] (array)
- primary_use: "space_heating" (string, largest consumer)

- water_heater_consumption_therms_per_day: 4 (therms, hot water for cleaning/mixing)
- hvac_heating_consumption_varies_by_weather: true (boolean)

- billing_cycle_start_date: 1 (integer, day of month)
- last_billing_date: "2025-10-01" (date string)
- last_bill_amount_usd: 156 (USD, fall moderate usage)
- next_billing_date: "2025-11-01" (date string)

- meter_reading_current_therms: 8473 (therms, cumulative lifetime)
- meter_reading_last_bill_therms: 8343 (therms)
- consumption_since_last_bill_therms: 130 (therms)

- gas_leak_risk_factor: 0.0001 (0-1, very low but catastrophic if occurs)
- safety_shutoff_valve: true (boolean, automatic shutoff if leak detected)

Rationale: Natural gas tracked for heating and hot water costs. Seasonal_variation affects monthly expenses (higher in winter). Lower cost than electricity per BTU. Less critical than electricity (oven is electric) but required for comfort and hot water. Gas_leak_risk is safety concern (would require evacuation, health inspection failure).
```

### OBJECT: water_utility
```
ID: resource_utility_water_sewer
Type: resource
Name: Water & Sewer (Municipal)
Emoji: 💧

Properties:
- resource_id: "utility_water_sewer" (string)
- category: "utility" (string)
- subcategory: "water" (string)

- current_quantity: 999999 (gallons, effectively unlimited from municipal supply)
- unit: "gallons" (string)
- unit_cost_water_usd_per_1000_gallons: 11.24 (USD/1000 gallons, water supply rate)
- unit_cost_sewer_usd_per_1000_gallons: 14.89 (USD/1000 gallons, sewer treatment rate)
- unit_cost_combined_usd_per_1000_gallons: 26.13 (USD, total water + sewer)

- supplier_water: "municipal_water_department" (string)
- supplier_sewer: "municipal_sewer_district" (string)
- account_number: "WAT-847-PARK-001" (string)

- current_flow_rate_gpm: 0 (gallons per minute, real-time)
- monthly_average_consumption_gallons: 3256 (gallons, historical average)
- monthly_average_cost_usd: 85 (USD, combined water + sewer)

- daily_average_consumption_gallons: 108 (gallons, on production days)
- sunday_consumption_gallons: 75 (gallons, shorter hours)
- monday_consumption_gallons: 20 (gallons, closed, minimal cleaning)

- used_for: ["dough_production_ingredient", "equipment_cleaning", "hand_washing", "restroom", "floor_mopping"] (array)
- production_use_percent: 60 (percentage, majority is ingredient water)
- cleaning_use_percent: 30 (percentage)
- restroom_use_percent: 10 (percentage, customer + staff)

- water_quality: "potable_municipal" (string)
- filtration: "carbon_filter_at_mixing_station" (string, chlorine removal)
- filter_maintenance_required: true (boolean)

- billing_cycle_start_date: 15 (integer, day of month)
- last_billing_date: "2025-10-15" (date string)
- last_bill_amount_usd: 83 (USD)
- next_billing_date: "2025-11-15" (date string)

- meter_reading_current_gallons: 78943 (gallons, cumulative lifetime)
- meter_reading_last_bill_gallons: 75691 (gallons)
- consumption_since_last_bill_gallons: 3252 (gallons)

- water_outage_risk_factor: 0.0005 (0-1, rare, ~0.05% daily)
- backup_water_storage: false (boolean, no water storage tank)
- impact_if_outage: "production_halt_cleaning_impossible" (string, critical)

Rationale: Water is ingredient and utility. Production_use tracks water going into dough (large quantity, \$0.003/liter from ingredient spec aligns with utility rate). Cleaning_use significant (3-compartment sink, floor mopping, hand washing). Sewer charge is often higher than water supply charge (realistic). Water_outage would halt production (need water for dough).
```

### OBJECT: cleaning_supplies_sanitizer
```
ID: resource_sanitizer_quaternary_ammonium
Type: resource
Name: Sanitizer (Quaternary Ammonium)
Emoji: 🧼

Properties:
- resource_id: "sanitizer_quaternary_ammonium" (string)
- category: "cleaning_supplies" (string)
- subcategory: "food_safe_sanitizer" (string)

- current_quantity_liters: 3.5 (liters, concentrate)
- unit: "liters" (string, concentrate form)
- reorder_point_liters: 2 (liters)
- reorder_quantity_liters: 10 (liters, bulk container)
- unit_cost_usd_per_liter: 18.50 (USD, food-safe sanitizer is expensive)

- dilution_ratio: "1:200" (string, 1 part concentrate to 200 parts water)
- diluted_solution_per_liter_concentrate: 200 (liters, how much working solution 1L makes)
- current_quantity_working_solution_equivalent_liters: 700 (liters, if all concentrate diluted)

- storage_location_id: "location_sanitation_supply_closet" (string)
- storage_requirement: "cool_dry_locked" (enum, chemical storage safety)
- storage_container: "5_liter_jug_original" (string)

- active_ingredient: "quaternary_ammonium_compound" (string, quat sanitizer)
- food_contact_safe: true (boolean, FDA approved for food surfaces)
- rinse_required: false (boolean, no-rinse formula)
- contact_time_seconds: 60 (seconds, surface must stay wet for 1 minute)

- effective_against: ["bacteria", "viruses", "fungi"] (array, broad spectrum)
- epa_registered: true (boolean, regulatory compliance)
- nsfansi_certified: true (boolean, food service approved)

- usage_per_day_liters_concentrate: 0.05 (liters, 50mL concentrate per day)
- daily_sanitizing_cycles: 10 (integer, times per day surfaces sanitized)
- days_of_supply_remaining: 70 (days, current_quantity / daily_usage)

- used_for: ["work_surfaces", "equipment", "floors", "tools", "containers", "hands_optional"] (array)
- critical_for: "health_code_compliance" (string, required by health department)

- safety_data_sheet_available: true (boolean, MSDS on file)
- ppe_required: "gloves_recommended" (string, personal protective equipment)

- supplier: "restaurant_supply_janitorial" (string)
- delivery_frequency: "quarterly" (string, bulk order lasts long time)
- last_delivery_date: "2025-08-15" (date string)

- shelf_life_unopened_months: 24 (months)
- shelf_life_opened_months: 12 (months)
- opened_date: "2025-09-01" (date string)
- expiration_date: "2026-09-01" (date string)

Rationale: Sanitizer is critical consumable for food safety and health code compliance. Used multiple times daily on all food-contact surfaces. Dilution_ratio means concentrate lasts long time. Cost per liter is high but usage per day is low. Running out would violate health codes (scenario #5). Storage in locked area is safety requirement (chemical hazard). EPA/NSF certification required for commercial food service.
```

### TEMPLATE FOR ADDITIONAL RESOURCES:
Similar specifications for:
- trash_bags_commercial (heavy-duty, 3x/week pickup)
- compost_bags_biodegradable (organic waste program)
- paper_towels_commercial (high-volume dispensers)
- hand_soap_antibacterial (handwashing stations)
- floor_cleaner_degreaser (daily mopping)
- gloves_nitrile_disposable (food handling)
- hairnets_disposable (all production staff)
- aprons_disposable (optional, heavy tasks)

---

## 14. LOCATIONS (SPATIAL ZONES)

### OBJECT: production_zone_mixing
```
ID: location_production_zone_mixing
Type: location
Name: Mixing & Prep Zone
Emoji: 🏭

Properties:
- location_id: "production_zone_mixing" (string)
- location_type: "production_workspace" (string)
- area_sq_ft: 120 (square feet, 12' x 10')

- temperature_current_f: 70 (degrees F, ambient)
- temperature_range_f: "68-72" (string, comfortable working temp)
- temperature_control: "hvac_general" (string, building HVAC)

- humidity_current_percent: 50 (percentage)
- humidity_control: false (boolean, no active control)

- ventilation: "moderate" (enum: ["poor", "moderate", "good", "excellent"])
- air_changes_per_hour: 8 (integer, HVAC circulation rate)

- flooring: "epoxy_coated_concrete" (string, non-slip, easy to clean)
- flooring_condition: "good" (enum: ["excellent", "good", "fair", "poor", "damaged"])
- slip_resistant: true (boolean, safety feature)

- lighting: "LED_overhead_5000_lumens" (string, bright task lighting)
- lighting_level_lux: 500 (lux, good visibility for precision work)

- equipment_present: ["equipment_spiral_mixer_ae4030", "equipment_prep_table_60x24", "digital_scales_large", "ingredient_staging_shelves"] (array)
- workstations: 2 (integer, how many people can work simultaneously)

- contents_current: [] (array of actor_ids and object_ids currently in this zone)
- occupancy_current: 0 (integer, how many actors in zone)
- occupancy_max: 3 (integer, comfortable maximum)

- adjacent_to: ["location_production_zone_shaping", "location_dry_storage", "equipment_reach_in_fridge_true_t49_1"] (array, nearby zones)
- access_from: ["main_production_floor"] (array, entry points)

- cleaning_frequency: "after_each_shift" (string)
- last_cleaned_timestamp: "2025-10-21T14:30:00Z" (ISO timestamp)
- cleanliness_state: "clean" (enum: ["clean", "in_use", "dirty", "sanitizing"])

- noise_level_db: 75 (decibels, mixer is loud when running)
- noise_source: "spiral_mixer_operation" (string)

- safety_hazards: ["electrical_equipment", "rotating_machinery", "floor_trip_hazard_if_wet"] (array)
- safety_equipment: ["first_aid_kit", "fire_extinguisher", "emergency_eyewash"] (array)

- utility_access: ["water_tap_hot_cold", "floor_drain", "208V_outlets_4", "overhead_electrical_for_mixer"] (array)

Rationale: Spatial zones organize workflow and create movement patterns for actors. Equipment_present defines what tasks can be performed here. Occupancy_max limits how many actors can work simultaneously (spatial constraint). Temperature and lighting affect working conditions. Adjacent_to enables pathfinding and movement time estimates. Cleanliness_state ties to health inspections. Noise_level affects worker fatigue. Safety_hazards create injury risk scenarios.
```

### OBJECT: production_zone_shaping
```
ID: location_production_zone_shaping
Type: location
Name: Shaping & Bench Work Zone
Emoji: 🏭

Properties:
- location_id: "production_zone_shaping" (string)
- location_type: "production_workspace" (string)
- area_sq_ft: 180 (square feet, 18' x 10')

- temperature_current_f: 70 (degrees F)
- temperature_optimal_for_shaping_f: 68 (degrees F, slightly cool preferred)

- equipment_present: ["equipment_shaping_table_96x30", "proofing_basket_storage_rack", "digital_scale_portioning", "bench_scrapers", "lames_scoring_tools"] (array)
- workstations: 3 (integer, can have 2-3 shapers working simultaneously)

- bench_space_occupied_sq_ft: 0 (square feet, how much of 20 sq ft bench is in use)
- bench_space_available_sq_ft: 20 (square feet, total usable surface)

- contents_current: [] (array, actors and items currently here)
- occupancy_current: 0 (integer)
- occupancy_max: 3 (integer, comfortable max, gets crowded beyond this)

- adjacent_to: ["location_production_zone_mixing", "location_fermentation_ambient_warm_zone", "equipment_proofing_retarder", "equipment_reach_in_fridge_true_t49_2"] (array)

- flour_dust_level: "low" (enum: ["none", "low", "moderate", "high"], air quality)
- flour_dust_cleanup_required: true (boolean, daily cleanup needed)

- cleaning_frequency: "multiple_times_per_day" (string, after each shaping session)
- sanitizing_required_between_batches: true (boolean, food safety)

- lighting_level_lux: 600 (lux, very bright for precision shaping)

- noise_level_db: 55 (decibels, quieter than mixing zone)

- primary_actors: ["actor_rachel_martinez", "actor_marcus_chen"] (array, who primarily works here)
- primary_activities: ["preshaping", "bench_rest", "final_shaping", "basket_loading"] (array)

Rationale: Shaping zone is where most hands-on production happens. Bench_space_occupied tracks spatial constraint (20 sq ft total, can only shape so many loaves at once). Occupancy_max models realistic crowding. Primary_actors indicates who has priority/expertise in this zone. Flour_dust_level affects cleanliness and air quality. Multiple cleanings per day required due to high food contact activity.
```

### OBJECT: oven_area
```
ID: location_oven_area
Type: location
Name: Oven & Hot Zone
Emoji: 🔥

Properties:
- location_id: "oven_area" (string)
- location_type: "production_hot_zone" (string)
- area_sq_ft: 160 (square feet, 16' x 10')

- temperature_current_f: 85 (degrees F, much warmer than ambient due to oven radiant heat)
- temperature_range_f: "80-95" (string, varies with oven usage)
- heat_source: "equipment_main_oven_lbc_se932_radiant" (string)

- temperature_gradient: true (boolean, temperature varies by distance from oven)
- temperature_at_oven_front_f: 95 (degrees F)
- temperature_at_zone_edge_f: 78 (degrees F)

- equipment_present: ["equipment_main_oven_lbc_se932", "oven_peels_3", "cooling_racks_staging_2", "timer_system", "infrared_thermometer"] (array)

- ventilation: "excellent" (enum, hood system extracts heat and steam)
- ventilation_hood_id: "ventilation_hood_6x4ft_1200cfm" (string)
- hood_active: true (boolean, runs when oven is on)

- contents_current: [] (array, actors and items)
- occupancy_current: 0 (integer)
- occupancy_max: 2 (integer, tight space near oven)

- adjacent_to: ["location_cooling_zone", "location_production_zone_shaping", "location_fermentation_ambient_warm_zone"] (array)

- safety_hazards: ["extreme_heat_burn_risk", "steam_burn_risk", "heavy_door_pinch_risk", "radiant_heat"] (array)
- safety_equipment: ["oven_mitts_heat_resistant", "long_handle_peels", "fire_extinguisher_class_k"] (array)
- required_ppe: "oven_mitts_mandatory_when_loading_unloading" (string)

- floor_anti_fatigue_mat: true (boolean, reduces standing fatigue)
- flooring_slip_resistant_extra: true (boolean, critical near steam)

- primary_actors: ["actor_marcus_chen", "actor_david_kim"] (array, oven specialists)
- primary_activities: ["oven_loading", "oven_monitoring", "oven_unloading", "scoring_loaves_immediately_before_load"] (array)

- noise_level_db: 70 (decibels, oven fans, steam injection)
- steam_presence: true (boolean, bursts of steam during loading)

- lighting_level_lux: 400 (lux, adequate but dimmer than shaping area)

- cleaning_frequency: "daily_after_baking_complete" (string)
- cleaning_challenges: "flour_on_floor_steam_residue_oven_door_glass" (string)

Rationale: Oven area is hot zone with safety hazards. Temperature_current affects actor fatigue and fermentation of nearby items. Occupancy_max is low (tight space). Safety_hazards create injury risk scenarios. Ventilation_hood is critical (building code requirement). Primary_actors limits who can work here effectively (requires training). Temperature_gradient means items placed near oven proof/ferment faster (strategic use of waste heat).
```

### OBJECT: cooling_zone
```
ID: location_cooling_zone
Type: location
Name: Cooling & Staging Area
Emoji: 🌬️

Properties:
- location_id: "cooling_zone_boh" (string)
- location_type: "production_cooling" (string)
- area_sq_ft: 100 (square feet, 10' x 10')

- temperature_current_f: 72 (degrees F, slightly warmer than ambient from nearby oven)
- temperature_range_f: "70-75" (string)

- air_circulation: "good" (enum, important for cooling efficiency)
- ceiling_fan_present: true (boolean, aids air movement)
- draft_prevention: true (boolean, no direct drafts on hot bread, causes cracking)

- equipment_present: ["equipment_cooling_rack_1", "equipment_cooling_rack_2", "equipment_cooling_rack_3", "equipment_cooling_rack_4"] (array)
- cooling_capacity_loaves: 320 (integer, max across all 4 racks)
- current_cooling_load_loaves: 0 (integer)
- capacity_utilized_percent: 0 (percentage)

- contents_current: [] (array, loaf_ids on racks)
- occupancy_current_actors: 0 (integer)

- adjacent_to: ["location_oven_area", "location_packaging_area", "location_foh_transition"] (array)

- primary_activities: ["cooling_hot_bread", "quality_inspection", "rack_rotation"] (array)

- aroma_level: "very_high" (enum: ["none", "low", "moderate", "high", "very_high"], fresh baked bread smell)
- aroma_notes: "yeasty_toasted_wheat_caramel" (string, sensory descriptor)

- noise_level_db: 50 (decibels, quiet, bread cooling is silent)

- cleaning_frequency: "daily_crumb_sweep" (string)
- crumb_accumulation: "moderate" (enum: ["none", "low", "moderate", "high"], from handling hot bread)

- space_constraint: "critical_saturday_morning" (string, all 320 positions full by 9 AM on peak days)

Rationale: Cooling zone is capacity bottleneck on high-volume days. Capacity_utilized_percent tracks constraint in real-time. Air_circulation affects cooling rate (better circulation = faster cooling). Adjacent_to oven means slightly warmer ambient. Aroma_level is sensory detail (could affect customer experience if FOH is nearby). Space_constraint property highlights operational challenge. When at 100% capacity, production must pause until loaves packaged and removed.
```

### OBJECT: front_of_house
```
ID: location_front_of_house
Type: location
Name: Front of House (Retail Counter & Customer Area)
Emoji: 🏪

Properties:
- location_id: "front_of_house" (string)
- location_type: "retail_customer_space" (string)
- area_sq_ft: 280 (square feet, customer service area)

- temperature_current_f: 70 (degrees F)
- temperature_range_f: "68-72" (string, comfortable for customers)
- temperature_control: "hvac_dedicated_zone" (string, separate from production)

- equipment_present: ["equipment_display_case_co57d", "equipment_pos_square_terminal", "packaging_station", "bread_slicer_electric", "customer_seating_4_stools"] (array)

- display_case_capacity_loaves: 38 (integer, max that fits in display)
- current_display_loaves: 0 (integer, how many currently displayed)
- restocking_required: false (boolean, trigger at threshold)

- customer_capacity: 8 (integer, comfortable max customers at once)
- customers_current: 0 (integer, how many customers present)
- queue_length: 0 (integer, how many waiting in line)

- staff_workstations: 1 (integer, POS counter)
- staff_present: [] (array of actor_ids, usually just Sarah)

- ambiance: "warm_welcoming_rustic" (string, design aesthetic)
- decor: ["wood_accents", "bread_photography_wall_art", "chalkboard_daily_menu", "warm_LED_lighting"] (array)
- music: "soft_instrumental" (string, background music)
- music_volume_db: 60 (decibels, unobtrusive)

- aroma: "fresh_baked_bread" (string, wafts from production area)
- aroma_strength: "strong" (enum, primary sensory draw)

- cleanliness_customer_visible: "excellent" (enum: ["poor", "fair", "good", "excellent"])
- cleanliness_impacts_sales: true (boolean, dirty FOH reduces customer confidence)
- last_cleaned_timestamp: "2025-10-22T06:15:00Z" (ISO timestamp)
- cleaning_frequency: "hourly_quick_wipe_daily_deep_clean" (string)

- point_of_sale_location: "center_counter" (string)
- cash_drawer_location: "under_counter_locked" (string)

- customer_flow: "enter_browse_display_queue_checkout_exit" (string, typical pattern)
- average_customer_dwell_time_minutes: 4 (minutes, browse to purchase)
- average_transaction_time_minutes: 1.5 (minutes, checkout duration)

- wi_fi_available: true (boolean, for customer and POS)
- wi_fi_ssid: "ParkSide_Guest" (string)

- restroom_access: true (boolean, customer restroom available)
- restroom_location: "adjacent_70_sqft" (string)
- restroom_cleanliness_checks_per_day: 6 (integer, Sarah checks regularly)

- security: ["security_camera_1", "alarm_system_entry_sensor"] (array)
- alarm_armed_after_hours: true (boolean)

- hours_of_operation: {"tuesday": "07:00-18:00", "wednesday": "07:00-18:00", "thursday": "07:00-18:00", "friday": "07:00-18:00", "saturday": "07:00-16:00", "sunday": "08:00-14:00", "monday": "closed"} (object)

- revenue_generated_here: true (boolean, this is where sales happen)
- critical_for_business: true (boolean, no sales without FOH)

Rationale: FOH is customer interface and revenue realization point. Display_case_capacity limits how much can be shown at once (merchandising constraint). Customer_capacity affects peak hour congestion. Cleanliness_customer_visible affects reputation and sales. Aroma_strength is sensory marketing (fresh bread smell attracts customers). Average_transaction_time affects queue length and Sarah's workload. Hours_of_operation drive staffing and production schedules. Wi_fi_available for POS functionality (internet dependency).
```

### OBJECT: packaging_area
```
ID: location_packaging_area
Type: location
Name: Packaging & Holding Station
Emoji: 📦

Properties:
- location_id: "packaging_area_foh_adjacent" (string)
- location_type: "transition_packaging" (string)
- area_sq_ft: 100 (square feet)

- temperature_current_f: 70 (degrees F)

- equipment_present: ["packaging_supply_shelves", "packaging_work_table", "bread_slicer_electric_backup"] (array)

- storage_capacity: {"bags_bread": 5000, "bags_baguette": 3000, "labels": 15000, "tissue_paper": 2000} (object, max quantities)

- current_loaf_holding: [] (array of loaf_ids waiting to be packaged or moved to FOH)
- holding_capacity_loaves: 60 (integer, temporary staging)

- workflow: "cooling_complete_→_move_here_→_package_→_display_or_wholesale" (string)

- staff_access: ["actor_sarah_thompson", "actor_david_kim", "actor_rachel_martinez_wholesale"] (array, who works here)

- primary_activities: ["packaging_retail", "slicing_bread", "wholesale_order_assembly", "inventory_staging"] (array)

- adjacent_to: ["location_cooling_zone", "location_front_of_house", "location_wholesale_staging"] (array)

- cleanliness_state: "clean" (enum)
- last_cleaned_timestamp: "2025-10-22T06:30:00Z"
- cleaning_frequency: "beginning_and_end_of_day" (string)

Rationale: Packaging area is transition zone between production and sales. Holding_capacity creates temporary staging constraint. Storage_capacity for packaging supplies (running out blocks sales). Staff_access indicates who performs packaging tasks. Adjacent_to cooling and FOH enables smooth workflow. This zone bridges BOH and FOH.
```

### OBJECT: wholesale_staging
```
ID: location_wholesale_staging
Type: location
Name: Wholesale Order Staging
Emoji: 📦

Properties:
- location_id: "wholesale_staging_area" (string)
- location_type: "wholesale_fulfillment" (string)
- area_sq_ft: 24 (square feet, small dedicated area)

- temperature_current_f: 70 (degrees F)

- equipment_present: ["staging_shelves_labeled_by_customer", "wholesale_packaging_materials", "clipboards_invoices"] (array)

- current_orders_staged: [] (array of order objects with {customer_id, loaf_ids, pickup_time})
- staging_capacity_orders: 6 (integer, max simultaneous orders)

- wholesale_customers: ["cedar_street_cafe", "northside_market", "downtown_deli", "sunday_farmers_market", "corporate_office_building_weekly"] (array, regular accounts)

- typical_order_size_loaves: 15 (integer, average wholesale order)
- pickup_window_morning: "07:30-09:30" (string, when customers pick up)
- delivery_window_marcus: "09:00-10:00" (string, when Marcus delivers)

- invoicing_method: "paper_clipboard_for_pickup_confirmation" (string)
- payment_terms: "net_14_days" (string, invoice payment)

- adjacent_to: ["location_packaging_area", "location_front_of_house_side_door"] (array)
- access_for_customers: "side_door_staff_escorted" (string, wholesale customers don't enter main FOH)

- primary_staff: ["actor_rachel_martinez", "actor_marcus_chen"] (array, who preps wholesale orders)

Rationale: Wholesale staging separates wholesale fulfillment from retail operations. Current_orders_staged tracks what's ready for pickup/delivery. Staging_capacity limits how many orders can be prepped simultaneously. Wholesale_customers array defines accounts. Pickup_window creates timing constraint (orders must be ready by specific time). Payment_terms affect cash flow (not immediate payment like retail).
```

---

## SUMMARY STATISTICS

**Total Objects Specified:** 100+ across all categories
- **Actors:** 4 (complete staff)
- **Custom Type Objects:** 50+ (levain cultures, dough batches, individual loaves, oven decks, baskets, containers, racks, storage locations, ingredients)
- **Equipment:** 15+ (standard type for non-custom equipment)
- **Products:** 10 (all bread varieties)
- **Resources:** 15+ (packaging, utilities, cleaning)
- **Locations:** 10+ (spatial zones)

**Key Simulation-Ready Features:**
1. **State Machines:** Every object with lifecycle (dough: mixed → fermenting → shaped → proofing → baking → cooling → sold)
2. **Capacity Constraints:** Oven (24-30 loaves/cycle), Retarder (190 loaves), Cooling (320 positions)
3. **Quality Tracking:** Quality_score (0-100) on all production objects, degrades with violations
4. **Cost Accounting:** Every ingredient, resource, labor hour tracked with USD values
5. **Timing Dependencies:** Timestamps track when processes start/end, enforce minimum durations
6. **Equipment Dependencies:** Objects reference equipment_ids they require, equipment has states
7. **Actor Skills:** Skill levels (0-100) affect quality and task eligibility
8. **Failure Modes:** Malfunction probabilities on all critical equipment
9. **Spatial Tracking:** Location properties enable workflow modeling and movement
10. **Financial Integration:** All costs and revenues flow to profit calculation

This specification provides the foundation for a complete, realistic bakery simulation with hundreds of interacting objects, realistic constraints, and emergent complexity from simple rules.