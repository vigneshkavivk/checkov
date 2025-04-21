from checkov.kubernetes.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckCategories, CheckResult

class ProbesConfigured(BaseResourceCheck):
    def __init__(self):
        name = "Ensure liveness and readiness probes are configured for containers"
        id = "CKV_K8S_9991"
        supported_resources = ["Deployment", "Pod"]
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        containers = conf.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
        for container in containers:
            if not container.get("livenessProbe") or not container.get("readinessProbe"):
                return CheckResult.FAILED
        return CheckResult.PASSED

check = ProbesConfigured()
