import boto3
import json
from kubernetes import client, config

def lambda_handler(event, context):
    # Load Kubernetes config (for example, from a secret or environment variable)
    config.load_kube_config(config_file='/path/to/kubeconfig')

    # Configure the Kubernetes client
    v1 = client.BatchV1Api()

    # Define the job manifest with generateName for unique job creation
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
    api_response = v1.create_namespaced_job(body=job, namespace="default")
    print(f"Job created. Status='{api_response.status}'")

    return {
        'statusCode': 200,
        'body': json.dumps('Job submitted to Kubernetes')
    }
