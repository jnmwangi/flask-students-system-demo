import { Link, Outlet } from "react-router-dom";

export default function Layout(){
    return (
        <div className="flex flex-col h-full">
            <header className="flex px-5 justify-between items-center bg-teal-300">
                <h2 className="text-2xl p-3 py-10">Bootcamp</h2>
                <nav className="flex-grow">
                    <ul className="flex gap-x-5 items-center">
                        <li><Link to={"/"} className="p-3 hover:bg-teal-200">Home</Link></li>
                        <li><Link to={"/"} className="p-3 hover:bg-teal-200">About</Link></li>
                        <li><Link to={"/"} className="p-3 hover:bg-teal-200">Services</Link></li>
                        <li className="ms-auto"><Link to={"/dashboard"} className="p-3 hover:bg-teal-200">Dashboard</Link></li>
                        <li><Link to={"/signup"} className="p-3 hover:bg-teal-200">Register</Link></li>
                        <li><Link to={"/signin"} className="p-3 hover:bg-teal-200">Sign In</Link></li>
                    </ul>
                </nav>
            </header>
            <main className="flex flex-col h-full">
                <Outlet />
            </main>
        </div>
    );
}