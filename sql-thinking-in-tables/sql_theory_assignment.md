# SQL Theory Assignment
## Understanding Relational Databases in AI Systems

---

## 1. Importance of Databases in Real-World AI Systems

Databases play a crucial role in real-world AI systems because AI models require large amounts of data for training, analysis, and decision-making. A database helps store, manage, and retrieve structured data efficiently.

In AI systems, databases may store different types of data such as:

- User information
- Transaction data
- Sensor data
- Image or text metadata
- Model predictions
- Training datasets

For example, a recommendation system used by an e-commerce platform stores user purchase history, product details, and browsing behavior in a database. AI models use this data to recommend products to users.

Structured storage is necessary because it ensures that data is organized, consistent, and easy to query. Without structured databases, managing large-scale AI data would become extremely difficult.

---

## 2. Relational Database Mental Model

A relational database organizes data in the form of tables. Each table represents a specific entity.

Key components include:

- **Table**: Represents an entity such as Users or Orders.
- **Row**: Represents a single record in a table.
- **Column**: Represents attributes or properties of the entity.

Example:

Users Table

| User_ID | Name | Email |
|--------|------|------|
| 1 | Alice | alice@email.com |
| 2 | Bob | bob@email.com |

In this table:
- Each row represents a user.
- Each column represents user information.

Each table should represent a **single entity** to keep the data organized and avoid redundancy.

---

## 3. Primary Key

A primary key is a column that uniquely identifies each record in a table.

Characteristics of a primary key:

- It must be **unique** for every row.
- It cannot contain **NULL values**.
- It ensures that every record can be uniquely identified.

Example:

Students Table

| Student_ID | Name | Age |
|-----------|------|-----|
| 1 | Aman | 21 |
| 2 | Riya | 22 |

Here, **Student_ID** is the primary key because it uniquely identifies each student.

Primary keys help maintain data integrity and allow efficient querying of records.

---

## 4. Database Schema

A database schema defines the structure of a database. It describes how the data is organized.

A schema typically defines:

- Table names
- Column names
- Data types
- Primary keys
- Relationships between tables

Example schema:

Users Table

| Column | Type |
|------|------|
| User_ID | INT |
| Name | TEXT |
| Email | TEXT |

Schemas are important because they maintain consistency and ensure that the database follows a predefined structure. This helps developers and AI systems interact with the data reliably.

---

## 5. Relationships Between Tables

In relational databases, tables are connected through relationships. These relationships are established using **foreign keys**.

A foreign key is a column in one table that refers to the primary key of another table.

Example:

Users Table

| User_ID | Name |
|--------|------|
| 1 | Alice |
| 2 | Bob |

Orders Table

| Order_ID | User_ID | Product |
|---------|--------|--------|
| 101 | 1 | Laptop |
| 102 | 2 | Phone |

In this example:
- **User_ID in Orders** is a foreign key.
- It references **User_ID in Users** table.

This relationship allows us to connect users with their orders.

Relational connections help AI systems analyze linked data such as user activity, purchases, and recommendations.