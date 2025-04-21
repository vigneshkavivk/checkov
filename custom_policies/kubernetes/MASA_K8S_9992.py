class LoggingSidecarCheck(BaseResourceCheck):
    def __init__(self):
        name = "Ensure at least one sidecar container is used for logging"
        id = "CKV_K8S_9992"
        supported_resources = ["Pod", "Deployment"]
        categories = [CheckCategories.LOGGING]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        containers = conf.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
        sidecars = [c for c in containers if 'log' in c.get("name", "").lower()]
        if not sidecars:
            return CheckResult.FAILED
        return CheckResult.PASSED

check = LoggingSidecarCheck()
