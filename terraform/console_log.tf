#Output information
#for observation
output "DB_webserver_instance_id" {
	value = aws_instance.db_server.id
}
output "APP_webserver_instance_id" {
	value = aws_instance.app_server.id
}


#Public IP (fluid)
output "DB_webserver_public_ip_adress" {
	value = aws_instance.db_server.public_ip
}
output "APP_webserver_public_ip_adress" {
	value = aws_instance.app_server.public_ip
}


#Security group
output "webserver_sg_id" {
	value = aws_security_group.sg_academy_docker.id
}


#Statik IP
output "static_ip-DB-server" {
	value = aws_eip.db_server_academy_static_ip.public_ip
}
output "static_ip-APP-server" {
	value = aws_eip.app_server_academy_static_ip.public_ip
}
