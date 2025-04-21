class DropCapabilities(BaseResourceCheck):
    def __init__(self):
        name = "Ensure capabilities are minimized"
        id = "CKV_K8S_40"
        supported_resources = ["Pod", "Deployment"]
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        containers = conf.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
        for container in containers:
            capabilities = container.get("securityContext", {}).get("capabilities", {})
            if "drop" not in capabilities or "ALL" not in capabilities.get("drop", []):
                return CheckResult.FAILED
        return CheckResult.PASSED

check = DropCapabilities()
