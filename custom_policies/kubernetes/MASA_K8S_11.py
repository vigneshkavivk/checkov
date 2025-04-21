class CPULimits(BaseResourceCheck):
    def __init__(self):
        name = "Ensure containers have CPU limits set"
        id = "MASA_K8S_11"
        supported_resources = ["Deployment", "Pod"]
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        containers = conf.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
        for container in containers:
            limits = container.get("resources", {}).get("limits", {})
            if not limits.get("cpu"):
                return CheckResult.FAILED
        return CheckResult.PASSED

check = CPULimits()
