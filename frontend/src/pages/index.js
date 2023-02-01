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
export default function Home({users}) {
  return (
    <div>
        <h1>Vote9ja Administration</h1>
        <div>
            {users.map((user) => (
                <div><h3>{user.get_full_name}</h3>
                <p>Username: {user.username}</p>
                <p>Email: {user.email}</p>
                <p>Polling State: {user.get_state}</p>
                <p>Polling Senatorial District: {user.get_senate}</p>
                <p>Polling Federal Constituency: {user.get_fedcon}</p>
                <p>Polling local government: {user.get_lga}</p>
                <p>Polling State Constituency: {user.get_state_con}</p>

                
                </div>
            ))}
        </div>
    </div>
  )
}

export async function getStaticProps() {
  // Call an external API endpoint to get posts.
  // You can use any data fetching library
  const res = await fetch(process.env.ACC_HOST)
  const users = await res.json()

  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  console.log(users);
  return {
    props: {
      users,
    },
  }
}
