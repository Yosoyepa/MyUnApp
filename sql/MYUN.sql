/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     1/05/2023 8:36:50 p. m.                      */
/*==============================================================*/

drop database if exists myundb;

create database myundb;

use myundb;
drop table if exists ADMINISTRADOR_GRUPO;

drop table if exists EVENTO;

drop table if exists EVENTO_APROBADO;

drop table if exists GRUPO;

drop table if exists MIEMBRO_GRUPO_;

drop table if exists USUARIO;

/*==============================================================*/
/* Table: ADMINISTRADOR_GRUPO                                   */
/*==============================================================*/
create table ADMINISTRADOR_GRUPO
(
   ID_ADMINISTRADOR     int auto_increment not null,
   ID_GRUPO             int not null,
   ID_USUARIO           int not null,
   CREADOR_GRUPO        bool not null,
   primary key (ID_ADMINISTRADOR)
);

/*==============================================================*/
/* Table: EVENTO                                                */
/*==============================================================*/
create table EVENTO
(
   ID_EVENTO            int auto_increment not null,
   ID_GRUPO             int not null,
   ID_USUARIO           int not null,
   NOMBRE_EVENTO        varchar(30) not null,
   FECHA_HORA_EVENTO    datetime not null,
   primary key (ID_EVENTO)
);

/*==============================================================*/
/* Table: EVENTO_APROBADO                                       */
/*==============================================================*/
create table EVENTO_APROBADO
(
   ID_EVENTO            int not null,
   ID_ADMINISTRADOR     int not null,
   APROBADO_EVENTO      bool not null,
   primary key (ID_EVENTO, ID_ADMINISTRADOR)
);

/*==============================================================*/
/* Table: GRUPO                                                 */
/*==============================================================*/
create table GRUPO
(
   ID_GRUPO             int auto_increment not null,
   NOMBRE_GRUPO         varchar(30) not null,
   TIPO_GRUPO           bool not null,
   DESCRIPCION_GRUPO    text not null,
   primary key (ID_GRUPO)
);

/*==============================================================*/
/* Table: MIEMBRO_GRUPO_                                        */
/*==============================================================*/
create table MIEMBRO_GRUPO_
(
   ID_GRUPO             int not null,
   ID_USUARIO           int not null,
   DENTROGRUPO          bool not null,
   primary key (ID_GRUPO, ID_USUARIO)
);

/*==============================================================*/
/* Table: USUARIO                                               */
/*==============================================================*/
create table USUARIO
(
   ID_USUARIO           int auto_increment not null,
   NOMBRE_USUARIO       varchar(30) not null,
   CORREO_USUARIO       varchar(30) not null,
   CONTRASENA_USUARIO   varchar(30) not null,
   FECHANACIMIENTO_USUARIO date not null,
   FECHAREGISTRO_USUARIO datetime not null,
   primary key (ID_USUARIO)
);

alter table ADMINISTRADOR_GRUPO add constraint FK_ES_UN_USUARIO foreign key (ID_GRUPO, ID_USUARIO)
      references MIEMBRO_GRUPO_ (ID_GRUPO, ID_USUARIO) on delete restrict on update restrict;

alter table EVENTO add constraint FK_ORGANIZA foreign key (ID_GRUPO, ID_USUARIO)
      references MIEMBRO_GRUPO_ (ID_GRUPO, ID_USUARIO) on delete restrict on update restrict;

alter table EVENTO_APROBADO add constraint FK_APRUEBA foreign key (ID_ADMINISTRADOR)
      references ADMINISTRADOR_GRUPO (ID_ADMINISTRADOR) on delete restrict on update restrict;

alter table EVENTO_APROBADO add constraint FK_ES_APROBADO foreign key (ID_EVENTO)
      references EVENTO (ID_EVENTO) on delete restrict on update restrict;

alter table MIEMBRO_GRUPO_ add constraint FK_MIEMBRO_GRUPO2 foreign key (ID_USUARIO)
      references USUARIO (ID_USUARIO) on delete restrict on update restrict;

alter table MIEMBRO_GRUPO_ add constraint FK_MIEMBRO_GRUPO_ foreign key (ID_GRUPO)
      references GRUPO (ID_GRUPO) on delete restrict on update restrict;

