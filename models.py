# ============== mysql draft =================
"""

CREATE TABLE blog_tbl (
    id int,
    title char(200) NOT NULL,
    text varchar(1000) NOT NULL,
    img_path varchar(255),
    created_by int NOT NULL,
    created_time TIMESTAMP NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (created_by) REFERENCES tbl_admins(id)
);

tbl_admins:
    id PK ,
    parten_id ,
    full_name ,
    access_level ,









"""

# ============== sqlite =================
"""


"""

# ============== sample for Create table =================
"""
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
"""