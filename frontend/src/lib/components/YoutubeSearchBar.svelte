<script lang="ts">
	// TODO: Test and Made it functional
	import { writable } from 'svelte/store';

	// Create a writable store to hold the search query
	export const searchQuery = writable('');

	// Function to handle form submission
	async function handleSubmit(event: Event) {
		event.preventDefault();
		const response = await fetch(`/api/search?q=${$searchQuery}`);
		const videoData = await response.json();
		// Pass the video data to a parent component for rendering
		$videoData = videoData;
	}
</script>

<form on:submit={handleSubmit}>
	<input bind:value={$searchQuery} placeholder="Search YouTube videos..." />
	<button type="submit">Search</button>
</form>
