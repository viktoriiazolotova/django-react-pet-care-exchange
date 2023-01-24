import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import { GiHollowCat, GiSearch } from "react-icons/gi";
import { GrSearch } from "react-icons/gr";

function NavScrollExample() {
  return (
    <Navbar bg="light" expand="lg">
      <Container fluid>
        <GiHollowCat size="30px" color="#38bac4"></GiHollowCat>

        <Navbar.Brand href="#">PetCareExchange</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: "100px" }}
            navbarScroll
          >
            <Nav.Link href="#action1">Home</Nav.Link>

            <Nav.Link href="#action3">
              <GrSearch size="20px"></GrSearch>Search a Petsitter
            </Nav.Link>

            {/* <Nav.Link href="#action2">SignUp</Nav.Link>
            <Nav.Link href="#action3">SignIn</Nav.Link> */}
          </Nav>

          <Button variant="outline-secondary">SignUp</Button>
          <Button variant="outline-secondary">SignIn</Button>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavScrollExample;
