CREATE TABLE m4j_quiz(
     qz_id INT(20) NOT NULL AUTO_INCREMENT,
     qz_subject VARCHAR(255) NOT NULL,
     qz_answer VARCHAR(255) NOT NULL,
     qz_analysis VARCHAR(255) NULL,
     qz_company VARCHAR(50) NULL,
     qz_category VARCHAR(50) NULL,
     qz_type TINYINT(4) NOT NULL DEFAULT 1,
     qz_hits INT(20),
     qz_year YEAR NULL,
     qz_create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (qz_id)
) ENGINE=InnoDB;


CREATE TABLE m4j_user(
     usr_id INT(20) NOT NULL AUTO_INCREMENT,
     usr_openid VARCHAR(255) NOT NULL,
     usr_create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     last_use_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     last_quiz_id INT(20) NULL,
     status VARCHAR(255) NULL,
     invite TINYINT(20) NULL,
     active_code VARCHAR(20) NULL,
     score INT(20) NULL,
     pass_quiz VARCHAR(255) NULL,
     location VARCHAR(255) NULL,
    PRIMARY KEY (usr_id),
    UNIQUE (usr_openid)
) ENGINE=InnoDB;

CREATE TABLE m4j_article(
    arti_id INT(20) NOT NULL AUTO_INCREMENT,
    arti_title VARCHAR(255) NOT NULL,
    arti_desc VARCHAR(1000) NULL, #need change type attribute
    arti_pic_url VARCHAR(255) NULL,
    arti_url VARCHAR(255) NULL,
    arti_category VARCHAR(255) NULL, #add to differentiate job chances & interview experience
    PRIMARY KEY (arti_id)
) ENGINE=InnoDB;

CREATE TABLE m4j_experience(
    exper_id INT(20) NOT NULL AUTO_INCREMENT,
    exper_title VARCHAR(255) NOT NULL,
    exper_author VARCHAR(255) NULL,
    exper_cover VARCHAR(255) NULL,
    exper_describe VARCHAR(1000) NULL,
    exper_content LONGTEXT NOT NULL,
    exper_create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (exper_id)
) ENGINE=InnoDB;


CREATE TABLE m4j_job(
    job_id INT(20) NOT NULL AUTO_INCREMENT,
    job_title VARCHAR(255) NOT NULL,
    job_area VARCHAR(100) NOT NULL,
    job_salary VARCHAR(100) NULL,
    job_years VARCHAR(100) NULL,
    job_academic VARCHAR(100) NULL,
    job_comments_1 VARCHAR(100) NULL,
    job_comments_2 VARCHAR(100) NULL,
    job_duty TEXT NOT NULL,
    job_postion_require TEXT NOT NULL,
    job_publish_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    job_attach_to INT(20),
    PRIMARY KEY (job_id),
    FOREIGN KEY (job_attach_to) REFERENCES m4j_company(cpany_id)
) ENGINE=InnoDB;


CREATE TABLE m4j_company(
    cpany_id INT(20) NOT NULL AUTO_INCREMENT,
    cpany_name VARCHAR(255) NOT NULL,
    cpany_introduce TEXT(255) NOT NULL,
    cpany_logo VARCHAR(255) NOT NULL,
    cpany_url VARCHAR(255) NOT NULL,
    PRIMARY KEY (cpany_id)
) ENGINE=InnoDB;



