class NoLatestTag(BaseResourceCheck):
    def __init__(self):
        name = "Ensure container images do not use the 'latest' tag"
        id = "CKV_K8S_9995"
        supported_resources = ["Deployment", "Pod"]
        categories = [CheckCategories.SUPPLY_CHAIN]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        containers = conf.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
        for container in containers:
            image = container.get("image", "")
            if ":" not in image or image.endswith(":latest"):
                return CheckResult.FAILED
        return CheckResult.PASSED

check = NoLatestTag()
