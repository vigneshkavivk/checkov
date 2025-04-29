from checkov.kubernetes.checks.resource.base_resource_check import BaseResourceCheck
from checkov.kubernetes.models import KubernetesResource

class CKV_K8S_CUSTOM_001(BaseResourceCheck):
    def __init__(self):
        # Define the name, ID, and categories for your custom check
        name = "Ensure XYZ policy is enforced"
        id = "CKV_K8S_CUSTOM_001"
        supported_resources = ["Pod", "Deployment"]  # Specify the Kubernetes resources you're targeting
        categories = ["KUBERNETES"]  # Add categories that make sense for your policy

        # Call the superclass constructor to initialize the check
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan(self, resource: KubernetesResource) -> bool:
        """
        Custom logic for your policy check.
        Example: Check if a label exists on a Pod or Deployment.
        """
        # Fetch the metadata and labels from the resource
        labels = resource.get("metadata", {}).get("labels", {})
        
        # Check if the label 'xyz-label' exists in the resource
        if "xyz-label" not in labels:
            return False  # The resource fails the check if the label is missing
        
        return True  # The resource passes the check if the label exists
