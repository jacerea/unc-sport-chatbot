const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('unc-duke-all-time')
		.setDescription('Replies with the unc - duke basketball all time score'),
	async execute(interaction) {
		await interaction.reply('Out of currently 261 meetings total, UNC leads the series 145 - 117, with the longest win streak being 16 in a row from UNC!');
	},
};