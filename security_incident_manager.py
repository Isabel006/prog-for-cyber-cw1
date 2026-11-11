
# ==========================================
# TASK 4: SECURITY INCIDENT MANAGER
# ==========================================

# 1. Create a dictionary containing security incident information
incident = {
    "username": "admin",
    "ip_address": "192.168.1.25",
    "event_type": "Multiple failed logins",
    "risk_level": "High"
}

# 2. Display the username and IP address
print("Username:", incident["username"])
print("IP Address:", incident["ip_address"])


# 3. Add a status field to show the current progress of the incident
incident["status"] = "Under Investigation"

print("\nStatus field successfully added:", incident["status"])


# 4. Update the risk level of the incident
incident["risk_level"] = "Critical"

print("Risk level successfully updated to:", incident["risk_level"])


# 5. Remove the event type field from the dictionary
del incident["event_type"]

print("Event type field successfully removed.")


# 6. Display all remaining dictionary keys and values
print("\n========== SECURITY INCIDENT DETAILS ==========")

for key, value in incident.items():

    # Display each key and its corresponding value
    print(f"{key}: {value}")


# 7. Count and display the total number of key-value pairs
total_items = len(incident)

print(f"\nTotal number of key-value pairs: {total_items}")
