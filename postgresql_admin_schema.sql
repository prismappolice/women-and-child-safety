-- PostgreSQL Schema for Admin Database
-- Database: admin_db

DROP TABLE IF EXISTS admin_security CASCADE;
DROP TABLE IF EXISTS admin_security_questions CASCADE;
DROP TABLE IF EXISTS admin_credentials CASCADE;

-- Create admin credentials table
CREATE TABLE admin_credentials (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create admin security questions table
CREATE TABLE admin_security_questions (
    id SERIAL PRIMARY KEY,
    admin_id INTEGER NOT NULL,
    question1 TEXT NOT NULL,
    answer1_hash TEXT NOT NULL,
    question2 TEXT NOT NULL,
    answer2_hash TEXT NOT NULL,
    question3 TEXT NOT NULL,
    answer3_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (admin_id) REFERENCES admin_credentials(id) ON DELETE CASCADE,
    UNIQUE(admin_id)
);

-- Create admin security table
CREATE TABLE admin_security (
    id SERIAL PRIMARY KEY,
    admin_id INTEGER NOT NULL,
    question1 TEXT NOT NULL,
    answer1_hash TEXT NOT NULL,
    question2 TEXT NOT NULL,
    answer2_hash TEXT NOT NULL,
    question3 TEXT NOT NULL,
    answer3_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create index
CREATE INDEX idx_admin_security_admin_id ON admin_security (admin_id);
