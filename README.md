# Artificial Intelligence Industry Alliance

We acquired a list of the AIIA membership from its website and manually populated the following fields for each member organization using open-source information from members’ websites, media coverage and commercial databases. The repo contains the annotated dataset,
as well as code to create visualizations using information gathered from that dataset.

To make everything in this workspace run:

1.)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

# Contents

This repository contains one CSV and two python scripts.

The csv, [aiia_annotated_collections.csv](aiia_annotated_collections.csv), contains the manually populated data on the AIIA membership.

The first script, [get_locations.py](get_locations.py), contains code to identify the latitudes 
and longitudes of cities within China, when those cities are provided in a csv file.

The second script, [organizational_structure.py](organizational_structure.py), makes a plot showing
the organizational structure of the AIIA.

