variable "gcp_credentials" {
  type = string
  description = "Location of service account for GCP"
}

variable "gcp_project_id" {
  type = string
  description = "GCP Project id"
}

variable "gcp_region" {
  type = string
  description = "GCP Region"
}

variable "gke_cluster_name" {
  type = string
  description = "GKE Cluster name"
}

variable "gcp_zones" {
  type = list(string)
  description = "List of zones for the cluster"
}
