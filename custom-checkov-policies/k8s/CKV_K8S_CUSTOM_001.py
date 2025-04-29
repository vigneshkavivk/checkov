from checkov.kubernetes.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckCategories, CheckResult


class NoDefaultNamespaceDefined(BaseResourceCheck):
    def __init__(self):
        name = "Ensure Kubernetes manifests explicitly define a namespace"
        id = "CKV_K8S_CUSTOM_001"
        supported_resources = ["*"]  # Apply to all K8s resource types
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_entity_conf(self, conf):
        metadata = conf.get("metadata")
        if metadata is None:
            return CheckResult.FAILED

        namespace = metadata.get("namespace")
        if not namespace:
            return CheckResult.FAILED
        return CheckResult.PASSED


check = NoDefaultNamespaceDefined()
