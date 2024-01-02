import React from 'react';
import { Navbar, Container, Nav } from 'react-bootstrap';

const MyNavbar = () => {
  return (
    <Navbar bg="light" data-bs-theme="light" className="py-5">
      <Container>
        <Navbar.Brand href="#home" className="text-3xl font-bold">
          BlackCoffer
        </Navbar.Brand>
        <Nav className="me-auto">
          <Nav.Link href="#home" className="text-lg text-black hover:text-gray-700">
            Home
          </Nav.Link>
          <Nav.Link href="#features" className="text-lg text-black hover:text-gray-700">
            Features
          </Nav.Link>
          <Nav.Link href="#pricing" className="text-lg text-black hover:text-gray-700">
            Pricing
          </Nav.Link>
        </Nav>
      </Container>
    </Navbar>
  );
};

export default MyNavbar;
