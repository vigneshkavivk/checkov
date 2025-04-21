class PrivilegedContainers(BaseResourceCheck):
    def __init__(self):
        name = "Ensure privileged containers are not allowed"
        id = "CKV_K8S_31"
        supported_resources = ["Pod", "Deployment"]
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        containers = conf.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
        for container in containers:
            security = container.get("securityContext", {})
            if security.get("privileged") is True:
                return CheckResult.FAILED
        return CheckResult.PASSED

check = PrivilegedContainers()
