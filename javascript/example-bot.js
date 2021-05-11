const Discord = require('discord.js');
const client = new Discord.Client();
const config = require('./config.json');
const fs = require('fs');
// Reason for using a config.json is that it makes it easier lol

client.on("ready", async () => {
    console.log(`${client.user.tag} is Online!`)
});

client.login(config.TOKEN)
