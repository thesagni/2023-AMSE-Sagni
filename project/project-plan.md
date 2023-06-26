# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
It has been seen in recent years that the rate of accidents has increased. 
So aim of this project is to identify how much of the increased rate of accidents is related to the increase in bicycle traffic in the city of Münster.
So, This projects draws a connections between the available cycle stations in Münster with the road accidents in Germany. 

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The analysis helps to do correlate increase in road accidents with the increase in bicycle traffic.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1:Mobilithek
* Metadata URL 1: https://mobilithek.info/offers/-6901989592576801458
* Data URL 1: https://opendata.stadt-muenster.de/dataset/verkehrsz%C3%A4hlung-fahrradverkehr-tagesaktuelle-daten/resource/c072d000-ffb3-4e79-8811 
* Data Type: CSV
Data of bicycle counting stations in city of Münster

### Datasource2:Federal Statistical Office of Germany
* Metadata URL 2: https://www.destatis.de/
* Data URL 2: https://www-genesis.destatis.de/genesis/online?language=en&sequenz=statistikTabellen&selectionname=46241#abreadcrumb
* Data Type: CSV
Road Accident Data in Germany

### Datasource3: Münster Polizie Nordrhein-Westfalen
* Metadata URL 2: https://muenster.polizei.nrw/artikel/verkehrsunfallstatistik-2021-1
* Data URL 2: https://muenster.polizei.nrw/sites/default/files/2022-03/Verkehrsunfallbilanz%202021
* Data Type: XLS
Road Accident Data in Münster

Münster is famous for it's bicycle traffic and hence we see an increase in bicycle stations in this city in recent years.
This projects draws a connections between the increase in cycle stations (hence the cycle traffic) in Münster with the road accidents rate increase in Germany in the year 2020 and 2021

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Extract Data from the two data sources
2. Create graph
3. Calculate the occurence of accidents with bicycle traffic from graph
4. Draw Conclusion from the graphs

[i1]: https://github.com/jvalue/2023-amse-template/issues/1
