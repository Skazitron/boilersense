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
                 {`${course["courseNum"]}: ${course["courseName"]}`}
             </Modal.Title>
           </Modal.Header>
           <Modal.Body>
               <div>
                
                <p>Description: {course.description}</p>
                <p>Credits: {course.credits}</p>
                <p>Department: {course.department}</p>
                <p>Offered By: {course.offeredby}</p>

               </div>
            </Modal.Body>
         </Modal>
         </div>
    )

}

export default ModalLocal