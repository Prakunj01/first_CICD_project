# import os

# # Define folder structure
# structure = [
#     "assets/css",
#     "assets/js",
#     "assets/images"
# ]

# # Define files to create
# files = {
#     "assets/css/style.css": "/* Main CSS file */\n",
#     "assets/js/app.js": "// Main JS file\n"
# }

# # Create folders
# for path in structure:
#     os.makedirs(path, exist_ok=True)
#     print(f"Created folder: {path}")

# # Create files
# for filepath, content in files.items():
#     with open(filepath, "w") as f:
#         f.write(content)
#     print(f"Created file: {filepath}")

# print("\nProject structure created successfully!")



# step 1: Import the os module to interact with the operating system

# import os

# # Base project folder
# base_folder = "aws-terraform-starter"

# # Files to create with optional starter content
# files = {
#     "main.tf": '# main Terraform configuration\n',
#     "provider.tf": '''provider "aws" {
#   region = var.region
# }
# ''',
#     "variables.tf": '''variable "region" {
#   description = "AWS region"
#   type        = string
#   default     = "ap-south-1"
# }
# ''',
#     "outputs.tf": '''# Example output
# output "example_output" {
#   value = "Terraform Starter"
# }
# ''',
#     "terraform.tfvars": '''region = "ap-south-1"
# '''
# }

# # Create base folder
# os.makedirs(base_folder, exist_ok=True)

# # Create each file inside folder
# for filename, content in files.items():
#     filepath = os.path.join(base_folder, filename)
#     with open(filepath, "w") as f:
#         f.write(content)
#     print(f"Created: {filepath}")

# print("\nTerraform project structure created successfully!")



# ----------------------------------------------
# import os

# # Base folder
# base_folder = "eks-network"

# # Files and their content
# files = {
#     "main.tf": '''# EKS Network (VPC, Subnets, IGW, Routes)

# module "vpc" {
#   source  = "terraform-aws-modules/vpc/aws"
#   version = "5.0.0"

#   name = var.vpc_name
#   cidr = var.vpc_cidr

#   azs             = var.azs
#   private_subnets = var.private_subnets
#   public_subnets  = var.public_subnets

#   enable_nat_gateway = true
#   single_nat_gateway = true

#   tags = var.tags
# }
# ''',

#     "variables.tf": '''variable "vpc_name" {
#   type        = string
#   description = "Name of the VPC"
#   default     = "eks-vpc"
# }

# variable "vpc_cidr" {
#   type        = string
#   description = "VPC CIDR block"
#   default     = "10.0.0.0/16"
# }

# variable "azs" {
#   type        = list(string)
#   description = "Availability Zones"
# }

# variable "private_subnets" {
#   type        = list(string)
#   description = "Private subnets"
# }

# variable "public_subnets" {
#   type        = list(string)
#   description = "Public subnets"
# }

# variable "tags" {
#   type        = map(string)
#   default     = {
#     Environment = "dev"
#     Project     = "eks"
#   }
# }
# ''',

#     "outputs.tf": '''output "vpc_id" {
#   value       = module.vpc.vpc_id
#   description = "ID of the VPC"
# }

# output "private_subnets" {
#   value       = module.vpc.private_subnets
#   description = "Private subnets"
# }

# output "public_subnets" {
#   value       = module.vpc.public_subnets
#   description = "Public subnets"
# }
# '''
# }

# # Create base folder
# os.makedirs(base_folder, exist_ok=True)

# # Create files with content
# for filename, content in files.items():
#     filepath = os.path.join(base_folder, filename)
#     with open(filepath, "w") as f:
#         f.write(content)
#     print(f"Created: {filepath}")

# print("\nEKS Network module structure created successfully!")


# step 7------------------------------------------
import os

# Base folder
base_folder = "eks-terraform"

# All files to create (blank)
files = [
    "main.tf",
    "provider.tf",
    "variables.tf",
    "outputs.tf",
    "terraform.tfvars",
    "vpc.tf"   # optional file
]

# Create base folder
os.makedirs(base_folder, exist_ok=True)

# Create each blank file
for filename in files:
    filepath = os.path.join(base_folder, filename)
    open(filepath, "w").close()
    print(f"Created blank file: {filepath}")

print("\nBlank EKS Terraform project structure created successfully!")
