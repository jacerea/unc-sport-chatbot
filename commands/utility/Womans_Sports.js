// This will output all of the sports that UNC women play at UNC
// For more commands, please jace keep in mind that you have to run your deploy-commands.js script in order for the bot to reapply the commands in the folder.

const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('unc-womans-sports')
		.setDescription('Lists all the sports played by the UNC men\'s teams'),
	async execute(interaction) {
		const womansSports = [
			'Basketball',
			'Softball',
			'Field Hockey',
			'Golf',
			'Lacrosse',
			'Soccer',
			'Swimming & Diving',
			'Rowing',
			'Tennis',
			'Track & Field',
			'Volleyball',
		];

		await interaction.reply(`The UNC men's teams participate in the following sports:\n- ${womansSports.join('\n- ')}`);
	},
};