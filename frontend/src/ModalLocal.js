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
                 {`${course["courseNum"] ? course["courseNum"] : "{COURSENUM}"}: ${course["courseName"] ? course["courseName"] : "{COURSENAME}"}`}
             </Modal.Title>
           </Modal.Header>
           <Modal.Body>
               <div>
                
                <p>Description: {course.description ? course.description : "Failed to retrieve course description"}</p>
                <p>Credits: {course.credits ? course.credits : "Failed to retrieve course credits"}</p>
                <p>Department: {course.department ? course.department : "Failed to retrieve course department"}</p>
                <p>Offered By: {course.offeredby ? course.offeredby : "Failed to retrieve course offered by"}</p>

               </div>
            </Modal.Body>
         </Modal>
         </div>
    )

}

export default ModalLocal