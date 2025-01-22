const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('unc-mens-sports')
		.setDescription('Lists all the sports played by the UNC men\'s teams'),
	async execute(interaction) {
		const mensSports = [
			'Basketball',
			'Baseball',
			'Football',
			'Golf',
			'Lacrosse',
			'Soccer',
			'Swimming & Diving',
			'Rowing',
			'Tennis',
			'Track & Field',
			'Wrestling',
		];

		await interaction.reply(`The UNC men's teams participate in the following sports:\n- ${mensSports.join('\n- ')}`);
	},
};