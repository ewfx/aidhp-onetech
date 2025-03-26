from fastapi import FastAPI

app = FastAPI()

@app.get("/recommendation")
def get_recommendation(customer_profile: str):
    recommendation = generate_product_recommendation(customer_profile)
    return {"recommendation": recommendation}

# To run: uvicorn app:app --reload
