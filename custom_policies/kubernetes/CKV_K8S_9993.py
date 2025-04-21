class ImagePullPolicyCheck(BaseResourceCheck):
    def __init__(self):
        name = "Ensure imagePullPolicy is set to 'Always'"
        id = "CKV_K8S_9993"
        supported_resources = ["Deployment", "Pod"]
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_resources)

    def scan_resource_conf(self, conf):
        containers = conf.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
        for container in containers:
            if container.get("imagePullPolicy") != "Always":
                return CheckResult.FAILED
        return CheckResult.PASSED

check = ImagePullPolicyCheck()
