import axios from "axios";
import "bootstrap/dist/css/bootstrap.css";
import { createApp } from "vue";
import "./../node_modules/bulma/css/bulma.css";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/";

app.use(router);
app.mount("#app");
