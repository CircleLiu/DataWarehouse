import Vue from "vue";
import ElementUI from 'element-ui'
import App from "./App.vue";
import router from "./router";
import axios from "axios"
import "./plugins/element.js";

Vue.use(ElementUI);

Vue.config.productionTip = false;
Vue.prototype.$axios = axios;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
