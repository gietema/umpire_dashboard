window.$ = window.jQuery = require('jquery');
require('bootstrap-sass');

import '../sass/main.scss';

import Vue from 'vue';

import GraphComponent from "./components/GraphComponent.vue";

window.Vue = Vue;
const app = new Vue({
    el: '#app',
    components: {
        GraphComponent
    }
});