import notebookimage from "../assets/images/notebook.jpg"

export default function Signin() {
    return (
        <div className="flex gap-3 m-auto min-w-[400px] bg-white shadow items-center">
            <div className="">
                <img src={notebookimage} className="mask-image-left h-full object-cover rounded" alt="" />
            </div>
            <form action="" className="flex flex-col gap-1 flex-grow w-[50%] p-5">
                <h3 className="text-2xl">Sign In</h3>
                <hr className="border-bottom-2 border-gray-200" />
                <div className="form-control">
                    <label htmlFor="name">Email Address</label>
                    <input type="email" name="email" placeholder="Email" />
                </div>
                <div className="form-control">
                    <label htmlFor="name">Password</label>
                    <input type="password" name="password" placeholder="Password" />
                </div>
                <div className="flex justify-between">
                    <button>Create new account</button>
                    <button className="button-primary">Sign In</button>
                </div>
            </form>
        </div>);
}