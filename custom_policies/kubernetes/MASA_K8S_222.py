class AvoidDefaultNamespace(BaseResourceCheck):
    def __init__(self):
        name = "Ensure resources are not deployed to the default namespace"
        id = "CKV_K8S_9994"
        supported_resources = ["Pod", "Deployment", "Service"]
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        metadata = conf.get("metadata", {})
        if metadata.get("namespace", "default") == "default":
            return CheckResult.FAILED
        return CheckResult.PASSED

check = AvoidDefaultNamespace()
