import {React, useState} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';

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

const CourseCard = ({CardTitle, CardSubtitle, CardText, CourseName, Info1, Body1, Info2, Body2}) => {
  const [lgShow, setLgShow] = useState(false);
  return (
    <Col md="3" style={{
            paddingBottom: 30
    }}>
      <Card style={{ width: '18rem' }}>
        <Card.Body>
          <Card.Title>{CardTitle}</Card.Title>
          <Card.Subtitle className="mb-2 text-muted">{CardSubtitle}</Card.Subtitle>
          <Card.Text>
            {CardText}
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
  const CardTitle = "Card Title"
  const CardSubtitle = "Card Subtitle"
  const CardText = "Some quick example text to build on the card title and make up the bulk of the card's content."
  const CourseName = "Course Name"
  const Info1 = "Info Item #1"
  const Body1 = "Body"
  const Info2 = "Info Item #2"
  const Body2 = "Body"

  const componentsRender = [<CourseCard CardTitle={CardTitle} 
                            CardSubtitle={CardSubtitle} 
                            CardText={CardText} 
                            CourseName={CourseName} 
                            Info1={Info1} 
                            Body1={Body1} 
                            Info2={Info2} 
                            Body2={Body2}/>,
                            <CourseCard CardTitle={CardTitle} 
                            CardSubtitle={CardSubtitle} 
                            CardText={CardText} 
                            CourseName={CourseName} 
                            Info1={Info1} 
                            Body1={Body1} 
                            Info2={Info2} 
                            Body2={Body2}/>,
                            <CourseCard CardTitle={CardTitle} 
                            CardSubtitle={CardSubtitle} 
                            CardText={CardText} 
                            CourseName={CourseName} 
                            Info1={Info1} 
                            Body1={Body1} 
                            Info2={Info2} 
                            Body2={Body2}/>,
                            <CourseCard CardTitle={CardTitle} 
                            CardSubtitle={CardSubtitle} 
                            CardText={CardText} 
                            CourseName={CourseName} 
                            Info1={Info1} 
                            Body1={Body1} 
                            Info2={Info2} 
                            Body2={Body2}/>,
                            <CourseCard CardTitle={CardTitle} 
                            CardSubtitle={CardSubtitle} 
                            CardText={CardText} 
                            CourseName={CourseName} 
                            Info1={Info1} 
                            Body1={Body1} 
                            Info2={Info2} 
                            Body2={Body2}/>,
                            <CourseCard CardTitle={CardTitle} 
                            CardSubtitle={CardSubtitle} 
                            CardText={CardText} 
                            CourseName={CourseName} 
                            Info1={Info1} 
                            Body1={Body1} 
                            Info2={Info2} 
                            Body2={Body2}/>,
                            <CourseCard CardTitle={CardTitle} 
                            CardSubtitle={CardSubtitle} 
                            CardText={CardText} 
                            CourseName={CourseName} 
                            Info1={Info1} 
                            Body1={Body1} 
                            Info2={Info2} 
                            Body2={Body2}/>,
                            <CourseCard CardTitle={CardTitle} 
                            CardSubtitle={CardSubtitle} 
                            CardText={CardText} 
                            CourseName={CourseName} 
                            Info1={Info1} 
                            Body1={Body1} 
                            Info2={Info2} 
                            Body2={Body2}/>,
                            <CourseCard CardTitle={CardTitle} 
                            CardSubtitle={CardSubtitle} 
                            CardText={CardText} 
                            CourseName={CourseName} 
                            Info1={Info1} 
                            Body1={Body1} 
                            Info2={Info2} 
                            Body2={Body2}/>]
  const [course, setCourse] = useState("");
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(course);
  }
  const demoArray = ["CS180", "CS182", "CS240", "CS250", "CS251", "CS252"]
  const outputArr = demoArray.filter(c => c === course)
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
          <Form className="d-flex" id="myForm" onSubmit={handleSubmit}>
            <FormControl
              type="search"
              placeholder="Course Name"
              className="me-2"
              aria-label="Search"
              value={course}
              onChange={e => setCourse(e.target.value )}
            />
            <Button form="myForm" type="submit" variant="outline-secondary">Search</Button>
          </Form>
        </Col>
        <Col xs="2" sm="3" md="3" lg="4">
        </Col>
      </Row>
      <Container>
        <Row>
          {componentsRender}
        </Row>
      </Container>
      {outputArr}
    </div>
  )
}

export default App