

// C:
const add = () => {
    const studentName = document.getElementById('StudentName').value;
    if (studentName) {


        axios.post('http://127.0.0.1:5000/add', {
            name: studentName.trim(),
        })

        document.getElementById("message-div").textContent = `Student has been added successfully!`
    }
    else {
        alert("You did not fill all of the fields!")
    }
}


const del = (id) => {
    axios.delete(`/delete/${id}`)
        .then(() => {
            // Handle UI updates after successful deletion (like removing the item from the list)
            alert('Student deleted successfully');
            location.reload(); // Reload the page to reflect the changes
        })
        .catch(err => {
            console.error('Error deleting student:', err);
        });
}

const update = (id) =>{
    const nameToUpdate = document.getElementById(`upd-${id}`).value
    if (nameToUpdate) {
        axios.put(`/update/${id}`, 
            {
                name : nameToUpdate
        })

        .then(() => {
            // Handle UI updates after successful deletion (like removing the item from the list)
            alert('Student updated successfully');
            location.reload(); // Reload the page to reflect the changes
        })
        .catch(err => {
            console.error('Error updating student:', err);
        });
    }
    else{
        alert("Please enter a name to update!")
    }
   
}

    
