# Reference: Terraform Registry. (n.d.-b). https:/registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster

provider "google" {
  credentials = file(var.gcp_credentials)
  project = var.gcp_project_id
  region = var.gcp_region
}

resource "google_container_cluster" "cluster" {
  name               = var.gke_cluster_name
  location           = var.gcp_zones[0]
  initial_node_count = 1

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 10
    disk_type    = "pd-standard"
    image_type   = "COS_CONTAINERD"
  }
}
