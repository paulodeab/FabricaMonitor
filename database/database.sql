create database if not exists db_hosts;

use db_hosts;

create table if not exists hosts(id integer primary key auto_increment,
								 ip varchar(40) not null,
                                 hostname varchar(100),
                                 mac_address varchar(20) not null,
                                 operating_system varchar(100) not null
								);
                                
create table if not exists port(id integer primary key auto_increment,
								port integer not null,
                                version varchar(100),
                                service varchar(100)not null,
                                hosts_id integer not null,
                                foreign key(hosts_id) references hosts(id));