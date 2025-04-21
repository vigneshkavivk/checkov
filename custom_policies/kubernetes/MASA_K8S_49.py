from checkov.kubernetes.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckCategories, CheckResult

class SecretsInConfigMap(BaseResourceCheck):
    def __init__(self):
        name = "Ensure secrets are not exposed in ConfigMaps"
        id = "CKV_K8S_49"
        supported_resources = ["ConfigMap"]
        categories = [CheckCategories.SECRETS]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        for key in conf.get("data", {}):
            if "secret" in key.lower():
                return CheckResult.FAILED
        return CheckResult.PASSED

check = SecretsInConfigMap()
