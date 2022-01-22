import {React, useState} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import DemoData from './DemoData/DemoData.json'

import { Navbar, Container, Form, FormControl, Button, Row, Col, Card, Modal} from 'react-bootstrap';

const NavBar = () => {
  return (
    <Navbar bg="dark"  expand="lg" sticky="top">
      <Container>
        <Navbar.Brand style={{
            color: "#C7B350"
          }}>BoilerSense</Navbar.Brand>
      </Container>
    </Navbar>
  )
}

const CourseCard = ({CourseNumber, CourseDescription, CourseName, Info1, Body1, Info2, Body2}) => {
  const [lgShow, setLgShow] = useState(false);
  return (
    <Col md="3" style={{
            paddingBottom: 30
    }}>
      <Card style={{ width: '18rem' }}>
        <Card.Body>
          <Card.Title>{CourseNumber}</Card.Title>
          <Card.Subtitle className="mb-2 text-muted">{CourseName}</Card.Subtitle>
          <Card.Text>
            {CourseDescription}
          </Card.Text>
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
  const [course, setCourse] = useState("");
  let filtered = DemoData.filter(courseObj =>  courseObj.CourseNumber.includes(course))
  return (
    <div>
      <NavBar/>
      <Row className="justify-content-md-center" style={{
        paddingTop: 20,
        paddingBottom: 30
      }}>
        <Col xs="2" sm="3" md="3" lg="4" >
        </Col>
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
        <Col xs="2" sm="3" md="3" lg="4">
        </Col>
      </Row>
      <Container>
        <Row>
          {filtered.map(elem => <CourseCard key={elem.id} 
                                CourseNumber={elem.CourseNumber} 
                                CourseName={elem.CourseName} 
                                CourseDescription={elem.CourseDescription} 
                                Info1={elem.Info1}
                                Body1={elem.Body1}
                                Info2={elem.Info2}
                                Body2={elem.Body2}
                                />)}
        </Row>
      </Container>
    </div>
  )
}

export default App