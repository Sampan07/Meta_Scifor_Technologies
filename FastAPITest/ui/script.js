const apiUrl = "http://127.0.0.1:8000/students/";

// Fetch and display all students
async function fetchStudents() {
    const response = await fetch(apiUrl);
    const students = await response.json();
    const studentTable = document.querySelector("#studentTable tbody");
    studentTable.innerHTML = "";
    students.forEach(student => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${student.name}</td>
            <td>${student.age}</td>
            <td>${student.grade}</td>
            <td class="actions">
                <button onclick="editStudent(${student.id})">Edit</button>
                <button onclick="deleteStudent(${student.id})">Delete</button>
            </td>
        `;
        studentTable.appendChild(row);
    });
}

// Add a new student
document.getElementById("studentForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const grade = document.getElementById("grade").value;

    await fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, age, grade })
    });

    window.location.href = "index.html"; // Redirect to the student list
});

// Delete a student
async function deleteStudent(id) {
    await fetch(`${apiUrl}${id}`, { method: "DELETE" });
    fetchStudents(); // Refresh the list
}

// Load students on page load
if (document.querySelector("#studentTable")) {
    fetchStudents();
}
