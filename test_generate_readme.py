import json

with open("job_ad_display.json", "r") as json_file:
    json_content = json.load(json_file)
readme_content = f"""# {json_content["title"]}

## Description

{json_content["description"]}

## Keys
"""
for field_name in list(json_content["properties"].keys()):
    readme_content += f"""
### {field_name}
{json_content["properties"][field_name]["description"]}
    """
with open("resultat.md", "w") as readme_file:
    readme_file.write(readme_content)
