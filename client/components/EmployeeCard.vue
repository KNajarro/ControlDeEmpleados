<template>
  <div class="card employee-card">
    <img src="/images/generic.png" class="card-img-top" >
    <div class="card-body">
      <h5 class="card-title">{{ employee.primer_nombre +" "+ employee.primer_apellido }}</h5>
      <p class="card-text">
        <strong>Área:</strong> {{ employee.area }} <br>
        <strong>Sub área:</strong> {{employee.subarea}}
      </p>
      <div class="action-buttons">
        <nuxt-link :to="`/empleados/${employee.id}/`" class="btn btn-sm btn-success">Ver</nuxt-link>
        <nuxt-link :to="`/empleados/${employee.id}/edit/`" class="btn btn-sm btn-primary">Editar</nuxt-link>
        <button @click="onDelete(employee.id)" class="btn btn-sm btn-danger">Eliminar</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    props: ["employee", "onDelete"]
};
</script>

<style>
.employee-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
}
</style>