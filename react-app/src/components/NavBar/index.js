import React from "react";
import { NavLink, Link } from "react-router-dom";
import { FcHome } from "react-icons/fc";
import { AiOutlineHome } from "react-icons/ai";
import { IoPaperPlaneOutline } from "react-icons/io5";
import { FaWpexplorer, FaUsers } from "react-icons/fa";
import { CgProfile } from "react-icons/cg";
import { BsHeart } from "react-icons/bs";

import LogoutButton from "../auth/LogoutButton";
import { useSelector } from "react-redux";

import MainSearchBar from "../Search";
import "./NavBar.css";

const NavBar = () => {
  const user = useSelector((state) => state.session.user);

  return (
    <nav className="top-navbar">
      <NavLink
        to="/"
        exact={true}
        className="nav-title-logo"
        activeclassname="active"
      >
        <img
          className="lioness hvr-grow hvr-pulse"
          src={require("./insta.png")}
        />
        <p className="nav-title navbar-content hvr-grow ">InstaVibes</p>
      </NavLink>
      <MainSearchBar />
      {/* <input
        className="search-navbar-content"
        type="text"
        placeholder="Search.."
      ></input> */}
      <div className="navbar-content right-side">
        <NavLink to="/" exact={true} activeclassname="active">
          <AiOutlineHome
            className="navbar-icon hvr-shrink  "
            activeclassname="active"
          />
        </NavLink>
        {!user && (
          <>
            <NavLink
              to="/login"
              exact={true}
              activeclassname="active"
              className="navbar-icon"
              style={{ width: "60px" }}
            >
              Login
            </NavLink>
            <NavLink
              to="/sign-up"
              exact={true}
              activeclassname="active"
              className="navbar-icon"
              style={{ width: "60px" }}
            >
              Sign Up
            </NavLink>
          </>
        )}
        {user && (
          <>
            <NavLink to="/messages" exact={true} activeclassname="active">
              <IoPaperPlaneOutline className="navbar-icon hvr-shrink  " />
            </NavLink>
            <NavLink to="/explore" exact={true} activeclassname="active">
              <FaWpexplorer className="navbar-icon hvr-shrink " />
            </NavLink>
            <NavLink to="/likes" exact={true} activeclassname="active">
              <BsHeart className="navbar-icon hvr-shrink heart-button " />
            </NavLink>
            <NavLink to={`/${user.username}`}>
              <CgProfile className="navbar-icon hvr-shrink profile-button " />
            </NavLink>
            <LogoutButton className="navbar-icon der hvr-grow" />
          </>
        )}
        {/* <NavLink to="/users" exact={true} activeclassname="active">
          <FaUsers className='navbar-icon' />
        </NavLink> */}
      </div>
    </nav>
  );
};

export default NavBar;
