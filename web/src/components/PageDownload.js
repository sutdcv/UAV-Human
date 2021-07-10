import RequestForm from './RequestForm'


const PageDownload = () => {
    return (
        <div>
            <div className="jumbotron jumbotron-fluid py-5 bg-dark">
                <div className="container">
                    <h1 className="display-3 text-white text-center" id="dataset-download-request-form">UAV-Human Dataset</h1>
                </div>
                <div className="mt-5 px-5 container text-light text-center">
                    <p className="alert alert-secondary">
                        To download the UAV-Human dataset, you need to complete the form below and agree to our terms & conditions. 
                    </p>
                </div>
            </div>
            <div className={"container my-4 py-4 px-3 jumbotron shadow"} style={{minWidth: 400}}>
                <RequestForm />
            </div>
        </div>
    )
}

export default PageDownload
