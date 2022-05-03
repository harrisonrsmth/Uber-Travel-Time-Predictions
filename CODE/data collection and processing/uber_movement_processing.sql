CREATE SCHEMA `uber`;

USE `uber`;

CREATE TABLE `uber_movement`.`atl_census_2020_qtr1` (
  `source_id` INT NOT NULL,
  `dest_id` INT NOT NULL,
  `month` INT NOT NULL,
  `day` INT NOT NULL,
  `year` INT NOT NULL,
  `start_hour` INT NOT NULL,
  `mean_travel_time` DECIMAL(9,2) NULL,
  `std_dev_travel_time` DECIMAL(9,2) NULL,
  `geom_mean_travel_time` DECIMAL(9,2) NULL,
  `geom_std_dev_travel_time` DECIMAL(9,2) NULL,
  PRIMARY KEY (`source_id`, `dest_id`, `month`, `day`, `year`, `start_hour`));
  
-- Load Uber Movement data into the above table

DROP VIEW IF EXISTS atl_census_2020_qtr1_view;
CREATE VIEW atl_census_2020_qtr1_view AS
	SELECT 
		source_id, 
        dest_id, 
        2020 as year, 
        month, 
        day, 
        start_hour,
        end_hour,
        DAYOFWEEK(CONCAT('2020-', month, '-', day)) AS day_of_week,
        IF(start_hour = 0 AND end_hour = 7,
            0, 
            IF(start_hour = 7 AND end_hour = 10,
				1,
                IF(start_hour = 10 AND end_hour = 16,
					2,
                    IF(start_hour = 16 AND end_hour = 19,
						3,
                        4)
				)
			)
		) AS hour_bucket,
        mean_travel_time,
        std_dev_travel_time,
        geom_mean_travel_time,
        geom_std_dev_travel_time
	FROM atl_census_2020_qtr1;
    
CREATE TABLE `uber_movement`.`weather_2020_qtr2` (
  `datetime` DATETIME NOT NULL,
  `temp` INT NULL,
  `precip` DECIMAL(9,2) NULL,
  `wind_speed` INT NULL,
  PRIMARY KEY (`datetime`));
  
-- Load weather data into the above table

INSERT INTO atl_census_2020_qtr1_enhanced
	SELECT 
		source_id,
		dest_id,
		year,
		month,
		day,
		start_hour,
		end_hour,
		day_of_week,
		hour_bucket,
		mean_travel_time,
		std_dev_travel_time,
		geom_mean_travel_time,
		geom_std_dev_travel_time,
		AVG(temp) as temp,
		AVG(precip) as precip,
		AVG(wind_speed) as wind_speed
	FROM atl_census_2020_qtr1_view 
	JOIN weather_2020_qtr1 ON datetime BETWEEN CONCAT(year, '-', month, '-', day, " ", start_hour, ":00:00") and CONCAT(year, '-', month, '-', day, " ", end_hour, ":59:59") 
	GROUP BY source_id, dest_id, year, month, day, start_hour, end_hour;

