import { Link, Outlet } from "react-router-dom";

export default function AuthedLayout(){
    return (
        <div className="flex h-full">
            <div className="bg-gray-200">
                <h5 className="text-xl bolder p-5">Resources</h5>
                <hr className="border-bottom border-gray-300" />
                <ul className="my-2 min-w-[200px] flex flex-col w-full">
                    <li><Link to={"/dashboard"} className="block p-2 px-5 w-full hover:bg-gray-300">Dashboard</Link></li>
                    <li><Link to={"/courses"} className="block p-2 px-5 w-full hover:bg-gray-300">Courses</Link></li>
                    <li><Link to={"/"} className="block p-2 px-5 w-full hover:bg-gray-300">Students</Link></li>
                </ul>
            </div>

            <div className="flex-grow p-3">
                <Outlet />
            </div>
        </div>
    );
}