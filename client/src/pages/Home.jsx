import owl from "../assets/images/owl.jpg"

export default function Home() {
    return (
        <div className="flex items-center py-20 gap-10 bg-teal-300">
            
            <div className={`flex-grow`}>
                <img src="/images/owl.jpg" className="object-cover w-full" />
            </div>
            {/* <img src={owl} className="flex-grow" /> */}

            <div className="flex flex-col w-[50%] p-10">
                <h3 className="text-2xl bolder">Welcome to the</h3>
                <h2 className="text-4xl font-black">Bootcamp</h2>
                {/* <hr className="border-bottom-2 border-gray-200" /> */}
                <h5 className="text-xl font-bold">Manage bootcamp resources with ease</h5>
                <p className="text-justify">Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                    when an unknown printer took a galley of type and scrambled it to make a type 
                    specimen book. It has survived not only five centuries, but also the leap 
                    into electronic typesetting, remaining essentially unchanged. </p>
            </div>
        </div>
    )
}