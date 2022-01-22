import {React, useState} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';

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

const CourseCard = () => {
  const [lgShow, setLgShow] = useState(false);
  return (
    <Col md="3" style={{
            paddingBottom: 30
    }}>
      <Card style={{ width: '18rem' }}>
        <Card.Body>
          <Card.Title>Card Title</Card.Title>
          <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
          <Card.Text>
            Some quick example text to build on the card title and make up the bulk of
            the card's content.
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
                Large Modal
              </Modal.Title>
            </Modal.Header>
            <Modal.Body>...</Modal.Body>
          </Modal>
        </Card.Body>
      </Card>
    </Col>
  )
}

const App = () => {
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
            />
            <Button variant="outline-secondary">Search</Button>
          </Form>
        </Col>
        <Col xs="2" sm="3" md="3" lg="4">
        </Col>
      </Row>
      <Container>
        <Row>
          <CourseCard/>      
          <CourseCard/>
          <CourseCard/>
          <CourseCard/>
          <CourseCard/>
          <CourseCard/>
          <CourseCard/>
          <CourseCard/>
          <CourseCard/>
        </Row>
      </Container>
    </div>
    
  )
}

export default App