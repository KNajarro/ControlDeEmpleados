<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ employee.name }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img
          v-if="preview"
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="preview"
          alt
        >
        <img
          v-else
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          src="@/static/images/placeholder.png"
        >
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitEmployee">
          <div class="form-group">
            <label for>Tipo de Documento</label>
            <input type="text" class="form-control" v-model="employee.tipo_documento">
          </div>
          <div class="form-group">
            <label for>Documento</label>
            <input type="text" class="form-control" v-model="employee.documento">
          </div>
          <div class="form-group">
            <label for>Primer Nombre</label>
            <input type="text" class="form-control" v-model="employee.primer_nombre">
          </div>
          <div class="form-group">
            <label for>Segundo Nombre</label>
            <input type="text" class="form-control" v-model="employee.segundo_nombre">
          </div>
          <div class="form-group">
            <label for>Primer Apellido</label>
            <input type="text" class="form-control" v-model="employee.primer_apellido">
          </div>
          <div class="form-group">
            <label for>Segundo Apellido</label>
            <input type="text" class="form-control" v-model="employee.segundo_apellido">
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for>Área</label>
                <select v-model="employee.area" class="form-control">
                  <option value="Operaciones">Operaciones</option>
                  <option value="IT">IT</option>
                  <option value="Mantenimiento">Mantenimiento</option>
                </select>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for>Sub área</label>
                <select v-model="employee.subarea" class="form-control">
                  <option value="Desarrollo">Desarrollo</option>
                  <option value="HelpDesk">Help Desk</option>
                  <option value="Entrenamiento">Entrenamiento</option>
                  <option value="RH">RH</option>
                  <option value="Clinica">Clinica Empresarial</option>
                  <option value="AtencionCliente">Atención al Cliente</option>
                </select>
              </div>
            </div>
          </div>
          <button type="submit" class="btn btn-primary">Agregar</button>
        </form>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  head() {
    return {
      title: "Agregar Empleado"
    };
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
      },
    };
  },
  methods: {
    async submitEmployee() {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.employee) {
        formData.append(data, this.employee[data]);
      }
      try {
        let response = await this.$axios.$post("/empleados/", formData, config);
        this.$router.push("/empleados/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>
</style>