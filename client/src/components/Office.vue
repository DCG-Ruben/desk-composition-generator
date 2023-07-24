<template>
    <div class="container vh-100">
        <div class="row mb-3 text-center">
            <h1 class="display-1">
                <span class="fw-bold" style="color: #00e17b">D</span>
                <span>esk </span>
                <span class="fw-bold" style="color: #00e17b">C</span>
                <span>omposition </span>
                <span class="fw-bold" style="color: #00e17b">G</span>
                <span>enerator</span>
            </h1>
        </div>
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
                                    <div class="col-md-4 pt-5 border border-3 border-success rounded text-center">
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
                    <div class="d-flex justify-content-center mb-2">
                        <div class="form-text me-3">
                            <h6>Per persoon</h6>
                        </div>
                        <div class="form-check form-switch" style="transform: scale(1.4); padding-top: .5%">
                            <input class="form-check-input" type="checkbox" id="toggleMode" v-model="officeMode">
                        </div>
                        <div class="form-text ms-1">
                            <h6>Hele kantoor</h6>
                        </div>
                    </div>
                </div>
                <transition name="fade" mode="out-in">
                    <div class="row" v-if="officeMode">
                        <div class="col-md-9 ps-0 pe-1">
                            <button type="button" class="btn btn-primary btn-lg w-100" @click="randomizeDesks">
                                Genereer indeling
                            </button>
                        </div>
                        <div class="col-md-3 ps-1 pe-0">
                            <button type="button" class="btn btn-danger btn-lg w-100" @click="resetAssignment">
                                Reset
                            </button>
                        </div>
                    </div>
                    <div class="row" v-else>
                        <div class="col-md-9 ps-0 pe-1">
                            <button type="button" class="btn btn-primary btn-lg w-100" @click="addPerson('single')">
                                Waar mag ik zitten?
                            </button>
                        </div>
                        <div class="col-md-3 ps-1 pe-0">
                            <button type="button" class="btn btn-danger btn-lg w-100" @click="resetAssignment">
                                Reset
                            </button>
                        </div>
                    </div>
                </transition>
                <transition name="fade" mode="out-in">
                    <div class="row mt-2" v-if="officeMode">
                        <form class="px-0">
                            <div class="input-group">
                                <input type="text" @keydown.enter.prevent="addPerson('office')" class="form-control" v-model="newNameOffice" placeholder="Naam">
                                <button type="button" class="btn btn-secondary btn-sm" @click="addPerson('office')">
                                    Voeg toe
                                </button>
                            </div>
                        </form>
                        <transition name="fade">
                            <alert :message="message" :alertClass="alertClass" v-if="showMessage">
                            </alert>
                        </transition>
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
                    <div class="row mt-2" v-else>
                        <form class="px-0">
                            <div class="input-group">
                                <input type="text" @keydown.enter.prevent class="form-control" v-model="newNameSingle" placeholder="Naam">
                            </div>
                        </form>
                        <transition name="fade">
                            <alert :message="message" :alertClass="alertClass" v-if="showMessage">
                            </alert>
                        </transition>
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th scope="col">Al aangemeld:</th>
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
                </transition>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import Alert from './Alert.vue';

    export default {
        data() {
            return {
                newNameSingle: '',
                newNameOffice: '',
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
                       },
                message: '',
                showMessage: false,
                alertClass: 'alert-success',
                officeMode: false,
            };
        },
        components: {
            alert: Alert,
        },
        methods: {
            activateAlert(message, setClass, duration) {
                this.message = message;
                this.alertClass = setClass;
                this.showMessage = true;
                setTimeout(() => this.showMessage = false, duration);
            },
            addPerson(mode) {
                const newName = (mode == 'office') ? this.newNameOffice : this.newNameSingle
                if (newName === '') {
                    this.activateAlert('Vul alsjeblieft eerst een naam in', 'alert-warning', 3000);
                } else {
                    const path = `http://localhost:5001/office/people`;
                    const payload = {
                        name: newName,
                        mode: mode
                    };
                    axios.post(path, payload).then((res) => {
                        this.getPeople();
                        const messageClass = (res.data.status == 'success') ? 'alert-success' : 'alert-danger'
                        this.activateAlert(res.data.message, messageClass, 1500);
                        if (mode == 'office') {
                            this.newNameOffice = '';
                        } else if (mode == 'single') {
                            this.newNameSingle = '';
                            this.desks = res.data.desks;
                        }
                    }).catch((error) => {
                        console.log(error);
                        this.getPeople();
                    });
                }
            },
            getPeople() {
                const path = `http://localhost:5001/office/people`;
                axios.get(path).then((res) => {
                    this.people = res.data.people;
                    this.desks = res.data.desks;
                }).catch((error) => {
                    console.error(error);
                });
            },
            randomizeDesks() {
                const path = `http://localhost:5001/office/randomize`;
                axios.get(path).then(() => {
                    this.getPeople();
                }).catch((error) => {
                    console.error(error);
                });
            },
            removePerson(person) {
                const path = `http://localhost:5001/office/people/${person.id}`;
                axios.delete(path).then(() => {
                    this.activateAlert(person.name + ' is succesvol verwijderd!', 'alert-success', 1500);
                    this.getPeople();
                }).catch((error) => {
                    console.error(error);
                    this.getPeople();
                });
            },
            resetAssignment() {
                const path = `http://localhost:5001/office/reset`;
                axios.get(path).then((res) => {
                    this.getPeople();
                    this.activateAlert('De lijst met aanwezigen is succesvol gereset!', 'alert-success', 1500);
                }).catch((error) => {
                    console.error(error);
                });
            },
        },
        created() {
            this.getPeople();
        },
    };
</script>