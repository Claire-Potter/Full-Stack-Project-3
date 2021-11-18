/* jshint esversion: 6 */
// https://getbootstrap.com/docs/5.0/components/tooltips/ referenced and edited for
// tooltips
const searchButton = document.getElementById('search-button');
const searchInput = document.getElementById('search-input');
let steps = [];
const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
});


// set timeout function for messages as per the code institute example project.
//setTimeout(function () {
// let messages = document.getElementById('msg');
//let alert = new bootstrap.Alert(messages);
//alert.close(messages);
//}, 2000);

