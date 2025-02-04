terraform {
  backend "s3" {
    bucket         = "my-terraform-ssstate-bucket"
    key            = "terraform/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
  }
}

