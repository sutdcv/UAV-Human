import React from 'react';
import { useState } from 'react'

import axios from "axios";
import Button from '@material-ui/core/Button';
import Checkbox from '@material-ui/core/Checkbox';
import FormControl from '@material-ui/core/FormControl';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import TextField from '@material-ui/core/TextField';
import Select from '@material-ui/core/Select';

import FeedbackModal from "./FeedbackModal"

const API_ROOT = "https://cvlab.sutd.markhh.com"
// const API_ROOT = "http://127.0.0.1:8000"

const countryList = require('country-list');
countryList.overwrite([{
    code: 'TW',
    name: 'Taiwan'
  }])

const countryNameList = countryList.getNames().sort()

const regionOptions = countryNameList.map(
    (regionName) => 
    <MenuItem 
    key={regionName} 
    value={regionName}>
        {regionName + " (" + countryList.getCode(regionName) +")"}
    </MenuItem> 
)


const RequestForm = () => {

    /////////////////////// Submitting State (while submitting) ///////////////////////////////////////
    
    const [submitting, setSubmitting] = useState(false);
    const startSubmitting = () => setSubmitting(true);
    const endSubmitting = () => setSubmitting(false);
    
    /////////////////////// Feedback Modal (after submission) ///////////////////////////////////////

    const [showModal, setShowModal] = useState(false);
    const handleShowModal = () => setShowModal(true);
    const handleCloseModal = () => setShowModal(false);

    const [submissionState, setSubmissionState] = useState(false);

    /////////////////////// //////////////// ///////////////////////////////////////

    const customStyle = {
        // minWidth: 300, 
        // maxWidth: "75%",
        width: 350,
    }

    const customStyle2 = {
        // minWidth: 300, 
        // maxWidth: "75%",
        width: 166,
    }

    const emptyState = {
        region: "",
        org: "",
        orgType: "",
        title: "",
        firstName: "",
        lastName: "",
        role: "",
        email: "",
        gmail: "",
        piTitle: "",
        piFirstName: "",
        piLastName: "",
        piRole: "",
        piEmail: "",
    }
    const [state, setState] = useState(emptyState)

    const [errorState, setErrorState] = useState({
        region: false,
        org: false,
        orgType: false,
        title: false,
        firstName: false,
        lastName: false,
        role: false,
        email: false,
        gmail: false,
        piTitle: false,
        piFirstName: false,
        piLastName: false,
        piRole: false,
        piEmail: false,
    })

    const [requiredState, setRequiredState] = useState({
        region: true,
        org: true,
        orgType: true,
        title: true,
        firstName: true,
        lastName: true,
        role: true,
        email: true,
        gmail: false,
        piTitle: false,
        piFirstName: false,
        piLastName: false,
        piRole: false,
        piEmail: false,
    })

    const [hideSection, setHideSection] = useState(true)

    const handlePiToggle = e => {
        setHideSection(e.target.checked)
        if (e.target.checked){
            setRequiredState({
                ...requiredState, 
                piTitle:false,
                piFirstName: false,
                piLastName: false,
                piRole: false,
                piEmail: false,
            })
            setState({
                ...state,
                piTitle: "",
                piFirstName: "",
                piLastName: "",
                piRole: "",
                piEmail: "",
            })
        } else {
            setRequiredState({
                ...requiredState, 
                piTitle:true,
                piFirstName: true,
                piLastName: true,
                piRole: true,
                piEmail: true,
            })
        }
    }

    const [acknowledgement, setAcknowledgement] = useState(false)
    const [warning, setWarning] = useState(false)

    const handleAcknowledgement = e => {
        setAcknowledgement(e.target.checked)
    }

    const checkAcknowledgement = () => {
        setWarning(!acknowledgement)
    }

    const resetSingleErrorState = e => {
        if (e.target.value !== ""){
            setErrorState({...errorState, [e.target.name]: false})
        }
    }

    const updateState = e => {
        resetSingleErrorState(e)
        setState({...state, [e.target.name]: e.target.value})
    }

    const validateEmail = (email) =>  {
        // ref: https://stackoverflow.com/a/46181
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }

    const validateAllField = () => {
        var key;
        var valid = true;
        var newErrorState = {};

        if (!acknowledgement){
            valid = false;
        }

        for (key in state) {
            var value = state[key];

            if (value === ""){
                if (requiredState[key]) {
                    newErrorState[key] = true
                    valid = false;
                }
            } else {
                if (["email", "gmail", "piEmail"].includes(key)){
                    var validEmail = validateEmail(value)
                    if (!validEmail){
                        newErrorState[key] = true
                        valid = false;
                        console.log("Invalid Email: " + state[key])
                    }
                }
            }
        }
        setErrorState(newErrorState)
        return valid
    }

    const resetAllFormStates = () => {
        if (submissionState){
            setState(emptyState)
            setAcknowledgement(false)
            setHideSection(true)
            setSubmitting(false)
            setSubmissionState(false)
        }
        
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        checkAcknowledgement();

        if (validateAllField()){
            startSubmitting()
            console.log(state)
            // Submit Form To Backend
            const config = {
                method: "POST",
                url: API_ROOT + "/uavHuman",
                headers: {
                    "accept": "application/json",
                    "Content-Type": "application/json",
                },
                data: JSON.stringify(state)
            };
            await axios(config)
            .then((response) => {
                // submission success
                endSubmitting()
                // check response status
                console.log(response)
                if (response.status === 201) {
                    setSubmissionState(true)
                    // Reset Form
                    resetAllFormStates()
                } else {
                    setState((state) => {
                        return {...state, "statusCode":response.status.toString()}
                    })
                }
                handleShowModal()
                
            })
            .catch((error) => {
                // submission failed
                endSubmitting()
                handleShowModal()
                console.error(error)
            })

        } else {
            console.log("Error: Request form is incomplete.")
        }
        
    }

    
    return (
        // <form className={classes.root} noValidate autoComplete="off">
        <form className={"mb-3 d-flex flex-column align-items-center"}>

                {/*////////////////// FeedbackModal //////////////////*/}
                {/* <Button name="dev debug button" variant="outlined" onClick={()=>{
                    handleShowModal()
                }}>
                    Launch static backdrop modal
                </Button> */}

                <FeedbackModal 
                data={state} 
                success={submissionState} 
                showModal={showModal} 
                handleCloseModal={handleCloseModal}
                callback={resetAllFormStates}
                />


                {/*////////////////// ORGANIZATION DETAILS SECTION //////////////////*/}
                <h5 className={"mb-3"}>Your Organization Details</h5>
                <div className={"mb-3"}>
                    <TextField 
                    style={customStyle} 
                    required={requiredState.org}
                    error={errorState.org}
                    id="filled-basic" 
                    name="org"
                    value={state.org}
                    onChange={updateState} 
                    label="Organization" 
                    helperText="Your University / Company / Institution Name"
                    variant="filled" />
                </div>

                <div className={"mb-3"}>
                    <FormControl 
                    style={customStyle} 
                    required={requiredState.region} 
                    error={errorState.region}
                    variant="filled" 
                    >
                        <InputLabel id="select-title">Country / Region</InputLabel>
                        <Select
                        name="region" 
                        value={state.region}
                        onChange={updateState} 
                        >
                            {regionOptions}         
                        </Select>
                    </FormControl>
                </div>

                <div className={"mb-3"}>
                    <FormControl 
                    style={customStyle} 
                    required={requiredState.orgType} 
                    error={errorState.orgType}
                    variant="filled" 
                    >
                        <InputLabel id="select-title">Organization Type</InputLabel>
                        <Select
                        name="orgType" 
                        value={state.orgType}
                        onChange={updateState} 
                        >
                        <MenuItem value={"University"}>University / College</MenuItem>         
                        <MenuItem value={"Company"}>Company</MenuItem>         
                        <MenuItem value={"Research Institution"}>Research Institution</MenuItem>         
                        <MenuItem value={"Public Sector"}>Public Sector</MenuItem>         
                        <MenuItem value={"Other"}>Other</MenuItem>         
                        </Select>
                    </FormControl>
                </div>

                <hr className={"my-2"}></hr>

                {/*////////////////// REQUESTER DETAILS SECTION //////////////////*/}
                <h5 className={"mb-3"}>Your Details</h5>

                <div className={"mb-3"}>
                    <FormControl 
                    style={customStyle} 
                    required={requiredState.title} 
                    error={errorState.title}
                    variant="filled" 
                    name="title" 
                    >
                        <InputLabel id="select-title">Title</InputLabel>
                        <Select
                        labelId="select-title"
                        id="select-title-filled"
                        value={state.title}
                        name="title" 
                        onChange={updateState}
                        >
                        <MenuItem value={"Prof."}>Prof.</MenuItem>
                        <MenuItem value={"Assoc. Prof."}>Assoc. Prof.</MenuItem>
                        <MenuItem value={"Asst. Prof."}>Asst. Prof.</MenuItem>
                        <MenuItem value={"Dr."}>Dr.</MenuItem>
                        <MenuItem value={"Mx."}>Mx.</MenuItem>
                        <MenuItem value={"Ms"}>Ms.</MenuItem>
                        <MenuItem value={"Mr."}>Mr.</MenuItem>            
                        </Select>
                    </FormControl>
                </div>

                <div className={"mb-3 clearfix"}>

                    <TextField 
                    className={"mx-2 my-1"}
                    style={customStyle2}
                    required={requiredState.firstName} 
                    error={errorState.firstName}
                    id="filled-basic" 
                    label="First Name" 
                    name="firstName" 
                    value={state.firstName}
                    onChange={updateState}
                    variant="filled" />

                    <TextField 
                    className={"mx-2 my-1"}
                    style={customStyle2}
                    required={requiredState.lastName} 
                    error={errorState.lastName}
                    id="filled-basic" 
                    label="Last Name" 
                    name="lastName" 
                    value={state.lastName}
                    onChange={updateState}
                    variant="filled" />

                </div>

                <div className={"mb-3"}>
                    <FormControl 
                    style={customStyle} 
                    required={requiredState.role} 
                    error={errorState.role}
                    variant="filled" 
                    className={"mb-3"}>
                        <InputLabel id="select-title">Role</InputLabel>
                        <Select
                        labelId="select-title"
                        id="select-title-filled"
                        name="role"
                        value={state.role}
                        onChange={updateState}
                        >
                        <MenuItem value={"Principle Investigator"}>Principle Investigator</MenuItem>
                        <MenuItem value={"Lab Director"}>Lab Director</MenuItem>
                        <MenuItem value={"Researcher"}>Researcher</MenuItem>
                        <MenuItem value={"Faculty"}>Faculty</MenuItem>
                        <MenuItem value={"Postdoc"}>Postdoc</MenuItem>
                        <MenuItem value={"PhD Student"}>PhD Student</MenuItem>
                        <MenuItem value={"Student"}>Student</MenuItem>
                        <MenuItem value={"Engineer"}>(Company) Software / Algorithm Engineer</MenuItem>               
                        <MenuItem value={"Data Scientist"}>(Company) Data Scientist</MenuItem>               
                        <MenuItem value={"Other"}>Other</MenuItem>        
                        </Select>
                    </FormControl>
                </div>

                <div className={"mb-3"}>
                    <TextField 
                    style={customStyle} 
                    required={requiredState.email} 
                    error={errorState.email}
                    id="filled-basic" 
                    name="email"
                    value={state.email}
                    onChange={updateState} 
                    label="Email Address" 
                    helperText="Email Address associated with your organization"
                    variant="filled" />
                </div>

                {/* <div className={"mb-3"}>
                    <TextField 
                    style={customStyle} 
                    required={requiredState.gmail} 
                    error={errorState.gmail}
                    id="filled-basic" 
                    name="gmail" 
                    value={state.gmail}
                    onChange={updateState} 
                    label="Gmail Address" 
                    // helperText="If you have a Google account, Dataset access will be shared to this account."
                    variant="filled" />
                </div> */}


                {/*////////////////// PI TOGGLE //////////////////*/}
                <div className={"mb-3"} style={{maxWidth: "90%"}}>
                    <FormControlLabel
                        control={
                        <Checkbox
                            checked={hideSection}
                            onChange={handlePiToggle}
                            name="isPI"
                            color="primary"
                        />
                        }
                        label="Myself is the Lab Director / Principle Investigator"
                    />
                </div>
                
                <hr className={"my-2"}></hr>

                {/*////////////////// PI Section //////////////////*/}
                {!hideSection? <h5 className={"mb-3"}>Your Supervisor / PI / Lab Director's Details</h5> : null} 
                
                {!hideSection? <div className={"mb-3"}>
                    <FormControl 
                    style={customStyle} 
                    required={requiredState.piTitle} 
                    error={errorState.piTitle}
                    variant="filled" 
                    >
                        <InputLabel id="select-title">Title</InputLabel>
                        <Select
                        value={state.piTitle}
                        name="piTitle" 
                        onChange={updateState}
                        >
                        <MenuItem value={"Prof."}>Prof.</MenuItem>
                        <MenuItem value={"Assoc. Prof."}>Assoc. Prof.</MenuItem>
                        <MenuItem value={"Asst. Prof."}>Asst. Prof.</MenuItem>
                        <MenuItem value={"Dr."}>Dr.</MenuItem>
                        <MenuItem value={"Mx."}>Mx.</MenuItem>
                        <MenuItem value={"Ms"}>Ms.</MenuItem>
                        <MenuItem value={"Mr."}>Mr.</MenuItem>            
                        </Select>
                    </FormControl>
                </div>: null} 

                {!hideSection? <div  className={"mb-3 clearfix"}>
                    <TextField 
                    className={"mx-2 my-1"}
                    style={customStyle2}
                    required={requiredState.piFirstName} 
                    error={errorState.piFirstName}
                    id="filled-basic" 
                    label="First Name" 
                    name="piFirstName" 
                    value={state.piFirstName}
                    onChange={updateState}
                    variant="filled" />

                    <TextField 
                    className={"mx-2 my-1"}
                    style={customStyle2}
                    required={requiredState.piLastName} 
                    error={errorState.piLastName}
                    id="filled-basic" 
                    label="Last Name" 
                    name="piLastName" 
                    value={state.piLastName}
                    onChange={updateState}
                    variant="filled" />

                </div> : null}

                {!hideSection? <div className={"mb-3"}>
                    <FormControl 
                    style={customStyle}
                    required={requiredState.piRole} 
                    error={errorState.piRole}
                    variant="filled" >
                        <InputLabel id="select-title">Role</InputLabel>
                        <Select
                        name="piRole"
                        value={state.piRole}
                        onChange={updateState} >
                            <MenuItem value={"Principle Investigator"}>Principle Investigator</MenuItem>
                            <MenuItem value={"Lab Director"}>Research Lab Director</MenuItem>
                            <MenuItem value={"Department Head"}>(Company) Department Head / Director / CTO</MenuItem>      
                            <MenuItem value={"Supervisor"}>(Company) Supervisor / Team Lead</MenuItem>            
                            <MenuItem value={"Other"}>Other</MenuItem>            
                        </Select>
                    </FormControl>
                </div> : null}

                {!hideSection? <div className={"mb-3"}>
                    <TextField 
                    style={customStyle}
                    required={requiredState.piEmail} 
                    error={errorState.piEmail}
                    id="filled-basic" 
                    name="piEmail"
                    value={state.piEmail}
                    onChange={updateState} 
                    className={"mb-3"} 
                    label="Email Address" 
                    helperText="Email Address associated with organization"
                    variant="filled" />
                </div> : null}
                
                {/*////////////////// TERMS & CONDITIONS //////////////////*/}
                <h5 className={"mb-3"}>Terms & Conditions</h5>

                <div className={"mb-3"} style={{maxWidth: "90%"}}>
                    <p className={"alert alert-primary text-start"} style={{maxWidth:500}}>
                        The Singapore University of Technology and Design (SUTD) provides access 
                        to the <em className={"fw-bold"}>UAV-Human Dataset</em> (referred to as "the Dataset" below) 
                        under the following conditions:
                        <p></p>
                        <ul>
                            <li>The Dataset should only be used for non-commercial scientific research purposes. Any other use is strictly prohibited.</li>
                            <li>Showing videos and images from the Dataset are only allowed in academic publications or presentations.</li>
                            <li>The Dataset must NOT be shared or redistributed in part or full with any third-party individual or organization.</li>
                            <li>The Dataset must NOT be altered to produce a new dataset without written consent from the authors.</li>
                            
                        </ul>
                    </p>
                </div>

                <div className={"mb-3"}  style={{maxWidth: "90%"}}>
                    <FormControlLabel
                        required
                        style={{maxWidth: 500}}
                        control={
                        <Checkbox
                            required
                            checked={acknowledgement}
                            onChange={handleAcknowledgement}
                            name="acknowledgement"
                            color="primary"
                        />
                        }
                        label="I acknowledge that I have read, and do hereby accept the terms and conditions listed above."
                    />
                </div>


                {(warning) ? <div 
                    className={"mb-3 alert alert-danger"} 
                    style={{maxWidth: "90%"}}>
                        * You must read and check above acknowledgement.
                    </div> : null}

                
                <div className={"mb-3"}>
                    <Button 
                    disabled={submitting}
                    style={{minWidth: "15%"}}
                    onClick={handleSubmit}
                    variant="contained" 
                    color="primary">
                        {submitting? <span className="spinner-grow spinner-grow-sm me-2" role="status" aria-hidden="true"></span>:null}
                        {submitting? "Submitting...":"Submit"}
                    </Button>
                </div>

        </form>
    )
}

export default RequestForm
