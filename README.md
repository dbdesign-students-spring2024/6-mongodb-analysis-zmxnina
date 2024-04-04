# Airbnb MongoDB Analysis
## Part 1: Data Set Details
### The original data file exceeds 100 MB and hence cannot not be pushed to GitHub. Here is a [link](https://drive.google.com/file/d/1eUHlpqhQIlAylS1r3kZHSUWxCLqBipTr/view?usp=sharing) to the raw data file.
The selected data set from [Inside Airbnb](https://insideairbnb.com/get-the-data/) is a comprehensive collection of individual Airbnb listings in London, United Kingdom, each encompassing a wide array of information from basic listing details to host profiles, and from booking specifics to guest reviews.

The original data file was in CSV format and below are the first 20 rows (exluding field headers) of the raw data:
|id    |listing_url        |scrape_id     |last_scraped|source         |name                  |description|neighborhood_overview    |picture_url         |host_id|host_url           |host_name   |host_since|host_location            |host_about                |host_response_time|host_response_rate|host_acceptance_rate|host_is_superhost|host_thumbnail_url  |host_picture_url    |host_neighbourhood  |host_listings_count|host_total_listings_count|host_verifications              |host_has_profile_pic|host_identity_verified|neighbourhood   |neighbourhood_cleansed|neighbourhood_group_cleansed|latitude          |longitude            |property_type     |room_type      |accommodates|bathrooms|bathrooms_text  |bedrooms|beds|amenities|price  |minimum_nights|maximum_nights|minimum_minimum_nights|maximum_minimum_nights|minimum_maximum_nights|maximum_maximum_nights|minimum_nights_avg_ntm|maximum_nights_avg_ntm|calendar_updated|has_availability|availability_30|availability_60|availability_90|availability_365|calendar_last_scraped|number_of_reviews|number_of_reviews_ltm|number_of_reviews_l30d|first_review|last_review|review_scores_rating|review_scores_accuracy|review_scores_cleanliness|review_scores_checkin|review_scores_communication|review_scores_location|review_scores_value|license|instant_bookable|calculated_host_listings_count|calculated_host_listings_count_entire_homes|calculated_host_listings_count_private_rooms|calculated_host_listings_count_shared_rooms|reviews_per_month|
|------|-------------------|--------------|------------|---------------|----------------------|-----------|-------------------------|--------------------|-------|-------------------|------------|----------|-------------------------|--------------------------|------------------|------------------|--------------------|-----------------|--------------------|--------------------|--------------------|-------------------|-------------------------|--------------------------------|--------------------|----------------------|----------------|----------------------|----------------------------|------------------|---------------------|------------------|---------------|------------|---------|----------------|--------|----|---------|-------|--------------|--------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------|----------------|---------------|---------------|---------------|----------------|---------------------|-----------------|---------------------|----------------------|------------|-----------|--------------------|----------------------|-------------------------|---------------------|---------------------------|----------------------|-------------------|-------|----------------|------------------------------|-------------------------------------------|--------------------------------------------|-------------------------------------------|-----------------|
|198258|https://www.aribnb…|20231210055232|2023-12-10  |city scrape    |Rental unit in…       |           |I live in…               |https://a0.muscache…|967537 |https://www.aribnb…|Ryan        |2011-08-14|Barking, United Kingdom  |Do the Math…              |within an hour    |100%              |75%                 |f                |https://a0.muscache…|https://a0.muscache…|                    |1                  |1                        |['email', 'phone']              |t                   |t                     |Barking,…       |Barking and Dagenham  |                            |51.5343           |0.08178              |Private room in…  |Private room   |1           |         |1 shared bath   |        |1   |[]       |$67.00 |2             |100           |2                     |2                     |100                   |100                   |2.0                   |100.0                 |                |t               |28             |58             |88             |363             |2023-12-10           |41               |1                    |0                     |2011-08-22  |2023-03-16 |4.74                |4.83                  |4.25                     |4.8                  |4.88                       |4.45                  |4.68               |       |f               |1                             |0                                          |1                                           |0                                          |0.27             |
|33332 |https://www.aribnb…|20231210055232|2023-12-10  |city scrape    |Home in St Margaret's…|           |Peaceful and friendly.   |https://a0.muscache…|144444 |https://www.aribnb…|Chi-Chi     |2010-06-14|Isleworth, United Kingdom|Quite busy and…           |N/A               |N/A               |N/A                 |f                |https://a0.muscache…|https://a0.muscache…|LB of Hounslow      |2                  |2                        |['email', 'phone']              |t                   |f                     | St Margaret’s,…|Richmond upon Thames  |                            |51.4641           |-0.32498             |Private room in…  |Private room   |2           |         |1 private bath  |        |1   |[]       |$140.00|2             |21            |2                     |2                     |21                    |21                    |2.0                   |21.0                  |                |t               |30             |60             |90             |365             |2023-12-10           |20               |0                    |0                     |2010-10-16  |2022-08-01 |4.4                 |4.47                  |4.58                     |4.58                 |4.53                       |4.68                  |4.26               |       |f               |2                             |0                                          |2                                           |0                                          |0.12             |
|42010 |https://www.aribnb…|20231210055232|2023-12-10  |city scrape    |Home in East…         |           |We have a…               |https://a0.muscache…|157884 |https://www.aribnb…|Agri & Roger|2010-07-04|London, United Kingdom   |We are a…                 |within a few hours|100%              |100%                |t                |https://a0.muscache…|https://a0.muscache…|LB of Haringey      |2                  |4                        |['email', 'phone']              |t                   |t                     |East Finchley,… |Barnet                |                            |51.5859           |-0.16434             |Private room in…  |Private room   |2           |         |1 shared bath   |        |1   |[]       |$65.00 |4             |365           |4                     |4                     |365                   |365                   |4.0                   |365.0                 |                |t               |9              |18             |31             |208             |2023-12-10           |556              |29                   |3                     |2010-09-22  |2023-12-03 |4.88                |4.89                  |4.83                     |4.96                 |4.95                       |4.73                  |4.87               |       |t               |2                             |0                                          |2                                           |0                                          |3.45             |
|284603|https://www.aribnb…|20231210055232|2023-12-11  |previous scrape|Rental unit in…       |           |                         |https://a0.muscache…|1481851|https://www.aribnb…|Tania       |2011-12-07|London, United Kingdom   |Hello! Thank you…         |N/A               |N/A               |100%                |f                |https://a0.muscache…|https://a0.muscache…|Westbourne Green    |1                  |2                        |['email', 'phone']              |t                   |t                     |                |Kensington and Chelsea|                            |51.51464          |-0.20004             |Entire rental unit|Entire home/apt|3           |         |1.5 baths       |        |1   |[]       |$297.00|14            |365           |14                    |14                    |365                   |365                   |14.0                  |365.0                 |                |f               |0              |0              |0              |0               |2023-12-11           |6                |0                    |0                     |2012-07-16  |2022-07-04 |4.83                |4.83                  |5.0                      |5.0                  |5.0                        |5.0                   |4.83               |       |f               |1                             |1                                          |0                                           |0                                          |0.04             |
|89870 |https://www.aribnb…|20231210055232|2023-12-10  |city scrape    |Rental unit in…       |           |Finsbury Park is…        |https://a0.muscache…|54730  |https://www.aribnb…|Alina       |2009-11-16|London, United Kingdom   |I am a…                   |within an hour    |90%               |85%                 |f                |https://a0.muscache…|https://a0.muscache…|LB of Islington     |3                  |5                        |['email', 'phone']              |t                   |t                     |London,…        |Islington             |                            |51.56792          |-0.11125             |Entire rental unit|Entire home/apt|4           |         |1 bath          |        |1   |[]       |$149.00|1             |60            |1                     |1                     |60                    |60                    |1.0                   |60.0                  |                |t               |22             |52             |82             |357             |2023-12-10           |133              |15                   |1                     |2011-08-14  |2023-12-03 |4.65                |4.68                  |4.64                     |4.9                  |4.91                       |4.73                  |4.5                |       |f               |3                             |2                                          |1                                           |0                                          |0.89             |
|326146|https://www.aribnb…|20231210055232|2023-12-13  |previous scrape|Rental unit in…       |           |                         |https://a0.muscache…|1667975|https://www.aribnb…|Inma        |2012-01-29|London, United Kingdom   |Hi my name…               |N/A               |N/A               |N/A                 |f                |https://a0.muscache…|https://a0.muscache…|                    |1                  |2                        |['email', 'phone']              |t                   |f                     |                |Waltham Forest        |                            |51.57139          |-0.03131             |Private room in…  |Private room   |2           |         |                |        |1   |[]       |$120.00|7             |21            |7                     |7                     |21                    |21                    |7.0                   |21.0                  |                |f               |0              |0              |0              |0               |2023-12-13           |0                |0                    |0                     |            |           |                    |                      |                         |                     |                           |                      |                   |       |f               |1                             |0                                          |1                                           |0                                          |                 |
|96052 |https://www.aribnb…|20231210055232|2023-12-10  |city scrape    |Condo in London…      |           |Residential, quiet and…  |https://a0.muscache…|448154 |https://www.aribnb…|Aneta       |2011-03-17|London, United Kingdom   |I also love…              |within a few hours|100%              |90%                 |t                |https://a0.muscache…|https://a0.muscache…|LB of Brent         |2                  |2                        |['email', 'phone']              |t                   |t                     |London,…        |Brent                 |                            |51.5593           |-0.22497             |Private room in…  |Private room   |2           |         |1 shared bath   |        |1   |[]       |$52.00 |3             |180           |3                     |3                     |180                   |180                   |3.0                   |180.0                 |                |t               |17             |47             |77             |352             |2023-12-10           |80               |5                    |1                     |2011-05-24  |2023-11-24 |4.82                |4.71                  |4.74                     |4.93                 |4.9                        |4.45                  |4.7                |       |f               |2                             |0                                          |2                                           |0                                          |0.52             |
|381467|https://www.aribnb…|20231210055232|2023-12-11  |previous scrape|Rental unit in…       |           |Peaceful and quite…      |https://a0.muscache…|1913410|https://www.aribnb…|Thanos      |2012-03-13|London, United Kingdom   |Professional and friendly…|N/A               |N/A               |N/A                 |f                |https://a0.muscache…|https://a0.muscache…|Earls Court         |1                  |7                        |['email', 'phone']              |t                   |t                     |London,…        |Kensington and Chelsea|                            |51.4875           |-0.19608             |Entire rental unit|Entire home/apt|4           |         |1.5 baths       |        |2   |[]       |$143.00|2             |1125          |2                     |2                     |1125                  |1125                  |2.0                   |1125.0                |                |f               |0              |0              |0              |0               |2023-12-11           |265              |0                    |0                     |2012-04-03  |2018-07-20 |4.66                |4.76                  |4.74                     |4.78                 |4.82                       |4.88                  |4.64               |       |f               |1                             |1                                          |0                                           |0                                          |1.86             |
|390987|https://www.aribnb…|20231210055232|2023-12-10  |city scrape    |Home in London…       |           |The neighbourhood is…    |https://a0.muscache…|1955537|https://www.aribnb…|Ali         |2012-03-18|London, United Kingdom   |Easy going, socialable…   |within a few hours|100%              |88%                 |t                |https://a0.muscache…|https://a0.muscache…|West Norwood        |4                  |6                        |['email', 'phone']              |t                   |t                     |London,…        |Lambeth               |                            |51.42643          |-0.09726             |Private room in…  |Private room   |2           |         |1 shared bath   |        |1   |[]       |$41.00 |14            |1000          |14                    |14                    |1000                  |1000                  |14.0                  |1000.0                |                |t               |0              |29             |59             |334             |2023-12-10           |12               |2                    |0                     |2013-05-15  |2023-07-11 |4.73                |4.75                  |4.83                     |4.92                 |4.83                       |4.75                  |4.75               |       |f               |3                             |0                                          |3                                           |0                                          |0.09             |
|394755|https://www.aribnb…|20231210055232|2023-12-11  |previous scrape|Rental unit in…       |           |                         |https://a0.muscache…|1973515|https://www.aribnb…|Lara        |2012-03-20|London, United Kingdom   |I am studying…            |N/A               |N/A               |N/A                 |f                |https://a0.muscache…|https://a0.muscache…|LB of Camden        |1                  |1                        |['email', 'phone']              |t                   |f                     |                |Camden                |                            |51.54632          |-0.13666             |Entire rental unit|Entire home/apt|2           |         |1.5 baths       |        |2   |[]       |$80.00 |5             |1125          |5                     |5                     |1125                  |1125                  |5.0                   |1125.0                |                |f               |0              |0              |0              |0               |2023-12-11           |1                |0                    |0                     |2016-08-05  |2016-08-05 |5.0                 |5.0                   |5.0                      |5.0                  |5.0                        |5.0                   |4.0                |       |f               |1                             |1                                          |0                                           |0                                          |0.01             |
|468438|https://www.aribnb…|20231210055232|2023-12-11  |previous scrape|Townhouse in London…  |           |We're very close…        |https://a0.muscache…|2324518|https://www.aribnb…|Alison      |2012-05-08|London, United Kingdom   |Hi, I'm Alison…           |N/A               |N/A               |N/A                 |f                |https://a0.muscache…|https://a0.muscache…|LB of Islington     |3                  |3                        |['email', 'phone']              |t                   |t                     |London,…        |Islington             |                            |51.56217          |-0.11416             |Private room in…  |Private room   |2           |         |1 shared bath   |        |1   |[]       |$30.00 |2             |40            |2                     |2                     |1125                  |1125                  |2.0                   |1125.0                |                |f               |0              |0              |0              |0               |2023-12-11           |237              |0                    |0                     |2012-07-30  |2019-10-06 |4.58                |4.8                   |4.5                      |4.82                 |4.8                        |4.53                  |4.7                |       |f               |3                             |0                                          |2                                           |1                                          |1.71             |
|475700|https://www.aribnb…|20231210055232|2023-12-11  |previous scrape|Loft in London…       |           |Our neighbourhood is…    |https://a0.muscache…|2358441|https://www.aribnb…|Jane        |2012-05-13|London, United Kingdom   |I work part…              |N/A               |N/A               |N/A                 |f                |https://a0.muscache…|https://a0.muscache…|Camden Town         |1                  |1                        |['email', 'phone']              |t                   |t                     |London,…        |Camden                |                            |51.53896          |-0.13997             |Private room in…  |Private room   |2           |         |1 bath          |        |1   |[]       |$95.00 |3             |30            |3                     |3                     |30                    |30                    |3.0                   |30.0                  |                |f               |0              |0              |0              |0               |2023-12-11           |7                |0                    |0                     |2013-10-13  |2015-11-02 |4.86                |4.71                  |4.86                     |5.0                  |5.0                        |5.0                   |4.71               |       |f               |1                             |0                                          |1                                           |0                                          |0.06             |
|117203|https://www.aribnb…|20231210055232|2023-12-10  |city scrape    |Rental unit in…       |           |For the lovers…          |https://a0.muscache…|255103 |https://www.aribnb…|Olga        |2010-10-06|London, United Kingdom   |A writer and…             |within an hour    |100%              |91%                 |t                |https://a0.muscache…|https://a0.muscache…|Hammersmith         |1                  |1                        |['email', 'phone', 'work_email']|t                   |t                     |London,…        |Hammersmith and Fulham|                            |51.50155001001140 |-0.2330022236049810  |Entire rental unit|Entire home/apt|2           |         |1 bath          |        |1   |[]       |$136.00|5             |120           |1                     |5                     |1125                  |1125                  |5.0                   |1125.0                |                |t               |0              |1              |13             |13              |2023-12-10           |86               |14                   |1                     |2012-01-04  |2023-11-19 |4.86                |4.9                   |4.89                     |4.8                  |4.93                       |4.54                  |4.72               |       |f               |1                             |1                                          |0                                           |0                                          |0.59             |
|565770|https://www.aribnb…|20231210055232|2023-12-10  |city scrape    |Cabin in Hounslow…    |           |                         |https://a0.muscache…|1958273|https://www.aribnb…|Mandeep     |2012-03-18|London, United Kingdom   |We have been…             |within an hour    |100%              |93%                 |f                |https://a0.muscache…|https://a0.muscache…|LB of Hounslow      |3                  |6                        |['email', 'phone', 'work_email']|t                   |t                     |                |Hounslow              |                            |51.47789          |-0.39478             |Entire cabin      |Entire home/apt|4           |         |1 bath          |        |4   |[]       |$50.00 |1             |1125          |1                     |1                     |1125                  |1125                  |1.0                   |1125.0                |                |t               |15             |45             |75             |350             |2023-12-10           |254              |34                   |2                     |2012-10-12  |2023-11-26 |4.42                |4.65                  |4.42                     |4.72                 |4.77                       |4.38                  |4.47               |       |f               |1                             |1                                          |0                                           |0                                          |1.87             |
|493679|https://www.aribnb…|20231210055232|2023-12-11  |previous scrape|Rental unit in…       |           |We are located…          |https://a0.muscache…|423121 |https://www.aribnb…|Olivia      |2011-03-04|London, United Kingdom   |I am a…                   |N/A               |N/A               |N/A                 |f                |https://a0.muscache…|https://a0.muscache…|Bethnal Green       |1                  |1                        |['email', 'phone', 'work_email']|t                   |t                     |Greater London,…|Tower Hamlets         |                            |51.53171          |-0.0612              |Entire rental unit|Entire home/apt|6           |         |1 bath          |        |2   |[]       |$140.00|2             |20            |2                     |2                     |20                    |20                    |2.0                   |20.0                  |                |f               |0              |0              |0              |0               |2023-12-11           |2                |0                    |0                     |2018-06-17  |2018-07-30 |5.0                 |5.0                   |5.0                      |5.0                  |5.0                        |5.0                   |4.5                |       |f               |1                             |1                                          |0                                           |0                                          |0.03             |
|569402|https://www.aribnb…|20231210055232|2023-12-11  |previous scrape|Home in London…       |           |                         |https://a0.muscache…|2802762|https://www.aribnb…|Dominic     |2012-07-02|London, United Kingdom   |.                         |N/A               |N/A               |N/A                 |f                |https://a0.muscache…|https://a0.muscache…|Forest Hill         |1                  |1                        |['email', 'phone']              |t                   |f                     |                |Lewisham              |                            |51.44878          |-0.05803             |Entire home       |Entire home/apt|12          |         |3 baths         |        |9   |[]       |$300.00|6             |1125          |6                     |6                     |1125                  |1125                  |6.0                   |1125.0                |                |f               |0              |0              |0              |0               |2023-12-11           |8                |0                    |0                     |2012-12-30  |2014-08-10 |4.75                |4.75                  |4.63                     |4.88                 |5.0                        |4.38                  |4.75               |       |f               |1                             |1                                          |0                                           |0                                          |0.06             |
|501837|https://www.aribnb…|20231210055232|2023-12-10  |city scrape    |Rental unit in…       |           |                         |https://a0.muscache…|2476271|https://www.aribnb…|Michael     |2012-05-27|London, United Kingdom   |I am a…                   |within an hour    |100%              |100%                |f                |https://a0.muscache…|https://a0.muscache…|Hampstead           |1                  |2                        |['email', 'phone']              |t                   |t                     |                |Camden                |                            |51.54548          |-0.16365             |Entire rental unit|Entire home/apt|4           |         |1 bath          |        |2   |[]       |$124.00|3             |1125          |1                     |3                     |2                     |1125                  |2.7                   |1119.8                |                |t               |4              |16             |24             |162             |2023-12-10           |137              |8                    |0                     |2012-07-13  |2023-11-07 |4.5                 |4.53                  |4.33                     |4.81                 |4.88                       |4.88                  |4.58               |       |t               |1                             |1                                          |0                                           |0                                          |0.99             |
|571906|https://www.aribnb…|20231210055232|2023-12-10  |city scrape    |Home in London…       |           |Leafy residential street…|https://a0.muscache…|375971 |https://www.aribnb…|Cathy       |2011-02-03|London, United Kingdom   |I am French…              |N/A               |N/A               |50%                 |f                |https://a0.muscache…|https://a0.muscache…|LB of Waltham Forest|1                  |1                        |['email', 'phone']              |t                   |t                     |London,…        |Waltham Forest        |                            |51.567997573832300|-0.006194299999999960|Private room in…  |Private room   |2           |         |1.5 shared baths|        |1   |[]       |$76.00 |2             |21            |2                     |2                     |21                    |21                    |2.0                   |21.0                  |                |t               |28             |58             |88             |363             |2023-12-10           |23               |1                    |0                     |2013-07-10  |2023-07-10 |4.81                |4.83                  |4.87                     |4.91                 |4.96                       |4.55                  |4.74               |       |f               |1                             |0                                          |1                                           |0                                          |0.18             |
|502190|https://www.aribnb…|20231210055232|2023-12-11  |previous scrape|Townhouse in London…  |           |Kilburn is a North…      |https://a0.muscache…|2478162|https://www.aribnb…|Agnes       |2012-05-27|London, United Kingdom   |I am French…              |N/A               |N/A               |N/A                 |f                |https://a0.muscache…|https://a0.muscache…|Hampstead           |1                  |1                        |['email', 'phone']              |t                   |t                     |London,…        |Camden                |                            |51.54609          |-0.20163             |Private room in…  |Private room   |3           |         |1 private bath  |        |1   |[]       |$50.00 |1             |21            |1                     |1                     |1125                  |1125                  |1.0                   |1125.0                |                |f               |0              |0              |0              |0               |2023-12-11           |548              |0                    |0                     |2012-06-20  |2020-03-09 |4.6                 |4.79                  |4.73                     |4.87                 |4.82                       |4.61                  |4.66               |       |f               |1                             |0                                          |1                                           |0                                          |3.92             |
|821334|https://www.aribnb…|20231210055232|2023-12-11  |previous scrape|Rental unit in…       |           |                         |https://a0.muscache…|4309270|https://www.aribnb…|Liana /Lilly|2012-12-03|London, United Kingdom   |I live on…                |N/A               |N/A               |100%                |f                |https://a0.muscache…|https://a0.muscache…|Clapham             |1                  |2                        |['email', 'phone']              |t                   |t                     |                |Lambeth               |                            |51.46914          |-0.13246             |Private room in…  |Private room   |2           |         |1 shared bath   |        |1   |[]       |$60.00 |1             |5             |1                     |1                     |5                     |5                     |1.0                   |5.0                   |                |f               |0              |0              |0              |0               |2023-12-11           |130              |7                    |0                     |2015-09-28  |2023-02-05 |4.83                |4.87                  |4.93                     |4.97                 |4.95                       |4.71                  |4.77               |       |f               |1                             |0                                          |1                                           |0                                          |1.30             |

The original data set contained an overwhelming number of 75 fields, most of which are irrelevant to our intended queries, making imports and analysis unnecessarily cumbersome. Thus, to prepare the data set for analysis in MongoDB, it is streamlined using `pandas` to include only a subset of relevant fields:
```
fieldnames = [
    'id',
    'name',
    'host_id',
    'host_name',
    'host_is_superhost',
    'host_total_listings_count',
    'neighbourhood_cleansed',
    'beds',
    'price',
    'review_scores_rating',
]
```

We observe that there were three neighborhood fields `neighborhood`, `neighbourhood_cleansed`, `neighbourhood_group_cleansed` in the original dataset. 

Specifically, the field `neighborhood` contained entries that were likely direct inputs from the hosts. The data in this field appears to be less standardized due to variations in spellings, capitalizations, and naming conventions. For example, the field contained ten variations of the same neighborhood - Islington, including but not limited to "London Borough of Islington, England, United Kingdom" and "Islington , london, United Kingdom". Since the field reflects raw, unprocessed information about the neighborhoods, it is not ideal for our intended analysis.

The `neighbourhood_group_cleansed` is blank for all listings and hence is insignificant.

The field `neighbourhood_cleansed` represents a standardized version of the neighborhood names, likely processed to account for the variability seen in the neighborhood field. Hence, it is included in the filtered data set in place of the other two.

## Part 2: Data Analysis in MongoDB
1. Show exactly two documents from the `listings` collection in any order.

    Code:
    ```
    db.listings.find().limit(2)
    ```
    Results:
    ```
    [
        {
            _id: ObjectId('660e3395b6515eb2057ca2cf'),
            id: 198258,
            name: 'Rental unit in Barking · ★4.74 · 1 bedroom · 1 bed · 1 shared bath',
            host_id: 967537,
            host_name: 'Ryan',
            host_is_superhost: 'f',
            host_total_listings_count: 1,
            neighbourhood_cleansed: 'Barking and Dagenham',
            beds: 1,
            price: '$67.00',
            review_scores_rating: 4.74
        },
        {
            _id: ObjectId('660e3395b6515eb2057ca2d0'),
            id: 33332,
            name: "Home in  St Margaret's, Isleworth · ★4.40 · 1 bedroom · 1 bed · 1 private bath",
            host_id: 144444,
            host_name: 'Chi-Chi',
            host_is_superhost: 'f',
            host_total_listings_count: 2,
            neighbourhood_cleansed: 'Richmond upon Thames',
            beds: 1,
            price: '$140.00',
            review_scores_rating: 4.4
        }
    ]
    ```

2. Show exactly ten documents in any order, but "prettyprint" in easier to read format, using the `pretty()` function.

    Code:
    ```
    db.listings.find().limit(10).pretty()
    ```
    Results (only includes the first three results):
    ```
    [
        {
            _id: ObjectId('660e3395b6515eb2057ca2cf'),
            id: 198258,
            name: 'Rental unit in Barking · ★4.74 · 1 bedroom · 1 bed · 1 shared bath',
            host_id: 967537,
            host_name: 'Ryan',
            host_is_superhost: 'f',
            host_total_listings_count: 1,
            neighbourhood_cleansed: 'Barking and Dagenham',
            beds: 1,
            price: '$67.00',
            review_scores_rating: 4.74
        },
        {
            _id: ObjectId('660e3395b6515eb2057ca2d0'),
            id: 33332,
            name: "Home in  St Margaret's, Isleworth · ★4.40 · 1 bedroom · 1 bed · 1 private bath",
            host_id: 144444,
            host_name: 'Chi-Chi',
            host_is_superhost: 'f',
            host_total_listings_count: 2,
            neighbourhood_cleansed: 'Richmond upon Thames',
            beds: 1,
            price: '$140.00',
            review_scores_rating: 4.4
        },
        {
            _id: ObjectId('660e3395b6515eb2057ca2d1'),
            id: 42010,
            name: 'Home in East Finchley · ★4.88 · 1 bedroom · 1 bed · 1 shared bath',
            host_id: 157884,
            host_name: 'Agri & Roger',
            host_is_superhost: 't',
            host_total_listings_count: 4,
            neighbourhood_cleansed: 'Barnet',
            beds: 1,
            price: '$65.00',
            review_scores_rating: 4.88
        },
        ...
    ]
    ```

3. Show all of the listings offered by the two superhosts each with `host_id` values of '26573070' and '2443213', respectively. Only show the `name`, `price`, `neighbourhood_cleansed`, `host_name`, and `host_is_superhost` for each result.

    Code:
    ```
    db.listings.find(
        {
            "host_id": {"$in": [26573070, 2443213]}
        },
        {
            "_id": 0, 
            "name": 1, 
            "price": 1, 
            "neighbourhood_cleansed": 1, 
            "host_name": 1, 
            "host_is_superhost": 1
        }
    )
    ```
    Results:
    ```
    [
        {
            name: 'Home in London · ★4.91 · 2 bedrooms · 2 beds · 2 baths',
            host_name: 'Mark',
            host_is_superhost: 't',
            neighbourhood_cleansed: 'Tower Hamlets',
            price: '$253.00'
        },
        {
            name: 'Home in London · ★4.91 · 2 bedrooms · 2 beds · 1 private bath',
            host_name: 'Annabelle',
            host_is_superhost: 't',
            neighbourhood_cleansed: 'Greenwich',
            price: '$123.00'
        },
        {
            name: 'Home in London · ★4.92 · 1 bedroom · 1 bed · 1 private bath',
            host_name: 'Annabelle',
            host_is_superhost: 't',
            neighbourhood_cleansed: 'Greenwich',
            price: '$75.00'
        }
    ]
    ```
4. Find all unique `host_name` values.

    Code:
    ```
    db.listings.distinct("host_name")
    ```
    Results (only includes the first three results):
    ```
    [ 360, '', "'Cassie", ...]
    ```

5. Find all of the listings that have more than 2 beds in Westminster, ordered by `review_scores_rating` descending. Only show the `name`, `beds`, `review_scores_rating`, and `price`.

    Code: 
    ```
    db.listings.find(
        {
            "beds": {"$gt": 2}, 
            "neighbourhood_cleansed": "Westminster"
        },
        {
            "_id": 0,
            "name": 1,
            "beds": 1,
            "review_scores_rating": 1,
            "price": 1
        }
    ).sort({"review_scores_rating": -1})
    ```
    Results (only includes the first three results): 
    ```
    [
        {
            name: 'Rental unit in Greater London · ★New · 3 bedrooms · 4 beds · 2 baths',
            beds: 4,
            price: '$453.00',
            review_scores_rating: ''
        },
        {
            name: 'Rental unit in Greater London · ★New · 2 bedrooms · 3 beds · 2 baths',
            beds: 3,
            price: '$300.00',
            review_scores_rating: ''
        },
        {
            name: 'Rental unit in Greater London · ★New · 3 bedrooms · 3 beds · 3 baths',
            beds: 3,
            price: '$786.00',
            review_scores_rating: ''
        },
        ...
    ]
    ```

6. Show the number of listings per host.

    There are two possible approaches in performing this query. 
    
    #### Approach 1:
    The collection includes a pre-existing field `host_total_listings_count`, which reflects the total number of listings by a host across all locations, not necessarily just in London. Hence, to show the total number of listings per host across all locations:
    ```
    db.listings.aggregate([
        {
            $group: {
                _id: "$host_id",
                total_listings_count: { $first: "$host_total_listings_count" }
            }
        }
    ])
    ```
    Results (only includes the first three results):
    ```
    [
        { _id: 72736418, total_listings_count: 1 },
        { _id: 529285194, total_listings_count: 1 },
        { _id: 483131444, total_listings_count: 1 },
        ...
    ]
    ```

    #### Approach 2:
    If we want to focus solely on the listings within London, we can count the listings per host specifically within the collection:
    ```
    db.listings.aggregate([
        {
            $group: {
                _id: "$host_id",
                london_listings_count: {$sum: 1}
            }
        }
    ])
    ```
    Results (only includes the first three results):
    ```
    [
        { _id: 72736418, london_listings_count: 1 },
        { _id: 529285194, london_listings_count: 1 },
        { _id: 483131444, london_listings_count: 1 },
        ...
    ]
    ```

7. Find the average `review_scores_rating` per neighborhood, and only show those that are 4 or above, sorted in descending order of rating.

    Code:
    ```
    db.listings.aggregate([
        {
            $group: {
                _id: "$neighbourhood_cleansed",
                average_rating: {$avg: "$review_scores_rating"}
            }
        },
        {
            $match: {
                average_rating: {$gte: 4}
            }
        },
        {
            $sort: {
                average_rating: -1
            }
        }
    ])
    ```
    Results (only includes the first three results):
    ```
    [
        { _id: 'Kingston upon Thames', average_rating: 4.809447619047619 },
        { _id: 'Richmond upon Thames', average_rating: 4.798598130841122 },
        { _id: 'Wandsworth', average_rating: 4.760058962264151 },
        ...
    ]
    ```
