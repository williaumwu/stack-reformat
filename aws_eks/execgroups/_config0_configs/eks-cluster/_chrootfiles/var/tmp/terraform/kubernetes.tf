# kubernetes

data "aws_eks_cluster" "eks" {
  name = aws_eks_cluster.this.id
}

data "aws_eks_cluster_auth" "eks" {
  name = aws_eks_cluster.this.id
}

provider "kubernetes" {
  host                   = data.aws_eks_cluster.eks.endpoint
  cluster_ca_certificate = base64decode(data.aws_eks_cluster.eks.certificate_authority[0].data)
  token                  = data.aws_eks_cluster_auth.eks.token
}
