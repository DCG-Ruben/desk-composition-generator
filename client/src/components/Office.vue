<template>
    <div class="container vh-100">
        <div class="row">
            <div class="col">
                <div class="row border border-4 border-dark bg-light" style="height: 32em; width: 48em">
                    <div class="col-md-4">
                        <div class="row h-50">
                            <div class="col-md-8 border border-4 bg-secondary bg-gradient" style="height: 83%">
                            </div>
                        </div>
                        <div class="row h-50">
                            <div class="col-md-9 offset-md-3">
                                <div class="row h-25">
                                </div>
                                <div class="row h-25">
                                    <div class="col-md-8 pt-3 border border-3 border-success rounded text-center fw-bold">
                                        {{ desks.desk1 }}
                                    </div>
                                </div>
                                <div class="row h-50">
                                    <div class="col-md-4 pt-5 border border-3 border-success rounded">
                                        <div class="mt-4 text-nowrap fw-bold" style="transform: rotate(-90deg)">
                                            {{ desks.desk2 }}
                                        </div>
                                    </div>
                                    <div class="col-md-4 pt-5 border border-3 border-success rounded text-center">
                                        <div class="mt-4 text-nowrap fw-bold" style="transform: rotate(-90deg)">
                                            {{ desks.desk3 }}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="row h-50">
                            <div class="col-md-3">
                                <div class="row h-25 border border-3 rounded bg-secondary bg-gradient">
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="row border-start border-4" style="height: 67%">
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="row border border-3 rounded bg-warning-subtle bg-gradient" style="height: 67%">
                                </div>
                            </div>
                        </div>
                        <div class="row h-50">
                            <div class="col-md-3 offset-md-3">
                                <div class="row h-50">
                                    <div class="col pt-5 border border-3 border-success rounded text-center">
                                        <div class="mt-4 text-nowrap fw-bold" style="transform: rotate(-90deg)">
                                            {{ desks.desk4 }}
                                        </div>
                                    </div>
                                </div>
                                <div class="row h-50">
                                    <div class="col pt-5 border border-3 border-success rounded text-center">
                                        <div class="mt-4 text-nowrap fw-bold" style="transform: rotate(-90deg)">
                                            {{ desks.desk6 }}
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="row h-50">
                                    <div class="col pt-5 border border-3 border-success rounded text-center">
                                        <div class="mt-4 text-nowrap fw-bold" style="transform: rotate(-90deg)">
                                            {{ desks.desk5 }}
                                        </div>
                                    </div>
                                </div>
                                <div class="row h-50">
                                    <div class="col pt-5 border border-3 border-success rounded text-center">
                                        <div class="mt-4 text-nowrap fw-bold" style="transform: rotate(-90deg)">
                                            {{ desks.desk7 }}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="row h-50">
                            <div class="col-md-3 offset-md-3">
                                <div class="row" style="height: 33%">
                                </div>
                                <div class="row border border-3 rounded bg-success-subtle bg-gradient" style="height: 42%">
                                </div>
                            </div>
                            <div class="col-md-2 offset-md-2">
                                <div class="row" style="height: 17%">
                                </div>
                                <div class="row border border-3 rounded bg-dark bg-gradient" style="height: 17%">
                                </div>
                            </div>
                        </div>
                        <div class="row h-50">
                            <div class="col-md-3 offset-md-3">
                                <div class="row h-50">
                                    <div class="col pt-5 border border-3 border-success rounded text-center">
                                        <div class="mt-4 text-nowrap fw-bold" style="transform: rotate(-90deg)">
                                            {{ desks.desk8 }}
                                        </div>
                                    </div>
                                </div>
                                <div class="row h-50">
                                    <div class="col pt-5 border border-3 border-success rounded text-center">
                                        <div class="mt-4 text-nowrap fw-bold" style="transform: rotate(-90deg)">
                                            {{ desks.desk10 }}
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="row h-50">
                                    <div class="col pt-5 border border-3 border-success rounded text-center">
                                        <div class="mt-4 text-nowrap fw-bold" style="transform: rotate(-90deg)">
                                            {{ desks.desk9 }}
                                        </div>
                                    </div>
                                </div>
                                <div class="row h-50">
                                    <div class="col pt-5 border border-3 border-success rounded text-center">
                                        <div class="mt-4 text-nowrap fw-bold" style="transform: rotate(-90deg)">
                                            {{ desks.desk11 }}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col ms-3">
                <div class="row">
                    <button type="button" class="btn btn-primary btn-lg btn-block" @click="randomizeDesks">
                        Randomize desks
                    </button>
                </div>
                <div class="row mt-2">
                    <form class="px-0">
                        <div class="input-group">
                            <input type="text" @keydown.enter.prevent="addPerson" class="form-control" v-model="newName" placeholder="Naam">
                            <button type="button" class="btn btn-secondary btn-sm" @click="addPerson">
                                Voeg toe
                            </button>
                        </div>
                    </form>
                    <table class="table table-hover">
                        <thead>
                            <tr>
                                <th scope="col">Aanwezig:</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(person, index) in people" :key="index">
                                <td>{{ person.name }}</td>
                                <td class="pe-0" style="text-align: right">
                                    <button type="button" class="btn btn-outline-danger btn-sm" @click="removePerson(person)">
                                        Verwijder
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                newName: '',
                people: [],
                desks: {'desk1': '',
                        'desk2': '',
                        'desk3': '',
                        'desk4': '',
                        'desk5': '',
                        'desk6': '',
                        'desk7': '',
                        'desk8': '',
                        'desk9': '',
                        'desk10': '',
                        'desk11': ''
                       }
            };
        },
        methods: {
            addPerson() {
                const path = `http://localhost:5001/office/people`;
                const payload = {
                    name: this.newName
                };
                axios.post(path, payload).then(() => {
                    this.getPeople();
                }).catch((error) => {
                    console.log(error);
                    this.getPeople();
                });
                this.newName = "";
            },
            getPeople() {
                const path = `http://localhost:5001/office/people`;
                axios.get(path).then((res) => {
                    this.people = res.data.people;
                }).catch((error) => {
                    console.error(error);
                });
            },
            randomizeDesks() {
                const path = `http://localhost:5001/office/randomize`;
                axios.get(path).then((res) => {
                    this.desks = res.data.desks;
                }).catch((error) => {
                    console.error(error);
                });
            },
            removePerson(person) {
                const path = `http://localhost:5001/office/people/${person.id}`;
                axios.delete(path).then(() => {
                    this.getPeople();
                }).catch((error) => {
                    console.error(error);
                    this.getPeople();
                });
            },
        },
        created() {
            this.getPeople();
        },
    };
</script>