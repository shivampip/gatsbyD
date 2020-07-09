import React from "react"
import { Link } from "gatsby"
import Header from "../components/header"
import Layout from "../components/layout"

export default function About() {
  return (
    <Layout>
      <Header headerText="About" />
      <p>Wow, GatsBy is awesome</p>
      <Link to="/">Back</Link>
    </Layout>
  )
}
