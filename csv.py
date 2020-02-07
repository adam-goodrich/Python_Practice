import csv


employees = [{
    "first_name":"Bill",
    "last_name":"Lunmbergh",
    "job_title":"Vice President",
    "hire_date":'1985',
    "performance_review":"Excellent"
},{
    "first_name":"Michael",
    "last_name":"Bolton",
    "job_title":"Programmer",
    "hire_date":'1995',
    "performance_review":"Poor"
},{
    "first_name":"Peter",
    "last_name":"Gibbons",
    "job_title":"Programmer",
    "hire_date":'1989',
    "performance_review":"Poor"
},{
    "first_name":"Samir",
    "last_name":"Nagheenanajar",
    "job_title":"Programmer",
    "hire_date":'1974',
    "performance_review":"Fair"
},{
    "first_name":"Milton",
    "last_name":"Waddams",
    "job_title":"Collator",
    "hire_date":'1974',
    "performance_review":"Does he even work here?"
},{
    "first_name":"Bob",
    "last_name":"Porter",
    "job_title":"Consultant",
    "hire_date":'1999',
    "performance_review":"Excellent"
},{
    "first_name":"Bob",
    "last_name":"Slydell",
    "job_title":"Consultant",
    "hire_date":'1999',
    "performance_review":"Excellent"
}]

with open('tps_report.csv','w',newline='') as csv_file:

    # set names for the heater rows at the top
    header = ['first_name','last_name','job_title','hire_date','performance_review',"finished_review"]
    writer = csv.DictWriter(csv_file, fieldnames=header)
    
    writer.writeheader()
    for employee in employees:
        employee["finished_review"] = "yes"
        if employee["job_title"] == "Consultant" or employee["first_name"] == "Bill":
            employee["performance_review"] = "Poor"
        else: employee["performance_review"] = "Excellent"

        writer.writerow(employee)