from checkov.kubernetes.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckCategories, CheckResult

class RunAsNonRoot(BaseResourceCheck):
    def __init__(self):
        name = "Ensure containers do not run as root (runAsNonRoot=true)"
        id = "MASA_K8S_22"
        supported_resources = ["Pod", "Deployment"]
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        spec = conf.get("spec", {}).get("template", {}).get("spec", {})
        security_context = spec.get("securityContext", {})
        if security_context.get("runAsNonRoot") is not True:
            return CheckResult.FAILED
        return CheckResult.PASSED

check = RunAsNonRoot()
