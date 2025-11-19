--
-- PostgreSQL database dump
--

\restrict LhUZk0yly9JUtOEqGZF6yRR6DsJdPMvhkaBH9J77d3eBe0Z3WDMTIgBGZ1S2boZ

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE IF EXISTS ONLY public.password_reset_tokens DROP CONSTRAINT IF EXISTS password_reset_tokens_admin_id_fkey;
ALTER TABLE IF EXISTS ONLY public.email_otp DROP CONSTRAINT IF EXISTS email_otp_admin_id_fkey;
ALTER TABLE IF EXISTS ONLY public.password_reset_tokens DROP CONSTRAINT IF EXISTS password_reset_tokens_token_key;
ALTER TABLE IF EXISTS ONLY public.password_reset_tokens DROP CONSTRAINT IF EXISTS password_reset_tokens_pkey;
ALTER TABLE IF EXISTS ONLY public.email_otp DROP CONSTRAINT IF EXISTS email_otp_pkey;
ALTER TABLE IF EXISTS ONLY public.admin_credentials DROP CONSTRAINT IF EXISTS admin_credentials_username_key;
ALTER TABLE IF EXISTS ONLY public.admin_credentials DROP CONSTRAINT IF EXISTS admin_credentials_pkey;
ALTER TABLE IF EXISTS public.women_police_stations ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.volunteers ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.success_stories ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.shakthi_teams ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.safety_tips ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.pdf_resources ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.password_reset_tokens ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.one_stop_centers ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.officers ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.initiatives ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.home_content ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.gallery_items ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.events ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.email_otp ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.district_sps ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.contact_info ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.admin_credentials ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE IF EXISTS public.women_police_stations_id_seq;
DROP TABLE IF EXISTS public.women_police_stations;
DROP SEQUENCE IF EXISTS public.volunteers_id_seq;
DROP TABLE IF EXISTS public.volunteers;
DROP TABLE IF EXISTS public.volunteer_scores;
DROP SEQUENCE IF EXISTS public.volunteer_scores_id_seq;
DROP SEQUENCE IF EXISTS public.success_stories_id_seq;
DROP TABLE IF EXISTS public.success_stories;
DROP TABLE IF EXISTS public.site_settings;
DROP SEQUENCE IF EXISTS public.shakthi_teams_id_seq;
DROP TABLE IF EXISTS public.shakthi_teams;
DROP SEQUENCE IF EXISTS public.safety_tips_id_seq;
DROP TABLE IF EXISTS public.safety_tips;
DROP SEQUENCE IF EXISTS public.pdf_resources_id_seq;
DROP TABLE IF EXISTS public.pdf_resources;
DROP SEQUENCE IF EXISTS public.password_reset_tokens_id_seq;
DROP TABLE IF EXISTS public.password_reset_tokens;
DROP TABLE IF EXISTS public.page_content;
DROP SEQUENCE IF EXISTS public.one_stop_centers_id_seq;
DROP TABLE IF EXISTS public.one_stop_centers;
DROP SEQUENCE IF EXISTS public.officers_id_seq;
DROP TABLE IF EXISTS public.officers;
DROP TABLE IF EXISTS public.navigation_menu;
DROP TABLE IF EXISTS public.media_gallery;
DROP SEQUENCE IF EXISTS public.initiatives_id_seq;
DROP TABLE IF EXISTS public.initiatives;
DROP SEQUENCE IF EXISTS public.home_content_id_seq;
DROP TABLE IF EXISTS public.home_content;
DROP SEQUENCE IF EXISTS public.gallery_items_id_seq;
DROP TABLE IF EXISTS public.gallery_items;
DROP SEQUENCE IF EXISTS public.events_id_seq;
DROP TABLE IF EXISTS public.events;
DROP TABLE IF EXISTS public.emergency_numbers;
DROP SEQUENCE IF EXISTS public.email_otp_id_seq;
DROP TABLE IF EXISTS public.email_otp;
DROP TABLE IF EXISTS public.email_notifications;
DROP TABLE IF EXISTS public.districts;
DROP SEQUENCE IF EXISTS public.district_sps_id_seq;
DROP TABLE IF EXISTS public.district_sps;
DROP TABLE IF EXISTS public.district_info;
DROP TABLE IF EXISTS public.content;
DROP SEQUENCE IF EXISTS public.contact_info_id_seq;
DROP TABLE IF EXISTS public.contact_info;
DROP TABLE IF EXISTS public.admin_settings;
DROP TABLE IF EXISTS public.admin_security_questions;
DROP TABLE IF EXISTS public.admin_security;
DROP SEQUENCE IF EXISTS public.admin_credentials_id_seq;
DROP TABLE IF EXISTS public.admin_credentials;
DROP TABLE IF EXISTS public.about_content;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: about_content; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.about_content (
    id integer,
    section_name text,
    title text,
    content text,
    image_url text,
    sort_order integer,
    is_active integer,
    created_at text,
    updated_at text
);


ALTER TABLE public.about_content OWNER TO postgres;

--
-- Name: admin_credentials; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.admin_credentials (
    id integer NOT NULL,
    username text NOT NULL,
    password_hash text NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    email character varying(255)
);


ALTER TABLE public.admin_credentials OWNER TO postgres;

--
-- Name: admin_credentials_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.admin_credentials_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.admin_credentials_id_seq OWNER TO postgres;

--
-- Name: admin_credentials_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.admin_credentials_id_seq OWNED BY public.admin_credentials.id;


--
-- Name: admin_security; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.admin_security (
    id integer,
    admin_id integer,
    question1 text,
    answer1_hash text,
    question2 text,
    answer2_hash text,
    question3 text,
    answer3_hash text,
    created_at text,
    updated_at text
);


ALTER TABLE public.admin_security OWNER TO postgres;

--
-- Name: admin_security_questions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.admin_security_questions (
    id integer,
    admin_id integer,
    question1 text,
    answer1_hash text,
    question2 text,
    answer2_hash text,
    question3 text,
    answer3_hash text,
    created_at text
);


ALTER TABLE public.admin_security_questions OWNER TO postgres;

--
-- Name: admin_settings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.admin_settings (
    id integer,
    setting_name text,
    setting_value text,
    description text,
    updated_at text
);


ALTER TABLE public.admin_settings OWNER TO postgres;

--
-- Name: contact_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contact_info (
    id integer,
    contact_type text,
    title text,
    value text,
    description text,
    icon_class text,
    is_primary integer,
    is_active integer,
    created_at text,
    updated_at text
);


ALTER TABLE public.contact_info OWNER TO postgres;

--
-- Name: contact_info_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contact_info_id_seq
    START WITH 16
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.contact_info_id_seq OWNER TO postgres;

--
-- Name: contact_info_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contact_info_id_seq OWNED BY public.contact_info.id;


--
-- Name: content; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.content (
    id integer,
    page_name text,
    section_name text,
    content_type text,
    title text,
    content text,
    image_url text,
    link_url text,
    position_order integer,
    is_active text,
    created_at text,
    updated_at text
);


ALTER TABLE public.content OWNER TO postgres;

--
-- Name: district_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.district_info (
    id integer,
    district_name text,
    district_code text,
    headquarters text,
    women_police_stations text,
    one_stop_centers text,
    shakti_teams text,
    emergency_contacts text,
    latitude real,
    longitude real,
    population integer,
    area_sq_km real,
    created_at text,
    updated_at text
);


ALTER TABLE public.district_info OWNER TO postgres;

--
-- Name: district_sps; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.district_sps (
    id integer,
    district_id integer,
    name text,
    contact_number text,
    email text,
    is_active text,
    created_at text
);


ALTER TABLE public.district_sps OWNER TO postgres;

--
-- Name: district_sps_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.district_sps_id_seq
    START WITH 55
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.district_sps_id_seq OWNER TO postgres;

--
-- Name: district_sps_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.district_sps_id_seq OWNED BY public.district_sps.id;


--
-- Name: districts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.districts (
    id integer,
    district_name text,
    district_code text,
    is_active text,
    created_at text
);


ALTER TABLE public.districts OWNER TO postgres;

--
-- Name: email_notifications; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.email_notifications (
    id integer,
    volunteer_id integer,
    email_type text,
    subject text,
    body text,
    sent_at text,
    status text
);


ALTER TABLE public.email_notifications OWNER TO postgres;

--
-- Name: email_otp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.email_otp (
    id integer NOT NULL,
    admin_id integer NOT NULL,
    email text NOT NULL,
    otp text NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    expires_at timestamp without time zone NOT NULL,
    verified integer DEFAULT 0
);


ALTER TABLE public.email_otp OWNER TO postgres;

--
-- Name: email_otp_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.email_otp_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.email_otp_id_seq OWNER TO postgres;

--
-- Name: email_otp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.email_otp_id_seq OWNED BY public.email_otp.id;


--
-- Name: emergency_numbers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.emergency_numbers (
    id integer,
    number text,
    label text,
    description text,
    is_active integer,
    sort_order integer,
    created_at text,
    updated_at text
);


ALTER TABLE public.emergency_numbers OWNER TO postgres;

--
-- Name: events; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.events (
    id integer,
    title text,
    description text,
    event_date text,
    location text,
    image_url text,
    is_upcoming integer,
    is_active integer,
    created_at text,
    updated_at text
);


ALTER TABLE public.events OWNER TO postgres;

--
-- Name: events_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.events_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.events_id_seq OWNER TO postgres;

--
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.events_id_seq OWNED BY public.events.id;


--
-- Name: gallery_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gallery_items (
    id integer,
    title text,
    description text,
    image_url text,
    event_date text,
    category text,
    is_featured integer,
    is_active integer,
    created_at text,
    updated_at text,
    video_url text
);


ALTER TABLE public.gallery_items OWNER TO postgres;

--
-- Name: gallery_items_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.gallery_items_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.gallery_items_id_seq OWNER TO postgres;

--
-- Name: gallery_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.gallery_items_id_seq OWNED BY public.gallery_items.id;


--
-- Name: home_content; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.home_content (
    id integer,
    section_name text,
    title text,
    content text,
    image_url text,
    link_url text,
    icon_class text,
    sort_order integer,
    is_active integer,
    created_at text,
    updated_at text
);


ALTER TABLE public.home_content OWNER TO postgres;

--
-- Name: home_content_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.home_content_id_seq
    START WITH 19
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.home_content_id_seq OWNER TO postgres;

--
-- Name: home_content_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.home_content_id_seq OWNED BY public.home_content.id;


--
-- Name: initiatives; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.initiatives (
    id integer,
    title text,
    description text,
    image_url text,
    is_featured integer,
    is_active integer,
    created_at text,
    updated_at text
);


ALTER TABLE public.initiatives OWNER TO postgres;

--
-- Name: initiatives_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.initiatives_id_seq
    START WITH 11
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.initiatives_id_seq OWNER TO postgres;

--
-- Name: initiatives_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.initiatives_id_seq OWNED BY public.initiatives.id;


--
-- Name: media_gallery; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.media_gallery (
    id integer,
    title text,
    description text,
    file_path text,
    file_type text,
    category text,
    upload_date text,
    is_active text
);


ALTER TABLE public.media_gallery OWNER TO postgres;

--
-- Name: navigation_menu; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.navigation_menu (
    id integer,
    menu_title text,
    menu_url text,
    parent_id integer,
    sort_order integer,
    is_active integer,
    created_at text
);


ALTER TABLE public.navigation_menu OWNER TO postgres;

--
-- Name: officers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.officers (
    id integer,
    name text,
    designation text,
    department text,
    phone text,
    email text,
    image_url text,
    bio text,
    position_order integer,
    is_active text
);


ALTER TABLE public.officers OWNER TO postgres;

--
-- Name: officers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.officers_id_seq
    START WITH 5
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.officers_id_seq OWNER TO postgres;

--
-- Name: officers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.officers_id_seq OWNED BY public.officers.id;


--
-- Name: one_stop_centers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.one_stop_centers (
    id integer,
    district_id integer,
    center_name text,
    address text,
    incharge_name text,
    contact_number text,
    services_offered text,
    is_active text,
    created_at text
);


ALTER TABLE public.one_stop_centers OWNER TO postgres;

--
-- Name: one_stop_centers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.one_stop_centers_id_seq
    START WITH 53
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.one_stop_centers_id_seq OWNER TO postgres;

--
-- Name: one_stop_centers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.one_stop_centers_id_seq OWNED BY public.one_stop_centers.id;


--
-- Name: page_content; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.page_content (
    id integer,
    page_name text,
    section_name text,
    content_type text,
    content_value text,
    is_active integer,
    created_at text,
    updated_at text
);


ALTER TABLE public.page_content OWNER TO postgres;

--
-- Name: password_reset_tokens; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.password_reset_tokens (
    id integer NOT NULL,
    admin_id integer NOT NULL,
    token text NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    expires_at timestamp without time zone NOT NULL,
    used integer DEFAULT 0
);


ALTER TABLE public.password_reset_tokens OWNER TO postgres;

--
-- Name: password_reset_tokens_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.password_reset_tokens_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.password_reset_tokens_id_seq OWNER TO postgres;

--
-- Name: password_reset_tokens_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.password_reset_tokens_id_seq OWNED BY public.password_reset_tokens.id;


--
-- Name: pdf_resources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pdf_resources (
    id integer,
    title text,
    description text,
    file_name text,
    file_path text,
    icon text,
    download_count integer,
    is_active integer,
    created_at text,
    updated_at text
);


ALTER TABLE public.pdf_resources OWNER TO postgres;

--
-- Name: pdf_resources_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pdf_resources_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.pdf_resources_id_seq OWNER TO postgres;

--
-- Name: pdf_resources_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pdf_resources_id_seq OWNED BY public.pdf_resources.id;


--
-- Name: safety_tips; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.safety_tips (
    id integer,
    category text,
    title text,
    icon text,
    tips text,
    is_active integer,
    created_at text,
    updated_at text
);


ALTER TABLE public.safety_tips OWNER TO postgres;

--
-- Name: safety_tips_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.safety_tips_id_seq
    START WITH 8
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.safety_tips_id_seq OWNER TO postgres;

--
-- Name: safety_tips_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.safety_tips_id_seq OWNED BY public.safety_tips.id;


--
-- Name: shakthi_teams; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shakthi_teams (
    id integer,
    district_id integer,
    team_name text,
    leader_name text,
    contact_number text,
    area_covered text,
    is_active text,
    created_at text
);


ALTER TABLE public.shakthi_teams OWNER TO postgres;

--
-- Name: shakthi_teams_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shakthi_teams_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.shakthi_teams_id_seq OWNER TO postgres;

--
-- Name: shakthi_teams_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.shakthi_teams_id_seq OWNED BY public.shakthi_teams.id;


--
-- Name: site_settings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.site_settings (
    id integer,
    setting_key text,
    setting_value text,
    setting_type text,
    description text,
    updated_at text
);


ALTER TABLE public.site_settings OWNER TO postgres;

--
-- Name: success_stories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.success_stories (
    id integer,
    title text,
    story_content text,
    image_url text,
    location text,
    date_occurred text,
    position_order integer,
    is_active text,
    description text,
    date text,
    stat1_number text,
    stat1_label text,
    stat2_number text,
    stat2_label text,
    stat3_number text,
    stat3_label text,
    sort_order integer
);


ALTER TABLE public.success_stories OWNER TO postgres;

--
-- Name: success_stories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.success_stories_id_seq
    START WITH 4
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.success_stories_id_seq OWNER TO postgres;

--
-- Name: success_stories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.success_stories_id_seq OWNED BY public.success_stories.id;


--
-- Name: volunteer_scores_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.volunteer_scores_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.volunteer_scores_id_seq OWNER TO postgres;

--
-- Name: volunteer_scores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.volunteer_scores (
    id integer DEFAULT nextval('public.volunteer_scores_id_seq'::regclass) NOT NULL,
    volunteer_id integer,
    age_score integer,
    education_score integer,
    motivation_score integer,
    skills_score integer,
    total_score integer,
    status text,
    admin_notes text,
    created_at text
);


ALTER TABLE public.volunteer_scores OWNER TO postgres;

--
-- Name: volunteers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.volunteers (
    id integer,
    registration_id text,
    name text,
    email text,
    phone text,
    age integer,
    address text,
    occupation text,
    education text,
    experience text,
    motivation text,
    availability text,
    skills text,
    created_at text
);


ALTER TABLE public.volunteers OWNER TO postgres;

--
-- Name: volunteers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.volunteers_id_seq
    START WITH 5
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.volunteers_id_seq OWNER TO postgres;

--
-- Name: volunteers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.volunteers_id_seq OWNED BY public.volunteers.id;


--
-- Name: women_police_stations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.women_police_stations (
    id integer,
    district_id integer,
    station_name text,
    incharge_name text,
    contact_number text,
    address text,
    is_active text,
    created_at text
);


ALTER TABLE public.women_police_stations OWNER TO postgres;

--
-- Name: women_police_stations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.women_police_stations_id_seq
    START WITH 53
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.women_police_stations_id_seq OWNER TO postgres;

--
-- Name: women_police_stations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.women_police_stations_id_seq OWNED BY public.women_police_stations.id;


--
-- Name: admin_credentials id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin_credentials ALTER COLUMN id SET DEFAULT nextval('public.admin_credentials_id_seq'::regclass);


--
-- Name: contact_info id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contact_info ALTER COLUMN id SET DEFAULT nextval('public.contact_info_id_seq'::regclass);


--
-- Name: district_sps id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.district_sps ALTER COLUMN id SET DEFAULT nextval('public.district_sps_id_seq'::regclass);


--
-- Name: email_otp id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.email_otp ALTER COLUMN id SET DEFAULT nextval('public.email_otp_id_seq'::regclass);


--
-- Name: events id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events ALTER COLUMN id SET DEFAULT nextval('public.events_id_seq'::regclass);


--
-- Name: gallery_items id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gallery_items ALTER COLUMN id SET DEFAULT nextval('public.gallery_items_id_seq'::regclass);


--
-- Name: home_content id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.home_content ALTER COLUMN id SET DEFAULT nextval('public.home_content_id_seq'::regclass);


--
-- Name: initiatives id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.initiatives ALTER COLUMN id SET DEFAULT nextval('public.initiatives_id_seq'::regclass);


--
-- Name: officers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.officers ALTER COLUMN id SET DEFAULT nextval('public.officers_id_seq'::regclass);


--
-- Name: one_stop_centers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.one_stop_centers ALTER COLUMN id SET DEFAULT nextval('public.one_stop_centers_id_seq'::regclass);


--
-- Name: password_reset_tokens id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.password_reset_tokens ALTER COLUMN id SET DEFAULT nextval('public.password_reset_tokens_id_seq'::regclass);


--
-- Name: pdf_resources id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pdf_resources ALTER COLUMN id SET DEFAULT nextval('public.pdf_resources_id_seq'::regclass);


--
-- Name: safety_tips id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.safety_tips ALTER COLUMN id SET DEFAULT nextval('public.safety_tips_id_seq'::regclass);


--
-- Name: shakthi_teams id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shakthi_teams ALTER COLUMN id SET DEFAULT nextval('public.shakthi_teams_id_seq'::regclass);


--
-- Name: success_stories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.success_stories ALTER COLUMN id SET DEFAULT nextval('public.success_stories_id_seq'::regclass);


--
-- Name: volunteers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.volunteers ALTER COLUMN id SET DEFAULT nextval('public.volunteers_id_seq'::regclass);


--
-- Name: women_police_stations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.women_police_stations ALTER COLUMN id SET DEFAULT nextval('public.women_police_stations_id_seq'::regclass);


--
-- Data for Name: about_content; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.about_content (id, section_name, title, content, image_url, sort_order, is_active, created_at, updated_at) VALUES (7, 'vision', 'Our Vision', 'To create a safe and secure environment for women and children in Andhra Pradesh, ensuring their dignity, safety, and empowerment through proactive policing and community engagement.', NULL, 0, 1, '2025-08-25 07:46:04', '2025-08-25 07:46:04');
INSERT INTO public.about_content (id, section_name, title, content, image_url, sort_order, is_active, created_at, updated_at) VALUES (8, 'mission', 'Our Mission', 'We are committed to preventing crimes against women and children, providing swift justice, and creating awareness about safety measures through education and community outreach programs.', '', 1, 1, '2025-08-25 07:46:04', '2025-08-25 07:46:04');
INSERT INTO public.about_content (id, section_name, title, content, image_url, sort_order, is_active, created_at, updated_at) VALUES (9, 'officers', 'Leadership Team', 'Our dedicated team of experienced officers works tirelessly to ensure the safety and security of women and children across Andhra Pradesh.', NULL, 0, 1, '2025-08-25 07:46:04', '2025-08-25 07:46:04');
INSERT INTO public.about_content (id, section_name, title, content, image_url, sort_order, is_active, created_at, updated_at) VALUES (10, 'success_stories', 'Success Stories', 'Over the past year, we have successfully handled over 10,000 cases, provided assistance to thousands of women, and conducted numerous awareness programs across the state.', NULL, 0, 1, '2025-08-25 07:46:04', '2025-08-25 07:46:04');


--
-- Data for Name: admin_credentials; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.admin_credentials (id, username, password_hash, updated_at, email) VALUES (1, 'admin', 'scrypt:32768:8:1$HxSYhyqCtqD3bdeq$b0c94087c3587cea83283be45eca0f71ef5c46424e6a67a904b26fba0cf2948e71021b9ba93db7987f4437a99f60bab609fba499a70ab51f678f93c9e7bd2b21', '2025-11-19 11:56:17.663449', 'meta1.aihackathon@gmail.com');


--
-- Data for Name: admin_security; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.admin_security (id, admin_id, question1, answer1_hash, question2, answer2_hash, question3, answer3_hash, created_at, updated_at) VALUES (1, 1, 'What is your mother''s maiden name?', 'scrypt:32768:8:1$OBcwHR7d2TrmGdSr$eaf02b1451b4b6390099de7da31ff94136af4bc8aa92189a2f7a9bc5fb0d1d387cc1117c809dd37da628e68aa7be8992fd44586e8f971ec8afe046c9e563642c', 'What was the name of your first pet?', 'scrypt:32768:8:1$2D6QGSFv81ztPStz$d2dd011975fa476262bdb5b9d9358c8b488455190937a0eca3fe7026bdba3490dc48643d851f77ebe21336aa5e7027a4e76fc1493d2c79a56e2b5436c7faef23', 'In which city were you born?', 'scrypt:32768:8:1$kZoTRgmhqVT2dW0X$ce3af8c3eb5d7ed2bbb6593123030e2ad9514829d398384d4c84ca1775d37589ea2f34e72d5336a80bb88412228f31f12f6d2bdb8214f03df270ebaa695c8745', '2025-10-10 09:06:53', '2025-11-10 07:12:32');


--
-- Data for Name: admin_security_questions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: admin_settings; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: contact_info; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.contact_info (id, contact_type, title, value, description, icon_class, is_primary, is_active, created_at, updated_at) VALUES (14, 'email', 'Complaints', 'complaints@apwomensafety.gov.in', 'File complaints and grievances', 'fas fa-file-alt', 1, 1, '2025-09-18 07:03:41', '2025-09-18 07:03:41');
INSERT INTO public.contact_info (id, contact_type, title, value, description, icon_class, is_primary, is_active, created_at, updated_at) VALUES (15, 'email', 'General Info', 'info@apwomensafety.gov.in', 'General inquiries and information', 'fas fa-info-circle', 1, 1, '2025-09-18 07:03:41', '2025-09-18 07:03:41');


--
-- Data for Name: content; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (1, 'home', 'hero_title', 'text', 'AP Police Women & Child Safety Wing', 'Protecting Women & Children Across Andhra Pradesh', '', '', 1, '1', '2025-08-23 09:32:56', '2025-08-23 09:32:56');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (2, 'home', 'hero_subtitle', 'text', 'Your Safety is Our Priority', 'Dedicated to ensuring the safety and security of women and children in AP', '', '', 2, '1', '2025-08-23 09:32:56', '2025-08-23 09:32:56');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (3, 'home', 'emergency_number', 'text', '112', 'National Emergency Number', '', '', 3, '1', '2025-08-23 09:32:56', '2025-08-23 09:32:56');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (4, 'home', 'womens_helpline', 'text', '181', 'Women Helpline Number', '', '', 4, '1', '2025-08-23 09:32:56', '2025-08-23 09:32:56');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (5, 'about', 'mission', 'text', 'Our Mission', 'To create a safe and secure environment for women and children in Andhra Pradesh through proactive policing, community engagement, and innovative initiatives.', '', '', 1, '1', '2025-08-23 09:32:56', '2025-08-23 09:32:56');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (6, 'about', 'vision', 'text', 'Our Vision', 'A society where every woman and child feels safe, empowered, and protected.', '', '', 2, '1', '2025-08-23 09:32:56', '2025-08-23 09:32:56');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (7, 'home', 'hero', 'text', 'Ensuring Safety. Empowering Women.', 'AP Women Safety Wing is committed to creating a secure environment for women across Andhra Pradesh through innovative programs, community engagement, and swift response systems.', '/static/images/hero-bg.jpg', '', 1, '1', '2025-08-23 10:02:18', '2025-08-23 10:02:18');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (8, 'home', 'services', 'service', 'SHE Teams', '24/7 mobile teams dedicated to women safety across the state.', '/static/images/she-teams.jpg', '/services#she-teams', 1, '1', '2025-08-23 10:02:18', '2025-08-23 10:02:18');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (9, 'home', 'services', 'service', 'Helpline 181', 'Round-the-clock helpline for women in distress.', '/static/images/helpline.jpg', '/contact', 2, '1', '2025-08-23 10:02:18', '2025-08-23 10:02:18');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (10, 'home', 'services', 'service', 'Cyber Crime Cell', 'Specialized unit to tackle cyber crimes against women.', '/static/images/cyber-cell.jpg', '/services#cyber-crime', 3, '1', '2025-08-23 10:02:18', '2025-08-23 10:02:18');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (11, 'about', 'mission', 'text', 'Our Mission', 'To create a safe and secure environment for women in Andhra Pradesh through proactive policing, community engagement, and innovative technology solutions.', '', '', 1, '1', '2025-08-23 10:02:18', '2025-08-23 10:02:18');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (12, 'about', 'vision', 'text', 'Our Vision', 'A society where every woman feels safe, empowered, and confident to pursue her dreams without fear.', '', '', 1, '1', '2025-08-23 10:02:18', '2025-08-23 10:02:18');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (16, 'contact', 'helplines', 'contact', 'Women Helpline', '181 - 24/7 toll-free helpline for women in distress', '', 'tel:181', 1, '1', '2025-08-23 10:02:18', '2025-08-23 10:02:18');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (17, 'contact', 'helplines', 'contact', 'SHE Teams', '9490617111 - Direct contact for SHE Teams', '', 'tel:9490617111', 2, '1', '2025-08-23 10:02:18', '2025-08-23 10:02:18');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (18, 'contact', 'helplines', 'contact', 'Cyber Crime Cell', '1930 - Cyber crime helpline', '', 'tel:1930', 3, '1', '2025-08-23 10:02:18', '2025-08-23 10:02:18');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (22, 'contact', 'helplines', 'contact', '181', 'Women Helpline - 24/7 Emergency Support', '', 'tel:181', 1, '1', '2025-08-23 10:32:17', '2025-08-23 10:32:17');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (23, 'contact', 'helplines', 'contact', '1930', 'Cyber Crime Helpline', '', 'tel:1930', 2, '1', '2025-08-23 10:32:17', '2025-08-23 10:32:17');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (24, 'contact', 'helplines', 'contact', '112', 'National Emergency Number', '', 'tel:112', 3, '1', '2025-08-23 10:32:17', '2025-08-23 10:32:17');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (30, 'contact', 'hero', 'banner', 'Contact Us', 'Get in touch with AP Women Safety Wing for assistance, reporting, or general inquiries', NULL, NULL, 1, '1', '2025-08-23 10:34:07', '2025-08-23 10:34:07');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (31, 'contact', 'emergency', 'helpline', 'Emergency Helpline', '100 - Police Emergency<br>1091 - Women Helpline<br>181 - Women in Distress<br>1098 - Child Helpline', NULL, NULL, 2, '1', '2025-08-23 10:34:07', '2025-08-23 10:34:07');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (32, 'contact', 'office', 'contact', 'Main Office', 'AP Women Safety Wing<br>Government of Andhra Pradesh<br>Secretariat, Amaravati<br>Phone: +91-863-2340000<br>Email: womensafety@ap.gov.in', NULL, NULL, 3, '1', '2025-08-23 10:34:07', '2025-08-23 10:34:07');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (33, 'contact', 'district_offices', 'section', 'District Offices', 'We have offices in all 13 districts of Andhra Pradesh. Contact your nearest district office for local assistance and support.', NULL, NULL, 4, '1', '2025-08-23 10:34:07', '2025-08-23 10:34:07');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (34, 'initiatives', 'hero', 'banner', 'Our Initiatives', 'Comprehensive programs and cells dedicated to ensuring women''s safety across Andhra Pradesh', NULL, NULL, 1, '1', '2025-08-23 10:55:09', '2025-08-23 10:55:09');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (35, 'initiatives', 'domestic_violence', 'initiative', 'Domestic Violence Cell', 'Specialized unit to address domestic violence cases with dedicated counselors, legal aid, and support services. Provides 24/7 assistance to victims and ensures proper investigation and prosecution of cases.', NULL, NULL, 2, '1', '2025-08-23 10:55:09', '2025-08-23 10:55:09');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (36, 'initiatives', 'ashraya', 'initiative', 'Victim Support Centre (Ashraya)', 'Comprehensive support center providing shelter, counseling, legal aid, and rehabilitation services to women victims of violence. Ashraya centers offer safe accommodation and holistic care for women in distress.', NULL, NULL, 3, '1', '2025-08-23 10:55:09', '2025-08-23 10:55:09');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (37, 'initiatives', 'anti_trafficking', 'initiative', 'Anti Human Trafficking Cell', 'Specialized unit combating human trafficking with focus on prevention, rescue operations, and rehabilitation of victims. Works closely with other agencies to dismantle trafficking networks and ensure justice.', NULL, NULL, 4, '1', '2025-08-23 10:55:09', '2025-08-23 10:55:09');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (38, 'initiatives', 'eve_teasing', 'initiative', 'Eve Teasing Prevention Cell', 'Dedicated cell to prevent and address eve teasing and street harassment. Conducts awareness programs, operates complaint mechanisms, and ensures swift action against offenders in public spaces.', NULL, NULL, 5, '1', '2025-08-23 10:55:09', '2025-08-23 10:55:09');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (39, 'initiatives', 'posh', 'initiative', 'POSH (Prevention of Sexual Harassment)', 'Implementation and monitoring of Prevention of Sexual Harassment Act at workplaces. Ensures all institutions have Internal Complaints Committees and provides training on workplace safety and gender sensitivity.', NULL, NULL, 6, '1', '2025-08-23 10:55:09', '2025-08-23 10:55:09');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (40, 'initiatives', 'transgender_protection', 'initiative', 'Transgender Persons Protection Cell', 'Specialized cell for protection and welfare of transgender persons. Addresses discrimination, provides support services, and ensures access to healthcare, education, and employment opportunities.', NULL, NULL, 7, '1', '2025-08-23 10:55:09', '2025-08-23 10:55:09');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (41, 'initiatives', 'css', 'initiative', 'CSS (Cyber Security for Women)', 'Cyber Security Services focusing on protecting women from online harassment, cyberbullying, and digital crimes. Provides cyber safety education and swift response to cyber crimes against women.', NULL, NULL, 8, '1', '2025-08-23 10:55:09', '2025-08-23 10:55:09');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (42, 'initiatives', 'wher', 'initiative', 'WHER (Women Helpline Emergency Response)', 'Women Helpline Emergency Response system providing immediate assistance through 24/7 helplines. Ensures quick response to emergency situations and connects victims to appropriate support services.', NULL, NULL, 9, '1', '2025-08-23 10:55:09', '2025-08-23 10:55:09');
INSERT INTO public.content (id, page_name, section_name, content_type, title, content, image_url, link_url, position_order, is_active, created_at, updated_at) VALUES (43, 'initiatives', 'ccc', 'initiative', 'CCC (Community Coordination Centre)', 'Community Coordination Centers that work at grassroots level to create awareness, build community support networks, and ensure local participation in women safety initiatives across villages and towns.', NULL, NULL, 10, '1', '2025-08-23 10:55:09', '2025-08-23 10:55:09');


--
-- Data for Name: district_info; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (1, 'Anantapur', 'ATP', 'Anantapur', 'Anantapur Women PS: +91-8554-255100
Kalyanadurg Women PS: +91-8554-242100
Hindupuram Women PS: +91-8554-230100', 'Anantapur One Stop Center: +91-8554-255200
Address: District Hospital, Anantapur', 'Anantapur Shakti Team: +91-9490617001
Kalyanadurg Shakti Team: +91-9490617002
Hindupuram Shakti Team: +91-9490617003', 'Emergency: 100, Women Helpline: 181, District SP: +91-8554-255000', 14.6819, 77.6006, 4081148, 19130, '2025-08-23 10:39:58', '2025-08-23 10:39:58');
INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (2, 'Chittoor', 'CTR', 'Chittoor', 'Chittoor Women PS: +91-8572-255100
Tirupati Women PS: +91-877-2249100
Madanapalle Women PS: +91-8571-255100', 'Chittoor One Stop Center: +91-8572-255200
Tirupati One Stop Center: +91-877-2249200', 'Chittoor Shakti Team: +91-9490617011
Tirupati Shakti Team: +91-9490617012
Madanapalle Shakti Team: +91-9490617013', 'Emergency: 100, Women Helpline: 181, District SP: +91-8572-255000', 13.2172, 79.1003, 4174064, 15152, '2025-08-23 10:39:58', '2025-08-23 10:39:58');
INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (3, 'East Godavari', 'EG', 'Kakinada', 'Kakinada Women PS: +91-884-2372100
Rajahmundry Women PS: +91-883-2424100
Amalapuram Women PS: +91-8856-255100', 'Kakinada One Stop Center: +91-884-2372200
Rajahmundry One Stop Center: +91-883-2424200', 'Kakinada Shakti Team: +91-9490617021
Rajahmundry Shakti Team: +91-9490617022
Amalapuram Shakti Team: +91-9490617023', 'Emergency: 100, Women Helpline: 181, District SP: +91-884-2372000', 16.9891, 82.2475, 5154296, 10807, '2025-08-23 10:39:58', '2025-08-23 10:39:58');
INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (4, 'Guntur', 'GTR', 'Guntur', 'Guntur Women PS: +91-863-2323100
Tenali Women PS: +91-8644-255100
Narasaraopet Women PS: +91-8647-255100', 'Guntur One Stop Center: +91-863-2323200
Narasaraopet One Stop Center: +91-8647-255200', 'Guntur Shakti Team: +91-9490617031
Tenali Shakti Team: +91-9490617032
Narasaraopet Shakti Team: +91-9490617033', 'Emergency: 100, Women Helpline: 181, District SP: +91-863-2323000', 16.3067, 80.4365, 4887813, 11391, '2025-08-23 10:39:58', '2025-08-23 10:39:58');
INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (5, 'Krishna', 'KRS', 'Machilipatnam', 'Machilipatnam Women PS: +91-8672-255100
Vijayawada Women PS: +91-866-2574100
Gudem Women PS: +91-8674-255100', 'Machilipatnam One Stop Center: +91-8672-255200
Vijayawada One Stop Center: +91-866-2574200', 'Machilipatnam Shakti Team: +91-9490617041
Vijayawada Shakti Team: +91-9490617042
Gudem Shakti Team: +91-9490617043', 'Emergency: 100, Women Helpline: 181, District SP: +91-8672-255000', 16.1875, 81.1389, 4517398, 8727, '2025-08-23 10:39:58', '2025-08-23 10:39:58');
INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (6, 'Kurnool', 'KNL', 'Kurnool', 'Kurnool Women PS: +91-8518-255100
Nandyal Women PS: +91-8514-255100
Adoni Women PS: +91-8512-255100', 'Kurnool One Stop Center: +91-8518-255200
Nandyal One Stop Center: +91-8514-255200', 'Kurnool Shakti Team: +91-9490617051
Nandyal Shakti Team: +91-9490617052
Adoni Shakti Team: +91-9490617053', 'Emergency: 100, Women Helpline: 181, District SP: +91-8518-255000', 15.8281, 78.0373, 4053463, 17658, '2025-08-23 10:39:58', '2025-08-23 10:39:58');
INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (7, 'Nellore', 'NLR', 'Nellore', 'Nellore Women PS: +91-861-2326100
Gudur Women PS: +91-8624-255100
Kavali Women PS: +91-8626-255100', 'Nellore One Stop Center: +91-861-2326200
Gudur One Stop Center: +91-8624-255200', 'Nellore Shakti Team: +91-9490617061
Gudur Shakti Team: +91-9490617062
Kavali Shakti Team: +91-9490617063', 'Emergency: 100, Women Helpline: 181, District SP: +91-861-2326000', 14.4426, 79.9865, 2966082, 13076, '2025-08-23 10:39:58', '2025-08-23 10:39:58');
INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (8, 'Prakasam', 'PKM', 'Ongole', 'Ongole Women PS: +91-8592-255100
Chirala Women PS: +91-8594-255100
Kandukur Women PS: +91-8596-255100', 'Ongole One Stop Center: +91-8592-255200
Chirala One Stop Center: +91-8594-255200', 'Ongole Shakti Team: +91-9490617071
Chirala Shakti Team: +91-9490617072
Kandukur Shakti Team: +91-9490617073', 'Emergency: 100, Women Helpline: 181, District SP: +91-8592-255000', 15.5057, 80.0499, 3397448, 17626, '2025-08-23 10:39:58', '2025-08-23 10:39:58');
INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (9, 'Srikakulam', 'SKL', 'Srikakulam', 'Srikakulam Women PS: +91-8942-255100
Ichchapuram Women PS: +91-8944-255100
Tekkali Women PS: +91-8946-255100', 'Srikakulam One Stop Center: +91-8942-255200
Ichchapuram One Stop Center: +91-8944-255200', 'Srikakulam Shakti Team: +91-9490617081
Ichchapuram Shakti Team: +91-9490617082
Tekkali Shakti Team: +91-9490617083', 'Emergency: 100, Women Helpline: 181, District SP: +91-8942-255000', 18.2949, 83.8987, 2703114, 5837, '2025-08-23 10:39:58', '2025-08-23 10:39:58');
INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (10, 'Visakhapatnam', 'VSP', 'Visakhapatnam', 'Visakhapatnam Women PS: +91-891-2746100
Anakapalle Women PS: +91-8924-255100
Narsipatnam Women PS: +91-8922-255100', 'Visakhapatnam One Stop Center: +91-891-2746200
Anakapalle One Stop Center: +91-8924-255200', 'Visakhapatnam Shakti Team: +91-9490617091
Anakapalle Shakti Team: +91-9490617092
Narsipatnam Shakti Team: +91-9490617093', 'Emergency: 100, Women Helpline: 181, District SP: +91-891-2746000', 17.6868, 83.2185, 4290589, 11161, '2025-08-23 10:39:58', '2025-08-23 10:39:58');
INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (11, 'Vizianagaram', 'VZM', 'Vizianagaram', 'Vizianagaram Women PS: +91-8922-255100
Bobbili Women PS: +91-8924-255100
Parvathipuram Women PS: +91-8926-255100', 'Vizianagaram One Stop Center: +91-8922-255200
Bobbili One Stop Center: +91-8924-255200', 'Vizianagaram Shakti Team: +91-9490617101
Bobbili Shakti Team: +91-9490617102
Parvathipuram Shakti Team: +91-9490617103', 'Emergency: 100, Women Helpline: 181, District SP: +91-8922-255000', 18.1167, 83.4, 2344474, 6539, '2025-08-23 10:39:58', '2025-08-23 10:39:58');
INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (12, 'West Godavari', 'WG', 'Eluru', 'Eluru Women PS: +91-8812-255100
Bhimavaram Women PS: +91-8816-255100
Tadepalligudem Women PS: +91-8818-255100', 'Eluru One Stop Center: +91-8812-255200
Bhimavaram One Stop Center: +91-8816-255200', 'Eluru Shakti Team: +91-9490617111
Bhimavaram Shakti Team: +91-9490617112
Tadepalligudem Shakti Team: +91-9490617113', 'Emergency: 100, Women Helpline: 181, District SP: +91-8812-255000', 16.7123, 81.0955, 3936966, 7742, '2025-08-23 10:39:58', '2025-08-23 10:39:58');
INSERT INTO public.district_info (id, district_name, district_code, headquarters, women_police_stations, one_stop_centers, shakti_teams, emergency_contacts, latitude, longitude, population, area_sq_km, created_at, updated_at) VALUES (13, 'YSR Kadapa', 'CDP', 'Kadapa', 'Kadapa Women PS: +91-8562-255100
Proddatur Women PS: +91-8564-255100
Jammalamadugu Women PS: +91-8566-255100', 'Kadapa One Stop Center: +91-8562-255200
Proddatur One Stop Center: +91-8564-255200', 'Kadapa Shakti Team: +91-9490617121
Proddatur Shakti Team: +91-9490617122
Jammalamadugu Shakti Team: +91-9490617123', 'Emergency: 100, Women Helpline: 181, District SP: +91-8562-255000', 14.4673, 78.8242, 2849647, 15359, '2025-08-23 10:39:58', '2025-08-23 10:39:58');


--
-- Data for Name: district_sps; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (30, 2, 'Tuhin Sinha,IPS', '08924-232024', 'spanakapalli@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (31, 3, 'P.Jagadeesh,IPS', '08554-240105', 'spatp1@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (32, 4, 'V.Vidhya Sagar Naidu,IPS', '08561-211444', 'spannamayyadistrict@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (33, 5, 'Tushar Dudi,IPS', '086643-293533', 'spbapatla@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (34, 6, 'V.N.Manikanta Chandolu,IPS', '08572-235828', 'sp-chittoor@ap.gov.in', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (35, 7, 'D.Narasimha Kishore,IPS', '0883-2427187', 'sp@rjyu.appolice.gov.in', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (36, 8, 'K.Pratap Siva Kishore,IPS', '08812-232662', 'spelurudistrict@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (37, 9, 'Satish Kumar,IPS', '0863-2233222', 'guntururbansp@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (38, 10, 'Bindhu Madhav Garikapati,IPS', '0884-2362000', 'sp@eg.appolice.gov.in', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (39, 11, 'B.Krishna Rao,IPS', '08856-235100', 'spkonaseema@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (40, 12, 'R.Gangadhara Rao,IPS', '08672-223057,223666', 'sp@kri.appolice.gov.in', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (41, 13, 'Vikranth Patil,IPS', '08518-225700', 'spkurnool.kur@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (42, 15, 'S.V.Rajasekhar Babu,IPS', '0866-2493333', 'cp@vza.appolice.gov.in', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (43, 14, 'Adhiraj Singh Rana,IPS', '08514-294915', 'spnandyal.official@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (44, 16, 'K.Srinivasa Rao,IPS', '08647-222999', 'sppalnadu@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (45, 17, 'S.V.Madhava Reddy.,IPS', '09490678872', 'sppvpmanyam@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (46, 18, 'A.R.Damodhar,IPS', '08592-286100', 'spongole@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (47, 19, 'G.Krishna Kanth,IPS', '0861-2331700', 'nelloresp@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (48, 20, 'V.Ratna,IPS', '08555-292433', 'spsss1ptp@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (49, 21, 'K.V.Maheswara Reddy.,IPS', '08492-222508', 'spsrikakulam@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (50, 22, 'V.Harsha Vardhan Raju,IPS', '0877-2289044', 'sptirupatiap@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (51, 23, 'Dr.Shanka Brata Bagchi,IPS', '0891-2562709', 'cpvspc@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (52, 24, 'Vakul Zindal,IPS', '08922-276163', 'spofvzm@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (53, 25, 'Adnan Nayeem Asmi,IPS', '08816-293100', 'spwgbvrm@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (54, 26, 'E.G.Ashok Kumar,IPS', '08562-242198', 'spkadapa2014@gmail.com', '1', '2025-09-01 08:15:45');
INSERT INTO public.district_sps (id, district_id, name, contact_number, email, is_active, created_at) VALUES (29, 1, 'Amit bardar ,IPS', '+91-9985574470', 'sp.asr123@gmail.com', '1', '2025-09-01 08:15:45');


--
-- Data for Name: districts; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (1, 'Alluri Sitarama Raju', 'ALLURI_SITARAMA_RAJU', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (2, 'Anakapalli', 'ANAKAPALLI', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (3, 'Ananthapuramu', 'ANANTHAPURAMU', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (4, 'Annamayya', 'ANNAMAYYA', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (5, 'Bapatla', 'BAPATLA', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (6, 'Chittoor', 'CHITTOOR', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (7, 'East Godavari', 'EAST_GODAVARI', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (8, 'Eluru', 'ELURU', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (9, 'Guntur', 'GUNTUR', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (10, 'Kakinada', 'KAKINADA', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (11, 'Konaseema', 'KONASEEMA', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (12, 'Krishna', 'KRISHNA', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (13, 'Kurnool', 'KURNOOL', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (14, 'Nandyal', 'NANDYAL', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (15, 'NTR', 'NTR', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (16, 'Palnadu', 'PALNADU', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (17, 'Parvathipuram Manyam', 'PARVATHIPURAM_MANYAM', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (18, 'Prakasam', 'PRAKASAM', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (19, 'Sri Potti Sriramulu Nellore', 'SRI_POTTI_SRIRAMULU_NELLORE', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (20, 'Sri Sathya Sai', 'SRI_SATHYA_SAI', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (21, 'Srikakulam', 'SRIKAKULAM', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (22, 'Tirupati', 'TIRUPATI', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (23, 'Visakhapatnam', 'VISAKHAPATNAM', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (24, 'Vizianagaram', 'VIZIANAGARAM', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (25, 'West Godavari', 'WEST_GODAVARI', '1', '2025-09-01 07:29:02');
INSERT INTO public.districts (id, district_name, district_code, is_active, created_at) VALUES (26, 'YSR (Kadapa)', 'YSR_KADAPA', '1', '2025-09-01 07:29:02');


--
-- Data for Name: email_notifications; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: email_otp; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.email_otp (id, admin_id, email, otp, created_at, expires_at, verified) VALUES (1, 1, 'meta1.aihackathon@gmail.com', '870178', '2025-11-19 11:41:24.434744', '2025-11-19 11:51:24.435844', 0);
INSERT INTO public.email_otp (id, admin_id, email, otp, created_at, expires_at, verified) VALUES (2, 1, 'meta1.aihackathon@gmail.com', '182165', '2025-11-19 11:41:43.009732', '2025-11-19 11:51:43.010943', 0);
INSERT INTO public.email_otp (id, admin_id, email, otp, created_at, expires_at, verified) VALUES (3, 1, 'meta1.aihackathon@gmail.com', '921951', '2025-11-19 11:43:41.814429', '2025-11-19 11:53:41.816261', 1);
INSERT INTO public.email_otp (id, admin_id, email, otp, created_at, expires_at, verified) VALUES (4, 1, 'meta1.aihackathon@gmail.com', '660634', '2025-11-19 11:54:03.900176', '2025-11-19 12:04:03.901327', 1);
INSERT INTO public.email_otp (id, admin_id, email, otp, created_at, expires_at, verified) VALUES (5, 1, 'meta1.aihackathon@gmail.com', '764380', '2025-11-19 11:55:03.543522', '2025-11-19 12:05:03.545049', 1);


--
-- Data for Name: emergency_numbers; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.emergency_numbers (id, number, label, description, is_active, sort_order, created_at, updated_at) VALUES (1, '181', 'Women Helpline', 'National women helpline for immediate assistance', 1, 1, '2025-08-23 13:55:42', '2025-08-23 13:55:42');
INSERT INTO public.emergency_numbers (id, number, label, description, is_active, sort_order, created_at, updated_at) VALUES (2, '100', 'Police Emergency', 'Police emergency number for immediate help', 1, 2, '2025-08-23 13:55:42', '2025-08-23 13:55:42');
INSERT INTO public.emergency_numbers (id, number, label, description, is_active, sort_order, created_at, updated_at) VALUES (3, '112', 'National Emergency', 'Universal emergency number for all emergencies', 1, 3, '2025-08-23 13:55:42', '2025-08-23 13:55:42');
INSERT INTO public.emergency_numbers (id, number, label, description, is_active, sort_order, created_at, updated_at) VALUES (4, '1091', 'Women''s Helpline', 'Dedicated women''s helpline for support and guidance', 1, 4, '2025-08-23 13:55:42', '2025-08-23 13:55:42');


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: gallery_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (1, 'Self Defense Workshop', 'Monthly self-defense training for college students', '/static/images/gallery/workshop1.jpg', '2024-08-15', 'training', 1, 1, '2025-08-23 14:09:46', '2025-08-23 14:09:46', NULL);
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (2, 'Awareness Campaign', 'Women safety awareness program in rural areas', '/static/images/gallery/awareness1.jpg', '2024-08-10', 'awareness', 0, 1, '2025-08-23 14:09:46', '2025-08-23 14:09:46', NULL);
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (3, 'SHE Team Training', 'Training program for new SHE team members', '/static/images/gallery/training1.jpg', '2024-08-05', 'training', 1, 1, '2025-08-23 14:09:46', '2025-08-23 14:09:46', NULL);
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (4, 'Community Meeting', 'Interactive session with community leaders', '/static/images/gallery/community1.jpg', '2024-07-30', 'event', 0, 1, '2025-08-23 14:09:46', '2025-08-23 14:09:46', NULL);
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (5, 'Basic Self Defence Moves - Part 1', 'Learn fundamental defensive techniques including proper stance, blocking, and basic strikes. Essential skills for personal safety.', '/static/images/slide1.jpg', '2024-12-20', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (6, 'Advanced Self Defence Techniques', 'Advanced defensive moves including escape from grabs, pressure points, and multiple attacker scenarios.', '/static/images/slide2.jpg', '2024-12-18', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (7, 'Self Defence with Objects', 'Using everyday items for defense - keys, bags, mobile phones, and other common objects as defensive tools.', '/static/images/slide3.jpg', '2024-12-16', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (8, 'Group Self Defence Training', 'Community-based training sessions where women learn together and practice defensive techniques in groups.', '/static/images/slide4.jpg', '2024-12-14', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (9, 'Self Defence Demonstration Video', 'Complete video demonstration of all basic self-defence moves with step-by-step instructions.', '/static/images/slide5.jpg', '2024-12-12', 'Self Defence Programme', 1, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '/static/videos/self_defence_demo.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (10, 'Safety Awareness Training Video', 'Comprehensive safety awareness video covering personal safety tips, emergency contacts, and prevention strategies.', '/static/images/slide1.jpg', '2024-12-15', 'Training Videos', 1, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '/static/videos/safety_awareness.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (11, 'Cyber Safety Education Video', 'Digital safety training covering online harassment prevention, safe social media practices, and cyber crime awareness.', '/static/images/slide2.jpg', '2024-12-13', 'Training Videos', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '/static/videos/cyber_safety.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (12, 'Emergency Response Training', 'Training video on how to respond in emergency situations, including calling for help and first aid basics.', '/static/images/slide3.jpg', '2024-12-11', 'Training Videos', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '/static/videos/emergency_response.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (13, 'Legal Awareness Training', 'Educational video about women''s legal rights, how to file complaints, and available legal support systems.', '/static/images/slide4.jpg', '2024-12-09', 'Training Videos', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '/static/videos/legal_awareness.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (14, 'Village Awareness Program - District 1', 'Rural outreach program focusing on women''s safety awareness in remote villages and agricultural communities.', '/static/images/slide1.jpg', '2024-12-08', 'Community Programmes', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (15, 'School Safety Education Program', 'Educational program conducted in schools to teach students about personal safety and anti-bullying measures.', '/static/images/slide2.jpg', '2024-12-06', 'Community Programmes', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (16, 'Workplace Safety Initiative', 'Corporate program addressing workplace harassment prevention and creating safe work environments for women.', '/static/images/slide3.jpg', '2024-12-04', 'Community Programmes', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (17, 'Community Safety Volunteers Training', 'Training program for community volunteers who help in spreading safety awareness and supporting local women.', '/static/images/slide4.jpg', '2024-12-02', 'Community Programmes', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (18, 'State Women Safety Conference 2024', 'Annual state-level conference discussing new policies, achievements, and future plans for women safety initiatives.', '/static/images/slide1.jpg', '2024-12-07', 'News & Events', 1, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (19, 'Safety Equipment Distribution Drive', 'Large-scale distribution of safety equipment including emergency whistles, pepper sprays, and safety apps.', '/static/images/slide2.jpg', '2024-12-05', 'News & Events', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (20, 'Awards Ceremony for Safety Champions', 'Recognition ceremony honoring individuals and organizations contributing significantly to women safety initiatives.', '/static/images/slide3.jpg', '2024-12-03', 'News & Events', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (21, 'Media Coverage - Safety Campaign Launch', 'Media coverage of the new safety campaign launch with participation from government officials and celebrities.', '/static/images/slide4.jpg', '2024-12-01', 'News & Events', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (22, 'Basic Self Defence Training', 'Learn essential self-defence techniques for personal safety', '/static/images/slide1.jpg', '2024-12-15', 'Self Defence Programme', 1, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (23, 'Advanced Martial Arts', 'Advanced defensive moves and techniques', '/static/images/slide2.jpg', '2024-12-12', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (24, 'Safety Training Video', 'Comprehensive safety awareness video', '/static/images/slide3.jpg', '2024-12-10', 'Training Videos', 1, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '/static/videos/safety.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (25, 'Community Outreach', 'Village-level safety awareness program', '/static/images/slide4.jpg', '2024-12-08', 'Community Programmes', 0, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (26, 'Safety Week Launch', 'Official launch of safety awareness week', '/static/images/slide5.jpg', '2024-12-05', 'News & Events', 1, 1, '2025-09-02 12:03:54', '2025-09-02 12:03:54', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (27, 'Basic Self Defence Training - Session 1', 'Learn fundamental defensive postures and basic strikes for personal safety', '/static/images/slide1.jpg', '2024-12-20', 'Self Defence Programme', 1, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (28, 'Advanced Self Defence Moves', 'Advanced techniques including escape from grabs and pressure points', '/static/images/slide2.jpg', '2024-12-18', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (29, 'Self Defence with Common Objects', 'Using everyday items like keys, bags for defense', '/static/images/slide3.jpg', '2024-12-16', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (30, 'Group Self Defence Workshop', 'Community training sessions for women groups', '/static/images/slide4.jpg', '2024-12-14', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (31, 'Martial Arts Basics for Women', 'Introduction to martial arts adapted for women', '/static/images/slide5.jpg', '2024-12-12', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (32, 'Self Defence for Students', 'Special program for college and school students', '/static/images/slide1.jpg', '2024-12-10', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (33, 'Emergency Response Training', 'How to respond in dangerous situations', '/static/images/slide2.jpg', '2024-12-08', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (34, 'Self Defence Demonstration', 'Live demonstration of defensive techniques', '/static/images/slide3.jpg', '2024-12-06', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (35, 'Safety Awareness Training Video', 'Comprehensive personal safety awareness video', '/static/images/slide1.jpg', '2024-12-15', 'Training Videos', 1, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '/static/videos/safety_awareness.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (36, 'Cyber Safety Education', 'Digital safety and online harassment prevention', '/static/images/slide2.jpg', '2024-12-13', 'Training Videos', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '/static/videos/cyber_safety.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (37, 'Emergency Response Tutorial', 'Step-by-step emergency response guide', '/static/images/slide3.jpg', '2024-12-11', 'Training Videos', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '/static/videos/emergency.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (38, 'Legal Rights Awareness', 'Know your legal rights and protections', '/static/images/slide4.jpg', '2024-12-09', 'Training Videos', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '/static/videos/legal_rights.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (39, 'Workplace Safety Training', 'Professional environment safety guidelines', '/static/images/slide5.jpg', '2024-12-07', 'Training Videos', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '/static/videos/workplace.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (40, 'Self Defence Video Tutorial', 'Complete self-defence video guide', '/static/images/slide1.jpg', '2024-12-05', 'Training Videos', 1, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '/static/videos/self_defence.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (41, 'Village Outreach Program - District 1', 'Rural awareness program in remote villages', '/static/images/slide2.jpg', '2024-12-14', 'Community Programmes', 1, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (42, 'School Safety Education Initiative', 'Safety education in schools and colleges', '/static/images/slide3.jpg', '2024-12-12', 'Community Programmes', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (43, 'Workplace Safety Campaign', 'Corporate awareness programs', '/static/images/slide4.jpg', '2024-12-10', 'Community Programmes', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (44, 'Community Volunteer Training', 'Training local volunteers for safety awareness', '/static/images/slide5.jpg', '2024-12-08', 'Community Programmes', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (45, 'Women Empowerment Workshop', 'Empowering women through education', '/static/images/slide1.jpg', '2024-12-06', 'Community Programmes', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (46, 'Public Transport Safety Drive', 'Safety awareness in public transportation', '/static/images/slide2.jpg', '2024-12-04', 'Community Programmes', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (47, 'State Women Safety Conference 2024', 'Annual conference on women safety policies', '/static/images/slide3.jpg', '2024-12-15', 'News & Events', 1, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (48, 'Safety Equipment Distribution', 'Mass distribution of safety devices', '/static/images/slide4.jpg', '2024-12-13', 'News & Events', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (49, 'Awards Ceremony - Safety Champions', 'Recognizing outstanding contributors', '/static/images/slide5.jpg', '2024-12-11', 'News & Events', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (50, 'Media Coverage - Campaign Launch', 'Press coverage of new safety initiatives', '/static/images/slide1.jpg', '2024-12-09', 'News & Events', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (51, 'International Women''s Day Celebration', 'Special event celebrating women achievements', '/static/images/slide2.jpg', '2024-12-07', 'News & Events', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (52, 'Safety Week Inauguration', 'Official launch of safety awareness week', '/static/images/slide3.jpg', '2024-12-05', 'News & Events', 1, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (53, 'Monthly Safety Workshop', 'Regular monthly safety training session in schools and colleges', '', '2026-01-15', 'Upcoming Events', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (55, 'women''s day', 'Meeting for all district safety coordinators ', '', '2026-02-03', 'Upcoming Events', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (56, 'Women Self Defence Workshop - Advanced Techniques', 'Advanced self-defence workshop covering escape techniques, pressure points, and situational awareness for women safety.', '/static/images/slide2.jpg', '2024-12-25', 'Self Defence Programme', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (57, 'Self Defense Workshop', '', '/static/uploads/gallery_1757315610_self_defence-4.jpeg', '', 'Images', 1, 1, '2025-09-02 12:52:10', '2025-09-02 12:52:10', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (58, 'Self Defense Workshop', '', '/static/uploads/gallery_1757315631_self_defence-3.jpeg', '', 'Images', 1, 1, '2025-09-02 12:52:40', '2025-09-02 12:52:40', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (59, 'Self Defense Workshop', 'self defence programme', '/static/uploads/gallery_1757315578_self_defence-5.jpeg', '2025-03-01', 'Images', 0, 1, '2025-09-08 07:12:59', '2025-09-08 07:12:59', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (60, 'Self Defense Workshop', 'self defense programme', '/static/uploads/gallery_1757315670_selfdefence-1.jpeg', '2025-03-01', 'Images', 0, 1, '2025-09-08 07:14:30', '2025-09-08 07:14:30', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (61, 'community program', 'community program', '/static/uploads/gallery_1757316293_community_progam-1.jpeg', '2025-03-02', 'Images', 0, 1, '2025-09-08 07:24:53', '2025-09-08 07:24:53', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (62, 'community program', '', '/static/uploads/gallery_1757316312_community_program-2.jpeg', '2025-03-02', 'Images', 0, 1, '2025-09-08 07:25:12', '2025-09-08 07:25:12', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (63, 'community program', '', '/static/uploads/gallery_1757316327_community_program-3.jpeg', '2025-03-02', 'Images', 0, 1, '2025-09-08 07:25:27', '2025-09-08 07:25:27', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (64, 'community program', '', '/static/uploads/gallery_1757316338_community_program-4.jpeg', '2025-03-02', 'Images', 0, 1, '2025-09-08 07:25:38', '2025-09-08 07:25:38', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (65, 'community program', '', '/static/uploads/gallery_1757316351_community_program-5.jpeg', '2025-03-02', 'Images', 0, 1, '2025-09-08 07:25:51', '2025-09-08 07:25:51', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (66, 'community program', '', '/static/uploads/gallery_1757316366_community_program-8.jpeg', '2025-03-02', 'Images', 0, 1, '2025-09-08 07:26:06', '2025-09-08 07:26:06', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (67, 'community program', '', '/static/uploads/gallery_1757316379_community_progrm-6.jpeg', '2025-03-02', 'Images', 0, 1, '2025-09-08 07:26:19', '2025-09-08 07:26:19', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (68, 'Self Defense Workshop', '', '', '2025-03-01', 'Videos', 0, 1, '2025-09-08 07:26:56', '2025-09-08 07:26:56', '/static/uploads/gallery_1757328808_self_defence.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (69, 'community program', '', '', '2025-03-02', 'Videos', 0, 1, '2025-09-08 07:27:37', '2025-09-08 07:27:37', '/static/uploads/gallery_1757329202_community_program.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (70, 'Self Defense Workshop', '', '/static/uploads/gallery_1757316744_self_defence-6.jpeg', '2025-03-01', 'Images', 0, 1, '2025-09-08 07:32:24', '2025-09-08 07:32:24', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (71, 'intiatives', '', '/static/uploads/gallery_1757317440_intiatives_-1.jpeg', '2025-03-03', 'Images', 0, 1, '2025-09-08 07:44:00', '2025-09-08 07:44:00', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (72, 'initiatives', '', '/static/uploads/gallery_1757317456_intiatives-2.jpeg', '2025-03-03', 'Images', 0, 1, '2025-09-08 07:44:16', '2025-09-08 07:44:16', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (73, 'women''s day', '', '/static/uploads/gallery_1757317485_womens_day.jpeg', '2025-03-08', 'Images', 0, 1, '2025-09-08 07:44:45', '2025-09-08 07:44:45', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (74, 'Shakthi WhatsApp', '', '/static/uploads/gallery_1757317586_watsapp_for_shakthi.jpeg', '2025-05-28', 'Images', 0, 1, '2025-09-08 07:46:26', '2025-09-08 07:46:26', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (75, 'community program', '', '/static/uploads/gallery_1757396059_community_program-4.jpeg', '2025-03-08', 'Images', 0, 1, '2025-09-08 07:47:11', '2025-09-08 07:47:11', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (76, 'community program', '', '/static/uploads/gallery_1757396090_community_program-5.jpeg', '2025-03-08', 'Images', 0, 1, '2025-09-08 07:48:57', '2025-09-08 07:48:57', '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (77, 'community program-2', '', '', '2025-02-03', 'Videos', 0, 1, '2025-09-08 10:55:36', '2025-09-08 10:55:36', '/static/uploads/gallery_1757330002_community_program-2.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (78, 'women safety tips', 'women safety tips and about shakthi app', '/static/uploads/gallery_1762940034_Screenshot_2025-11-12_144603.png', '2025-10-05', 'Images', 0, 1, NULL, NULL, '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (80, 'self defence', 'children self defense', '/static/images/slide2.jpg', '72025-02-20', 'Videos', 0, 1, NULL, NULL, '/static/uploads/gallery_1762941714_videoplayback.mp4');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (81, 'ap wowen self defence awareness week', 'this shows how women should behave in present days', '/static/uploads/gallery_1762945168_self_defence.jpg', '2026-02-10', 'Upcoming Events', 0, 1, NULL, NULL, '');
INSERT INTO public.gallery_items (id, title, description, image_url, event_date, category, is_featured, is_active, created_at, updated_at, video_url) VALUES (54, 'Cyber Security Awareness Week for all police officers', 'Week-long digital safety program', '', '2026-02-10', 'Upcoming Events', 0, 1, '2025-09-02 12:03:55', '2025-09-02 12:03:55', '');


--
-- Data for Name: home_content; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.home_content (id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active, created_at, updated_at) VALUES (8, 'hero', 'Andhra Pradesh Women & Child Safety Wing', 'Dedicated to ensuring the safety and security of women and children across Andhra Pradesh. Join us in creating a safer community for everyone.', '/static/images/hero-bg.jpg', '#contact', 'fas fa-shield-alt', 1, 1, '2025-08-25 07:37:31', '2025-08-25 07:37:31');
INSERT INTO public.home_content (id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active, created_at, updated_at) VALUES (9, 'features', 'Emergency Response', '24/7 emergency helpline and rapid response system for women in distress.', NULL, NULL, 'fas fa-phone-alt', 1, 1, '2025-08-25 07:37:31', '2025-08-25 07:37:31');
INSERT INTO public.home_content (id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active, created_at, updated_at) VALUES (10, 'features', 'Safety Education', 'Comprehensive safety awareness programs and self-defense training workshops.', NULL, NULL, 'fas fa-graduation-cap', 2, 1, '2025-08-25 07:37:31', '2025-08-25 07:37:31');
INSERT INTO public.home_content (id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active, created_at, updated_at) VALUES (11, 'features', 'Community Support', 'Building strong community networks to support and protect women and children.', NULL, NULL, 'fas fa-hands-helping', 3, 1, '2025-08-25 07:37:31', '2025-08-25 07:37:31');
INSERT INTO public.home_content (id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active, created_at, updated_at) VALUES (12, 'features', 'Legal Assistance', 'Free legal aid and counseling services for victims of violence and harassment.', NULL, NULL, 'fas fa-gavel', 4, 1, '2025-08-25 07:37:31', '2025-08-25 07:37:31');
INSERT INTO public.home_content (id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active, created_at, updated_at) VALUES (13, 'statistics', '10,000+', 'Women Helped', NULL, NULL, 'fas fa-female', 1, 1, '2025-08-25 07:37:31', '2025-08-25 07:37:31');
INSERT INTO public.home_content (id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active, created_at, updated_at) VALUES (14, 'statistics', '50+', 'Safety Programs', NULL, NULL, 'fas fa-clipboard-list', 2, 1, '2025-08-25 07:37:31', '2025-08-25 07:37:31');
INSERT INTO public.home_content (id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active, created_at, updated_at) VALUES (15, 'statistics', '100+', 'Volunteers', NULL, NULL, 'fas fa-users', 3, 1, '2025-08-25 07:37:31', '2025-08-25 07:37:31');
INSERT INTO public.home_content (id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active, created_at, updated_at) VALUES (16, 'statistics', '24/7', 'Emergency Support', NULL, NULL, 'fas fa-clock', 4, 1, '2025-08-25 07:37:31', '2025-08-25 07:37:31');
INSERT INTO public.home_content (id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active, created_at, updated_at) VALUES (17, 'testimonials', 'Life-Changing Support', 'The safety wing helped me when I needed it most. Their quick response and compassionate support changed my life. - Priya, Hyderabad', NULL, NULL, 'fas fa-quote-left', 1, 1, '2025-08-25 07:37:31', '2025-08-25 07:37:31');
INSERT INTO public.home_content (id, section_name, title, content, image_url, link_url, icon_class, sort_order, is_active, created_at, updated_at) VALUES (18, 'testimonials', 'Excellent Training', 'The self-defense workshop gave me confidence and practical skills to protect myself. Highly recommended! - Sunitha, Vijayawada', NULL, NULL, 'fas fa-star', 2, 1, '2025-08-25 07:37:31', '2025-08-25 07:37:31');


--
-- Data for Name: initiatives; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.initiatives (id, title, description, image_url, is_featured, is_active, created_at, updated_at) VALUES (2, 'Victim Support Center (ASHRAYA)', 'Shelter homes for survivors of violence.
Counselling services for psychological and emotional support.
Assistance in employment and financial independence.
Collection of data and monitoring of victim''s compensation scheme.', '/static/uploads/initiative_1756211934_WhatsApp_Image_2025-08-26_at_6.08.17_PM.jpeg', 1, 1, '2025-08-23 14:02:47', '2025-08-23 14:02:47');
INSERT INTO public.initiatives (id, title, description, image_url, is_featured, is_active, created_at, updated_at) VALUES (3, 'Domestic Violence cell', 'addresses domestic violence cases and provides support to victims.
1.Counselling & Empowerment Cell: -Offers immediate support and counselling services for domestic violence victims.
2.NRI Cell: - Assists women facing domestic violence in NRI marriages and coordinates with international authorities.', '/static/uploads/initiative_1756381284_dvc.jpg', 0, 1, '2025-08-23 14:02:47', '2025-08-23 14:02:47');
INSERT INTO public.initiatives (id, title, description, image_url, is_featured, is_active, created_at, updated_at) VALUES (4, 'Anti Human Trafficking Cell (AHTC)', 'Anti Human Trafficking Cell (AHTC): Dedicated for preventing and investigating human trafficking cases.
	** Works on tracking traffickers, rescuing victims, and ensuring rehabilitation. Conducts Operations in collaboration with line departments and NGOs for rescuing children from child labor, and ensuring rehabilitation.

', '/static/uploads/initiative_1756382058_ahtc.jpg', 0, 1, '2025-08-23 14:02:47', '2025-08-23 14:02:47');
INSERT INTO public.initiatives (id, title, description, image_url, is_featured, is_active, created_at, updated_at) VALUES (5, 'Eve Teasing Prevention Cell (ETPC)', 'Eve Teasing Prevention Cell (ETPC): Focus on curbing public harassment and ensuring women''s safety in public spaces.

Shakthi Team: Rapid response teams patrol public places to prevent street harassment. 

WEA (Women Empowerment &Awareness): Engage the public through awareness programs on existing legal provisions, carrier guidance and skill development programs.  The team shall also conduct self-defense training programs and awareness sessions in Schools and Colleges.  

CEO (Community Engagement & Outreach): The Women Protection Committees in collaboration with NGOs, Civil Society Organizations conducts safety level programs in community level. 



', '/static/uploads/initiative_1756445723_eve_teasing.jpeg', 0, 1, '2025-08-23 14:02:47', '2025-08-23 14:02:47');
INSERT INTO public.initiatives (id, title, description, image_url, is_featured, is_active, created_at, updated_at) VALUES (6, 'POSH (Sexual Harassment at Workplaces)', 'POSH: Handles complaints of workplace harassment and ensures compliance with POSH Act guidelines.

Coordinates with corporate and government organizations to establish Internal Complaints Committees (ICCs).
', '/static/uploads/initiative_1756445848_posh.jpeg', 0, 1, '2025-08-23 14:02:47', '2025-08-23 14:02:47');
INSERT INTO public.initiatives (id, title, description, image_url, is_featured, is_active, created_at, updated_at) VALUES (7, 'Transgender Persons Protection Cell', 'Works to prevent discrimination and violence against LGBTQIA++ individuals.

SELF (Self Esteem Liberty & Fraternity): A support center offering legal aid, counselling, and rehabilitation for the LGBTQIA++ community.', '/static/uploads/initiative_1756452480_tglb.jpeg', 0, 1, '2025-08-29 07:28:00', '2025-08-29 07:28:00');
INSERT INTO public.initiatives (id, title, description, image_url, is_featured, is_active, created_at, updated_at) VALUES (8, 'CSS (Cyber Safety &Surveillance)', 'Uses technology to enhance safety measures and improve law enforcement response.Conducts forensic analysis of digital evidence.Monitors and analyzes cybercrimes related to women and children. Coordination with social media platforms and cyber forensic experts.

CAP (Cyber Awareness Program): Cyber awareness campaigns will be conducted to create awareness among the Women & Children to not to became cyber victims. 
', '/static/uploads/initiative_1756454313_css2.jpeg', 0, 1, '2025-08-29 07:34:13', '2025-08-29 07:34:13');
INSERT INTO public.initiatives (id, title, description, image_url, is_featured, is_active, created_at, updated_at) VALUES (9, 'WHER(Women Help Line Emergency Response):', 'This Centre functions round the clock (24/7) and attends all calls received on Help Line numbers such as 1098, 112/100,181 and immediately inform/forward the information to concern jurisdiction for redressal. ', '/static/uploads/initiative_1756453328_wher1.jpeg', 0, 1, '2025-08-29 07:42:08', '2025-08-29 07:42:08');
INSERT INTO public.initiatives (id, title, description, image_url, is_featured, is_active, created_at, updated_at) VALUES (10, 'CCC(Command & Control Centre)', 'Monitoring & Data Analytics (MDA): The center shall obtain the information in respect of Women & Child cases from all units and consolidated the data to analyze the crime trends periodically. 

', '/static/uploads/initiative_1756453419_css.jpeg', 0, 1, '2025-08-29 07:43:39', '2025-08-29 07:43:39');


--
-- Data for Name: media_gallery; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: navigation_menu; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: officers; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.officers (id, name, designation, department, phone, email, image_url, bio, position_order, is_active) VALUES (1, 'Sri Harish Kumar Guptha., IPS', 'Director General of Police', 'Andhra Pradesh Police', '0863-1213456', 'dgp@appolice.gov.in', '/static/uploads/officer_1756206065_dg_sir.jpg', '', 1, '1');
INSERT INTO public.officers (id, name, designation, department, phone, email, image_url, bio, position_order, is_active) VALUES (2, 'Sri N.Madhusudhan Reddy., IPS', 'Additional Director General of Police', 'Andhra Pradesh Police', '0863-2340454', 'adglocamp@gmail.com', '/static/uploads/officer_1756206467_adg_sir.jpg', '', 2, '1');
INSERT INTO public.officers (id, name, designation, department, phone, email, image_url, bio, position_order, is_active) VALUES (3, 'B.Rajakumari., IPS', 'Inspector General of Police', 'Andhra Pradesh Police', '0864-5237348', 'womensafety@appolice.gov.in', '/static/uploads/officer_1756207063_slide3.jpg', '', 3, '1');


--
-- Data for Name: one_stop_centers; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (27, 1, 'One Stop Center Alluri Sitarama Raju', 'One Stop Center,Govt General Hospital,Paderu -523 241', 'WSI D.Shankuntala', '+91-7013015028', 'Counseling, Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (28, 2, 'One Stop Center Anakapalli', 'OSC,Govt NTR Hospital Compound,Anakapalli 531 001', 'WSI B.Yamuna', '+91-9912498784', 'Counseling, Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (29, 3, 'One Stop Center Ananthapuramu', 'OSC,Govt general hospital,Ananthapur -524 344', 'WSI B.Bharathi', '+91-7032145434', 'Counseling, Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (30, 4, 'One Stop Center Annamayya', 'OSC,S.N.Colony,Near governor function hall, Rayachoty-516 269', 'WSI P.Ramadevi', '+91-8897336061', 'Counseling,Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (31, 5, 'One Stop Center Bapatla', 'OSC,Akbar peta,Near gurukulapatasala Opposite,Sakhi one stop center- 522 101', 'WHC M.Lakshmi', '+91-8500328568', 'Counseling, Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (32, 6, 'One Stop Center Chittoor', 'OSC,Govt hospital premises,Chittoor-517 001', 'WASI R.P.Sujatha', '+91-9441914166', 'Counseling,Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (33, 7, 'One Stop Center East Godavari', 'OSC,O/o DWCWEO Mahila Pranghanam,Bommuru,East Godavari-533 124', 'WSI Sk.Ameen Begum', '+91-9494969414', 'Counseling,Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (34, 8, 'One Stop Center, Eluru', 'OSC,Beside TB Wardat Govt Genaral Hospital,Ramachandrarao peta,Eluru -534 001', 'WSI Y.Bharathi', '+91-9395596275', 'Counseling, Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (35, 9, 'One Stop Center Guntur', 'OSC,Opposite Zilla Parishad,Mahila Pranganam Premises,Guntur-522 002', 'WHC S.Jayamani', '+91-7386500097', 'Counseling,Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (36, 10, 'One Stop Center Kakinada', 'OSC,Beside dept of forensic medicine and toxicology,Govt Hospital,Kakinada-533 001', 'WSI K.S.Chandra', '+91-7396614777', 'Counseling, Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (37, 11, 'One Stop Center Konaseema', 'OSC,Near Red Bridge,APIIC Colony,Amalapuram - 533 201', 'WSI P.Ganga Bhavani', '+91-6302066686', 'Counseling, Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (38, 12, 'One Stop Center Krishna', 'OSC, D.NO.27/271, Patharamanapeta,Beside bala sai degree college near dist govt general hospital road, SAA building 1st floor,Machilipatnam -521 001', 'WSI K.Hymavathi', '+91-9032505054', 'Counseling, Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (39, 13, 'One Stop Center Kurnool', 'Scabicide new gynaec ward,near women PG hostel,govt general hospital, Kurnool-518 002', 'WASI G.Lalitamma', '+91-8500437332', 'Counseling,Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (40, 15, 'One Stop Center NTR', 'OSC,Old govt hospital premises,Hanumanpeta,Vijayawada-520 002', 'WSI M.Premalatha', '+91-9766687897', 'Counseling,Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (41, 14, 'One Stop Center Nandyal', 'OSC,O/o DWCW&EO,Uppara veedi,near anjaneya swami temple,Nandyal 518 501', 'WSI K.Kumari', '+91-8367037525', 'Counseling,Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (42, 16, 'One Stop Center Palnadu', 'OSC,13th line,Mahalakshmi nagar,Pedda cheruvu road,Narasarao peta, Palnadu-522 601', 'WCI K.V.Subashini', '+91-9703616949', 'Counseling, Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (43, 17, 'One Stop Center Parvathipuram', 'One Stop Center,Room NO 29,Area Hospital,Parvathipuram-535 501', 'WSI B.Santhoshi Kumari', '+91-9121109468', 'Counseling, Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (44, 18, 'One Stop Center Prakasam', 'OSC,RIMS Hospital Premises,Bagyanagar,beside D MART, ONGOLE-523 001', 'WASI V.Gowthami', '+91-8309077480', 'Counseling,Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (45, 19, 'One Stop Center Sri Potti Sriramulu Nellore', 'OSC,Dodla Subbareddy Govt Hospitalnear Mahila Police Station SPS Nellore -524 003', 'CI M.Nageswaramma', '+91-9490439604', 'Counseling,Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (46, 20, 'One Stop Center Sri Sathya Sai', 'OSC,C/O-ICDS Office,Near super speciality hospital,Puttaparthi-515 134', 'WSI K.L.Kalavathi', '+91-9490482724', 'Counseling,Shelter', '1', '2025-09-01 08:15:45');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (47, 21, 'One Stop Center', 'One Stop Center,MCH Govt General Hospital,Balaga,Srikakulam', 'WASI K.Renuka Rani', '+91-9492146378', 'shelter for victims', '1', '2025-09-01 09:31:03');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (48, 24, 'One Stop Center ', 'OSC,Near Mahila PS,Govt General Hospital Premises,Beside drug store,Vizianagaram 535 558', 'WASI B.Shoba Rani', '+91-9494973174', '', '1', '2025-09-01 09:48:22');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (49, 23, 'One Stop Center ', 'One Stop Center, KGH Premises,Near Pedeiatric Ward,Maharani peta,Vishakapatnam 530 001', 'WSI B.Adi Lakshmi', '+91-9490898493', '', '1', '2025-09-01 10:12:10');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (50, 25, 'One Stop Center ', 'One Stop Center ,Vuissakoderu Panchayat Building,Palakoderu(M), West Godavari 534 210', 'CI Md.Ahmadunissa', '+91-9182350533', '', '1', '2025-09-01 10:52:02');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (51, 26, 'One Stop Center ', 'OSC,Motuary road,new RIMS campus,kadapa 516 001', 'WSI S.Santamma', '+91-8074289479', '', '1', '2025-09-01 12:13:28');
INSERT INTO public.one_stop_centers (id, district_id, center_name, address, incharge_name, contact_number, services_offered, is_active, created_at) VALUES (52, 22, 'One Stop Center ', 'OSC,Govt metarnity hospital,Tirupathi -517 507', 'WSI P.L.Vasundhara devi', '+91-8125783272', '', '1', '2025-09-01 12:23:44');


--
-- Data for Name: page_content; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: password_reset_tokens; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.password_reset_tokens (id, admin_id, token, created_at, expires_at, used) VALUES (1, 1, 'suH0W4J3UWtlgH5qCcFCPOnGCkfEI9Cx3bGUwFtJNiM', '2025-11-18 16:30:42.317596', '2025-11-18 17:30:42.319115', 0);
INSERT INTO public.password_reset_tokens (id, admin_id, token, created_at, expires_at, used) VALUES (2, 1, 'MU0mePNIoXTVJ3FcpifGLfJumnaS8s_wcNBw85KMugo', '2025-11-18 16:31:35.323938', '2025-11-18 17:31:35.325518', 0);
INSERT INTO public.password_reset_tokens (id, admin_id, token, created_at, expires_at, used) VALUES (3, 1, '6DOHUbCSH3OKNwIn5gDrZX5UEvPu0m65NUwOXS3hCK8', '2025-11-18 16:38:33.202812', '2025-11-18 17:38:33.204785', 0);
INSERT INTO public.password_reset_tokens (id, admin_id, token, created_at, expires_at, used) VALUES (4, 1, 'ptVDYYO8r6OUAOetKCOq4hj5dwO4k41cGBYm29o2q0w', '2025-11-18 17:26:34.76112', '2025-11-18 18:26:34.762658', 0);


--
-- Data for Name: pdf_resources; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pdf_resources (id, title, description, file_name, file_path, icon, download_count, is_active, created_at, updated_at) VALUES (1, 'Dowry prohibition act', 'The Dowry Prohibition Act, 1961 was enacted to prohibit the giving or taking of dowry in all formsâ€”monetary, property, or valuablesâ€”before, during, or after marriage, across all religions in India', 'dowry_prohibition.pdf', '/static/pdfs/dowry_prohibition.pdf', 'fas fa-file-pdf', 0, 1, '2025-08-23 13:55:42', '2025-08-23 13:55:42');
INSERT INTO public.pdf_resources (id, title, description, file_name, file_path, icon, download_count, is_active, created_at, updated_at) VALUES (2, 'Domestic Violence Act', 'The Protection of Women from Domestic Violence Act, 2005 is a law that provides women with protection and legal remedies against physical, emotional, sexual, and economic abuse within domestic relationships.', 'protection_of_women_from_domestic_violence_act_2005.pdf', '/static/pdfs/protection_of_women_from_domestic_violence_act_2005.pdf', 'fas fa-file-pdf', 0, 1, '2025-08-23 13:55:42', '2025-08-23 13:55:42');
INSERT INTO public.pdf_resources (id, title, description, file_name, file_path, icon, download_count, is_active, created_at, updated_at) VALUES (3, 'POSH (Sexual Harassment at Workplaces) Act', 'The POSH Act, 2013 (Prevention of Sexual Harassment at Workplace Act) is a law that ensures protection of women from sexual harassment at the workplace and provides a mechanism for redressal of complaints.', 'posh.pdf', '/static/pdfs/posh.pdf', 'fas fa-file-pdf', 0, 1, '2025-08-23 13:55:42', '2025-08-23 13:55:42');
INSERT INTO public.pdf_resources (id, title, description, file_name, file_path, icon, download_count, is_active, created_at, updated_at) VALUES (4, 'Senior Citizens Act', 'The Maintenance and Welfare of Parents and Senior Citizens Act, 2007 is a law that ensures the care, protection, and maintenance of elderly parents and senior citizens by their children or relatives.', 'senior_citizen_act.pdf', '/static/pdfs/senior_citizen_act.pdf', 'fas fa-file-pdf', 0, 1, '2025-08-23 13:55:42', '2025-08-23 13:55:42');
INSERT INTO public.pdf_resources (id, title, description, file_name, file_path, icon, download_count, is_active, created_at, updated_at) VALUES (5, 'The Prohibition of Child Marriage Act', 'The Prohibition of Child Marriage Act, 2006 is a law that prohibits child marriages in India and provides for their prevention and protection of childrenâ€™s rights.', 'child_marriage.pdf', '/static/pdfs/child_marriage.pdf', 'fas fa-file-pdf', 0, 1, '2025-08-23 13:55:42', '2025-08-23 13:55:42');
INSERT INTO public.pdf_resources (id, title, description, file_name, file_path, icon, download_count, is_active, created_at, updated_at) VALUES (6, 'Nirbhaya Act', 'The Criminal Law (Amendment) Act, 2013â€”popularly known as the Nirbhaya Actâ€”strengthens laws on sexual offences by introducing stricter punishments and new categories of crimes to enhance womenâ€™s safety.', 'Nirbhaya-Act.pdf', '/static/pdfs/Nirbhaya-Act.pdf', 'fas fa-file-pdf', 0, 1, '2025-08-23 13:55:42', '2025-08-23 13:55:42');
INSERT INTO public.pdf_resources (id, title, description, file_name, file_path, icon, download_count, is_active, created_at, updated_at) VALUES (7, 'POCSO Act', 'The Protection of Children from Sexual Offences (POCSO) Act, 2012 is a law that safeguards children from sexual abuse, harassment, and exploitation while ensuring child-friendly procedures for reporting and trial.', 'sexualoffencea2012-32.pdf', '/static/pdfs/sexualoffencea2012-32.pdf', 'fas fa-file-pdf', 0, 1, '2025-08-29 08:31:04', '2025-08-29 08:31:04');
INSERT INTO public.pdf_resources (id, title, description, file_name, file_path, icon, download_count, is_active, created_at, updated_at) VALUES (8, 'SC & ST Act', 'The Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, 1989 is a law that protects SC/ST communities from discrimination, atrocities, and hate crimes, ensuring their dignity and rights.', 'sc__stact.pdf', '/static/pdfs/sc__stact.pdf', 'fas fa-file-pdf', 0, 1, '2025-08-29 08:34:58', '2025-08-29 08:34:58');
INSERT INTO public.pdf_resources (id, title, description, file_name, file_path, icon, download_count, is_active, created_at, updated_at) VALUES (9, 'Equal Remuneration Act', 'this tells about equal remuneration for men and women', 'equal_remuneration_act_1976_0.pdf', '/static/pdfs/equal_remuneration_act_1976_0.pdf', 'fas fa-file-pdf', NULL, 1, NULL, NULL);


--
-- Data for Name: safety_tips; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.safety_tips (id, category, title, icon, tips, is_active, created_at, updated_at) VALUES (1, 'Home Safety', 'Home Safety', 'fas fa-home', 'Always lock doors and windows when leaving home
Install proper lighting around your home
Know your neighbors and maintain good relationships
Keep emergency numbers readily available
Don''t open doors to strangers
Have a safety plan and emergency contact list
Install locks on all windows, especially on the ground floor.', 1, '2025-08-23 13:55:42', '2025-11-12 15:57:44.036917');
INSERT INTO public.safety_tips (id, category, title, icon, tips, is_active, created_at, updated_at) VALUES (2, 'Transportation Safety', 'Transportation Safety', 'fas fa-car', 'Always book verified cab services
Share your ride details with family/friends
Sit behind the driver, not next to them
Keep emergency contacts on speed dial
Trust your instincts if something feels wrong
Avoid traveling alone late at night', 1, '2025-08-23 13:55:42', '2025-11-12 15:58:07.435222');
INSERT INTO public.safety_tips (id, category, title, icon, tips, is_active, created_at, updated_at) VALUES (3, 'Digital Safety', 'Digital Safety', 'fas fa-mobile-alt', 'Keep your social media profiles private
Don''t share personal information online
Be cautious about meeting online friends
Report cyberbullying immediately
Use strong passwords and two-factor authentication
Be aware of online predators and scams', 1, '2025-08-23 13:55:42', '2025-11-12 15:58:22.84878');
INSERT INTO public.safety_tips (id, category, title, icon, tips, is_active, created_at, updated_at) VALUES (4, 'Workplace Safety', 'Workplace Safety', 'fas fa-graduation-cap', 'Know your company''s harassment policy
Report inappropriate behavior immediately
Maintain professional boundaries
Document any incidents of harassment
Seek support from HR or management
Know your rights and legal protections', 1, '2025-08-23 13:55:42', '2025-11-12 15:58:41.28046');
INSERT INTO public.safety_tips (id, category, title, icon, tips, is_active, created_at, updated_at) VALUES (5, 'Public Places', 'Public Places', 'fas fa-users', 'Stay in well-lit, populated areas
Walk confidently and stay alert
Avoid wearing expensive jewelry in public
Keep your phone charged and accessible
Trust your instincts about people and situations
Learn basic self-defense techniques', 1, '2025-08-23 13:55:42', '2025-11-12 15:58:56.532287');
INSERT INTO public.safety_tips (id, category, title, icon, tips, is_active, created_at, updated_at) VALUES (6, 'Emergency Preparedness', 'Emergency Preparedness', 'fas fa-phone', 'Save emergency numbers: 181, 1091, 112
Install safety apps on your phone like SHAKTHI
Inform family about your whereabouts
Keep local police station numbers handy
Know the nearest hospital locations
Have a personal safety plan', 1, '2025-08-23 13:55:42', '2025-11-12 15:59:10.149686');


--
-- Data for Name: shakthi_teams; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (79, 1, 'Unit Team-1', 'WSI D.Sankutala', '+91-7013015028', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (80, 1, 'Unit Team-2', 'SI J.Ratna Raju', '+91-8309600959', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (81, 1, 'SDPO,Paderu', 'SI A.Surya Narayana', '+91-8309749689', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (82, 2, 'Unit Team-1', 'SI A.Venkatewsra Rao', '+91-9291314099', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (83, 2, 'Unit Team-2', 'SI P.V.Ramana', '+91-8332811727', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (84, 2, 'SDPO,Narsipatnam', 'SI G.Uma Maheswara Rao', '+91-9493617565', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (85, 3, 'SDPO Ananthapur Urban', 'SI M.Alla bakash', '+91-8919291452', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (86, 3, 'SDPO Ananthapur Rural', 'SI K.Rambabu', '+91-9346917101', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (87, 3, 'SDPO Guntakal', 'WSI S.Asha begum', '+91-6300801826', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (88, 4, 'Unit Team-1', 'SI Ravindra', '+91-9121100555', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (89, 4, 'SDPO Rajampeta', 'SI V.L.Prasad Reddy', '+91-9121100570', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (90, 4, 'SDPO Rayachoty', 'SI Srinivasa Naik', '+91-6300094042', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (91, 5, 'SDPO Repalle', 'SI M.Sivaiah', '+91-9440900875', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (92, 5, 'SDPO,Chirala', 'SI A.Hari babu', '+91-9849559556', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (93, 5, 'SDPO Bapatla', 'WSI Ch.Chandravathi', '+91-7569137676', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (94, 6, 'Unit Team-1', 'WSI Sk.Karimunissa', '+91-9441393493', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (95, 6, 'Unit Team-2', 'WSI K.Naga sowjanya', '+91-9703480505', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (96, 6, 'SDPO Chitoor', 'WASI M.Krishna veni', '+91-9441865124', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (97, 7, 'Unit Team-1', 'HC 2401 M.Srinivasa Rao', '+91-9390077529', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (98, 7, 'DSP East Zone RJVM', 'SI Ch.V.Ramesh', '+91-9491122811', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (99, 7, 'DSP South Zone RJVM', 'WSI P.D.Lakshmi Prasanna', '+91-8639417879', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (100, 8, 'SDPO Eluru', 'ASI D.Srinivasa Rao', '+91-9395104277', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (101, 8, 'SDPO,Polavaram', 'ASI K.Soma Raju', '+91-8341616289', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (102, 8, 'SDPO,Nuzividu', 'ASI P.Suresh', '+91-8341797222', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (103, 9, 'East Sub Division', 'WSI K.Tharangini', '+91-8688831608', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (104, 9, 'North Sub Division', 'SI P. Mahesh Kumar', '+91-8688831362', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (105, 9, 'South Sub Division', 'WSI B.Jaya rani', '+91-9985714642', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (106, 10, 'Unit Team-1', 'WSI S.Kanaka Durga', '+91-9494544755', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (107, 10, 'Unit Team-2', 'WSI N.Lalitha Devi', '+91-9346327443', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (108, 10, 'SDPO,Kakinada', 'SI M.Venkatewsara Rao', '+91-9705779833', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (109, 11, 'SDPO Amalapuram', 'SI P.Bhagavan Narayana', '+91-7032779799', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (110, 11, 'SDPO,Kothapeta', 'SI S.Murali Mohan', '+91-8712692109', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (111, 11, 'SDPO,Ramachandrapuram', 'SI B.Raghuveer', '+91-9440796570', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (112, 12, 'SDPO Bandar', 'WSI M.Manikyamma', '+91-9440796410', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (113, 12, 'SDPO Gudivada', 'WSI V.Jasmin', '+91-9494382591', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (114, 12, 'SDPO Gannavaram', 'WSI K.Usha Rani', '+91-7993004552', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (115, 13, 'Unit Team-1', 'CI L.Vijaya Lakshmi', '+91-9121101084', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (116, 13, 'Unit Team-2', 'WSI P.Nirmala devi', '+91-9963245706', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (117, 13, 'SDPO Yemmiganur', 'ASI B.Nata Raju', '+91-9160314165', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (118, 15, 'ACP West', 'WSI K.Sarala', '+91-9381937708', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (119, 15, 'ACP Central', 'WSI A.Durgadevi', '+91-9032477788', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (120, 15, 'ACP North', 'WSI M.Adi lakshmi', '+91-9885776534', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (121, 14, 'Unit Team-1', 'HQ Team', '+91-9963875979', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (122, 14, 'SDPO Nandyal', 'WSI G.Dhanamma', '+91-7601024256', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (123, 14, 'SDPO Allagadda', 'WSI Sk.Najeena', '+91-9121101165', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (124, 16, 'Unit Team-1', 'WSI G.Aruna Jyothi', '+91-9705513318', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (125, 16, 'Unit Team-2', 'WSI Sk.Firoz fatima', '+91-9885426262', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (126, 17, 'Unit Team-1', 'ASI P.Srinivasa rao', '+91-9491769473', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (127, 17, 'SDPO,Parvathipuram', 'ASI,P.Sriramulu', '+91-9441567848', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (128, 18, 'Unit Team-1', 'SI P.Venkatewsarlu', '+91-9490566577', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (129, 18, 'Unit Team-2', 'SI Sk.Meeravali', '+91-9908026287', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (130, 19, 'Unit Team-1', 'SI S.Anand Bhaskar Babu', '+91-9948503701', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (131, 19, 'Unit Team-2', 'SI U.Nagaiah', '+91-9441685122', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (132, 20, 'Urban Protection Team', 'Inspector SRI-1', '+91-9000300020', 'Urban areas of Sri Sathya Sai', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (133, 20, 'Rural Safety Team', 'Inspector SRI-2', '+91-9000310020', 'Rural areas of Sri Sathya Sai', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (134, 21, 'Unit Team-1', 'WSI Smt Chandrakala', '+91-8978079866', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (135, 21, 'Unit Team-2', 'SI G.Vasudeva Rao', '+91-9908241356', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (136, 22, 'Unit Team-1', 'WASI G.Rohini', '+91-9493126748', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (137, 22, 'Unit Team-2', 'WASI S.Girija', '+91-9603707691', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (138, 23, 'Commissionerate Team 1', 'RI K.Srinivasa Kumar', '+91-9440904323', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (139, 23, 'Commissionerate Team 2', 'RI T.Uma Maheswara Rao', '+91-9440796026', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (140, 24, 'Unit Team-1', 'WASI B.Bhagyam', '+91-7981121823', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (141, 24, 'Unit Team-2', 'WSI B.Revathi', '+91-9121109437', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (142, 25, 'Unit Team-1', 'SI N.Hari babu', '+91-9440664881', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (143, 25, 'Unit Team-2', 'CI Md.Ahmaduneesa', '+91-9182350533', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (144, 26, 'Unit Team-1', 'WSI K.Santamma', '+91-9063860608', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (145, 26, 'Unit Team-2', 'ASI P.Mohan', '+91-8074289479', '', '1', '2025-09-01 08:15:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (146, 21, 'SDPO Srikakulam', 'SI M.Ravi', '+91-9849596618', '', '1', '2025-09-01 09:27:20');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (147, 21, 'SDPO Tekkali', 'SI Sri Balakrishna', '+91-7396441784', '', '1', '2025-09-01 09:27:50');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (148, 21, 'SDPO Kasibugga', 'SI Sri Rajesh', '+91-7303544559', '', '1', '2025-09-01 09:28:14');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (149, 17, 'SDPO,Palakonda', 'ASI,P.Sursh kumar', '+91-9154242135', '', '1', '2025-09-01 09:36:19');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (150, 24, 'SDPO,Vizianagaram', 'WSI Sk.Nazim Begum', '+91-7842556581', '', '1', '2025-09-01 09:43:42');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (151, 24, 'SDPO Bobbili', 'SI V.Gana Prasad', '+91-8919690805', '', '1', '2025-09-01 09:44:32');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (152, 24, 'SDPO Chepurupalli', 'SI S.Srinivasa Rao', '+91-9492662297', '', '1', '2025-09-01 09:45:28');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (153, 1, 'SDPO,Chintapalli', 'SI V.Venkatewsra Rao', '+91-9440904238', '', '1', '2025-09-01 10:03:01');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (154, 1, 'SDPO,Rampachodavaram', 'SI K.Shaffi', '+91-9440900769', '', '1', '2025-09-01 10:03:52');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (155, 1, 'SDPO,Chinturu', 'WSI L.Latha', '+91-9490617850', '', '1', '2025-09-01 10:04:30');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (156, 23, 'Commissionerate Team 3', 'Beach mobile', '+91-8331041653', '', '1', '2025-09-01 10:09:46');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (157, 23, 'Commissionerate Team 4', 'IT Sez', '+91-8374201699', '', '1', '2025-09-01 10:12:48');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (158, 23, 'ACP East', 'SI K.Narasinga Rao', '+91-9703117526', '', '1', '2025-09-01 10:13:51');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (159, 23, 'ACP Dwaraka', 'SI K.Srinu', '+91-8331041588', '', '1', '2025-09-01 10:14:29');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (160, 23, 'ACP North', 'WASI S.Suseela', '+91-9493527376', '', '1', '2025-09-01 10:15:11');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (161, 23, 'ACP Harbour', 'WSI B.Adi Lakshmi', '+91-9490898493', '', '1', '2025-09-01 10:16:09');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (162, 23, 'ACP South', 'WSI L.Surya Kala', '+91-9542372241', '', '1', '2025-09-01 10:16:51');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (163, 23, 'ACP West', 'WSI J.Divya Bharathi', '+91-7993981948', '', '1', '2025-09-01 10:17:30');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (164, 2, 'SDPO,Anakapalli', 'SI P.Manoj Kumar', '+91-8688096380', '', '1', '2025-09-01 10:22:01');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (165, 2, 'SDPO,Parawada', 'WSI G.S.V.Mahalakshmi', '+91-9182296247', '', '1', '2025-09-01 10:22:52');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (166, 10, 'SDPO,Peddapuram', 'WSI S.Lakshmi Kantham', '+91-9440796570', '', '1', '2025-09-01 10:28:09');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (167, 7, 'DSP North Zone RJVM', 'WSI P.Narayanamma', '+91-9441023561', '', '1', '2025-09-01 10:35:47');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (168, 25, 'SDPO,Narasapuram', 'WSI Ch.Jayalakshmi', '+91-9848578781', '', '1', '2025-09-01 10:48:03');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (169, 25, 'SDPO,Bhimavaram', 'Si Md.Naseerulla', '+91-9440796648', '', '1', '2025-09-01 10:48:54');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (170, 25, 'SDPO,Tadepalligudem', 'SI K.Kondala Rao', '+91-9848278504', '', '1', '2025-09-01 10:49:48');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (171, 12, 'SDPO Avanigadda', 'SI K.Srinivasa Rao', '+91-9440796467', '', '1', '2025-09-01 11:10:08');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (172, 9, 'Tulluru Sub Division', 'SI K.Ramakrishna', '+91-9985714642', '', '1', '2025-09-01 11:15:44');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (173, 9, 'Tenali Sub Division', 'WSI Ch.Rajya Lakshmi', '+91-8978432474', '', '1', '2025-09-01 11:16:29');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (174, 16, 'Unit Team-3', 'WSI K.Aruna', '+91-8501863727', '', '1', '2025-09-01 11:18:43');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (175, 16, 'SDPO Sattenapalli', 'WSI M.Sandya Rani', '+91-8501863727', '', '1', '2025-09-01 11:19:30');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (176, 16, 'SDPO Gurazala', 'WSI G.Sandya Rani', '+91-8639901698', '', '1', '2025-09-01 11:23:34');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (177, 18, 'SDPO Ongole', 'WSI G.Krishna Pavani', '+91-9121104780', '', '1', '2025-09-01 11:45:01');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (178, 18, 'SDPO Darsi', 'SI Sk.Gouse Basha', '+91-9885768776', '', '1', '2025-09-01 11:45:38');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (179, 18, 'SDPO Markapur', 'SI M.Raja mohan Rao', '+91-9121104798', '', '1', '2025-09-01 11:48:46');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (180, 18, 'SDPO Kanigiri', 'SI K.Madhava Rao', '+91-9121102211', '', '1', '2025-09-01 11:49:29');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (181, 19, 'SDPO Nellore Town', 'ASI B.Sudhakar Reddy', '+91-9949268257', '', '1', '2025-09-01 11:51:43');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (182, 19, 'SDPO Nellore Rural', 'ASI J.Subba Raju', '+91-9866356173', '', '1', '2025-09-01 11:52:18');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (183, 19, 'SDPO Kavali', 'WASI B.Sailaja Kumari', '+91-8074848236', '', '1', '2025-09-01 11:55:02');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (184, 19, 'SDPO Atmakur', 'WASI P.Anusha', '+91-9440700013', '', '1', '2025-09-01 11:55:36');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (185, 19, 'SDPO Kandukur', 'ASI P.Isaq Prasad', '+91-9110345185', '', '1', '2025-09-01 11:56:13');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (186, 13, 'SDPO Adoni', 'CI M.Sonakka', '+91-9121101142', '', '1', '2025-09-01 12:02:05');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (187, 13, 'SDPO Pattikonda', 'HC 969 G.Girish Vara Prasad', '+91-9989730969', '', '1', '2025-09-01 12:02:48');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (188, 14, 'SDPO Dhone', 'WSI K.Mamatha', '+91-7286804706', '', '1', '2025-09-01 12:07:16');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (189, 14, 'SDPO Atmakur', 'ASI B.Raghu Ramaiah Goud', '+91-9440505799', '', '1', '2025-09-01 12:08:01');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (190, 26, 'SDPO Kadapa', 'SI E.A.Subash chandra bose', '+91-9885092273', '', '1', '2025-09-01 12:10:16');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (191, 26, 'SDPO Pulivendula', 'SI M.Vishnu Narayana', '+91-9121100547', '', '1', '2025-09-01 12:10:52');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (192, 26, 'SDPO Proddutur', 'SI K.P.B.Venkat Reddy', '+91-9441621864', '', '1', '2025-09-01 12:14:23');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (193, 26, 'SDPO Mydukur', 'SI S.Subba rao', '+91-9121100620', '', '1', '2025-09-01 12:14:52');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (194, 26, 'SDPO Jammalamadugu', 'SI B.Ramakrishna', '+91-9121100604', '', '1', '2025-09-01 12:15:25');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (195, 4, 'SDPO Madanapalli', 'WSI S.Gayatri', '+91-9963263134', '', '1', '2025-09-01 12:18:02');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (196, 22, 'DSP Tirumala L&O', 'SI D.Venkatewsarlu', '+91-9491455322', '', '1', '2025-09-01 12:22:15');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (197, 22, 'DSP Chandragiri', 'WSI M.Aruna', '+91-8978220683', '', '1', '2025-09-01 12:24:35');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (198, 22, 'DSP Renigunta', 'SI P.Aruna Kumar Reddy', '+91-9440796765', '', '1', '2025-09-01 12:25:18');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (199, 22, 'DSP Srikalahasthi', 'SI L.Sudhakar Reddy', '+91-9440900721', '', '1', '2025-09-01 12:25:57');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (200, 22, 'DSP Puttur', 'SI K.Raja sekhar', '+91-9440900693', '', '1', '2025-09-01 12:26:44');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (201, 22, 'DSP Gudur', 'SI B.Gopala', '+91-9100244099', '', '1', '2025-09-01 12:27:15');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (202, 22, 'DSP Naidupeta', 'SI G.Ajay kumar', '+91-9440796359', '', '1', '2025-09-01 12:27:52');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (203, 22, 'DSP Sricity', 'SI A.Hariprasad', '+91-8333992295', '', '1', '2025-09-01 12:28:31');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (204, 22, 'DSP Tirupathi', 'WSI Ch.Saraswathi', '+91-9704461984', '', '1', '2025-09-01 12:29:04');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (205, 6, 'SDPO Palamaner', 'WSI K.Swarna Teja', '+91-9440796734', '', '1', '2025-09-01 12:33:45');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (206, 6, 'SDPO Nagari', 'ASI Emelu Reddy', '+91-9985447582', '', '1', '2025-09-01 12:34:23');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (207, 6, 'SDPO Kuppam', 'SI E.Babu', '+91-8074927671', '', '1', '2025-09-01 12:34:51');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (208, 3, 'SDPO Kalyanadurgam', 'ASI T.Hanumantha Reddy', '+91-9390231216', '', '1', '2025-09-01 12:42:34');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (209, 3, 'SDPO Tadipatri', 'WASI Vijayagowri', '+91-9059710028', '', '1', '2025-09-01 12:43:10');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (210, 15, 'ACP South', 'WASI P.V.Ragini', '+91-8331832353', '', '1', '2025-09-01 12:48:42');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (211, 15, 'ACP Tiruvuru', 'WASI Y.S.M.Lakshmi', '+91-8978257677', '', '1', '2025-09-01 12:49:29');
INSERT INTO public.shakthi_teams (id, district_id, team_name, leader_name, contact_number, area_covered, is_active, created_at) VALUES (212, 15, 'ACP Nandigama', 'ASI L.Ravi kumar', '+91-8341278512', '', '1', '2025-09-01 12:50:04');


--
-- Data for Name: site_settings; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (1, 'site_title', 'AP Women Safety Wing', 'text', 'Main website title', '2025-08-23 15:32:18.249234');
INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (2, 'contact_email', 'info@apwomensafety.gov.in', 'email', 'Primary contact email', '2025-08-23 15:32:18.258234');
INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (3, 'contact_phone', '181', 'phone', 'Primary contact phone', '2025-08-23 15:32:18.266250');
INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (4, 'whatsapp_number', '+919876543210', 'phone', 'WhatsApp support number', '2025-08-23 09:32:56');
INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (5, 'office_address', 'AP Police Headquarters, Mangalagiri, Andhra Pradesh', 'textarea', 'Head office address', '2025-08-23 15:32:18.276090');
INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (6, 'district_map_image', '/static/uploads/ap_district_map.jpg', 'text', NULL, '2025-08-23 10:44:04');
INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (7, 'use_custom_map', 'true', 'text', NULL, '2025-08-23 10:44:04');
INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (9, 'site_description', 'Empowering women through safety, support, and solidarity', 'text', 'Website description', '2025-08-23 14:09:46');
INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (12, 'office_hours', '24/7 Emergency Services Available', 'text', 'Office working hours', '2025-08-23 14:09:46');
INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (13, 'social_facebook', 'https://facebook.com/apwomensafety', 'text', 'Facebook page URL', '2025-08-23 14:09:46');
INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (14, 'social_twitter', 'https://twitter.com/apwomensafety', 'text', 'Twitter page URL', '2025-08-23 14:09:46');
INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (15, 'enable_chatbot', 'true', 'boolean', 'Enable/disable chatbot', '2025-08-23 14:09:46');
INSERT INTO public.site_settings (id, setting_key, setting_value, setting_type, description, updated_at) VALUES (16, 'maintenance_mode', 'false', 'boolean', 'Enable maintenance mode', '2025-08-23 14:09:46');


--
-- Data for Name: success_stories; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.success_stories (id, title, story_content, image_url, location, date_occurred, position_order, is_active, description, date, stat1_number, stat1_label, stat2_number, stat2_label, stat3_number, stat3_label, sort_order) VALUES (1, 'Shakthi traced out missing person', 'A 28-year-old software engineer from Hyderabad was being stalked by an unknown person. She used the SHE Teams helpline and within 30 minutes, our team tracked down the culprit and took immediate action. The woman expressed her gratitude for the prompt response.', '/static/uploads/success_story_1756377890_success_stories2.jpg', 'Hyderabad', '2024-01-15', 1, '1', 'The SHAKTHI TEAM  members are traced out the missing person Puvvalal Kavya age 24 years, H/o. P. Ramesh, Labour Colony, Tekkali Mandal,  Srikakulam Dist.,  through Instagram (ID: golden_sunshine125) & conducted family counselling hand over to her parents on 20.05.2025.', '20-05-2025', NULL, NULL, NULL, NULL, NULL, NULL, 2);
INSERT INTO public.success_stories (id, title, story_content, image_url, location, date_occurred, position_order, is_active, description, date, stat1_number, stat1_label, stat2_number, stat2_label, stat3_number, stat3_label, sort_order) VALUES (2, 'Quick response to SOS by Shakthi team', 'A housewife from Vijayawada reached out through our helpline regarding domestic violence. Our counselors provided immediate support and legal guidance. The case was resolved through mediation and the family is now living peacefully.', '/static/uploads/success_story_1756377749_success_stories3.jpg', 'Vijayawada', '2024-01-10', 2, '1', 'We received SOS 03:59PM from the caller Veera Narayan A/41 Yrs, Vinukonda PS limits, Palanadu Dist. Caller stated that his son (Mannam Lakshman A/14 Yrs) was missing from 8 days, on that day he attended for  10 th class science exams at school and went away. On the caller gave complaint at PS and also they enquired possible locations like  in bus station, Railway station and etc. based o enquiry  they came to know that he had reserved a ticket to tirupathi on 02/03/2025. But  his where and abouts were not known. on that we informed to SHO of Vinukonda  PS. SHO stated that in this case a FIR with Cr. No: 43/2025 U/S boy missing on Date : 04/03/2025 of Vinukonda PS was registered. Based on FIR  Police staff traced missing boy and handed over to his family members on 19.03.2025 AN.', '19-03-2025', NULL, NULL, NULL, NULL, NULL, NULL, 3);
INSERT INTO public.success_stories (id, title, story_content, image_url, location, date_occurred, position_order, is_active, description, date, stat1_number, stat1_label, stat2_number, stat2_label, stat3_number, stat3_label, sort_order) VALUES (3, 'Shakthi team saved a women life', 'A college student was being blackmailed through social media. Our cyber crime team quickly traced the perpetrator and recovered the compromised content. The victim was provided counseling support.', '/static/uploads/success_story_1756377284_Picture1.jpg', 'Visakhapatnam', '2024-01-05', 3, '1', 'A Married woman namely Vinjamuri Sirisha W/o Rajesh  Age 38 Chodidhibba, Tangellamudi, Eluru Dist. went to near Railway track and commit suicide.  Due to   she is facing unbearable family problem.  While shakthi teams moving the surrounding of their respective jurisdiction, they found the said women and rescued.  After that they gave counseling and handed over to her family members.', '23-05-2025', NULL, NULL, NULL, NULL, NULL, NULL, 1);


--
-- Data for Name: volunteer_scores; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.volunteer_scores (id, volunteer_id, age_score, education_score, motivation_score, skills_score, total_score, status, admin_notes, created_at) VALUES (1, 4, NULL, NULL, NULL, NULL, NULL, 'rejected', 'Fixed NULL ID record', NULL);
INSERT INTO public.volunteer_scores (id, volunteer_id, age_score, education_score, motivation_score, skills_score, total_score, status, admin_notes, created_at) VALUES (3, 1, NULL, NULL, NULL, NULL, NULL, 'approved', 'Fixed NULL ID record', NULL);
INSERT INTO public.volunteer_scores (id, volunteer_id, age_score, education_score, motivation_score, skills_score, total_score, status, admin_notes, created_at) VALUES (4, 3, NULL, NULL, NULL, NULL, NULL, 'rejected', 'Fixed NULL ID record', NULL);
INSERT INTO public.volunteer_scores (id, volunteer_id, age_score, education_score, motivation_score, skills_score, total_score, status, admin_notes, created_at) VALUES (5, 2, NULL, NULL, NULL, NULL, NULL, 'rejected', 'Fixed NULL ID record', NULL);
INSERT INTO public.volunteer_scores (id, volunteer_id, age_score, education_score, motivation_score, skills_score, total_score, status, admin_notes, created_at) VALUES (2, 5, NULL, NULL, NULL, NULL, NULL, 'approved', 'Fixed NULL ID record
Status updated to approved', NULL);


--
-- Data for Name: volunteers; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.volunteers (id, registration_id, name, email, phone, age, address, occupation, education, experience, motivation, availability, skills, created_at) VALUES (1, 'VOL-2025-0001', 'vijay', 'yesu@gmail.com', '9959156155', 23, 'bhavanipuram,vijayawada.', 'social worker', 'graduate', 'worked as a volunteer for last 02 years', 'i am very much interested in this field', 'weekends', 'telugu ,english', '2025-09-10 13:22:30');
INSERT INTO public.volunteers (id, registration_id, name, email, phone, age, address, occupation, education, experience, motivation, availability, skills, created_at) VALUES (2, 'VOL-2025-0002', 'surendra', 'surinukathoti.262@gmail.com', '9959156196', 32, '1-9-224/1 
undavalli
vijayawada', 'social worker', 'graduate', 'i have interested in this i have 02 years of volunteer experience', 'yes i am very much helpful to people', 'weekends', 'English ', '2025-10-30 08:04:47');
INSERT INTO public.volunteers (id, registration_id, name, email, phone, age, address, occupation, education, experience, motivation, availability, skills, created_at) VALUES (3, 'VOL-2025-0003', 'narayana', 'meta25.aihackathon@gmail.com', '9959153189', 35, 'podili,prakasam ', 'social worker', 'graduate', 'i have no experience sir ', 'i am very eager to join this program ', 'weekdays', 'English ', '2025-11-10 07:27:21');
INSERT INTO public.volunteers (id, registration_id, name, email, phone, age, address, occupation, education, experience, motivation, availability, skills, created_at) VALUES (4, 'VOL-2025-0004', 'surendra reddy', 'surinukathoti.252@gmail.com', '9959156197', 32, '1-9-224/1 
undavalli
vijayawada', 'social worker', 'graduate', 'i have no experience', 'i am interested in this field to work for poor', 'weekdays', 'English ', '2025-11-12 17:38:02');
INSERT INTO public.volunteers (id, registration_id, name, email, phone, age, address, occupation, education, experience, motivation, availability, skills, created_at) VALUES (5, 'VOL-2025-0005', 'narayana', 'meta2.aihackathon@gmail.com', '9959143121', 33, '1-9-224/1 
undavalli
vijayawada', 'social worker', 'graduate', 'i have 3 years of experience in volunteer', 'i am specially intersted in this field for the purpose of service to poor', 'weekdays', 'English ', NULL);


--
-- Data for Name: women_police_stations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (27, 1, 'Women Police Station Alluri Sitarama Raju', 'SI Srinivasa Rao', '+91-7013015028', 'Alluri Sitarama Raju District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (28, 2, 'Women Police Station Anakapalli', 'Circle Inspector ', '+91-9440904207', 'Anakapalli District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (29, 3, 'Women Police Station Ananthapuramu', 'Circle Inspector ', '+91-9392918037', 'Ananthapuramu District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (30, 4, 'Women Police Station Annamayya', 'Circle Inspector ', '+91-9154960163', 'Women PS at SP Office,Annamayya District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (31, 5, 'Women Police Station Bapatla', 'Circle Inspector', '+91-8978777273', 'Women PS at SP Office,Bapatla District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (32, 6, 'Women Police Station Chittoor', 'Circle Inspector ', '+91-9491086012', 'Chittoor District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (33, 7, 'Women Police Station East Godavari', 'Circle Inspector ', '+91-9493206402', 'East Godavari District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (34, 8, 'Women Police Station Eluru', 'Circle Inspector ', '+91-9440796609', 'Eluru District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (35, 9, 'Women Police Station Guntur', 'Circle Inspector ', '+91-8688831469', 'Guntur District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (36, 10, 'Women Police Station Kakinada', 'Circle Inspector ', '+91-8332957920', 'Kakinada District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (37, 11, 'Women Police Station Konaseema', 'Circle Inspector ', '+91-9441192739', 'Women PS at SP Office ,Konaseema District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (38, 12, 'Women Police Station Krishna', 'Circle Inspector ', '+91-9491063904', 'Krishna District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (39, 13, 'Women Police Station Kurnool', 'Circle Inspector ', '+91-9121101040', 'Kurnool District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (40, 15, 'Women Police Station NTR', 'Circle Inspector ', '+91-9392917735', 'NTR District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (41, 14, 'Women Police Station Nandyal', 'Circle Inspector ', '+91-9154987036', 'Nandyal District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (42, 16, 'Women Police Station Palnadu', 'Circle Inspector', '+91-9440796245', 'Palnadu District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (43, 17, 'Women PS,Manyam', 'CI T.Sarada', '+91-9908667407', 'Women PS,Manyam located at SP office', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (44, 18, 'Women Police Station Prakasam', 'Circle Inspector ', '+91-9121104797', 'Prakasam District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (45, 19, 'Women Police Station Sri Potti Sriramulu Nellore', 'Circle Inspector ', '+91-9398960140', 'Sri Potti Sriramulu Nellore District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (46, 20, 'Women Police Station Sri Sathya Sai', 'Circle Inspector ', '+91-9281107070', 'Sri Sathya Sai District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (47, 21, 'Women PS,Srikakulam', 'Smt T.Trinetri,CI', '+91-6309990836', 'Women PS,Srikakulam', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (48, 22, 'Women Police Station Tirupati', 'Circle Inspector ', '+91-9490617874', 'Tirupati District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (49, 23, 'Women Police Station Visakhapatnam', 'CI G.Malleswari', '+91-7995093610', 'Visakhapatnam District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (50, 24, 'Women Police Station Vizianagaram', 'CI E.Narasimha Murhty', '+91-9121109496', 'Vizianagaram District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (51, 25, 'Women Police Station West Godavari', 'Circle Inspector ', '+91-9182350533', 'West Godavari District, Andhra Pradesh', '1', '2025-09-01 08:15:45');
INSERT INTO public.women_police_stations (id, district_id, station_name, incharge_name, contact_number, address, is_active, created_at) VALUES (52, 26, 'Women Police Station YSR (Kadapa)', 'DSP Bala swamy Reddy', '+91-9121100535', '', '1', '2025-09-01 08:15:45');


--
-- Name: admin_credentials_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.admin_credentials_id_seq', 1, true);


--
-- Name: contact_info_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contact_info_id_seq', 16, false);


--
-- Name: district_sps_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.district_sps_id_seq', 55, false);


--
-- Name: email_otp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.email_otp_id_seq', 5, true);


--
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.events_id_seq', 1, false);


--
-- Name: gallery_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.gallery_items_id_seq', 82, false);


--
-- Name: home_content_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.home_content_id_seq', 19, false);


--
-- Name: initiatives_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.initiatives_id_seq', 12, true);


--
-- Name: officers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.officers_id_seq', 6, true);


--
-- Name: one_stop_centers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.one_stop_centers_id_seq', 54, true);


--
-- Name: password_reset_tokens_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.password_reset_tokens_id_seq', 4, true);


--
-- Name: pdf_resources_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pdf_resources_id_seq', 10, true);


--
-- Name: safety_tips_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.safety_tips_id_seq', 8, false);


--
-- Name: shakthi_teams_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shakthi_teams_id_seq', 214, true);


--
-- Name: success_stories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.success_stories_id_seq', 4, true);


--
-- Name: volunteer_scores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.volunteer_scores_id_seq', 6, true);


--
-- Name: volunteers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.volunteers_id_seq', 5, true);


--
-- Name: women_police_stations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.women_police_stations_id_seq', 56, true);


--
-- Name: admin_credentials admin_credentials_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin_credentials
    ADD CONSTRAINT admin_credentials_pkey PRIMARY KEY (id);


--
-- Name: admin_credentials admin_credentials_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin_credentials
    ADD CONSTRAINT admin_credentials_username_key UNIQUE (username);


--
-- Name: email_otp email_otp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.email_otp
    ADD CONSTRAINT email_otp_pkey PRIMARY KEY (id);


--
-- Name: password_reset_tokens password_reset_tokens_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.password_reset_tokens
    ADD CONSTRAINT password_reset_tokens_pkey PRIMARY KEY (id);


--
-- Name: password_reset_tokens password_reset_tokens_token_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.password_reset_tokens
    ADD CONSTRAINT password_reset_tokens_token_key UNIQUE (token);


--
-- Name: email_otp email_otp_admin_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.email_otp
    ADD CONSTRAINT email_otp_admin_id_fkey FOREIGN KEY (admin_id) REFERENCES public.admin_credentials(id) ON DELETE CASCADE;


--
-- Name: password_reset_tokens password_reset_tokens_admin_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.password_reset_tokens
    ADD CONSTRAINT password_reset_tokens_admin_id_fkey FOREIGN KEY (admin_id) REFERENCES public.admin_credentials(id) ON DELETE CASCADE;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT ALL ON SCHEMA public TO women_safety_user;


--
-- Name: TABLE about_content; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.about_content TO women_safety_user;


--
-- Name: TABLE admin_security; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.admin_security TO women_safety_user;


--
-- Name: TABLE admin_security_questions; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.admin_security_questions TO women_safety_user;


--
-- Name: TABLE admin_settings; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.admin_settings TO women_safety_user;


--
-- Name: TABLE contact_info; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.contact_info TO women_safety_user;


--
-- Name: TABLE content; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.content TO women_safety_user;


--
-- Name: TABLE district_info; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.district_info TO women_safety_user;


--
-- Name: TABLE district_sps; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.district_sps TO women_safety_user;


--
-- Name: TABLE districts; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.districts TO women_safety_user;


--
-- Name: TABLE email_notifications; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.email_notifications TO women_safety_user;


--
-- Name: TABLE emergency_numbers; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.emergency_numbers TO women_safety_user;


--
-- Name: TABLE events; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.events TO women_safety_user;


--
-- Name: TABLE gallery_items; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.gallery_items TO women_safety_user;


--
-- Name: TABLE home_content; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.home_content TO women_safety_user;


--
-- Name: TABLE initiatives; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.initiatives TO women_safety_user;


--
-- Name: TABLE media_gallery; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.media_gallery TO women_safety_user;


--
-- Name: TABLE navigation_menu; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.navigation_menu TO women_safety_user;


--
-- Name: TABLE officers; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.officers TO women_safety_user;


--
-- Name: TABLE one_stop_centers; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.one_stop_centers TO women_safety_user;


--
-- Name: TABLE page_content; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.page_content TO women_safety_user;


--
-- Name: TABLE pdf_resources; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.pdf_resources TO women_safety_user;


--
-- Name: TABLE safety_tips; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.safety_tips TO women_safety_user;


--
-- Name: TABLE shakthi_teams; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.shakthi_teams TO women_safety_user;


--
-- Name: TABLE site_settings; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.site_settings TO women_safety_user;


--
-- Name: TABLE success_stories; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.success_stories TO women_safety_user;


--
-- Name: TABLE volunteer_scores; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.volunteer_scores TO women_safety_user;


--
-- Name: TABLE volunteers; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.volunteers TO women_safety_user;


--
-- Name: TABLE women_police_stations; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.women_police_stations TO women_safety_user;


--
-- PostgreSQL database dump complete
--

\unrestrict LhUZk0yly9JUtOEqGZF6yRR6DsJdPMvhkaBH9J77d3eBe0Z3WDMTIgBGZ1S2boZ

