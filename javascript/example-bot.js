const Discord = require('discord.js');
const client = new Discord.Client();
const config = require('./config.json');
const fs = require('fs');
client.aliases = new Discord.Collection();
client.commands = new Discord.Collection();
const cooldowns = new Discord.Collection();
// Reason for using a config.json is that it makes it easier lol

client.on("ready", async () => {
    console.log(`${client.user.tag} is Online!`)
    client.user
   function randomStatus() {
    let status = ["discord.gg/tca", "Ping for Prefix!", `over ${client.users.cache.size} Online Friends! <3`, `over ${client.guilds.cache.size} Servers! <3`]
    let rstatus = Math.floor(Math.random() * status.length);

    client.user.setActivity(status[rstatus], {type: "WATCHING"});
    }; setInterval(randomStatus, 20000)
});

client.login(config.TOKEN)
