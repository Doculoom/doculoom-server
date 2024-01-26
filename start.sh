#!/bin/bash

#https://gist.github.com/juancsr/5927e6660d6ba5d2a34c61802d26e50a

# Define a custom tag for your Docker image
IMAGE_TAG="custom-tag"  # Replace 'custom-tag' with your desired tag

# Check if the tag is empty and provide a default one if it is
if [ -z "$IMAGE_TAG" ]; then
    echo "No custom tag provided. Using default 'latest'."
    IMAGE_TAG="latest"
fi

# Start Minikube
minikube start

# Set Docker environment to Minikube's Docker daemon
eval $(minikube docker-env)

# Navigate to your project directory (if necessary)
# cd path/to/your/project

# Build the Docker image
docker build -t doculoom:tag .

# Create the Kubernetes deployment (delete the old one if it exists)
kubectl get deployment doculoom && kubectl delete deployment doculoom
kubectl create deployment doculoom --image=doculoom:tag

# Expose the deployment as a NodePort service
kubectl expose deployment doculoom --type=NodePort --port=6666

# Wait for the deployment to be ready
echo "Waiting for deployment to be ready..."
kubectl rollout status deployment/doculoom

# Get the pod name
POD_NAME=$(kubectl get pod -l app=doculoom -o jsonpath="{.items[0].metadata.name}")

# Set up port forwarding
echo "Setting up port forwarding to pod $POD_NAME..."
kubectl port-forward pod/$POD_NAME 30322:6666 &

echo "Port forwarding set up. You can now access the application at http://localhost:30322"

