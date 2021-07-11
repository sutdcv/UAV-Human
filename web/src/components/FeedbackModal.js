import React from 'react'
import PropTypes from 'prop-types'
import Button from '@material-ui/core/Button';
import Modal from 'react-bootstrap/Modal'

const FeedbackModal = (props) => {

    const oneDriveLink = "https://sutdapac-my.sharepoint.com/:f:/g/personal/tianjiao_li_mymail_sutd_edu_sg/EtLLkN49_C9Bq14ur0ZLpHkB-bi9Tc_LlIQBv0Ds4JE49A?e=IqX67X"

    return (
        <Modal
        centered
        show={props.showModal}
        onHide={props.handleCloseModal}
        backdrop="static"
        keyboard={false}
        onExited={props.callback}
        >
            <Modal.Header>
                <Modal.Title>
                    <div className={props.success?"text-success":"text-danger"}>
                        {props.success ? "Success!": "Error!"}
                    </div>
                    
                </Modal.Title>
            </Modal.Header>

            <Modal.Body>
                {props.success ? 
                
                <div>
                    <b className="text-success">You have successfully requested UAV-Human dataset, please use the link below to download the dataset!</b>
                    {/* <a href="" className="button btn btn-outline-primary mt-3 mx-1" target="_blank" rel="noopener noreferrer">Google Drive Link</a> */}
                    <a href={oneDriveLink} className="button btn btn-outline-primary mt-3 mx-1" target="_blank" rel="noopener noreferrer">MS OneDrive Link</a>
                </div>
                : 
                <div>
                    <p>Sorry, something is wrong at server side. (error: {props.statusCode})</p>
                    <b className="text-danger">Please take a screenshot now and send it to us via email.</b>
                    <p><code>tianjiao_li [AT] mymail.sutd.edu.sg</code></p>
                </div>}
            </Modal.Body>

            <Modal.Footer>
                <Button href="" variant="contained" onClick={props.handleCloseModal}>OK</Button>
            </Modal.Footer>
            
        </Modal>
    )
}

FeedbackModal.defaultProps = {
    title: "Title",
    success: false,
    body: "Body",
    data: {},
    showModal:false,
    handleCloseModal: ()=>{},
    callback: ()=>{},
    statusCode: "000",
}

FeedbackModal.propTypes = {
    title: PropTypes.string,
    body: PropTypes.string,
    showModal: PropTypes.bool,
    handleCloseModal: PropTypes.func,
}

export default FeedbackModal
