// Command is deployed and it does work, however need to fix the scraper

const { SlashCommandBuilder } = require('discord.js');
const { exec } = require('child_process');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('schedule')
		.setDescription('Get the schedule for a UNC men\'s sport')
		.addStringOption(option =>
			option.setName('sport')
				.setDescription('The sport to get the schedule for')
				.setRequired(true)
				.addChoices(
					{ name: 'Basketball', value: 'mens-basketball' },
					{ name: 'Baseball', value: 'baseball' },
					{ name: 'Football', value: 'football' },
					{ name: 'Lacrosse', value: 'mens-lacrosse' },
					{ name: 'Soccer', value: 'mens-soccer' },
				),
		),
	async execute(interaction) {
		const sport = interaction.options.getString('sport');
		const season = '2024-25';

		// Execute Python script and capture output
		exec(`python3 soup_scrape.py ${season} ${sport}`, (error, stdout, stderr) => {
			if (error) {
				console.error(`Error executing script: ${error}`);
				return interaction.reply({ content: 'Error retrieving schedule.', ephemeral: true });
			}
			if (stderr) {
				console.error(`stderr: ${stderr}`);
			}

			try {
				const data = JSON.parse(stdout);
				if (data.error) {
					return interaction.reply({ content: data.error, ephemeral: true });
				}

				const schedule = data.join('\n');
				interaction.reply(`📅 **UNC ${sport.replace('-', ' ').toUpperCase()} Schedule (${season})**:\n\n${schedule}`);
			}
			catch (e) {
				console.error(`Parsing error: ${e}`);
				interaction.reply({ content: 'Error parsing schedule data.', ephemeral: true });
			}
		});
	},
};
