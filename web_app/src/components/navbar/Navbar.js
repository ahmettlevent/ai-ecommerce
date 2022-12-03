import React from "react";
import { Link } from "react-router-dom";
import styles from "./Navbar.module.css";

function Navbar() {
  function loginUser(email, password) {
    fetch(
      "http://localhost:8083/auth/login",

      {
        headers: {
          "Content-Type": "application/json",
        },
        method: "POST",

        credentials: "include",
        body: JSON.stringify({ email: email, password: password }),
      }
    )
      .then((data) => data.json())
      .then((data) => {
        fetch("http://localhost:8083/users/", { credentials: "include" })
          .then((a) => a.json())
          .then((a) => console.log(a));
      });
  }

  return (
    <div className={styles.container}>
      <ul className={styles.nav_list}>
        <li className={`${styles.nav_list_item}`}>
          <Link
            onClick={(e) => loginUser("ahmettlevent@gmail.com", "utku123321")}
            to={"/"}
          >
            Login
          </Link>
        </li>
        <li className={`${styles.nav_list_item} ${styles.nav_list_item_logo}`}>
          <h1>AI E-Commerce</h1>
        </li>
        <li className={`${styles.nav_list_item}`}>
          <Link to={"/profile"}>Profile</Link>
        </li>
      </ul>
    </div>
  );
}

export default Navbar;
