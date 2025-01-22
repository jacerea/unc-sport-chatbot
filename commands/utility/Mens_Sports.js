// This will output all of the sports that UNC men play at UNC
// For more commands, please jace keep in mind that you have to run your deploy-commands.js script in order for the bot to reapply the commands in the folder.

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