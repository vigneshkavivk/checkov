module "vpc" {
  source   = "./modules/vpc"
  vpc_cidr = "10.0.0.0/16"
  vpc_name = "MyVPC"
}

module "subnet" {
  source             = "./modules/subnet"
  vpc_id             = module.vpc.vpc_id
  public_subnet_cidr = "10.0.1.0/24"
  availability_zone  = "us-east-1a"
}

module "igw" {
  source = "./modules/igw"
  vpc_id = module.vpc.vpc_id
}

module "nat" {
  source          = "./modules/nat"
  public_subnet_id = module.subnet.public_subnet_id
}

module "route" {
  source = "./modules/route"
  vpc_id = module.vpc.vpc_id
  igw_id = module.igw.igw_id
}

