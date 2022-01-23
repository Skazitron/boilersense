import React, { useContext } from 'react'
import { ModalContext } from './ModalContextProvider'
import { Modal } from 'react-bootstrap'


const ModalLocal = () => {
    const values = useContext(ModalContext)
    const course = values.modalval.course
    console.log(course)
    return (
        <div>
        <Modal
           size="lg"
           show={values.modalval.show}
           onHide={() => values.hideModal()}
           aria-labelledby="example-modal-sizes-title-lg"
         >
           <Modal.Header closeButton>
             <Modal.Title id="example-modal-sizes-title-lg">
                 {`${course && course["courseNum"] ? course["courseNum"] : "{COURSENUM}"}: ${course && course["courseName"] ? course["courseName"] : "{COURSENAME}"}`}
             </Modal.Title>
           </Modal.Header>
           <Modal.Body>
               <div>
                
                <p>Description: {course && course.description ? course.description : "Failed to retrieve course description"}</p>
                <p>Credits: {course && course.credits ? course.credits : "Failed to retrieve course credits"}</p>
                <p>Department: {course && course.department ? course.department : "Failed to retrieve course department"}</p>
                <p>Offered By: {course && course.offeredby ? course.offeredby : "Failed to retrieve course offered by"}</p>
                <p>Quality: {Math.floor(Math.random() * 2) + 1} Confidence: {Math.floor(Math.random() * 2)}</p>
                <p>Difficulty: {Math.floor(Math.random() * 2) + 1} Confidence: {Math.floor(Math.random() * 2)}</p>

               </div>
            </Modal.Body>
         </Modal>
         </div>
    )

}

export default ModalLocal