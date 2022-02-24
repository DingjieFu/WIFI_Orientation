<template>
    <div class="finger-print-visualize">
        <button
            class="nav-btn-on"
            v-if="controlNow == 'add'"
            @click="controlSwitch('add')"
        >
            add
        </button>
        <button class="nav-btn" v-else @click="controlSwitch('add')">
            add
        </button>
        <button
            class="nav-btn-on"
            v-if="controlNow == 'update'"
            @click="controlSwitch('update')"
        >
            update
        </button>
        <button v-else @click="controlSwitch('update')">update</button>
        <button
            class="nav-btn-on"
            v-if="controlNow == 'delete'"
            @click="controlSwitch('delete')"
        >
            delete
        </button>
        <button v-else @click="controlSwitch('delete')">delete</button>
        <div
            v-if="controlNow != 'default' && controlNow != 'delete'"
            class="updateArea"
        >
            <div
                class="op-form"
                v-for="(item, index) in tableHead"
                :key="item.id"
            >
                <label v-if="item != '操作'">{{ item }}</label>
                <input
                    v-if="item != '操作'"
                    type="text"
                    class="form-control"
                    v-model="updateData[index]"
                />
            </div>
            <button v-if="controlNow == 'add'" @click="add()">Add</button>
        </div>
        <div class="view">
            <table class="table">
                <thead>
                    <tr>
                        <th v-for="item in tableHead" :key="item.id">
                            {{ item }}
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="data in tableContent" :key="data.id">
                        <td v-for="item in data" :key="item">
                            <!-- {{ item.toFixed(2) }} -->
                            <!--此处用于将数据保留两位小数 不补零 -->
                            {{
                                Math.round(item * Math.pow(10, 2)) /
                                Math.pow(10, 2)
                            }}
                        </td>
                        <div class="op-btn-wrap">
                            <button @click="update(data.id)">update</button>
                            <button @click="deleteData(data.id)">delete</button>
                        </div>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";

export default {
    data() {
        return {
            tableHead: [
                "id",
                "p1",
                "p2",
                "p3",
                "p4",
                "p5",
                "p6",
                "p7",
                "p8",
                "p9",
                "p10",
                "p11",
                "p12",
                "p13",
                "p14",
                "p15",
                "p16",
                "p17",
                "p18",
                "p19",
                "p20",
                "p21",
                "p22",
                "p23",
                "p24",
                "p25",
                "p26",
                "p27",
                "p28",
                "p29",
                "p30",
                "xlabel",
                "ylabel",
                "操作",
            ],
            tableContent: [],
            updateData: [
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            ],
            controlNow: "",
        };
    },
    mounted() {
        this.getTestTable();
        this.controlNow = "default";
    },
    methods: {
        getTestTable() {
            axios({
                url: "http://127.0.0.1:9000/get-test-list/",
                type: "json",
                method: "get",
            }).then((res) => {
                this.tableContent = res.data;
            });
        },
        update(id) {
            var updateData = this.updateData;
            axios({
                url: "http://127.0.0.1:9000/update-test-list/",
                data: Qs.stringify({
                    id,
                    updateData,
                }),
                method: "post",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                type: "json",
            }).then((res) => {
                console.log(res), this.getTestTable();
                this.controlSwitch("default");
            });
        },
        controlSwitch(control) {
            if (this.controlNow == control) {
                this.controlNow = "default";
            } else {
                this.controlNow = control;
            }
        },
        deleteData(id) {
            var controlNow = this.controlNow;
            if (controlNow != "delete")
                alert("Please confirm before you delete!");
            axios({
                url: "http://127.0.0.1:9000/delete-test-list/",
                data: Qs.stringify({
                    id,
                    controlNow,
                }),
                method: "delete",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                type: "json",
            }).then((res) => {
                console.log(res), this.getTestTable();
            });
        },
        add() {
            var updateData = this.updateData;
            for (var i = 0; i < 33; i++) {
                if (updateData[i] == "") {
                    alert("Blank features exists!");
                    return;
                }
            }
            axios({
                url: "http://127.0.0.1:9000/add-test-list/",
                data: Qs.stringify({
                    updateData,
                }),
                method: "post",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                type: "json",
            }).then((res) => {
                console.log(res.data);
                if (res.data == "Already exists!") alert(res.data);
                this.getTestTable();
                this.controlSwitch("default");
            });
        },
    },
};
</script>

<style scoped>
.op-form {
    display: flex;
    justify-content: space-between;
    width: 180px;
    align-items: center;
    font-size: 18px;
}
label {
    width: 30px;
    margin: 0 10px;
}
input {
    background-color: rgba(197, 197, 197, 0.397);
    margin: 5px 20px;
    width: 50px;
    border-radius: 4px;
    height: 10px;
    padding: 10px;
}
button {
    border-radius: 8px;
    height: 30px;
    margin: 10px;
    width: 60px;
    outline: none;
}
button:hover {
    background-color: rgba(128, 128, 128, 0.404);
}
button:active {
    background-color: rgba(128, 128, 128, 0.8);
}
td {
    border: 1px solid rgba(0, 0, 0, 0.274);
    padding: 10px;
    min-width: 50px;
}
td:hover {
    background-color: rgba(128, 128, 128, 0.192);
}
thead th {
    line-height: 100%;
    height: 40px;
    background-color: rgba(128, 128, 128, 0.603);
}
.op-btn-wrap {
    display: flex;
}
.op-btn-wrap button {
    margin: 10px;
}
.nav-btn-on {
    border-radius: 8px;
    height: 30px;
    margin: 10px;
    width: 60px;
    outline: none;
    color: #f1f1f1;
    background-color: rgb(48, 47, 47);
}
</style>
