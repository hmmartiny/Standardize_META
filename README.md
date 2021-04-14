# STandardize METAdata
A collection of Python scripts for cleaning and standardizing metadata.

## How-to
### Normalize geograpical names
```python
>>> from STMETA.country_lookup import CountryLookup
>>> cl = CountryLookup(data_dir='/data')

# Fix spelling mistake
>>> cl.search('Danmark')
'Denmark'
```

## Data sources
### Geographical areas
The files in the data/ folder have been downloaded from [Natural Earth Data](https://www.naturalearthdata.com/). 
The following files are needed for `CountryLookup` to work:
* [ne_10m_admin_0_countries](https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_countries.zip)
* [ne_10m_geography_marine_polys](https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_geography_marine_polys.zip)
* [ne_10m_lakes](https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_lakes.zip)