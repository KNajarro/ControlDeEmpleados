<template>
  <div>
    <div>
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="/" class="nombre-app">Control de Empleados</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <!-- <b-navbar-nav>
            <b-nav-item href="#">Link</b-nav-item>
            <b-nav-item href="#" disabled>Disabled</b-nav-item>
          </b-navbar-nav> -->

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-form>
              <b-form-input
                size="sm"
                class="mr-sm-2"
                placeholder="Nombre o Documento"
              ></b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit"
                >Buscar</b-button
              >
            </b-nav-form>

            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template #button-content>
                <em>Acciones</em>
              </template>
              <b-dropdown-item href="/empleados">Lista de Empleados</b-dropdown-item>
              <b-dropdown-item href="/empleados/add">Agregar Empleado</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    <nuxt />
  </div>
</template>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap');
  #nombre-app {
    font-family: 'Varela Round', sans-serif;
  }
</style>