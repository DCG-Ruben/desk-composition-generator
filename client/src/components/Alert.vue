<template>
    <div class="mt-2 px-0">
        <div class="alert mb-0 py-2" :class="alertClass" role="alert">
            {{ message }}
        </div>
    </div>
</template>

<script>
    export default {
        props: ['message', 'alertClass'],
    };
</script>