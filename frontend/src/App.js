import {React, useState, useEffect} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import DemoData from './DemoData/DemoData.json'
import axios from 'axios'


import { Navbar, Container, Form, FormControl, Button, Row, Col, Card, Modal} from 'react-bootstrap';

const NavBar = () => {
  return (
    <Navbar style={{backgroundColor: "#303030"}} expand="lg" sticky="top">
      <Container>
        <Navbar.Brand style={{
            color: "#C7B350"
          }}>BoilerSense</Navbar.Brand>
      </Container>
    </Navbar>
  )
}

const CourseCard = ({CourseNumber, CourseName}) => {
  const [lgShow, setLgShow] = useState(false);
  const CourseDescription = "Loreum Ipsum"
  const Info1 = "Info #1"
  const Body1 = "Body"
  const Info2 = "Info #2"
  const Body2 = "Body"

  return (
    <Col md="3" style={{
            paddingBottom: 30
    }}>
      <Card style={{ width: '18rem' }}>
        <Card.Body>
          <Card.Title>{CourseNumber}</Card.Title>
          <Card.Subtitle className="mb-2 text-muted">{CourseName}</Card.Subtitle>

          <Button variant="outline-secondary" onClick={() => setLgShow(true)}>Show More</Button>
          <Modal
            size="lg"
            show={lgShow}
            onHide={() => setLgShow(false)}
            aria-labelledby="example-modal-sizes-title-lg"
          >
            <Modal.Header closeButton>
              <Modal.Title id="example-modal-sizes-title-lg">
                {CourseName}
              </Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <h4>
                {Info1}
              </h4>
              <h6>{Body1}</h6>
              <h4>
                {Info2}
              </h4>
              <h6>{Body2}</h6>
            </Modal.Body>
          </Modal>
        </Card.Body>
      </Card>
    </Col>
  )
}


const App = () => {  
  const [courses, setCourses] = useState([])
  const [course, setCourse] = useState("");
  const hook = () => {
    console.log('effect')
    axios
      .get('http://127.0.0.1:5000/')
      .then(response => {
        console.log('promise fulfilled')
        setCourses(response.data)
      })
  }
  useEffect(hook, [])
 



  const filtered = courses.filter(courseObj =>  courseObj.courseNumber.toUpperCase().includes(course.toUpperCase()) || courseObj.courseName.toUpperCase().includes(course.toUpperCase()))
  const stuffToRender = filtered.map(elem => <CourseCard key={elem.id} CourseNumber={elem.courseNumber} CourseName={elem.courseName}/>)
  return (
    <div>
      <NavBar/>
      <Row className="justify-content-md-center" style={{
        paddingTop: 20,
        paddingBottom: 30
      }}>
        <Col xs="2" sm="3" md="3" lg="4" ></Col>
        <Col>
          <Form className="d-flex">
            <FormControl
              type="search"
              placeholder="Course Name"
              className="me-2"
              aria-label="Search"
              value={course}
              onChange={e => setCourse(e.target.value )}
            />
          </Form>
        </Col>
        <Col xs="2" sm="3" md="3" lg="4"></Col>
      </Row>
      <Container>
        <Row>
          {stuffToRender}
        </Row>
      </Container>
      <Row className="justify-content-md-center" style={{
        paddingTop: 20,
        paddingBottom: 30
      }}>
       
      </Row>
    </div>
  )
}

export default App