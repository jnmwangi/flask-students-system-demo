import { useEffect, useState } from "react"

const BASEAPIURL = import.meta.env.VITE_BASEAPIURL

export default function Courses() {

    const [courses, setCourses] = useState([]);
    useEffect(()=>{
        fetch(`${BASEAPIURL}/api/courses`, {
            headers:{
                "Content-Type":"application/json",
                Authorization: `Bearer ${btoa(sessionStorage.getItem("access_token"))}`
            }
        })
        .then(r=>r.json())
        .then(console.log)
        .catch(console.log)

    }, [])

    return (
        <div className="p-5 px-10 flex flex-col gap-3">
            <div className="flex justify-between py-3 py-3">
                <h2 className="text-3xl text-bold">Courses</h2>
                <button className="button-primary">Add Course</button>
            </div>
            <hr className="divider border-bottom-2 py-3" />

            <table className="table-auto w-full">
                <thead>
                    <tr>
                        <th className="text-left p-2 border-b border-gray-200">Name</th>
                        <th className="text-left p-2 border-b border-gray-200">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td className="border-b border-gray-200 p-2">Course</td>
                        <td className="border-b border-gray-200 p-2">
                            <button className="text-sm shadow border border-gray-200 p-1 m-1">Edit</button> 
                            <button className="text-sm shadow border border-gray-200 p-1 m-1">Delete</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    )
}