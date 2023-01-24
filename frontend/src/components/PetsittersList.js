import React from "react";
import PropTypes from "prop-types";
import "./PetsittersList.css";
import Button from "react-bootstrap/Button";

const PetsittersList = ({ petsitters, loadPetsitterOnclick }) => {
  const getPetsittersCards = (petsitters) => {
    return petsitters.map((petsitter) => (
      <li key={petsitter.id} onClick={() => loadPetsitterOnclick(petsitter)}>
        {petsitter.name}
      </li>
    ));
  };
  return (
    <div className="petsitters-list">
      <ul className="petsitters-list-no-bullet">
        {getPetsittersCards(petsitters)}
      </ul>
      <Button variant="outline-primary">Edit</Button>
    </div>
  );
};

PetsittersList.propTypes = {
  petsitters: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number,
      name: PropTypes.string.isRequired,
      //   email: PropTypes.string.isRequired,
      //   zipcode: PropTypes.string.isRequired,
      //   city: PropTypes.string.isRequired,
      //   isAvailableHelp: PropTypes.bool.isRequired,
      //   pet_type: PropTypes.string.isRequired,
    })
  ).isRequired,
  //   loadPetsitterOnclick: PropTypes.func.isRequired,
};

export default PetsittersList;
