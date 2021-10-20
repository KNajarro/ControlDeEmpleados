<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>Lista de Empleados</h3>
          <nuxt-link to="/empleados/add" class="btn btn-info">Agregar Empleado</nuxt-link>
        </div>
      </div>
      <template v-for="employee in employees">
        <div :key="employee.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <employee-card :onDelete="deleteEmployee" :employee="employee"></employee-card>
        </div>
      </template>
    </div>
  </main>
</template>

<script>
import EmployeeCard from "~/components/EmployeeCard.vue";

export default {
  head() {
    return {
      title: "Lista de Empleados"
    };
  },
  components: {
    EmployeeCard
  },
  async asyncData({ $axios, params }) {
    try {
      let employees = await $axios.$get(`/empleados/`);
      return { employees };
    } catch (e) {
      return { employees: [] };
    }
  },
  data() {
    return {
      employees: []
    };
  },
  methods: {
    async deleteEmployee(employee_id) {
      try {
        await this.$axios.$delete(`/empleados/${employee_id}/`); // delete recipe
        let newEmployees = await this.$axios.$get("/empleados/"); // get new list of recipes
        this.employees = newEmployees; // update list of recipes
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>
</style>