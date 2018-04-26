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
-- Name: items; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE items (
    name character varying(64),
    price character varying(32),
    images character varying(32),
    tags character varying(64)
);


ALTER TABLE public.items OWNER TO ubuntu;

--
-- Name: users; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE users (
    usr character varying(64),
    pwd character varying(64)
);


ALTER TABLE public.users OWNER TO ubuntu;

--
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY items (name, price, images, tags) FROM stdin;
Jiffy	$5,000.00	jiffy.png	jiffy peyton linux terminal vm virtual machine
Toywars	42 N	toywars.png	kevin moba tower defense video game toy wars toywars
Surfin	$0.00	surfin.png	ethan surfin surfing video game
Utopia	$75,000,000.00	utopia.png	utopia conner roller coaster theme park amusement video game
Backwoods Bash	$59.99	backwoodsbash.png	davis backwoods bash video game driving woods
The Intel CPU	$250.00	intel.png	intel cpu computer
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: ubuntu
--

COPY users (usr, pwd) FROM stdin;
realDonaldTrump	letmein
\.


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: items; Type: ACL; Schema: public; Owner: ubuntu
--

REVOKE ALL ON TABLE items FROM PUBLIC;
REVOKE ALL ON TABLE items FROM ubuntu;
GRANT ALL ON TABLE items TO ubuntu;
GRANT SELECT ON TABLE items TO nile;


--
-- Name: users; Type: ACL; Schema: public; Owner: ubuntu
--

REVOKE ALL ON TABLE users FROM PUBLIC;
REVOKE ALL ON TABLE users FROM ubuntu;
GRANT ALL ON TABLE users TO ubuntu;
GRANT SELECT ON TABLE users TO nile;


--
-- PostgreSQL database dump complete
--

