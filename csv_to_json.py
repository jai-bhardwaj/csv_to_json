import pandas as pd

#created path variables 
dataPath1 = r"/Users/sujalsharma/Downloads/customer_data_one.csv"
dataPath2 = r"/Users/sujalsharma/Downloads/customer_data_two.csv"
outPath = r"/Users/sujalsharma/Desktop/First Project/customer_data_package.json"

#read the csv files
data1 = pd.read_csv(dataPath1)
data2 = pd.read_csv(dataPath2)

#merged the data1 data2 csv files
merged_data = pd.concat([data1,data2], ignore_index=True)

#initialized variables for columns
first_name = merged_data.first_name
last_name = merged_data.last_name
company_name = merged_data.company_name
address = merged_data.address
city = merged_data.city
county = merged_data.county
state = merged_data.state
zip_code = merged_data.zip
mobile_number = merged_data.mobile_number
email = merged_data.email
web = merged_data.web


#initialized a container,
#here I have used the dictionary so that if primary key is present we don't have to append and we'll just update the data.
container = {}

x = 0

#loop to arrange the data accordingly
while x < len(mobile_number):
    #primary key is mobile_number 
    container[mobile_number[x]] = {
        "First Name": first_name[x],
        "Last Name": last_name[x],
        "Company Name": company_name[x],
        "Address": address[x],
        "City": city[x],
        "County": county[x],
        "State": state[x],
        "Zip": zip_code[x],
        "Mobile Number": mobile_number[x],
        "Email": email[x],
        "Web": web[x]
    }
    x = x + 1
    
#created the final_container
final_container = list(container.values())

#sorted the final_container according to the First Name in ascending order
final_container.sort(key=lambda x:x['First Name'])

print(final_container)

#created a data frame so that we can convert it to json
df = pd.DataFrame(final_container)

#converted df to json
df.to_json(outPath, indent=4,orient='records')


print(pd.read_json(outPath))
