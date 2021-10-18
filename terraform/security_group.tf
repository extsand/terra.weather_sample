resource "aws_security_group" "sg_academy_docker" {

	dynamic "ingress" {
		for_each = ["80","27017"]
		content {
			from_port = ingress.value
			to_port = ingress.value
			protocol = "tcp"
			cidr_blocks = ["0.0.0.0/0"]
		}
	}

	ingress {
		description = "ssh"
		from_port = 22
		to_port = 22
		protocol = "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}
 
 	egress {
		from_port = 0
		to_port = 0
		protocol = -1
		cidr_blocks = ["0.0.0.0/0"]
	}

	tags = {
		Name = "Academy Docker Security Group"
	}
	
}

