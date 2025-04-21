class ReadOnlyRootFS(BaseResourceCheck):
    def __init__(self):
        name = "Ensure containers have read-only root file system"
        id = "CKV_K8S_29"
        supported_resources = ["Deployment", "Pod"]
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        containers = conf.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
        for container in containers:
            security = container.get("securityContext", {})
            if not security.get("readOnlyRootFilesystem"):
                return CheckResult.FAILED
        return CheckResult.PASSED

check = ReadOnlyRootFS()
