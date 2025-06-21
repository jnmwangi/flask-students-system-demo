import notebookimage from "../assets/images/notebook.jpg"

export default function Signup() {
    return (
        <div className="flex gap-3 m-auto min-w-[400px] shadow p-0 m-0 bg-white">
            <div className="">
                <img src={notebookimage} className="mask-image-left h-full object-cover rounded" alt="" />
            </div>
            <form action="" className="flex flex-col gap-1 flex-grow w-[50%] p-5">
                <h3 className="text-2xl">Register</h3>
                <hr className="border-bottom-2 border-gray-200" />
                <div className="form-control">
                    <label htmlFor="name">Fullname</label>
                    <input type="text" name="name" placeholder="Firstname Lastname" />
                </div>
                <div className="form-control">
                    <label htmlFor="name">Email Address</label>
                    <input type="email" name="email" placeholder="Email" />
                </div>
                <div className="form-control">
                    <label htmlFor="name">Password</label>
                    <input type="password" name="password" placeholder="Password" />
                </div>
                <div className="form-control">
                    <label htmlFor="name">Re-Type Password</label>
                    <input type="password" name="re-password" placeholder="Password" />
                </div>
                <div className="flex justify-between">
                    <button>Have an account? Sign In</button>
                    <button className="button-primary">Sign Up</button>
                </div>
            </form>
        </div>
    );
}