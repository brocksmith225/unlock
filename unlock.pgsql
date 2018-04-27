--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'SQL_ASCII';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: bmail_emails; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE bmail_emails (
    title character varying(100),
    body character varying(1000),
    sender character varying(100),
    tags character varying(100),
    account character varying(40)
);


ALTER TABLE public.bmail_emails OWNER TO ubuntu;

--
-- Name: bmail_users; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE bmail_users (
    account character varying(40) NOT NULL,
    pwd character varying(64)
);


ALTER TABLE public.bmail_users OWNER TO ubuntu;

--
-- Name: nile_items; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE nile_items (
    name character varying(100),
    price character varying(10),
    images character varying(100),
    tags character varying(200)
);


ALTER TABLE public.nile_items OWNER TO ubuntu;

--
-- Name: nile_users; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE nile_users (
    account character varying(40) NOT NULL,
    pwd character varying(64)
);


ALTER TABLE public.nile_users OWNER TO ubuntu;

--
-- Name: pursue_actions; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE pursue_actions (
    account character varying(64),
    name character varying(200),
    type character varying(20),
    change character varying(20)
);


ALTER TABLE public.pursue_actions OWNER TO ubuntu;

--
-- Name: pursue_users; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE pursue_users (
    account character varying(40) NOT NULL,
    pwd character varying(64),
    balance integer DEFAULT 1000
);


ALTER TABLE public.pursue_users OWNER TO ubuntu;

--
-- Name: sir_user; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE sir_user (
    email character varying(40),
    pwd character varying(64),
    uid integer NOT NULL
);


ALTER TABLE public.sir_user OWNER TO ubuntu;

--
-- Name: sir_user_uid_seq; Type: SEQUENCE; Schema: public; Owner: ubuntu
--

CREATE SEQUENCE sir_user_uid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sir_user_uid_seq OWNER TO ubuntu;

--
-- Name: sir_user_uid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ubuntu
--

ALTER SEQUENCE sir_user_uid_seq OWNED BY sir_user.uid;


--
-- Name: unlock_flags; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE unlock_flags (
    level integer,
    flag character varying(64)
);


ALTER TABLE public.unlock_flags OWNER TO ubuntu;

--
-- Name: unlock_hints; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE unlock_hints (
    level integer,
    progress integer,
    difficulty integer,
    hint character varying(200)
);


ALTER TABLE public.unlock_hints OWNER TO ubuntu;

--
-- Name: unlock_users; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE unlock_users (
    email character varying(40) NOT NULL,
    pwd character varying(64),
    progress integer,
    authenticated boolean,
    difficulty integer,
    level1_progress integer,
    level2_progress integer,
    level3_progress integer,
    level4_progress integer
);


ALTER TABLE public.unlock_users OWNER TO ubuntu;

--
-- Name: user; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE "user" (
    u_id integer NOT NULL,
    usr character varying(20),
    pwd character varying(64),
    progress integer,
    email character varying(40),
    authenticated boolean
);


ALTER TABLE public."user" OWNER TO ubuntu;

--
-- Name: user_u_id_seq; Type: SEQUENCE; Schema: public; Owner: ubuntu
--

CREATE SEQUENCE user_u_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_u_id_seq OWNER TO ubuntu;

--
-- Name: user_u_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ubuntu
--

ALTER SEQUENCE user_u_id_seq OWNED BY "user".u_id;


--
-- Name: uid; Type: DEFAULT; Schema: public; Owner: ubuntu
--

ALTER TABLE ONLY sir_user ALTER COLUMN uid SET DEFAULT nextval('sir_user_uid_seq'::regclass);


--
-- Name: u_id; Type: DEFAULT; Schema: public; Owner: ubuntu
--

ALTER TABLE ONLY "user" ALTER COLUMN u_id SET DEFAULT nextval('user_u_id_seq'::regclass);


--
-- Data for Name: bmail_emails; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY bmail_emails (title, body, sender, tags, account) FROM stdin;
Lasers	Hello,<br/><br/>We need some lasers; what kind of deal can you give us for 100?<br/><br/> - B-Mail Dev Team	Laser Emporium	email-sent	dev.team
RE: Lasers	We can do $27.18 for each one for a total of $2,718.28.	Laser Emporium	email-inbox	dev.team
RE: RE: Lasers	Sounds great!	Laser Emporium	email-sent	dev.team
RE: RE: RE: Lasers	Okay! I will send the order confirmation your way once we get your order processed.	Laser Emporium	email-inbox	dev.team
Credit Card Info	Hey,<br/><br/>Here's the card info. Go ahead and place the order.<br/><br/>Credit Card Number: 8675 3093 8921 2895<br/>Security Code: 154<br/>Expiration Date: 09/19<br/><br/>Flag: maybe_password_complexity_is_good	Dwight Shrute	email-sent	dev.team
Laser Emporium Order	Your Order:<br/><br/>Laser..........$27.18<br/>---x1000<br/><br/>Total: $2,718.28<br/><br/>Thank you for ordering from Laser Emporium. Enjoy!	noreply@laseremporium.co.uk	email-inbox email-starred	dev.team
\.


--
-- Data for Name: bmail_users; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY bmail_users (account, pwd) FROM stdin;
dev.team	5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
\.


--
-- Data for Name: nile_items; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY nile_items (name, price, images, tags) FROM stdin;
test	$17.99	test.png	test 
\.


--
-- Data for Name: nile_users; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY nile_users (account, pwd) FROM stdin;
realDonaldTrump	letmein
\.


--
-- Data for Name: pursue_actions; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY pursue_actions (account, name, type, change) FROM stdin;
\.


--
-- Data for Name: pursue_users; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY pursue_users (account, pwd, balance) FROM stdin;
\.


--
-- Data for Name: sir_user; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY sir_user (email, pwd, uid) FROM stdin;
\.


--
-- Name: sir_user_uid_seq; Type: SEQUENCE SET; Schema: public; Owner: ubuntu
--

SELECT pg_catalog.setval('sir_user_uid_seq', 6, true);


--
-- Data for Name: unlock_flags; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY unlock_flags (level, flag) FROM stdin;
1	maybe_password_complexity_is_good
4	much_better_than_equifax
\.


--
-- Data for Name: unlock_hints; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY unlock_hints (level, progress, difficulty, hint) FROM stdin;
1	1	0	Read the welcome email and look carefully for login information
1	0	0	Make an account to continue
1	2	0	The flag is in an email containing credit card information
1	0	1	Without login information, the only thing you can do is create an account
1	1	1	There is login information in your inbox
1	2	1	The flag is in an email containing sensitive information
1	0	2	Try the two options you have on-screen
1	1	2	All the information you need is in your inbox
1	2	2	The flag is in an email in the Dev Team's account
2	0	0	Try searching for an item
2	1	0	Try to perform a SQL injection on the search bar
2	3	0	Login using the information you just found
2	0	1	Try to find an input field
2	1	1	Try to perform an injection on that input field
2	3	1	Use the information you just found
2	0	2	Look for a CPU
2	1	2	Try to exploit the input field you just used
2	2	2	Look for private information
2	3	2	Login
2	2	0	Use UNION to SELECT from information_schema.tables (you must select 4 values)
2	2	1	Look for login information (the current query gets 4 values)
3	0	0	Make an account to continue
3	1	0	Try to transfer money from your account
3	2	0	Manipulate the URL of the transfer to send money to your account
3	0	1	The only thing you can do from here is create an account
3	1	1	Try to complete a typical bank action from the account management page
3	2	1	Try to exploit the URL of the transfer functionality to give yourself money
3	0	2	Try to use the user account system
3	1	2	Try to complete something you would do with a normal bank account
3	2	2	Try to exploit the transfer functionality to give yourself money
4	0	0	Make an account to continue
4	1	0	Check out your own 1040 form
4	2	0	Manipulate the URL of your request for your own 1040 form to get the 1040 form of another user
4	3	0	Look for the flag on this document
4	0	1	The only thing you can do from here is create an account
4	1	1	Check out a form
4	2	1	Try to exploit the URL of the request for your own 1040 form to get someone else's form
4	3	1	Look for the flag here
4	3	2	Find the flag
4	2	2	Try to exploit the document request functionality to get another user's information
4	1	2	Start doing your taxes
4	0	2	Try to use the user account system
\.


--
-- Data for Name: unlock_users; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY unlock_users (email, pwd, progress, authenticated, difficulty, level1_progress, level2_progress, level3_progress, level4_progress) FROM stdin;
test@gmail.com	d4ab234a5ba4cd586fae9557a0f1ab322f4322819657ffd840b6f1632a93d15a	5	f	2	3	4	3	4
brocksmith225@gmail.com	d4ab234a5ba4cd586fae9557a0f1ab322f4322819657ffd840b6f1632a93d15a	5	f	0	4	4	3	4
pwpon500@gmail.com	2dc61f4a7b100b48c2a0ce96f647fa7b462f82f97f8f2dd1d467ac94e378d301	3	t	2	3	4	0	0
bigboy@yahoo.net	c4f7423836870a23ce9b19f09777e77eb919c680f1d606776b4cb18e2a9fc1a2	1	f	0	0	0	0	0
Kevin.ngo0407@gmail.com	13004d8331d779808a2336d46b3553d1594229e2bb696a8e9e14554d82a648da	1	t	2	2	0	0	0
pwpon501@gmail.com	d4ab234a5ba4cd586fae9557a0f1ab322f4322819657ffd840b6f1632a93d15a	5	t	2	3	4	3	4
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY "user" (u_id, usr, pwd, progress, email, authenticated) FROM stdin;
1	test	3faebbbfcae364da3f14ab80a2a826f3c27a7b6a8c763d8fe96b25d2f8334e94	0	pwpon501@gmail.com	f
\.


--
-- Name: user_u_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ubuntu
--

SELECT pg_catalog.setval('user_u_id_seq', 1, true);


--
-- Name: bmail_users_pkey; Type: CONSTRAINT; Schema: public; Owner: ubuntu; Tablespace: 
--

ALTER TABLE ONLY bmail_users
    ADD CONSTRAINT bmail_users_pkey PRIMARY KEY (account);


--
-- Name: nile_users_pkey; Type: CONSTRAINT; Schema: public; Owner: ubuntu; Tablespace: 
--

ALTER TABLE ONLY nile_users
    ADD CONSTRAINT nile_users_pkey PRIMARY KEY (account);


--
-- Name: pursue_users_pkey; Type: CONSTRAINT; Schema: public; Owner: ubuntu; Tablespace: 
--

ALTER TABLE ONLY pursue_users
    ADD CONSTRAINT pursue_users_pkey PRIMARY KEY (account);


--
-- Name: sir_user_pkey; Type: CONSTRAINT; Schema: public; Owner: ubuntu; Tablespace: 
--

ALTER TABLE ONLY sir_user
    ADD CONSTRAINT sir_user_pkey PRIMARY KEY (uid);


--
-- Name: unlock_users_pkey; Type: CONSTRAINT; Schema: public; Owner: ubuntu; Tablespace: 
--

ALTER TABLE ONLY unlock_users
    ADD CONSTRAINT unlock_users_pkey PRIMARY KEY (email);


--
-- Name: user_email_key; Type: CONSTRAINT; Schema: public; Owner: ubuntu; Tablespace: 
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


--
-- Name: user_pkey; Type: CONSTRAINT; Schema: public; Owner: ubuntu; Tablespace: 
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (u_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

