import React, { createContext, useReducer } from 'react';

const initialState = {
    courseNum: null,
    show: false, 
    course: null
}

export const ModalContext = createContext(initialState);


function ModalReducer(state = initialState, action) {
    switch(action.type) {
        case 'HIDE':
            return ({
                ...state,
                show: false
            })
        case 'NEW_COURSE':
            return ({
                course: action.payload,
                show: true
            })
        case 'SHOW': 
            return ({
                ...state,
                show: true
            })

        case 'RENAME':
            return ({
                ...state,
                courseNum: action.payload
            })
    }
}

export const ModalContextProvider = ({ children }, context) => {

   const [state, dispatch] = useReducer(ModalReducer, initialState);


    function hideModal() {
        console.log("HIDING")
        dispatch({
            type: "HIDE",
        })
    }

    function showModal() {
        console.log("SHOWING")
        dispatch({
            type: "SHOW"
        })
    }

    function updateCourse(item) {
        dispatch({
            type: 'NEW_COURSE',
            payload: item
        })
    }

    function setCourseNum(item) {
        dispatch({
            type: 'RENAME',
            payload: item
        })
    }


   return(
      <ModalContext.Provider value = {{modalval: state, setCourseNum, hideModal, updateCourse, showModal}}> 
        {children} 
      </ModalContext.Provider>
   )
}