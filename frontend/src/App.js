import "./App.css";
import { useState, useEffect } from "react";
import axios from "axios";
import PetsittersList from "./components/PetsittersList";
import { API_URL } from "./constants";

function App() {
  const [petsittersList, setPetsitterList] = useState([]);
  const [selectedPetsitter, setSelectedPetsitter] = useState(null);

  // const URL = "http://localhost:8000/api/petsitters/";

  const fetchAllPetsitters = () => {
    axios
      .get(API_URL)
      .then((res) => {
        console.log(res);
        const petsittersAPIResCopy = res.data.map((petsitter) => {
          return {
            id: petsitter.pk,
            name: petsitter.name,
            email: petsitter.email,
            zipcode: petsitter.zipcode,
            city: petsitter.city,
            isAvailableHelp: petsitter.is_available_help,
            petType: petsitter.pet_type,
          };
        });
        console.log(petsittersAPIResCopy);
        setPetsitterList(petsittersAPIResCopy);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(fetchAllPetsitters, []);

  const loadPetsitterOnClick = (petsitter) => {
    console.log("load petsitter function called");
    setSelectedPetsitter(petsitter);
  };

  return (
    <div className="App">
      <header className="App-header"></header>

      <h1>Welcome to the PetCareExchange!</h1>
      <h2>Select PetSitter</h2>
      <PetsittersList
        petsitters={petsittersList}
        loadPetsitterOnClick={loadPetsitterOnClick}
      />
      {/* <h2>Selected Petsitter</h2>
      {selectedPetsitter
        ? `${selectedPetsitter.name} - ${selectedPetsitter.email}`
        : "Click on the petsitter to get more info"} */}
    </div>
  );
}

export default App;
