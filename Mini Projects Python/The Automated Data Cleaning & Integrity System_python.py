# Mini-Project 2 :- The Automated Data Cleaning & Integrity System 🛠️🚀 :-

# Step 1 : Define the Blueprint (class) -

class DataPipeline :

    def __init__(self,dataset_name,raw_records):
        self.dataset_name = dataset_name
        self.raw_records = raw_records

# Step 2 : Add Action Tool 1 (clean_data) -

    def clean_data(self) :
        self.cleaned_records = set(self.raw_records)
        print("Duplicates removed from",self.dataset_name,self.cleaned_records)

# Step 3 : Add Action Tool 2 (audit_metrics) -

    def audit_metrics(self, accuracy_list) :
        for lists in accuracy_list :
            percentage_list = lists * 100

            if(percentage_list >= 50.0) :
                print("Pass: ",percentage_list)
            else :
                print("Fail: Alert Team!",percentage_list)

# Step 4 : The Main Execution (Outside the Class) -

print("Tracking IDs: ", [201, 202, 201, 203, 202])
my_pipeline = DataPipeline("Tracking IDs: ", [201, 202, 201, 203, 202])
my_pipeline.clean_data( )
print("List: ",[0.88, 0.42, 0.95])
my_pipeline.audit_metrics([0.88, 0.42, 0.95])

        
        
