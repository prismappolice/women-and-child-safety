-- PostgreSQL Schema Migration Script
-- Generated for Women and Child Safety Wing Project
-- Date: 2025-11-11

-- Database: women_safety
-- Drop tables if exist (for fresh installation)
DROP TABLE IF EXISTS email_notifications CASCADE;
DROP TABLE IF EXISTS volunteer_scores CASCADE;
DROP TABLE IF EXISTS volunteer_status CASCADE;
DROP TABLE IF EXISTS volunteers CASCADE;
DROP TABLE IF EXISTS district_sps CASCADE;
DROP TABLE IF EXISTS shakthi_teams CASCADE;
DROP TABLE IF EXISTS women_police_stations CASCADE;
DROP TABLE IF EXISTS one_stop_centers CASCADE;
DROP TABLE IF EXISTS districts CASCADE;
DROP TABLE IF EXISTS admin_settings CASCADE;
DROP TABLE IF EXISTS navigation_menu CASCADE;
DROP TABLE IF EXISTS contact_info CASCADE;
DROP TABLE IF EXISTS gallery_items CASCADE;
DROP TABLE IF EXISTS home_content CASCADE;
DROP TABLE IF EXISTS about_content CASCADE;
DROP TABLE IF EXISTS emergency_numbers CASCADE;
DROP TABLE IF EXISTS page_content CASCADE;
DROP TABLE IF EXISTS events CASCADE;
DROP TABLE IF EXISTS pdf_resources CASCADE;
DROP TABLE IF EXISTS initiatives CASCADE;
DROP TABLE IF EXISTS safety_tips CASCADE;
DROP TABLE IF EXISTS district_info CASCADE;
DROP TABLE IF EXISTS site_settings CASCADE;
DROP TABLE IF EXISTS success_stories CASCADE;
DROP TABLE IF EXISTS officers CASCADE;
DROP TABLE IF EXISTS media_gallery CASCADE;
DROP TABLE IF EXISTS content CASCADE;

-- Create content table
CREATE TABLE content (
    id SERIAL PRIMARY KEY,
    page_name TEXT NOT NULL,
    section_name TEXT NOT NULL,
    content_type TEXT NOT NULL,
    title TEXT,
    content TEXT,
    image_url TEXT,
    link_url TEXT,
    position_order INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create media_gallery table
CREATE TABLE media_gallery (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    file_path TEXT NOT NULL,
    file_type TEXT NOT NULL,
    category TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Create officers table
CREATE TABLE officers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    designation TEXT NOT NULL,
    department TEXT,
    phone TEXT,
    email TEXT,
    image_url TEXT,
    bio TEXT,
    position_order INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE
);

-- Create success_stories table
CREATE TABLE success_stories (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    story_content TEXT NOT NULL,
    image_url TEXT,
    location TEXT,
    date_occurred DATE,
    position_order INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    description TEXT,
    date TEXT,
    stat1_number TEXT,
    stat1_label TEXT,
    stat2_number TEXT,
    stat2_label TEXT,
    stat3_number TEXT,
    stat3_label TEXT,
    sort_order INTEGER DEFAULT 0
);

-- Create site_settings table
CREATE TABLE site_settings (
    id SERIAL PRIMARY KEY,
    setting_key TEXT UNIQUE NOT NULL,
    setting_value TEXT,
    setting_type TEXT DEFAULT 'text',
    description TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create district_info table
CREATE TABLE district_info (
    id SERIAL PRIMARY KEY,
    district_name TEXT NOT NULL,
    district_code TEXT NOT NULL,
    headquarters TEXT NOT NULL,
    women_police_stations TEXT,
    one_stop_centers TEXT,
    shakti_teams TEXT,
    emergency_contacts TEXT,
    latitude REAL,
    longitude REAL,
    population INTEGER,
    area_sq_km REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create safety_tips table
CREATE TABLE safety_tips (
    id SERIAL PRIMARY KEY,
    category TEXT NOT NULL,
    title TEXT NOT NULL,
    icon TEXT NOT NULL,
    tips TEXT NOT NULL,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create initiatives table
CREATE TABLE initiatives (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    image_url TEXT,
    is_featured INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create pdf_resources table
CREATE TABLE pdf_resources (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    icon TEXT DEFAULT 'fas fa-file-pdf',
    download_count INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create events table
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    event_date DATE,
    location TEXT,
    image_url TEXT,
    is_upcoming INTEGER DEFAULT 1,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create page_content table
CREATE TABLE page_content (
    id SERIAL PRIMARY KEY,
    page_name TEXT NOT NULL,
    section_name TEXT NOT NULL,
    content_type TEXT NOT NULL,
    content_value TEXT NOT NULL,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create emergency_numbers table
CREATE TABLE emergency_numbers (
    id SERIAL PRIMARY KEY,
    number TEXT NOT NULL,
    label TEXT NOT NULL,
    description TEXT,
    is_active INTEGER DEFAULT 1,
    sort_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create about_content table
CREATE TABLE about_content (
    id SERIAL PRIMARY KEY,
    section_name TEXT NOT NULL,
    title TEXT,
    content TEXT NOT NULL,
    image_url TEXT,
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create home_content table
CREATE TABLE home_content (
    id SERIAL PRIMARY KEY,
    section_name TEXT NOT NULL,
    title TEXT,
    content TEXT NOT NULL,
    image_url TEXT,
    link_url TEXT,
    icon_class TEXT,
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create gallery_items table
CREATE TABLE gallery_items (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    image_url TEXT NOT NULL,
    event_date DATE,
    category TEXT,
    is_featured INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    video_url TEXT
);

-- Create navigation_menu table
CREATE TABLE navigation_menu (
    id SERIAL PRIMARY KEY,
    menu_title TEXT NOT NULL,
    menu_url TEXT NOT NULL,
    parent_id INTEGER DEFAULT NULL,
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create contact_info table
CREATE TABLE contact_info (
    id SERIAL PRIMARY KEY,
    contact_type TEXT NOT NULL,
    title TEXT NOT NULL,
    value TEXT NOT NULL,
    description TEXT,
    icon_class TEXT,
    is_primary INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create districts table (Master table)
CREATE TABLE districts (
    id SERIAL PRIMARY KEY,
    district_name TEXT NOT NULL UNIQUE,
    district_code TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create district_sps table
CREATE TABLE district_sps (
    id SERIAL PRIMARY KEY,
    district_id INTEGER,
    name TEXT NOT NULL,
    contact_number TEXT,
    email TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (district_id) REFERENCES districts (id) ON DELETE CASCADE
);

-- Create shakthi_teams table
CREATE TABLE shakthi_teams (
    id SERIAL PRIMARY KEY,
    district_id INTEGER,
    team_name TEXT NOT NULL,
    leader_name TEXT,
    contact_number TEXT,
    area_covered TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (district_id) REFERENCES districts (id) ON DELETE CASCADE
);

-- Create women_police_stations table
CREATE TABLE women_police_stations (
    id SERIAL PRIMARY KEY,
    district_id INTEGER,
    station_name TEXT NOT NULL,
    incharge_name TEXT,
    contact_number TEXT,
    address TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (district_id) REFERENCES districts (id) ON DELETE CASCADE
);

-- Create one_stop_centers table
CREATE TABLE one_stop_centers (
    id SERIAL PRIMARY KEY,
    district_id INTEGER,
    center_name TEXT NOT NULL,
    address TEXT,
    incharge_name TEXT,
    contact_number TEXT,
    services_offered TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (district_id) REFERENCES districts (id) ON DELETE CASCADE
);

-- Create volunteers table
CREATE TABLE volunteers (
    id SERIAL PRIMARY KEY,
    registration_id TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE,
    age INTEGER,
    address TEXT NOT NULL,
    occupation TEXT,
    education TEXT,
    experience TEXT,
    motivation TEXT,
    availability TEXT,
    skills TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create volunteer_status table
CREATE TABLE volunteer_status (
    id SERIAL PRIMARY KEY,
    volunteer_id INTEGER UNIQUE,
    status TEXT DEFAULT 'pending',
    admin_notes TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers (id) ON DELETE CASCADE
);

-- Create volunteer_scores table
CREATE TABLE volunteer_scores (
    id SERIAL PRIMARY KEY,
    volunteer_id INTEGER UNIQUE,
    age_score INTEGER DEFAULT 0,
    education_score INTEGER DEFAULT 0,
    motivation_score INTEGER DEFAULT 0,
    skills_score INTEGER DEFAULT 0,
    total_score INTEGER DEFAULT 0,
    status TEXT DEFAULT 'pending',
    admin_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers (id) ON DELETE CASCADE
);

-- Create email_notifications table
CREATE TABLE email_notifications (
    id SERIAL PRIMARY KEY,
    volunteer_id INTEGER,
    email_type TEXT NOT NULL,
    subject TEXT NOT NULL,
    body TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'sent',
    FOREIGN KEY (volunteer_id) REFERENCES volunteers (id) ON DELETE CASCADE
);

-- Create admin_settings table
CREATE TABLE admin_settings (
    id SERIAL PRIMARY KEY,
    setting_name TEXT UNIQUE NOT NULL,
    setting_value TEXT,
    description TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_content_page ON content(page_name);
CREATE INDEX idx_gallery_category ON gallery_items(category);
CREATE INDEX idx_volunteers_phone ON volunteers(phone);
CREATE INDEX idx_volunteers_reg_id ON volunteers(registration_id);
CREATE INDEX idx_district_sps_district ON district_sps(district_id);
CREATE INDEX idx_shakthi_teams_district ON shakthi_teams(district_id);
CREATE INDEX idx_women_police_stations_district ON women_police_stations(district_id);
CREATE INDEX idx_one_stop_centers_district ON one_stop_centers(district_id);

-- Admin credentials table (separate database.db)
-- This will be in a separate schema or database
