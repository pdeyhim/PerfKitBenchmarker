import boto3

client = boto3.client('firehose',region_name="us-east-1")
for sample in range(0, 600):
    response = client.put_record(
        DeliveryStreamName="performance_fire",
        Record={
            'Data': str(sample)+"\n"
        }
    )
    print(response)

