#Create SSH AWS_key_pair
resource "aws_key_pair" "aws_ssh_academy_docker" {
  key_name   = "aws_ssh_user"
  public_key = "${file("${path.module}/.credentials/.ssh/aws_ssh_user.pub")}"
}

