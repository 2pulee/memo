import streamlit as st
import calendar

st.header("Calendar")
    
    # Get user input for the year
year = st.number_input("Enter a year", min_value=0, max_value=9999, value=2022)
    
    # Create a calendar for the specified year
cal = calendar.Calendar(calendar.SUNDAY)
    
    # Create a list to hold all months' calendars
all_months = []
    
    # Loop through each month of the year
for month in range(1, 13):
        # Generate the month's calendar
        month_cal = cal.monthdayscalendar(year, month)
        month_name = calendar.month_name[month]
        
        # Create a title for the month
        month_title = f"### {month_name} {year}"
        
        # Create a header row with day names
        days_header = "|".join(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
        separator = "|".join(["---"] * 7)
        header_row = f"|{days_header}|\n|{separator}|"
        
        # Format the month's calendar as a Markdown table
        month_table = month_title + "\n" + header_row + "\n"
        for week in month_cal:
            week_str = "|".join(f"{day:2}" if day != 0 else "  " for day in week)
            month_table += f"|{week_str}|\n"
        
        all_months.append(month_table)
    
    # Display all months' calendars
st.markdown("\n\n".join(all_months), unsafe_allow_html=True)