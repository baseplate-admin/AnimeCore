// https://gist.github.com/maximilian-lindsey/a446a7ee87838a62099d

import express from "express";
import cors from "cors";
import { Database as ORM } from "$database/index";

const app = express();

const orm = new ORM();
orm.migrate();

app.use(cors());

app.get("/", (_, res) => {
	res.send("Hello World!");
});

app.get("/shiinobi-healthcheck", (_, res) => {
	res.send("We are friends");
});

app.get("/staff", (_, res) => {
	const item = orm.get_all_null_staff();
	res.json(item);
});

app.get("/staff/:id", (req, res) => {
	const item = orm.get_staff(Number(req.params.id));
	res.json(item);
});

app.get("/staff/create/:id", (req, res) => {
	orm.create_staff({ mal_id: Number(req.params.id) });
	res.send("OK");
});

export { app };
