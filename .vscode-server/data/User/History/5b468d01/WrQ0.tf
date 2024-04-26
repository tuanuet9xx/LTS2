#provider "aws" {
#  region = "ap-southeast-1"
#}

#data "aws_ami" "ubuntu" {
#  most_recent = true

#  filter {
#    name   = "name"
#    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
#  }

#  owners = ["099720109477"] # Canonical Ubuntu AWS account id
#}

#resource "aws_instance" "hello" {
#  ami           = data.aws_ami.ubuntu.id # Change here, reference to result of data block instead of fix value
#  instance_type = "t2.micro"
#  tags = {
#    Name = "HelloWorldAAA"
#  }
#}



/*provider "aws" {
  region = "ap-southeast-1"
}


resource "aws_s3_bucket" "static" {
  bucket = "terraform-series-bai3"
  acl    = "public-read"
  policy = file("s3_static_policy.json")

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}

locals {
  mime_types = {
    html  = "text/html"
    css   = "text/css"
    ttf   = "font/ttf"
    woff  = "font/woff"
    woff2 = "font/woff2"
    js    = "application/javascript"
    map   = "application/javascript"
    json  = "application/json"
    jpg   = "image/jpeg"
    png   = "image/png"
    svg   = "image/svg+xml"
    eot   = "application/vnd.ms-fontobject"
  }
}

resource "aws_s3_bucket_object" "object" {
  for_each = fileset(path.module, "static-web/88/*")
  bucket = aws_s3_bucket.static.id
  key    = replace(each.value, "static-web", "")
  source = each.value
  etag         = filemd5("${each.value}")
  content_type = lookup(local.mime_types, split(".", each.value)[length(split(".", each.value)) - 1])
}*/

terraform {
  cloud {
    organization = "LTSorganization"

    workspaces {
      name = "testlab-remotebackend-second"
    }
  }
}

locals {
  project = "terraform-series"
}
provider "aws" {
  region = "ap-southeast-1"
}



module "networking" {
  source = "./modules/networking"

  project          = local.project
  vpc_cidr         = "10.0.0.0/16"
  private_subnets  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets   = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
  database_subnets = ["10.0.7.0/24", "10.0.8.0/24", "10.0.9.0/24"]
}

module "database" {
  source = "./modules/database"

  project = local.project
  vpc     = module.networking.vpc
  sg      = module.networking.sg
}

module "autoscaling" {
  source = "./modules/autoscaling"

  project   = local.project
  vpc       = module.networking.vpc
  sg        = module.networking.sg
  db_config = module.database.config
}



