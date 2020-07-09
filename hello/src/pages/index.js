import React from "react"
import { Link } from "gatsby"
import Layout from "../components/layout"
import Header from "../components/header"

export default function Home() {
  return (
    <Layout>
      <Header headerText="Welcome to GatsBy" />
      <p>I'm Shivam Agrawal. I live at pipariya.</p>
      <Link to="/about/">About</Link>
      <br></br>
      <Link to="/contact/">Contact</Link>
    </Layout>
  )
}
