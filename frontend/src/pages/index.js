import Image from 'next/image'
import { Inter } from '@next/font/google'
import styles from './page.module.css'


import {StrictMode } from "react";
import ReactDOM from "react-router-dom" 
import App from "./app/App" 
import {BrowserRouter} from "react-router-dom" 
//const rootElement = document.getElementById("root") 
//ReactDOM.render( 
//<StrictMode> 
//    <BrowserRouter> 
//      <App /> 
//   </BrowserRouter> 
//</StrictMode>, 
// rootElement 
//);
const inter = Inter({ subsets: ['latin'] })
export default function Home({blogs}) {
  return (
    <div>
        <h1>Eniblog</h1>
        <div>
            {blogs.map((blog) => (
                <div><h3>{blog.title}</h3>
                <p>{blog.body}</p>
                <span>{blog.username}</span>
                </div>
            ))}
        </div>
    </div>
  )
}

export async function getStaticProps() {
  // Call an external API endpoint to get posts.
  // You can use any data fetching library
  const res = await fetch(process.env.DB_HOST)
  const blogs = await res.json()

  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  console.log(blogs);
  return {
    props: {
      blogs,
    },
  }
}
