# Mini-Project 3 :- The Automated Machine Learning Model Auditor 🤖📊 :-

# Step 1 : Define the Blueprint (class) -

class ModelAuditor :
    def __init__(self,auditor_name,min_threshold):
        self.auditor_name = auditor_name
        self.min_threshold = min_threshold

# Step 2 : Add the Action Tool (run_audit) -

    def run_audit(self, performance_dict) :
        for name in performance_dict :
            decimal_score = performance_dict[name]
            acc_performance_dict = decimal_score * 100

            if acc_performance_dict >= self.min_threshold :
                print(name,": Deployed (Score: ",acc_performance_dict,")")
            else :
                print(name,": Rejected (Score : ",acc_performance_dict,")")

# Step 3 : The Main Execution (Outside the Class) -

my_auditor = ModelAuditor("Rehan",75.0)
results = {
    "Model_Alpha": 0.82, "Model_Beta": 0.64, "Model_Gamma": 0.91
    }
my_auditor.run_audit(results)
    