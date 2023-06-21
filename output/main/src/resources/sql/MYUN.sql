/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     18/05/2023 11:20:36 a. m.                    */
/*==============================================================*/


drop table if exists EVENTO;

drop table if exists GRUPO;

drop table if exists MENSAJE;

drop table if exists MIEMBRO_GRUPO_;

drop table if exists USUARIO;

/*==============================================================*/
/* Table: EVENTO                                                */
/*==============================================================*/
create table EVENTO
(
   ID_EVENTO            int not null auto_increment,
   ID_GRUPO             int not null,
   CORREO_USUARIO       varchar(60) not null,
   NOMBRE_EVENTO        varchar(30) not null,
   FECHA_HORA_EVENTO    datetime not null,
   APROBADO             bool not null,
   primary key (ID_EVENTO, ID_GRUPO)
);

/*==============================================================*/
/* Table: GRUPO                                                 */
/*==============================================================*/
create table GRUPO
(
   ID_GRUPO             int not null auto_increment,
   NOMBRE_GRUPO         varchar(30) not null,
   ESTADO_GRUPO         bool not null,
   DESCRIPCION_GRUPO    text not null,
   primary key (ID_GRUPO)
);

/*==============================================================*/
/* Table: MENSAJE                                               */
/*==============================================================*/
create table MENSAJE
(
   ID_MENSAJE           int not null auto_increment,
   ID_GRUPO             int not null,
   CORREO_USUARIO       varchar(60) not null,
   TEXTO_MENSAJE        text not null,
   FECHA_HORA_MENSAJE   datetime not null,
   primary key (ID_MENSAJE, ID_GRUPO, CORREO_USUARIO)
);

/*==============================================================*/
/* Table: MIEMBRO_GRUPO_                                        */
/*==============================================================*/
create table MIEMBRO_GRUPO_
(
   ID_GRUPO             int not null,
   CORREO_USUARIO       varchar(60) not null,
   DENTROGRUPO          bool not null,
   CREADOR_GRUPO        bool not null,
   ADMIN_GRUPO          bool not null,
   primary key (ID_GRUPO, CORREO_USUARIO)
);

/*==============================================================*/
/* Table: USUARIO                                               */
/*==============================================================*/
create table USUARIO
(
   CORREO_USUARIO       varchar(60) not null,
   NOMBRE_USUARIO       varchar(30) not null,
   APELLIDO_USUARIO     varchar(30) not null,
   CONTRASENA_USUARIO   varchar(162) not null,
   FECHANACIMIENTO_USUARIO date not null,
   FECHAREGISTRO_USUARIO datetime not null,
   primary key (CORREO_USUARIO)
);

alter table EVENTO add constraint FK_ORGANIZA foreign key (ID_GRUPO, CORREO_USUARIO)
      references MIEMBRO_GRUPO_ (ID_GRUPO, CORREO_USUARIO) on delete restrict on update restrict;

alter table EVENTO add constraint FK_ORGANIZA2 foreign key (ID_GRUPO)
      references GRUPO (ID_GRUPO) on delete restrict on update restrict;

alter table MENSAJE add constraint FK_EL_USUARIO_ESCRIBIO foreign key (ID_GRUPO, CORREO_USUARIO)
      references MIEMBRO_GRUPO_ (ID_GRUPO, CORREO_USUARIO) on delete restrict on update restrict;

alter table MIEMBRO_GRUPO_ add constraint FK_MIEMBRO_GRUPO2 foreign key (CORREO_USUARIO)
      references USUARIO (CORREO_USUARIO) on delete restrict on update restrict;

alter table MIEMBRO_GRUPO_ add constraint FK_MIEMBRO_GRUPO_ foreign key (ID_GRUPO)
      references GRUPO (ID_GRUPO) on delete restrict on update restrict;

