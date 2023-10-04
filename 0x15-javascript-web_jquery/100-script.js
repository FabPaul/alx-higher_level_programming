// Create a <script> element
const scriptElement = document.createElement("script");

// Update the header color
const scriptCode =`
  document.addEventListener("DOMContentLoaded", function() {
    const header = document.querySelector("header");
    header.style.color = "#FF0000";
  });
`;

// Set the script code to the <script> element
scriptElement.text = scriptCode;

// Append the <script> element to the <head>
document.head.appendChild(scriptElement);
