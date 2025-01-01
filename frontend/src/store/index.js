import { createStore } from "vuex";

export default createStore({
  state: {
    drawer: false,
    userCredentials: {
      user: null,
      password: null,
    },
    isAuthenticated: false,
  },
  getters: {},
  mutations: {
    mutateDrawer: (state, payload) => {
      state.drawer = payload.drawer;
    },
    setUser: (state, payload) => {
      state.userCredentials["user"] = payload.user;
      state.userCredentials["password"] = payload.password;
      state.isAuthenticated = payload.isAuthenticated;
    },
  },
  actions: {
    updateUser({ commit }, payload) {
      commit("setUser", payload);
    },
    updateDrawer({ commit }, payload) {
      commit("mutateDrawer", payload);
    },
  },
  modules: {},
});
