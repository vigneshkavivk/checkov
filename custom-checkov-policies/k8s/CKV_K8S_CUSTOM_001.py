from checkov.kubernetes.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckCategories

class CKV_K8S_CUSTOM_001(BaseResourceCheck):
    def __init__(self):
        name = "Ensure 'xyz-label' label is present in metadata"
        id = "CKV_K8S_CUSTOM_001"
        supported_resources = ["Pod", "Deployment"]
        categories = [CheckCategories.KUBERNETES]

        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        """
        Custom logic to validate if 'xyz-label' exists in metadata.labels.
        """
        metadata = conf.get("metadata")
        if metadata:
            labels = metadata.get("labels", {})
            if labels and "xyz-label" in labels:
                return True  # Passes check
        return False  # Fails check
