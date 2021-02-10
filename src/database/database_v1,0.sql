CREATE DATABASE secom;

USE secom; 

CREATE TABLE user(
    user_id INT(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(20) NOT NULL,
    pswd VARCHAR(60) NOT NULL,
    hint VARCHAR(30) NOT NULL,
    user_type INT(2) NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    second_name VARCHAR(30),
    f_last_name VARCHAR(30) NOT NULL,
    m_last_name VARCHAR(30) NOT NULL
);

CREATE TABLE item(
    item_id INT(5) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    unit VARCHAR(20), 
    category VARCHAR(20)
);

CREATE TABLE warehouse(
    wh_id INT(5) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    wh_descripion VARCHAR(20),
    addr VARCHAR(20)
);

CREATE TABLE transaction_type(
    transaction_id INT(5) PRIMARY KEY NOT NULL,
    code VARCHAR(10),
    trans_description VARCHAR(30)
);

CREATE TABLE kardex(
    trans_id INT(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ware_id_kardex INT(5),
    FOREIGN KEY (ware_id_kardex) REFERENCES warehouse(wh_id),
    item_id_kardex INT(5),
    FOREIGN KEY (item_id_kardex) REFERENCES item(item_id),
    quantity INT(5),
    trans_time DATE,
    user_id_kardex INT(10),
    FOREIGN KEY (user_id_kardex) REFERENCES user(user_id)

);
CREATE TABLE bom(
      bom_id INT(5) NOT NULL PRIMARY KEY AUTO_INCREMENT,
      project_id_bom INT(5) NOT NULL,
      item_id_bom INT(5) NOT NULL,
      quantity INT(5) NOT NULL,
      user_id_bom INT(10) NOT NULL, 
      FOREIGN KEY (project_id_bom) REFERENCES project(project_id),
      FOREIGN KEY (item_id_bom) REFERENCES item(item_id),
      FOREIGN KEY (user_id_bom) REFERENCES user(user_id)
);

CREATE TABLE project(
    project_id INT(5) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    prj_name VARCHAR(10) NOT NULL,
    recipient VARCHAR(20) NOT NULL,
    begin_date DATE,
    finish_date DATE,
    curr_state VARCHAR(10) NOT NULL,
    addr VARCHAR(70) NOT NULL
);

CREATE TABLE stock(
    item_id INT(5) NOT NULL,
    wh_id INT(5) NOT NULL,
    quantity_physical INT NOT NULL,
    quantity_backorder INT NOT NULL,
    quantity_reserved INT NOT NULL,
    FOREIGN KEY(item_id) REFERENCES item(item_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(wh_id) REFERENCES warehouse(wh_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    PRIMARY KEY(item_id,wh_id,quantity_physical,quantity_backorder,quantity_reserved)
);
