resource "aws_eip" "app_server_academy_static_ip" {
	instance = aws_instance.app_server.id
}

resource "aws_eip" "db_server_academy_static_ip" {
	instance = aws_instance.db_server.id
}


