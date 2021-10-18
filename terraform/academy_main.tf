provider "aws" {
	region = "eu-central-1"
	
}

resource "aws_instance" "app_server" {
	ami = "ami-05f7491af5eef733a"
	instance_type = "t2.micro"
	 tags = {
    # create visual name
    Name      = "APP Academy Docker Server"
    "project" = "Academy DevOps"
  }

	vpc_security_group_ids = [aws_security_group.sg_academy_docker.id]
	user_data = file("./user_data/install_docker.sh")
	key_name = aws_key_pair.aws_ssh_academy_docker.key_name

}

resource "aws_instance" "db_server" {
	ami = "ami-05f7491af5eef733a"
	instance_type = "t2.micro"
	 tags = {
    # create visual name
    Name      = "DB Academy Docker Server"
    "project" = "Academy DevOps"
  }

	vpc_security_group_ids = [aws_security_group.sg_academy_docker.id]
	user_data = file("./user_data/install_docker.sh")
	key_name = aws_key_pair.aws_ssh_academy_docker.key_name
	
}


