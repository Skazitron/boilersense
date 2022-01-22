import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';

import { Navbar, Container, Form, FormControl, Button, Row, Col, Card} from 'react-bootstrap';




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
  return (
    <Card style={{ width: '18rem' }}>
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
        <Card.Text>
          Some quick example text to build on the card title and make up the bulk of
          the card's content.
        </Card.Text>
        <Card.Link href="#">Card Link</Card.Link>
        <Card.Link href="#">Another Link</Card.Link>
      </Card.Body>
    </Card>
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
          <Col md="3" style={{
            paddingBottom: 30
          }}>
            <CourseCard/>
          </Col>
          <Col md="3" style={{
            paddingBottom: 30
          }}>
            <CourseCard/>
          </Col>
          <Col md="3" style={{
            paddingBottom: 30
          }}>
            <CourseCard/>
          </Col>
          <Col md="3" style={{
            paddingBottom: 30
          }}>
            <CourseCard/>
          </Col>
          <Col md="3" style={{
            paddingBottom: 30
          }}>
            <CourseCard/>
          </Col>
          <Col md="3" style={{
            paddingBottom: 30
          }}>
            <CourseCard/>
          </Col>         
        </Row>
      </Container>
    </div>
    
  )
}

export default App