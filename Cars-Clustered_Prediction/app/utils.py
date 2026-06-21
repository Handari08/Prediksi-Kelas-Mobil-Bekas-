def preprocess_input(data, scaler):
    """
    Convert request JSON -> format model
    """

    try:
        features = [
            float(data["model_year"]),
            float(data["milage"]),
            float(data["horsepower"]),
            float(data["engine_size"]),
            float(data["price"])
        ]

        scaled = scaler.transform([features])
        return scaled

    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")