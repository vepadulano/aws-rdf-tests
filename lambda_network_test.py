import boto3
import json
import random

def dostuff():
    lambda_client = boto3.client("lambda", region_name="us-east-1")

    response = lambda_client.invoke(
        FunctionName="lambda_network_test",
        Payload=json.dumps({"bogus": random.random()}),
    )

    result = response["Payload"].read().decode("utf-8").strip('"').split(",")
    result = [float(value) for value in result]
    print(type(result))
    print(type(result[0]))
    print(result)


if __name__ == "__main__":
    dostuff()
