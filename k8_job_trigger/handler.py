import boto3
import json
from kubernetes import client
import os

def get_k8s_token():
    # Create a Secrets Manager client
    session = boto3.session.Session()
    secrets_manager = session.client(service_name='secretsmanager', region_name='eu-west-2')
    secret = secrets_manager.get_secret_value(SecretId='aurora_token_100320242')
    return secret['SecretString']

def configure_k8s_client():
    configuration = client.Configuration()
    configuration.host = os.environ.get("K8S_API_ENDPOINT")
    configuration.verify_ssl = False 
    configuration.api_key['authorization'] = f"Bearer {get_k8s_token()}"
    
    client.Configuration.set_default(configuration)
    
def lambda_handler(event, context):
    # Configure the Kubernetes client
    configure_k8s_client()
    v1 = client.BatchV1Api()

    job = {
        "apiVersion": "batch/v1",
        "kind": "Job",
        "metadata": {
            "generateName": "aurora-intensity-processor-job-"
        },
        "spec": {
            "template": {
                "spec": {
                    "serviceAccountName": "aurora-s3-access",
                    "containers": [{
                        "name": "aurora-intensity-processor",
                        "image": "884329724388.dkr.ecr.eu-west-2.amazonaws.com/aurora-intensity-processor:latest",
                        "ports": [{"containerPort": 80}],
                        "env": [
                            {"name": "BUCKET_NAME", "value": "aurora-explorer-data"},
                            {"name": "PREFIX", "value": "aurora-data-raw/"}
                        ]
                    }],
                    "restartPolicy": "Never"
                }
            },
            "backoffLimit": 1
        }
    }

    # Create the job
    try:
        api_response = v1.create_namespaced_job(
            body=job,
            namespace="default"
        )
        
        print(f"Job created. Status='{api_response.status}'")

        return {
            'statusCode': 200,
            'body': json.dumps('Job submitted to Kubernetes')
        }
    except Exception as e:
        print(f"Exception when calling create_namespaced_job: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error submitting job to Kubernetes')
        }


if __name__ == "__main__":
    lambda_handler(None, None)
