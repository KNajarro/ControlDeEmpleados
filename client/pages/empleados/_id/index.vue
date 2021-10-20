<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ employee.primer_nombre + " " + employee.segundo_nombre }}</h2>
        <h2 class="mb-3 display-4 text-uppercase">{{ employee.primer_apellido + " " + employee.segundo_apellido }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          src="/images/generic.png"
          alt
        >
      </div>
      <div class="col-md-6">
        <div class="recipe-details">
          <h4>Información del Empleado</h4>
          <p> <strong>Tipo de Documento: </strong> {{ employee.tipo_documento }}</p>
          <p> <strong>Documento: </strong> {{ employee.documento }}</p>
          <p> <strong> Área: </strong>{{ employee.area }}</p>
          <p> <strong> Subárea: </strong> {{employee.subarea}} </p>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  head() {
    return {
      title: "Información de Empleados"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let employee = await $axios.$get(`/empleados/${params.id}`);
      return { employee };
    } catch (e) {
      return { employee: [] };
    }
  },
  data() {
    return {
      employee: {
        tipo_documento: "",
        documento: "",
        primer_nombre: "",
        segundo_nombre: "",
        primer_apellido: "",
        segundo_apellido: "",
        area: "",
        subarea: "",
      }
    };
  }
};
</script>

<style scoped>
</style>