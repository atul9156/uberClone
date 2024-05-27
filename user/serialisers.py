from pydantic import BaseModel

class PassengerSerializer(BaseModel):
    type: str
    name: str
    email: str

    # TODO: Add validation methods on name and email

class CabSerializer(BaseModel):
    type: str
    cab_number: str
    cab_model: str
    latitude: int
    longitude: int

def validate_request(data: dict):
    model = None
    if data.get("type", "") == "passenger":
        model = PassengerSerializer
    elif data.get("type", "") == "user":
        model = CabSerializer
    else:
        raise NotImplementedError(f'Model for type {data.get("type", "")} is not implemnted')
    return model(**data)
