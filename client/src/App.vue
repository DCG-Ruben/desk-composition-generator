<template>
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<style>
#app {
  margin-top: 10px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.form-check-input:checked {
  background-color: #00e17b !important;
  border-color: #00e17b !important;
}

.form-check-input:focus {
  border-color: #00e17b !important;
}

</style>