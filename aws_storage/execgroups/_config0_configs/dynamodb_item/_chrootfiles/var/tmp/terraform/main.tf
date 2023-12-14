variable "aws_default_region" { default = "eu-west-1" }

variable "item_hash" { default = "eyJidWlsZF9pbWFnZSI6IHsiUyI6ICJhd3MvY29kZWJ1aWxkL3N0YW5kYXJkOjUuMCJ9LCAidHJpZ2dlcl9pZCI6IHsiUyI6ICIxMjM0NTYifSwgImRvY2tlcl9yZXBvX25hbWUiOiB7IlMiOiAiZmxhc2tfc2FtcGxlIn0sICJnaXRfdXJsIjogeyJTIjogImdpdEBnaXRodWIuY29tOmpvZWJsb3cvZmxhc2tfc2FtcGxlLXByaXZhdGUuZ2l0In0sICJnaXRfcmVwbyI6IHsiUyI6ICJmbGFzay1zYW1wbGUtcHJpdmF0ZSJ9LCAiYXdzX2RlZmF1bHRfcmVnaW9uIjogeyJTIjogImV1LXdlc3QtMSJ9LCAiX2lkIjogeyJTIjogIjEyMzQ1NiJ9LCAiaW1hZ2VfdHlwZSI6IHsiUyI6ICJMSU5VWF9DT05UQUlORVIifSwgImNvbXB1dGVfdHlwZSI6IHsiUyI6ICJCVUlMRF9HRU5FUkFMMV9TTUFMTCJ9LCAiYnVpbGRfdGltZW91dCI6IHsiUyI6ICI1In0sICJwcml2aWxlZ2VkX21vZGUiOiB7IlMiOiAidHJ1ZSJ9LCAic2VjcmV0IjogeyJTIjogInNlY3JldDEyMyJ9LCAiYnJhbmNoIjogeyJTIjogIm1hc3RlciJ9LCAiZG9ja2VyX3JlZ2lzdHJ5IjogeyJTIjogIm51bGwifSwgImNvZGVidWlsZF9uYW1lIjogeyJTIjogImZsYXNrLXNhbXBsZS1wcml2YXRlIn19" }

variable "table_name" { default = "codebuild-shared-config0-eval-settings" }
variable "hash_key" { default = "_id" }

variable "cloud_tags" {
  description = "additional tags as a map"
  type        = map(string)
  default     = {}
}

resource "aws_dynamodb_table_item" "example" {
  table_name = var.table_name
  hash_key = var.hash_key
  item     = base64decode(var.item_hash)
}
