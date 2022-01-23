import React, { useContext } from 'react'
import { ModalContext } from './ModalContextProvider'
import { Modal } from 'react-bootstrap'

//[{'CS 25000': ['2', 0.8, 2, 1.0, 2, 1.0]}, {'CS15900': ['2', 0.8390804597701149, 2, 0.6551724137931034, 2, 0.6551724137931034]}, {'CS18000': ['2', 0.7017543859649122, 2, 0.6491228070175439, 2, 0.6491228070175439]}, {'CS18200': ['2', 0.8333333333333334, 2, 0.5714285714285714, 2, 0.5714285714285714]}, {'CS19100': ['2', 0.5714285714285714, 1, 1.0, 1, 1.0]}, {'CS19300': ['1', 0.5, 1, 1.0, 1, 1.0]}, {'CS24000': ['2', 0.8902439024390244, 2, 0.7073170731707317, 2, 0.7073170731707317]}, {'CS25000': ['2', 0.6666666666666666, 1, 0.5333333333333333, 1, 0.5333333333333333]}, {'CS25100': ['2', 1.0, 2, 0.8717948717948718, 2, 0.8717948717948718]}, {'CS25200': ['2', 0.9, 2, 0.95, 2, 0.95]}, {'CS35200': ['2', 1.0, 2, 1.0, 2, 1.0]}, {'CS35400': ['2', 1.0, 2, 1.0, 2, 1.0]}, {'CS35500': ['2', 1.0, 1, 0.5, 1, 0.5]}, {'CS38100': ['2', 0.7058823529411765, 1, 0.5882352941176471, 1, 0.5882352941176471]}, {'EAPS 10000': ['1', 0.5714285714285714, 1, 0.7142857142857143, 1, 0.7142857142857143]}, {'EAPS10000': ['1', 1.0, 1, 1.0, 1, 1.0]}, {'EAPS10600': ['1', 0.5, 1, 0.5, 1, 0.5]}, {'MA 26100': ['2', 1.0, 2, 1.0, 2, 1.0]}, {'SOC 10000': ['1', 0.6, 1, 1.0, 1, 1.0]}]

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
                <p>Quality: {course && (course["courseNum"]) == } Confidence: </p>
                <p>Difficulty:  Confidence: </p>

               </div>
            </Modal.Body>
         </Modal>
         </div>
    )

}

export default ModalLocal