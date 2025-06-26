# Risk_calculator_api
## Brief overview
- This flask based rest api that calculates a mock rick score. Post endpoint is  '/api/v1/risk-score'
- Accepts model metadata like region, data sensitivity, processor name and purpose.
- Calculates a rule based risk score based on the instructions provided in task definition.
- Token based authetication using bearer token. I used a fixed token.
- Dockerized for easy deployment to the cloud and to run locally.



## Setup instructions
- Download docker desktop and POstman (Optional). Using docker desktop we can build the docker file. Open the risk_api_project folder and then open terminal from the same folder. Run these commands to build the image and run the container `docker build -t flask-risk-api .` and `docker run -p 8000:8000 flask-risk-api`
- I then used Postman to send post requests on the endpoint `http://localhost:8000/api/v1/risk-score`. I have attached the postman collection used here. Open Postman and click on import on the top left corner and attach this file.
- Alternatively we can use bash commands to do the same but I'm more familiar with Postman.
  Example bash command : curl -X POST http://localhost:8000/api/v1/risk-score \
                          -H "Authorization: Bearer supersecrettoken123" \
                          -H "Content-Type: application/json" \
                          -d '{
                          "purpose": "marketing",
                          "data_sensitivity": "high",
                          "region": "EU",
                          "processor_name": "UnknownVendor"
                          }'
## Example usage![Screenshot 2025-06-26 174148](https://github.com/user-attachments/assets/b890939a-3fa8-4c2e-8fbf-5c2bd03e759b)

   - Using either postman or bash we send the JSON {"purpose": "marketing","data_sensitivity": "high","region": "EU","processor_name": "UnknownVendor"}
   - Expected response would be : {
    "risk_breakdown": {"EU + High Sensitivity": 30,"Marketing Purpose": 15,"Unknown Vendor": 20},"risk_score": 65}

## Design decisions
- Used Flask framework due to familiarity and relatively easier to dockerize or run locally
- Hardcoded business rules simulate real-world scenarios:
EU + High Sensitivity → +30
Unknown Processor → +20
Marketing Purpose → +15
Score is capped at 100
- Containerized the app to make it cloud ready and to be able to run on different systems locally without any version conflicts.
