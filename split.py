import json
import os

for file in os.listdir(f'{os.getcwd()}/omni-biome'):
    if 'en_us' in file:
        continue

    with open(f'omni-biome/{file}', 'r') as f:
        biome_data: dict = json.load(f)

    with open(f'incendium/{file}', 'r') as f:
        incendium_data: dict = json.load(f)

    terralith_data = {k: v for k, v in biome_data.items() if 'terralith' in k}
    nullscape_data = {k: v for k, v in biome_data.items() if 'nullscape' in k}
    incendium_data.update({k: v for k, v in biome_data.items() if 'incendium' in k})

    with open(f'terralith/{file}', 'w', encoding='utf-8') as f:
        json.dump(terralith_data, f, indent=4, ensure_ascii=False)

    with open(f'incendium/{file}', 'w', encoding='utf-8') as f:
        json.dump(incendium_data, f, indent=4, ensure_ascii=False)

    with open(f'nullscape/{file}', 'w', encoding='utf-8') as f:
        json.dump(nullscape_data, f, indent=4, ensure_ascii=False)