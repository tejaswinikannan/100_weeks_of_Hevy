
# 🏋️‍♂️ 100 Weeks of Hevy: Workout Analytics

> [!TIP]
> Explore your fitness journey with interactive dashboards and clean data insights from 100 weeks of personal workout logs.

## Overview
This project analyzes 100 weeks of workout data, transforming raw exercise logs into actionable insights and visualizations. Using Power BI and Python, it highlights trends in workout frequency, time commitment, and consistency, helping you understand progress and patterns over time.

## Project Structure
- **Hevy_workouts_log_100_weeks.csv**: Cleaned dataset of 100 weeks of workouts
- **Hevy_workouts_log_part1.csv**, **Hevy_workouts_log_part2.csv**: Split datasets for easier handling
- **Workout_Analytics.pbix**: Power BI dashboard file
- **Split.py**: Python script to split large CSV files

## Getting Started
1. **View the Dashboard**: Open `Workout_Analytics.pbix` in Power BI Desktop to explore interactive visuals.
2. **Work with Data**: Use the provided CSV files for your own analysis or import into other BI tools.
3. **Split Large Files**: Run `Split.py` to divide large CSVs into manageable parts.

## Dashboard Highlights
- **Total Sessions & Hours**: See total workouts and hours logged over 100 weeks
- **Consistency Gauge**: Track how often weekly workout goals were met
- **Duration Breakdown**: Analyze workout lengths (under 30 min, 30–45 min, over 45 min)
- **Trends & Plateaus**: Visualize progress, plateaus, and spikes in training
- **Calendar Heatmap**: Python-powered heatmap shows workout intensity by day

> [!NOTE]
> The dataset logs exercises, not sessions. Deduplication logic ensures accurate workout counts by consolidating duplicate session IDs.

## Skills Demonstrated
- Data cleaning & transformation (Power Query, Python)
- Data modeling & deduplication
- Interactive dashboard design (Power BI)
- Analytical storytelling: uncovering trends, plateaus, and insights

## Author
**Tejaswini Damodara Kannan**  
Data Analyst, Student Affairs  
East Texas A&M University
