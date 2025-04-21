from checkov.kubernetes.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckCategories, CheckResult

class SecretsInEnv(BaseResourceCheck):
    def __init__(self):
        name = "Ensure sensitive data is not stored in environment variables"
        id = "CKV_K8S_43"
        supported_resources = ["Deployment", "Pod"]
        categories = [CheckCategories.SECRETS]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        containers = conf.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
        for container in containers:
            env = container.get("env", [])
            for var in env:
                if "value" in var and "SECRET" in var.get("name", "").upper():
                    return CheckResult.FAILED
        return CheckResult.PASSED

check = SecretsInEnv()
