import pandas as pd
import streamlit as st 
from io import BytesIO  # Add this import

def generate_excel_file():
    # Sample data for project metrics
    data = {
        "project_id": ["P001", "P002", "P003", "P004", "P005", "P006", "P007"],
        "sprint_id": ["S01", "S02", "S03", "S04", "S05", "S06", "S07"],
        "total_tasks": [50, 60, 40, 70, 55, 65, 45],
        "completed_tasks": [45, 40, 35, 50, 50, 55, 30],
        "pending_tasks": [5, 20, 5, 20, 5, 10, 15],
        "overdue_tasks": [1, 5, 0, 6, 1, 3, 4],
        "avg_completion_time": [3.5, 6.0, 2.8, 7.5, 3.2, 4.5, 6.5],
        "high_priority_bugs": [2, 5, 1, 6, 2, 3, 4],
        "resource_availability": [85, 60, 90, 55, 80, 75, 60],
        "sprint_velocity": [12, 8, 14, 7, 11, 9, 6],
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)

    # Create a BytesIO object to hold the Excel file in memory
    excel_buffer = BytesIO()

    # Write the DataFrame to the BytesIO object
    df.to_excel(excel_buffer, index=False)

    # Set the cursor position to the beginning of the BytesIO buffer
    excel_buffer.seek(0)

    # Generate the filename
    file_name = "sample_data.xlsx"

    # Notify the user
    st.success(f"Sample Excel file '{file_name}' has been generated! You can now download it.")
    st.download_button(
        label="Download Excel file",
        data=excel_buffer,
        file_name=file_name,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
