from checkov.kubernetes.checks.base_check import BaseK8Check
from checkov.kubernetes.models import KubernetesResource
from checkov.kubernetes.parsers import parse

class CKV_K8S_CUSTOM_001(BaseK8Check):
    def __init__(self):
        name = "Ensure XYZ policy is enforced"
        id = "CKV_K8S_CUSTOM_001"
        supported_resources = ["Pod", "Deployment"]  # Update with the relevant resources you want to check
        categories = ["KUBERNETES"]

        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan(self, resource: KubernetesResource) -> bool:
        # Custom logic to check the resource
        # For example, checking if a label exists on a Pod or Deployment
        labels = resource.get("metadata", {}).get("labels", {})
        if "xyz-label" not in labels:
            return False  # The resource does not pass the check
        return True  # The resource passes the check

