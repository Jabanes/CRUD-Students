

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
    }}

const del = () =>{
    console.log("Deleting...");
    
}