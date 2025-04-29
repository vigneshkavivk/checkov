from checkov.kubernetes.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckCategories, CheckResult

class ExampleCustomCheck(BaseResourceCheck):
    def __init__(self):
        name = "Ensure containers have resource limits"
        id = "CKV_K8S_CUSTOM_001"
        supported_resources = ["Pod", "Deployment", "StatefulSet"]
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        # your logic here
        return CheckResult.PASSED
