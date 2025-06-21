import { createBrowserRouter } from 'react-router-dom'
import Signup from './pages/Signup'
import Signin from './pages/Signin'
import Home from './pages/Home'
import Layout from './components/Layout'
import AuthedLayout from './components/AuthedLayout'
import Dashboard from './pages/Dashboard'
import Courses from './pages/Courses'

export default createBrowserRouter([
    {
        path: '/',
        element: <Layout />,
        children: [
            {
                path: '/',
                element: <Home />
            },
            {
                path: '/signup',
                element: <Signup />
            },
            {
                path: '/signin',
                element: <Signin />
            }, 
            {
                path:"/",
                element: <AuthedLayout />,
                children:[
                    {
                        path:"/dashboard",
                        element:<Dashboard />
                    },
                    {
                        path:"/courses",
                        element:<Courses />
                    }
                ]
            }
        ]
    }
])